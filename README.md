# Mutation
Set of Python-based scripts for assessing amino acid mutations from a multifasta file.

**Note:**
It requires a multifasta file containing all the sequences (Including reference sequences) to be analysed.
The script will ask for user inputs step by step.
All scripts have multiple dependencies. It would be ideal to have anaconda installed in the system (https://www.anaconda.com/)

It is useful to filter out sequences that have low-quality sequences from the input multifasta files. Either use fasta_filter.py or xsort.py, depending on the use case scenario.

**1. fasta_filter.py**

Quality scoring will be available if you have a multifasta amino acid sequence generated through tools such as NextClade. The program takes details in a .xlsx file as input with two rows: ID and Rating. The program filters out only those sequences that have been scored as good.

Usgae: python3 fasta_filter.py

**2. xsort.py**

Removing all sequences containing ambiguous amino acids would be ideal when running mutation analysis. This program takes the input multifasta file and then creates a new sorted.fasta file. It also outputs a .csv file containing details on how many ambiguous amino acids were found.

**Usage:** python3 xsort.py

**3. heatmap.py**

Takes a multifasta file previously aligned using multiple alignment (Prefer to use MAFFT; https://github.com/GSLBiotech/mafft) and then converts it into an interactive .html plot highlighting the mutations against the reference. The input multifasta file should contain both references and other sequences.

**Usage:** python3 heatmap.py

**4. signmutations.py**

Takes the same aligned multifasta file as input and creates a .csv file with the list of mutations. The script also asks the user for input cut-off ranging from 0.01 to 1 (Indicating 1% to 100%).

**Usage:** python3 signmutations.py

