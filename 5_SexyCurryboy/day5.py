import numpy as np

line_n = 0
row = []
crates = []
instructions = []
with open ('input.txt', 'r') as file:
    for line in file:
        line_n += 1
        if line[0] == "[": #Kisten
            for i in range(1,len(line)-2,4):
                if line[i] != " ":
                    row.append(line[i])
                else:
                    row.append(None)
            crates.append(row)
            row = []
        elif line_n > 10: #Anweisungen
            instructions.append([int(item) for item in line.split() if item.isdigit()])

#Rotate 90° & remove None
crates = np.asanyarray(crates)
crates = np.rot90(crates, 3)
crates = crates.tolist()
crates_cleaned = []
for column in crates:
    column_cleaned = [item for item in column if item is not None]
    crates_cleaned.append(column_cleaned)

crates_cleaned_copy = crates_cleaned
for instr in instructions:
    for i in range(instr[0]):
        crates_cleaned_copy[instr[2]-1].append(crates_cleaned_copy[instr[1]-1].pop())

message = ""

for column in crates_cleaned_copy:
    message += column.pop()

print(message)