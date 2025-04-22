import random
import matplotlib.pyplot as plt
from collections import deque


class Packet:
    def __init__(self, pkt_id, src, dst, gen_time):
        self.pkt_id = pkt_id
        self.src = src
        self.dst = dst
        self.gen_time = gen_time
        self.acknowledged = False


class Router:
    def __init__(self, name, buffer_size):
        self.name = name
        self.buffer_size = buffer_size
        self.queue = deque()

    def has_space(self):
        return len(self.queue) < self.buffer_size

    def enqueue(self, packet):
        if self.has_space():
            self.queue.append(packet)
            return True
        return False

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None


class Network:
    def __init__(self, graph, buffer_size=5, error_rate=0.1):
        self.graph = graph
        self.routers = {node: Router(node, buffer_size) for node in graph}
        self.error_rate = error_rate
        self.time = 0
        self.packets = {}
        self.acknowledged = set()

    def route_packet(self, packet, timeout):
        path = self.find_path(packet.src, packet.dst)
        timers = {packet.pkt_id: self.time + timeout}
        queue = deque([(path[0], 0)])

        while queue:
            current_router, idx = queue.popleft()
            self.time += 1

            if idx + 1 < len(path):
                next_router = path[idx + 1]

                if random.random() < self.error_rate:
                    continue

                if self.routers[next_router].enqueue(packet):
                    queue.append((next_router, idx + 1))
                else:
                    continue

            if path[-1] == current_router:
                packet.acknowledged = True
                self.acknowledged.add(packet.pkt_id)
                break

            if self.time >= timers[packet.pkt_id] and packet.pkt_id not in self.acknowledged:
                queue.append((path[0], 0))
                timers[packet.pkt_id] = self.time + timeout

    def find_path(self, src, dst):
        # Simple BFS for shortest path
        visited = {src}
        queue = deque([[src]])

        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == dst:
                return path
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return []


def simulate(timeout_vals, error_rate):
    graph = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['C']
    }

    throughput_results = []

    for timeout in timeout_vals:
        network = Network(graph, buffer_size=3, error_rate=error_rate)
        total_packets = 20

        for i in range(total_packets):
            pkt = Packet(i, 'A', 'D', gen_time=network.time)
            network.packets[i] = pkt
            network.route_packet(pkt, timeout)

        throughput = len(network.acknowledged) / total_packets
        throughput_results.append(throughput)

    return throughput_results


# Plotting
timeouts = list(range(1, 21))
print(timeouts)
plt.figure(figsize=(10, 6))

for error in [0.0, 0.5, 0.8]:
    throughput = simulate(timeouts, error)
    print(throughput)
    plt.plot(timeouts, throughput, label=f"Error Rate: {error}")

plt.xlabel("Timeout Interval")
plt.ylabel("Throughput")
plt.title("Network Throughput vs Timeout Interval")
plt.legend()
plt.grid(True)
plt.show()
