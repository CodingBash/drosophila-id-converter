from dros_id_converter import retrieve_gene_name as rgn

if __name__ == "__main__":
    protein_acc_list = ["M9NH29", "P12426", "Q960Z4"]
    gene_id_list = ["FBgn0000163", "FBgn0000239", "FBgn0000286"]
    unknown_list = ["P07183", "FBgn0000427", "A0A0B4KET9"]
    
    print("\nIterating protein_acc_list")
    for input_protein_acc in protein_acc_list:
        print(str(rgn(protein_acc=input_protein_acc , filename="../res/gene_id_list.tsv")))
        
    print("\nIterating gene_id_list")
    for input_gene_id in gene_id_list:
        print(str(rgn(gene_id=input_gene_id, filename="../res/gene_id_list.tsv")))
    
    print("\nIterating unknown_list")
    for input_unknown in unknown_list:
        print(str(rgn(unknown=input_unknown, filename="../res/gene_id_list.tsv")))
    