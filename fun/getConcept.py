
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

if __name__ == "__main__":
    from fun.getConcept import get_json_concept
    from fun.getConcept import get_rdf_concept

    path = r'./Ontology_Concepts/VAD_da'
    lang = "en"
    concept_json = get_json_concept(path, lang)


    path = r'./Ontology_Concepts/vad.ttl'
    lang = "en"
    fmt = 'ttl'
    concept_rdf = get_rdf_concept(path, lang, fmt)



