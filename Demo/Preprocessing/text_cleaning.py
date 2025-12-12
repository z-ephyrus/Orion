import spacy
import re
from spellchecker import SpellChecker

nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()

#text = input("Enter a string \n")

def text_cleaning(text):
        
        text = re.sub(r'http\S+|www\.\S+',"",text)
        text = re.sub(r'\s+'," ",text).strip()
        text = text.encode("ascii","ignore").decode()
        doc = nlp(text)
        tokens = [
                        token.lemma_
                        for token in doc
                        if not token.is_space
                        and not token.is_punct
        ]
        corrected = []
        mispelled = spell.unknown(tokens)
        for word in tokens:
                if word in mispelled:
                        corrected.append(spell.correction(word))
                else:
                        corrected.append(word)

        cleaned = " ".join(corrected)
        print(cleaned)
        return cleaned,tokens