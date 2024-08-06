import plotly.graph_objs as go
from Bio import SeqIO
from collections import defaultdict
import numpy as np
import plotly.io as pio

def retrieve_sequences_from_fasta_with_reference(fasta_file, reference_id):
    protein_sequences = []
    reference_sequence = None
    
    # Parse the FASTA file and retrieve the protein sequences and reference sequence
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id == reference_id:
            reference_sequence = str(record.seq)
        else:
            protein_sequences.append(str(record.seq))
    
    if not reference_sequence:
        raise ValueError(f"Reference ID {reference_id} not found in the provided fasta file.")
    
    return reference_sequence, protein_sequences

def create_mutation_heatmap(reference_sequence, protein_sequences, output_html):
    # Create a matrix to store the mutation data
    mutation_matrix = []
    mutation_info = []

    # Iterate over each protein sequence
    for seq_index, sequence in enumerate(protein_sequences):
        mutations = []
        info = []
        
        # Compare each amino acid in the protein sequence with the reference sequence
        for pos, (ref_aa, seq_aa) in enumerate(zip(reference_sequence, sequence)):
            if ref_aa != seq_aa and seq_aa != 'X':
                mutations.append(1)  # Mutated position
                info.append(f"{ref_aa}{pos+1}{seq_aa}")
            else:
                mutations.append(0)  # Non-mutated position
                info.append('')
        
        mutation_matrix.append(mutations)
        mutation_info.append(info)
    
    mutation_matrix = np.array(mutation_matrix)
    mutation_info = np.array(mutation_info)

    # Create the heatmap
    trace = go.Heatmap(
        z=mutation_matrix,
        text=mutation_info,
        hoverinfo='text',
        colorscale='viridis'
    )
    layout = go.Layout(
        title='Mutation Heatmap',
        xaxis=dict(title='Amino acid position'),
        yaxis=dict(title='Sequence ID')
    )
    fig = go.Figure(data=[trace], layout=layout)
    pio.write_html(fig, output_html)
    print(f"Heatmap saved to {output_html}")

def main():
    fasta_file = input("Enter path to multifasta file containing all sequences: ")
    reference_id = input("Enter the reference ID: ")
    output_html = input("Enter the output HTML file path: ")
    reference_sequence, protein_sequences = retrieve_sequences_from_fasta_with_reference(fasta_file, reference_id)
    create_mutation_heatmap(reference_sequence, protein_sequences, output_html)

if __name__ == "__main__":
    main()

