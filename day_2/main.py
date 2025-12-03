###### PART ONE ######

def is_valid(i):
  s = str(i)
  if len(s) % 2 != 0:
    return True
  return s[:len(s) // 2] != s[-len(s) // 2:]


id_ranges = []
with open("input.txt", "r") as f:
  for r in f.read().strip().split(","):
    vals = r.split("-")
    id_ranges.append((
      int(vals[0]),
      int(vals[1])
    ))

count = 0
for r in id_ranges:
  print(r)
  for i in range(r[0], r[1]+1):
    if not is_valid(i):
      print(f"   c += {i}")
      count += i

print(count)


###### PART TWO ######

def is_valid(s: str) -> bool:
  n = len(s)
  if n < 2:
    return True
  for l in range(1, n // 2 + 1):
    if n % l == 0:
      repeat = s[:l] * (n // l)
      if s == repeat:
        return False
  return True

count = 0
for r in id_ranges:
  print(r)
  for i in range(r[0], r[1]+1):
    if not is_valid(str(i)):
      count += i

print(count)
