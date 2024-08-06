from Bio import SeqIO
import csv

def count_X(sequence):
    return sequence.count("X")

def main(input_fasta, output_csv, output_fasta):
    sequences_without_X = []
    
    # Open the output CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Sequence ID", "Number of X"])
        
        # Open the input FASTA file
        for record in SeqIO.parse(input_fasta, "fasta"):
            sequence_id = record.id
            sequence = str(record.seq)
            
            # Count the number of 'X' in the sequence
            num_X = count_X(sequence)
            
            # Write to CSV
            csv_writer.writerow([sequence_id, num_X])
            
            # If no 'X' found, store the sequence
            if num_X == 0:
                sequences_without_X.append(record)
    
    # Write sequences without 'X' to a new FASTA file
    SeqIO.write(sequences_without_X, output_fasta, "fasta")

if __name__ == "__main__":
    input_fasta = input("Path to input Multi-fasta file with all sequences: ")
    output_csv = input("Path to Output .csv file: ")
    output_fasta = input("Path to sorted .fasta file: ")
    main(input_fasta, output_csv, output_fasta)

