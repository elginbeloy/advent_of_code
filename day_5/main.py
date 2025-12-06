###### PART ONE ######

ranges = []
ids = []
with open("input.txt", "r") as f:
  for line in f:
    to_add = line.strip()
    if to_add == "": break
    ranges.append(to_add)

  for line in f:
    to_add = line.strip()
    if to_add == "": break
    ids.append(to_add)

def is_fresh(id):
  for r in ranges:
    b, t = r.split("-")
    if int(b) <= int(id) <= int(t):
      return True

  return False

fresh = 0
for id in ids:
  if is_fresh(id):
    fresh += 1

print(fresh)

print("###### PART TWO")
###### PART TWO ######

# go through check for any overlap, if there is combine
# the ranges into a single range
# when we are sure we have all ranges with no overlap we
# can simply add up t-b for all ranges

r_tuples = []
for r in ranges:
  b, t = r.split("-")
  r_tuples.append((int(b), int(t)))

print(r_tuples)

r_tuples.sort(key=lambda x: x[0])

merged = []
for current in r_tuples:
  if not merged or current[0] > merged[-1][1]:
    merged.append(current)
  else:
    merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))

total_fresh = sum(end - start + 1 for start, end in merged)
print(total_fresh)
