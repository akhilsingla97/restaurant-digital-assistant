# This module identifies specifications of Named entities, which could be anything- Example: McDonalds as an ORG, U.K. as a country

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I want to order a cheese burger from McDonalds')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
