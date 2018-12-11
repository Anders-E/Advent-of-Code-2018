from sys import stdin, exit

freq = 0
visited = {0: True}

nums = list(map(int, stdin.readlines()))

while True:
    for num in nums:
        freq += num
        if freq in visited:
            print(freq)
            exit()
        visited[freq] = True

