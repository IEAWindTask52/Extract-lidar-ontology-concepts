
def get_json_concept(path, lang):
    """
    # get the details of the concept based on the path where json file is stored

    Input:
        path = r'./Ontology_Concepts/VAD_da'
        lang = "en"

    Output:
        concept - dictionary containing substructure of concept
        concept['prefLabel'] gives the standard name
        concept['definition'] gives the definition of the concept
        concept['altLabel'] gives the abbreviation

    References:
    """

    import json

    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    concept = dict()
    for k,v in data['graph'][1].items():
        concept[k] = v
        if (type(v)==dict) and ('lang' in v):
            concept[k]=v['value']
        elif (type(v)==dict) and ('uri' in v):
            concept[k]['uri']=v['uri']
        elif type(v)==list:
            for f in v:
                if f['lang']==lang:
                    concept[k]=f['value']
        else:
            continue

    return concept

def get_rdf_concept(path, lang, fmt):
    """
    # get the details of the concept based on the path where rdf/xml or ttl file is stored

    Input:
        path = r"Ontology_Concepts/vad.ttl"
        lang = "en" (options: en/it/cn/de)
        fmt = "ttl" (options: xml/ttl)

    Output:
        concept - dictionary containing substructure of concept
        concept['prefLabel'] gives the standard name
        concept['definition'] gives the definition of the concept
        concept['altLabel'] gives the abbreviation

    Syntax:
        concept = get_rdf_concept(path, lang, fmt)

    References:
    https://github.com/cadmiumkitty/rdfpandas
    """

    from rdfpandas.graph import to_dataframe
    import pandas as pd
    import rdflib
    import sys
    sys.path

    g = rdflib.Graph()
    g.parse(path, format = fmt)
    df = to_dataframe(g)
    df = df[df.index.str.contains('VelocityAzimuthDisplay')]
    concept_df = pd.DataFrame()
    for x in df.filter(like='URIRef'):
        column_name = x.split(':')[1].split('{')[0]
        concept_df[column_name] = df[x].values
    for x in df.filter(like = "@"+lang):
        column_name =  x.split(':')[1].split('{')[0]
        if column_name not in concept_df:
            concept_df[column_name] = df[x].values
        else:
            continue

    concept = concept_df.to_dict(orient='records')

    return concept

def parseOntology(url, var_search_str, uri_search_str):
    # script to parse all the variables on the Ontology website of DTU
    # Input:
    # url - the input url for accessing the ontology (see example)
    # var_search_str - the variable search string in html format (can be identified from the structure of html)
    # uri_search_str -  the uri search string in html format (search through the html developer site for span + class_)
    # Output:
    # onto_paths - a dataframe output with variable, url_path and uri path (definition)
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np

    def parse_ontology_html(base_url, var_url):
        
        page = requests.get(var_url)
        soup = BeautifulSoup(page.content, "html.parser")
        content = soup.find_all("span", class_ = "versal concept-download-links")[0].find_all("a")
        # get the elements for page extraction
        output_links = [k for k in content if uri_search_str in str(k)]
        uri = [base_url + links["href"] for links in output_links]

        return uri
        

    # import parse_ontology_html

    page = requests.get(url)
    base_url = "https://data.windenergy.dtu.dk/ontologies/view/"

    soup = BeautifulSoup(page.content, "html.parser")
    # change if the structure on the website changes
    content = soup.find_all("a")

    # get the elements for page extraction
    onto_var = [k for k in content if var_search_str in str(k)]
    var_url = [(base_url + links["href"]) for links in onto_var]
    var_string = [links.text for links in onto_var]

    onto_paths = pd.DataFrame(np.transpose([var_string, var_url]), columns=['variable', 'var_url'])
    uri = onto_paths.var_url.apply(lambda x: parse_ontology_html(base_url,x))
    df_uri = pd.DataFrame(data=[*uri], columns=['uri_rdf', 'uri_ttl', 'uri_json'])
    onto_paths = onto_paths.join(df_uri)

    return onto_paths



if __name__ == "__main__":
    from getConcept import get_json_concept, get_rdf_concept, parseOntology

    # get ontology paths
    url = r"https://data.windenergy.dtu.dk/ontologies/view/ontolidar/en/index"
    var_search_str = "ontolidar/en/page"
    uri_search_str = "rest/v1/ontolidar/data?uri="
    
    onto_paths = parseOntology(url,var_search_str, uri_search_str)

    path = r'../Ontology_Concepts/VAD_da'
    lang = "en"
    concept_json = get_json_concept(path, lang)


    path = r'../Ontology_Concepts/vad.ttl'
    lang = "en"
    fmt = 'ttl'
    concept_rdf = get_rdf_concept(path, lang, fmt)



