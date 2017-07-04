import csv

class Entry:
    def __init__(self, protein_db_id="", protein_acc="", gene_db_id="", gene_name="", sec_id=""):
        self.gene_db_id = gene_db_id
        self.gene_name = gene_name
        self.protein_acc = protein_acc
        self.protein_db_id = protein_db_id
        self.sec_id = sec_id
        
gene_container = list()

def read_id_file(filenames):
    for file in filenames:
        with open(file, 'rt') as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')    
            for row in tsvin:
                sec_id =""
                try:
                    sec_id = row[4]
                except IndexError:
                    pass
                gene_container.append(Entry(row[0], row[1], row[2], row[3], sec_id))
                
def retrieve_gene_name(term, filenames=[], debug=True):
    if len(gene_container) == 0:
        if debug: print("INFO: Loading " + str(filenames))
        read_id_file(filenames)
        
    
    matches = [(entry.gene_name, entry.sec_id) for entry in gene_container if entry_exist(entry, term)]
    if len(matches) == 0:
        result = ([],[])
    else:
        gene_names, sec_ids = zip(*matches)
        result= (list(set([gene_name for gene_name in gene_names if gene_name.strip() != ""])), list(set([sec_id for sec_id in sec_ids if sec_id.strip() != ""])))    
    
    if len(result[0]) == 0:
        if debug: print('WARNING: No matches found for term="' + term + '"')
    elif debug and len(result[0]) > 1:
        if debug: print('WARNING: ' + str(len(result[0])) + '  matches found for term="' + term + '"')
    
    return result
    
def entry_exist(entry, term):
        return entry.gene_db_id.upper() == term.upper() or entry.protein_acc.upper() == term.upper() or entry.protein_db_id.upper() == term.upper() 

# TEST
if __name__ == "__main__":
    print(retrieve_gene_name(term="FBgn0053855", filenames=["../res/mortimer_gene_ids.txt", "../res/flymine_id_list_3.tsv"], debug=False))
    