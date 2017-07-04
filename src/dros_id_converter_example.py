from dros_id_converter import retrieve_gene_name as rgn

if __name__ == "__main__":
    term_list = ["M9NH29", "P12426", "Q960Z4", "1433Z_DROME", "Q8SWR6_DROME", "FBgn0250848"]
    unknown_term_list = ["POL3_DROME", "E8NH50_DROME", "Q9VXG3_DROME", "Q7YTZ8_DROME", "Y7446_DROME", "Q4V3M5_DROME", "Q8INZ4_DROME"]

    print("\nIterating term list")
    for input_term in unknown_term_list:
        print(str(rgn(term=input_term , filenames=["../res/mortimer_gene_ids.txt", "../res/flymine_id_list_3.tsv"])))
        
    