rows = []
with open("input.txt", "r") as f:
  for line in f:
    rows.append(line.split())

for row in rows:
  assert len(row) == 1000

grand_total = 0
for column in range(1000):
  current_sum = 0 if rows[-1][column] == "+" else 1
  for row in range(len(rows) - 1):
    if rows[-1][column] == "+":
      current_sum += int(rows[row][column])
    else:
      current_sum *= int(rows[row][column])
  grand_total += current_sum
  print(current_sum)
print(grand_total)
