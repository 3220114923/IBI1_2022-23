# Step 1: Read the input sequences and BLOSUM62 matrix
with open('Seq1.txt', 'r') as f:
    seq1_name = f.readline().strip()
    seq1 = f.readline().strip()

with open('Seq2.txt', 'r') as f:
    seq2_name = f.readline().strip()
    seq2 = f.readline().strip()

blosum62 = {}
with open('BLOSUM62.txt', 'r') as f:
    header = f.readline().split()
    for line in f:
        values = line.split()
        amino_acid1 = values[0]
        for i in range(1, len(values)):
            amino_acid2 = header[i-1]
            blosum62[(amino_acid1, amino_acid2)] = int(values[i])

# Step 2: Calculate the alignment score
score = 0
for i in range(len(seq1)):
    amino_acid1 = seq1[i]
    amino_acid2 = seq2[i]
    score += blosum62[(amino_acid1, amino_acid2)]

# Step 3: Calculate the percentage identity
identity = 0
for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
        identity += 1

percentage_identity = (identity/len(seq1)) * 100

# Print the results
print(seq1_name + ": " + seq1)
print(seq2_name + ": " + seq2)
print("Alignment score: " + str(score))
print("Percentage identity: " + str(percentage_identity) + "%")
