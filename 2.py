import heapq

def a_star(grid, start, end):

    open_list = []

    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {start: 0}

    while open_list:

        current = heapq.heappop(open_list)[1]

        # Goal reached
        if current == end:

            path = []

            while current in came_from:

                path.append(current)

                current = came_from[current]

            path.append(start)

            return path[::-1]

        x, y = current

        # Possible movements
        for move in [(0,1), (1,0), (0,-1), (-1,0)]:

            neighbor = (x + move[0], y + move[1])

            # Boundary check
            if not (0 <= neighbor[0] < len(grid) and
                    0 <= neighbor[1] < len(grid[0])):
                continue

            # Obstacle check
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue

            new_g = g_cost[current] + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                # Heuristic function
                f = new_g + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])

                heapq.heappush(open_list, (f, neighbor))

                came_from[neighbor] = current

    return None

# ---------------- USER INPUT ----------------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("\nEnter grid values row by row")
print("0 = Free Path")
print("1 = Obstacle\n")

for i in range(rows):

    row = list(map(int, input(f"Enter row {i+1}: ").split()))

    grid.append(row)

print("\nEnter Start Position")

sx = int(input("Start X: "))
sy = int(input("Start Y: "))

print("\nEnter End Position")

ex = int(input("End X: "))
ey = int(input("End Y: "))

start = (sx, sy)
end = (ex, ey)

# Run A*
path = a_star(grid, start, end)

# Output
if path:
    print("\nPath found:", path)
else:
    print("\nNo path found")
