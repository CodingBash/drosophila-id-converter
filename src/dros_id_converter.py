import csv

class Entry:
    def __init__(self, protein_db_id="", protein_acc="", gene_db_id="", gene_name=""):
        self.gene_db_id = gene_db_id
        self.gene_name = gene_name
        self.protein_acc = protein_acc
        self.protein_db_id = protein_db_id
        
gene_container = list()

def read_id_file(filename):
    with open(filename, 'rt') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')    
        for row in tsvin:
            gene_container.append(Entry(row[0], row[1], row[2], row[3]))
    return gene_container
                
def retrieve_gene_name(term, filename=""):
    if len(gene_container) == 0:
        print("INFO: Loading " + filename)
        read_id_file(filename)
        
    
    matches = list(set([entry.gene_name for entry in gene_container if entry_exist(entry, term)]))    
    
    if len(matches) == 0:
        print('WARNING: No matches found for term="' + term + '"')
    elif len(matches) > 1:
        print('WARNING: ' + str(len(matches)) + '  matches found for term="' + term + '"')
    
    return matches
    
def entry_exist(entry, term):
        return entry.gene_db_id == term or entry.protein_acc == term or entry.protein_db_id == term 

# TEST
if __name__ == "__main__":
    print(retrieve_gene_name(term="Q0E8P0_DROME", filename="../res/gene_id_list_2.tsv"))
    