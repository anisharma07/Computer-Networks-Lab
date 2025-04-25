import matplotlib.pyplot as plt
import random

# Simulation Parameters
TIME_STEPS = 500
BUFFER_SIZE = 5
LINK_ERROR_RATE = 0.1  # Probability a packet is lost on link
NUM_ROUTERS = 4
TIMEOUTS = [2, 4, 6, 8, 10]
ERROR_RATES = [0.0, 0.05, 0.1, 0.2]


class Packet:
    def __init__(self, id, timeout):
        self.id = id
        self.age = 0
        self.timeout = timeout
        self.sent_time = 0


def simulate(timeout_interval, error_rate):
    buffer = [[] for _ in range(NUM_ROUTERS)]
    source_queue = [Packet(i, timeout_interval) for i in range(100)]
    waiting_for_ack = {}
    acks = set()
    delivered = 0
    time = 0

    while time < TIME_STEPS:
        # Send packet if waiting for ACK
        for pid, pkt in list(waiting_for_ack.items()):
            pkt.age += 1
            if pkt.age >= pkt.timeout:
                pkt.age = 0  # reset timeout
                buffer[0].append(pkt)

        # New packet from source
        if source_queue and len(buffer[0]) < BUFFER_SIZE:
            pkt = source_queue.pop(0)
            buffer[0].append(pkt)
            waiting_for_ack[pkt.id] = pkt

        # Move packets along the routers
        for i in reversed(range(NUM_ROUTERS)):
            if buffer[i]:
                pkt = buffer[i][0]
                if i == NUM_ROUTERS - 1:  # Last router = destination
                    # Simulate link error
                    if random.random() > error_rate:
                        acks.add(pkt.id)
                        delivered += 1
                    buffer[i].pop(0)
                    waiting_for_ack.pop(pkt.id, None)
                else:
                    if len(buffer[i + 1]) < BUFFER_SIZE:
                        # Simulate link error
                        if random.random() > error_rate:
                            buffer[i + 1].append(pkt)
                        buffer[i].pop(0)

        time += 1

    throughput = delivered / TIME_STEPS
    return throughput


# Run simulation
plt.figure(figsize=(10, 6))
for error_rate in ERROR_RATES:
    results = []
    for timeout in TIMEOUTS:
        th = simulate(timeout, error_rate)
        results.append(th)
    plt.plot(TIMEOUTS, results, label=f"Error Rate = {error_rate}")

plt.title("Throughput vs Timeout Interval")
plt.xlabel("Timeout Interval")
plt.ylabel("Throughput (packets per time step)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
