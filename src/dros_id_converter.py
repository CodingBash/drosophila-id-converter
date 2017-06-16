import csv

class Entry:
    def __init__(self, gene_id="", gene_name="", protein_acc=""):
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.protein_acc = protein_acc
        
gene_container = list()

def read_id_file(filename):
    with open(filename, 'rt') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')    
        for row in tsvin:
            gene_container.append(Entry(row[0], row[1], row[2]))
    return gene_container
                
def retrieve_gene_name(gene_id="", protein_acc="", unknown="", filename=""):
    if len(gene_container) == 0:
        print("INFO: Loading " + filename)
        read_id_file(filename)
    
    search_gene_id = True if gene_id != "" else False
    search_protein_acc = True if protein_acc != "" else False
    search_unknown = True if unknown != "" else False
    
    matches = []
    if search_unknown:
        matches = list(set([entry.gene_name for entry in gene_container if entry.gene_id == unknown or entry.protein_acc == unknown]))
    elif search_gene_id and not search_protein_acc:
        matches = list(set([entry.gene_name for entry in gene_container if entry.gene_id == gene_id]))
    elif search_protein_acc and not search_gene_id:
        matches = list(set([entry.gene_name for entry in gene_container if entry.protein_acc == protein_acc]))
    elif search_gene_id and search_protein_acc:
        gene_id_matches = [entry.gene_name for entry in gene_container if entry.gene_id == gene_id]
        protein_acc_matches = [entry.gene_name for entry in gene_container if entry.protein_acc == protein_acc]
        matches = list(set(gene_id_matches) & set(protein_acc_matches))
    
    if len(matches) == 0:
        print('WARNING: No matches found for gene_id="' + gene_id + '" and protein_acc="' + protein_acc + '"')
    elif len(matches) > 1:
        print('WARNING: ' + str(len(matches)) + '  matches found for gene_id="' + gene_id + '" and protein_acc="' + protein_acc + '" with matches="' + str(matches) + '"')
    return matches
    
    
# TEST
if __name__ == "__main__":
    print(retrieve_gene_name(gene_id="FBgn0000028", protein_acc="M9NH29", unknown="", filename="../res/gene_id_list.tsv"))
    