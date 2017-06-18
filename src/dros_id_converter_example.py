from dros_id_converter import retrieve_gene_name as rgn

if __name__ == "__main__":
    term_list = ["M9NH29", "P12426", "Q960Z4", "1433Z_DROME", "Q8SWR6_DROME", "FBgn0250848"]

    print("\nIterating term list")
    for input_term in term_list:
        print(str(rgn(term=input_term , filename="../res/gene_id_list_2.tsv")))
        
    