from Bio import SeqIO

# Open the input and output files
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "TGA_genes.fa"

with open(output_file, "w") as out_fh:
    # Iterate over each sequence in the input file
    for record in SeqIO.parse(input_file, "fasta"):
        # Check if the sequence ends with 'TGA'
        if str(record.seq)[-3:] == "TGA":
            # Simplify the sequence name by extracting only the gene name
            gene_name = record.description.split(" ")[0]
            # Write the sequence to the output file with the simplified name
            out_fh.write(">" + gene_name + "\n")


