def getLabel(path, key, lang, index_inScheme):
    import json
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    if key in data['graph'][index_inScheme].keys():
        for index_def in range(len(data['graph'][index_inScheme][key])):
            try:
                src = data['graph'][index_inScheme][key][index_def]
                items0 = data['graph'][index_inScheme][key][index_def].items()
            except KeyError:
                src = data['graph'][index_inScheme][key]
                items0 = data['graph'][index_inScheme][key].items()
        
        # Select idiom
            if lang == 'en' and ('lang','en') in items0:
                Value = list(src.values())[1]
        
            elif lang == 'es' and ('lang','es') in items0:
                Value = list(src.values())[1]
        
            elif lang == 'cn' and  ('lang','cn') in items0:
                Value = list(src.values())[1]
        
            elif lang == 'it' and  ('lang','it') in items0:
                Value = list(src.values())[1]
    return Value

if __name__ == "__main__":
    from getLabel import getLabel
    path = r'../Ontology_Concepts/VAD_da'
    Alternative_Label = getLabel(path, key = "altLabel", lang='en', index_inScheme=1)

