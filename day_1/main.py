def rotate(p, d, a):
  return (p + (a * (-1 if d == "L" else 1))) % 100


rotations = []
with open("input.txt", "r") as f:
  for line in f:
    rotations.append(line.strip())

###### PART ONE ######

count = 0
dial_position = 50

for r in rotations:
  dial_position = rotate(dial_position, r[0], int(r[1:]))
  if dial_position == 0:
    count += 1

print(count)

###### PART TWO ATTEMPT 1 ######

count = 0
dial_position = 50

for r in rotations:
  dial_position += (int(r[1:]) * (-1 if r[0] == "L" else 1))
  q, r = divmod(dial_position, 100)
  count += abs(q)
  dial_position = r
  if dial_position == 0 and q == 0:
    count += 1

print(count)

###### PART TWO WITH HELP ######

count = 0
dial_position = 50

for r in rotations:
  assert dial_position >= 0
  a = int(r[1:])
  dir_val = 1 if r[0] == 'R' else -1
  if a == 0:
    hits = 0
  else:
    if dir_val == 1:
      dist = 100 - dial_position
    else:
      dist = dial_position if dial_position != 0 else 100
    if a < dist:
      hits = 0
    else:
      hits = 1 + ((a - dist) // 100)
  count += hits
  dial_position = (dial_position + (a * dir_val)) % 100

print(count)
