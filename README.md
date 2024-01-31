There are two Python scripts available.

1. mutations.py

**Use case:** To find a list of mutations in an individual sequence of interest against a reference sequence

**Requirements:** A single multi-fasta file containing the sequence of interest and reference sequence aligned in .fasta format.

**Additional dependencies:** biopython (For installation Refer: https://biopython.org/)

**Example Usage:** python3 mutations.py

**Output:** Creates a .csv file containing a list of mutations

   

2. signmutations.py

**Use case:** To find a list of mutations that are conserved across sequences against a reference sequence

**Requirements:** A multi-fasta file containing reference and other sequences of interest in .fasta format. Work best with Nextclade output.

**Example Usage:** python3 mutations.py

“cutoff value” indicates % of sequences that need to qualify to call it a signature mutation. The value ranges from 0- 1, indicating 0 to 100

**Output:** Creates a .csv file containing a list of mutations
