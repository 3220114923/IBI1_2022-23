# import necessary modules
import re

# ask user for stop codon input
stop_codon = input("Enter stop codon (TAA, TAG or TGA): ")

# create output file name
output_file = stop_codon + "_stop_genes.fa"

# open input and output files
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file, open(output_file, "w") as output_file:
    # initialize variables
    gene_count = 0
    gene_name = ""
    sequence = ""

    # loop through each line in input file
    for line in input_file:
        # if line starts with ">", it's a header line
        if line.startswith(">"):
            # if we have a gene sequence, check if it ends with the given stop codon
            if sequence != "" and sequence.endswith(stop_codon):
                # simplify gene name by keeping only the gene ID
                gene_id = re.search(r"(?<=gene:)[^\s]+", gene_name).group()

                # write sequence to output file in fasta format
                output_file.write(">" + gene_id + "_" + str(gene_count) + "\n" + sequence + "\n")

                # update gene count
                gene_count += 1

            # reset variables for new gene sequence
            gene_name = line.strip()
            sequence = ""
        else:
            # append sequence to current gene sequence
            sequence += line.strip()

    # check if last gene sequence ends with the given stop codon
    if sequence != "" and sequence.endswith(stop_codon):
        # simplify gene name by keeping only the gene ID
        gene_id = re.search(r"(?<=gene:)[^\s]+", gene_name).group()

        # write sequence to output file in fasta format
        output_file.write(">" + gene_id + "_" + str(gene_count) + "\n" + sequence + "\n")

        # update gene count
        gene_count += 1

    # print number of genes with given stop codon
    print("Number of genes with stop codon", stop_codon, ":", gene_count)
