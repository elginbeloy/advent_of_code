###### PART ONE ######

positions_to_check = (
  (-1, -1), (0, -1), (1, -1),
  (-1, 0), (1, 0),
  (-1, 1), (0, 1), (1, 1),
)

grid = []
with open("input.txt", "r") as f:
  for line in f:
    grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

def can_be_grabbed(x: int, y: int) -> bool:
  if grid[x][y] == ".":
    return False

  count = 0
  for p in positions_to_check:
    xc, yc = x + p[0], y +  p[1]
    if 0 <= xc < rows and 0 <= yc < cols:
      if grid[xc][yc] == "@":
        count += 1

  return count < 4

grabbed_count = 0
for i in range(rows):
  for j in range(cols):
    if can_be_grabbed(i, j):
      grabbed_count += 1

print(grabbed_count)
