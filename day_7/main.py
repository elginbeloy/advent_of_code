rows = []
with open("input.txt", "r") as f:
  for line in f:
    rows.append(line)

t_locs = set()
for i, c in enumerate(rows[0]):
  if c == "S":
    t_locs.add(i)

splits = 0
for row in rows[1:]:
  for i, c in enumerate(row):
    if c == "^":
      if i in t_locs:
        splits += 1
        print(f"t hit ^ @ {i}")
        t_locs.remove(i)
        if i > 0:
          t_locs.add(i-1)
        if i < len(row) - 1:
          t_locs.add(i + 1)

print(splits)
