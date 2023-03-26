punishment_pattern = r"(ter dood gebragt|)"
@Language.component("find_punishment")
def find_punishment(doc):
    text = doc.text
    new_ents = []
    original_ents = list(doc.ents)
    legal = ["vonis", "straf", "Scherpregter"]
    for match in re.finditer(punishment_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        context = text[start-100:end+100]
        if any(term in context.lower() for term in legal):
            if span is not None:
                new_ents.append((span.start, span.end, span.text))
            else:
                span = doc.char_span(start, end-1)
                if span is not None:
                    new_ents.append((span.start, span.end-1, span.text))
    for ent in new_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="SHIP")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)
nlp.add_pipe("find_ships", before="ner")
