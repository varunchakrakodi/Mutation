import pandas as pd
from Bio import SeqIO

def filter_fasta_by_ratings(fasta_file, excel_file, output_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    good_ids = set(df[df['Rating'] == 'good']['ID'])
    
    # Read the FASTA file and filter sequences
    filtered_sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence_id = record.id
        if sequence_id in good_ids:
            filtered_sequences.append(record)
    
    # Write the filtered sequences to a new FASTA file
    SeqIO.write(filtered_sequences, output_file, "fasta")
    
fasta_file = input("Enter the path to multifasta file: ")
excel_file = input("Enter the path to .xlsx file containing the list: ")
output_file = input("Enter the path to sorted multifasta file: ")

filter_fasta_by_ratings(fasta_file, excel_file, output_file)
