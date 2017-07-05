from dros_id_converter import find_gene_name as fgn, retrieve_gene_name_facilitator as rgnf, Preferences

if __name__ == "__main__":
    term_list = ["M9NH29", "P12426", "Q960Z4", "1433Z_DROME", "Q8SWR6_DROME", "FBgn0250848"]
    unknown_term_list = ["POL3_DROME", "E8NH50_DROME", "Q9VXG3_DROME", "Q7YTZ8_DROME", "Y7446_DROME", "Q4V3M5_DROME", "Q8INZ4_DROME"]

    #print("\nIterating term list")
    #for input_term in term_list:
    #    print(str(rgn(term=input_term , filenames=["../res/mortimer_gene_ids.txt", "../res/flymine_id_list_3.tsv"])))
        
    print("\nIterating term list with new method")
    for input_term in term_list+unknown_term_list:
        print(rgnf(input_term=input_term, input_filenames=["../res/mortimer_gene_ids.txt", "../res/flymine_id_list_3.tsv"],
                        preferences=Preferences(prefer_small_gene_names=True, prefer_first_selection_on_multiple=True, prefer_remember_selection=True, prefer_output=False))
    )
        
    #
    # Testing Remember History
    #
    print(rgnf(input_term="FBgn0053855", input_filenames=["../res/mortimer_gene_ids.txt", "../res/flymine_id_list_3.tsv"], 
                        preferences=Preferences(prefer_small_gene_names=True, prefer_first_selection_on_multiple=False, prefer_remember_selection=True, prefer_output=False)))
    print(rgnf(input_term="FBgn0053855", input_filenames=["../res/mortimer_gene_ids.txt", "../res/flymine_id_list_3.tsv"], 
                        preferences=Preferences(prefer_small_gene_names=True, prefer_first_selection_on_multiple=False, prefer_remember_selection=True, prefer_output=False)))
    
       