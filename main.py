import spacy
import json

filename = "data/.txt"

with open(filename, "r", encoding="utf-8") as f:
    text = f.read().split("\n")
    # chapters = text.split("Den ")[1:]
# nlp = spacy.load("nl_core_news_sm")
# doc = nlp(text)
# sentences = list(doc.sents)

# ruler = nlp.add_pipe("entity_ruler")

print(text)