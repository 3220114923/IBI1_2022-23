seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

# Find the index of the start codon
start_codon_index = seq.find('ATG')

# Find the indices of all the stop codons
stop_codon_indices = [seq.find(stop_codon, start_codon_index) for stop_codon in ['TAA', 'TAG', 'TGA']]

# Remove any stop codon indices that are not found after the start codon
stop_codon_indices = [index for index in stop_codon_indices if index != -1]

# Count the number of possible coding sequences
num_coding_sequences = len(stop_codon_indices)

print(f'Total number of possible coding sequences: {num_coding_sequences}')
