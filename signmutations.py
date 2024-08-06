import csv

# User input for reference and test headers
fasta_file = input("Enter the path to multifasta file: ")
reference_sequence_id = input("Enter the Reference ID: ")
cutoff_value = float(input("Enter the cutoff value: "))

def read_fasta(filename):
    sequences = {}
    current_sequence = ""
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                sequence_id = line[1:]
                sequences[sequence_id] = ""
                current_sequence = sequence_id
            else:
                sequences[current_sequence] += line
    return sequences
    
def find_signature_mutations(fasta_file, reference_sequence_id, cutoff_value):
    sequences = read_fasta(fasta_file)
    reference_sequence = sequences.get(reference_sequence_id)

    if reference_sequence is None:
        print("Reference sequence not found.")
        return

    sequence_ids = list(sequences.keys())
    num_sequences = len(sequence_ids)
    sequence_length = len(reference_sequence)

    signature_mutations = []
    
    for i in range(sequence_length):
        reference_amino_acid = reference_sequence[i]
        amino_acids = {}

        for sequence_id in sequence_ids:
            if sequence_id != reference_sequence_id:
                current_amino_acid = sequences[sequence_id][i]
                if current_amino_acid != reference_amino_acid and current_amino_acid != "X":
                    if current_amino_acid not in amino_acids:
                        amino_acids[current_amino_acid] = 0
                    amino_acids[current_amino_acid] += 1

        for amino_acid, count in amino_acids.items():
            if count >= cutoff_value * (num_sequences - 1):
                signature_mutations.append({
                    "position": i + 1,
                    "reference_amino_acid": reference_amino_acid,
                    "amino_acid": amino_acid,
                    "count": count
                })

    return signature_mutations
    
def write_results_to_csv(mutations, output_filename):
    fieldnames = ["Position", "Reference Amino Acid", "Amino Acid", "Count"]

    with open(output_filename, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for mutation in mutations:
            writer.writerow({
                "Position": mutation["position"],
                "Reference Amino Acid": mutation["reference_amino_acid"],
                "Amino Acid": mutation["amino_acid"],
                "Count": mutation["count"]
            })

    print(f"Results written to {output_filename}")

output_filename = input("Enter the path for the output CSV file: ")
mutations = find_signature_mutations(fasta_file, reference_sequence_id, cutoff_value)

if mutations:
    write_results_to_csv(mutations, output_filename)
