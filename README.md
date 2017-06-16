# drosophila-id-converter

### Overview
Take a protein accession number or a gene database ID and retrieve the corresponding gene name

### Setup
Requires Python 3 (and PIP 3)

Download and extract this repository. Should have the following project directory

src/

---dros_id_converter.py

---dros_id_converter_example.py

res/

---gene_id_list.tsv


The only dependency the python script uses is `csv`. If the `csv` package isn't in the environment, run the command `pip3 install csv`

### Interface
`dros_id_converter.py` is the script that operates the conversion. The script takes four optional arguments: `gene_id`, `protein_acc`, `unknown`, and `filename`

The `gene_id` is the input for a gene DB ID (ie. FBgn00000000)

The `protein_acc` is the input for a protein accession ID (ie. Q960Z4)

The `unknown` is the input for either a gene DB ID or a protein accession ID

The `filename` is the input of the filename which is a TSV file with all ID and gene name data

If you are certain that the input is a gene DB ID, use the `gene_id` field. If certain that the input is a protein accession number, use the `protein_acc` field. If uncertain what the input ID is, use the `unknown` field and the script will find out (however the script will be slower).

If an `unknown` field is provided, then the `gene_id` and `protein_acc` fields are ignored. If both the `gene_id` and `protein_acc` fields are provided, then the script will return the intersection of the matches from `gene_id` and `protein_acc` used separately.

The `filename` is used to load the ID data. The `filename` is only required on the first method call, however, it is safe the include the `filename` on every call.

The method will return a list of all gene name matches. A warning will output if the amount of matches is 0 or more than 1.

### How to consume
Example for running script from the command line: `python -c 'from dros_id_converter import retrieve_gene_name as rgn; print(str(rgn(protein_acc="M9NH29", filename="../res/gene_id_list.tsv")))'
`

`dros_id_converter_example.py` contains example for running script from another python script


