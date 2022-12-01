input = []
kalorien = 0
elf = 1
suchtrupp = {}
kalorien_max = 0
kalorien_1 = 0
kalorien_2 = 0
kalorien_3 = 0

with open ('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

for line in input:
    if line != "":
        kalorien += int(line)
    else:
        suchtrupp[elf] = kalorien
        kalorien = 0
        elf += 1

#### Part1 ####
for elf_nummer in suchtrupp:
    if suchtrupp[elf_nummer] > kalorien_max:
        kalorien_max = suchtrupp[elf_nummer]
print(kalorien_max)

#### Part2 ####
for elf_nummer in suchtrupp:
    if suchtrupp[elf_nummer] > kalorien_1:
        kalorien_3 = kalorien_2
        kalorien_2 = kalorien_1
        kalorien_1 = suchtrupp[elf_nummer]

    elif suchtrupp[elf_nummer] > kalorien_2:
        kalorien_3 = kalorien_2
        kalorien_2 = suchtrupp[elf_nummer]

    elif suchtrupp[elf_nummer] > kalorien_3:
        kalorien_3 = suchtrupp[elf_nummer]

print(kalorien_1 + kalorien_2 + kalorien_3)