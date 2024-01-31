print("This program finds a list of mutations against a Reference sequence")
print("V1.0. Code Compiled by: Varun CN, NIMHANS")
print("Require a multifasta file that contains Reference Sequence along with other sequences that has been aligned")

from Bio import AlignIO
import csv

def get_mutations(reference_seq, test_seq):
    mutations = []
    for i, (ref_base, test_base) in enumerate(zip(reference_seq, test_seq)):
        if ref_base != test_base:
            mutations.append((i + 1, ref_base, test_base))  # Adding 1 to position to make it 1-based instead of 0-based
    return mutations

def write_to_csv(mutations, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Position", "Reference", "Test"])
        csv_writer.writerows(mutations)

# Input multi-fasta file
input_file = input("Enter the path to the aligned multi-fasta file: ")

# Parse the aligned multi-fasta file
alignment = AlignIO.read(input_file, "fasta")

# User input for reference and test headers
ref_header = input("Enter the header of the reference sequence: ")
test_header = input("Enter the header of the test sequence: ")

# Extract reference and test sequences
ref_seq = next(record.seq for record in alignment if record.id == ref_header)
test_seq = next(record.seq for record in alignment if record.id == test_header)

# Get mutations
mutations = get_mutations(ref_seq, test_seq)

# Display mutations
print("\nMutations:")
print("{:<10} {:<15} {:<15}".format("Position", "Reference", "Test"))
for position, ref_base, test_base in mutations:
	print("{:<10} {:<15} {:<15}".format(position, ref_base, test_base))

# Request output CSV file
output_file = input("Enter the path for the output CSV file: ")
    
# Write mutations to CSV file
write_to_csv(mutations, output_file)
print(f"Output written to {output_file}")
