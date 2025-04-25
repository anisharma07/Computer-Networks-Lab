# Write a program to simulate routing using flooding. Each packet should contain a counter that is decremented on each hop.
# When the counter gets to zero, the packet is discarded. Time is discrete, with each line handling one packet per time interval.
# Make three versions of the program: all lines are flooded, all lines except the input line are flooded, and only the (statically
# chosen) best k lines are flooded. Compare flooding with deterministic routing (k = 1) in terms of both delay and the bandwidth
# used.

from collections import defaultdict, deque


class Packet:
    def __init__(self, src, dst, ttl):
        self.src = src
        self.dst = dst
        self.ttl = ttl
        self.path = [src]

    def copy(self):
        new_pkt = Packet(self.src, self.dst, self.ttl)
        new_pkt.path = self.path[:]
        return new_pkt


class Network:
    def __init__(self, graph):
        self.graph = graph

    def simulate(self, src, dst, ttl, strategy, k=1):
        time = 0
        queue = deque([(src, None, Packet(src, dst, ttl))])
        visited = defaultdict(set)  # (node, ttl): set of paths

        reached_time = None
        total_transmissions = 0

        while queue:
            time += 1
            next_queue = deque()

            while queue:
                current, prev, pkt = queue.popleft()
                if pkt.ttl <= 0:
                    continue

                pkt.ttl -= 1
                pkt.path.append(current)

                if pkt.dst == current:
                    if reached_time is None:
                        reached_time = time
                    continue

                total_transmissions += 1

                if strategy == 'All_lines_flooded':
                    neighbors = self.graph[current]
                elif strategy == 'except_input':
                    neighbors = [n for n in self.graph[current] if n != prev]
                elif strategy == 'best_k_flooded':
                    neighbors = sorted(self.graph[current])[:k]
                elif strategy == 'deterministic':
                    neighbors = [sorted(self.graph[current])[0]]
                else:
                    raise ValueError("Unknown strategy")

                for neighbor in neighbors:
                    new_pkt = pkt.copy()
                    if tuple(new_pkt.path + [neighbor]) not in visited[(neighbor, new_pkt.ttl)]:
                        visited[(neighbor, new_pkt.ttl)].add(
                            tuple(new_pkt.path + [neighbor]))
                        next_queue.append((neighbor, current, new_pkt))

            queue = next_queue

        return reached_time if reached_time else -1, total_transmissions


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

network = Network(graph)

strategies = ['All_lines_flooded', 'except_input',
              'best_k_flooded', 'deterministic']
results = {}

for strategy in strategies:
    delay, bandwidth = network.simulate(
        'A', 'E', ttl=5, strategy=strategy, k=1)
    results[strategy] = {'delay': delay, 'bandwidth_used': bandwidth}

print("\nRouting Strategy Comparison")
print("===========================")
for strategy, stats in results.items():
    print(
        f"{strategy.title():<20} | Delay: {stats['delay']:<2} | Bandwidth: {stats['bandwidth_used']}")
