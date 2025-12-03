###### PART ONE ######

def get_highest_jolt(b: str) -> int:
  first_digit = [-1, -1] # [value, index] of largest digit
  for index, c in enumerate(b[:-1]): # dont include last number (think)
    if int(c) > first_digit[0]:
      first_digit = [int(c), index]

  second_digit = -1
  for c in b[first_digit[1]+1:]:
    if int(c) > second_digit:
      second_digit = int(c)

  return int(str(first_digit[0]) + str(second_digit))


banks = []
with open("input.txt", "r") as f:
  for line in f:
    banks.append(line.strip())

total_count = 0
for bank in banks:
  print(bank)
  c = get_highest_jolt(bank)
  print(c)
  total_count += c

print(total_count)


###### PART TWO ######

def get_highest_jolt(b: str) -> int:
  jolt_str = ""
  digit_index = 0

  # Find largest digit in b leaving enough string to grab later
  # so we prioritize having at least 12 digits, then largest digit
  # highness which should make the biggest number possible
  for i in range(1, 13):
    largest_digit = -1
    remaining = 12 - i
    slice_to = -remaining if remaining > 0 else None
    best_jump_index = 0

    for index, c in enumerate(b[digit_index:slice_to]):
      if int(c) > largest_digit:
        largest_digit = int(c)
        best_jump_index = index+1

    jolt_str += str(largest_digit)
    digit_index += best_jump_index

  return jolt_str


print("987654321111111")
print(">> " + get_highest_jolt("987654321111111"))
print()
print("234234234234278")
print(">> " + get_highest_jolt("234234234234278"))

total_count = 0
for bank in banks:
  c = get_highest_jolt(bank)
  total_count += int(c)

print(total_count)
