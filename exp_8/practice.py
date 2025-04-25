def simulate(graph, source, destination, ttl, flood_mode, k=2):
     current, previous, delay, ttl_left = queue.popleft()
        transmissions += 1

        if current == destination:
            if reached_time is None or delay < reached_time:
                reached_time = delay
            continue

        if ttl_left <= 0:
            continue

     queue = deque()0, None, 0, TTL
     transmissions = 0
     reached_time = None

    while queue:
        current, prev, delay, ttl = queue.popleft()

        if strat == 'all':
        graph[current]
        if strat ==
        [n for n in graph[current] if n != prev]

        bestk.get(curre, graph(current))[:k]

        for neighbour in neighbours:
            if (neighbour, ttl_left-1) not in visited:
                visited.append
                queue.append(neighbour, current, delay+1, ttl-1)
