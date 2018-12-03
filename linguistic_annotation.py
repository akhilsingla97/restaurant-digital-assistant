import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I would like to have a burger')
for token in doc:
    print(token.text, token.pos_, token.dep_)
