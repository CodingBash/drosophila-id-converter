# drosophila-id-converter

### Overview
Take a gene DB id, protein accession number, protein name, or protein DB id and retrieve the corresponding gene name

### Setup
Requires Python 3 (and PIP 3)

Download and extract this repository. Should have the following project directory

src/

---dros_id_converter.py

---dros_id_converter_example.py

res/

---gene_id_list_2.tsv


The only dependency the python script uses is `csv`. If the `csv` package isn't in the environment, run the command `pip3 install csv`

### Interface
`dros_id_converter.py` is the script that operates the conversion. The script method takes two arguments: `term` and `filename`

The `term` is the input for the ID you want to convert (i.e., gene DB id, protein accession number, protein name, or protein DB id)

The `filename` is the input of the filename which is a TSV file with all ID and gene name data

The `filename` is used to load the ID data. The `filename` is only required on the first method call, however, it is safe the include the `filename` on every call.

The method will return a list of all gene name matches. A warning will output if the amount of matches is 0 or more than 1.

### How to consume
Example for running script from the command line: `python -c 'from dros_id_converter import retrieve_gene_name as rgn; print(str(rgn(term="M9NH29", filename="../res/gene_id_list_2.tsv")))'
`

`dros_id_converter_example.py` contains example for running script from another python script


