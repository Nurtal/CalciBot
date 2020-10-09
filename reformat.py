

def craft_short_list():
    """
    """

    ## importation
    import pandas as pd

    ## parameters
    raw_file = "GeneCards-SearchResults.csv"
    n = 3000
    output_filename = "gene_short_list.csv"

    ## load dataset
    df = pd.read_csv(raw_file)
    df = df.head(n)

    ## save dataset
    df.to_csv(output_filename)




def scan_gene_card_info(adress):
    """
    """

    ## importation
    from bs4 import BeautifulSoup
    import requests

    url = 'https://google.com'
    name = requests.get(url)


    soup = BeautifulSoup(name.content, 'html.parser')

    print(soup.Publication)


## RUN
#craft_short_list()
scan_gene_card_info("https://www.genecards.org/cgi-bin/carddisp.pl?gene=CACNA1A")
