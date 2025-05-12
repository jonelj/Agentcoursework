import json
import difflib
import re

'''
This file uses fuzzy matching to correct erroneous text in the corresponding category
'''

def load_keywords(label):
    path = f"data/AgenKinds/{label}_keywords.json"
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def correct_spelling(label, sentence, cutoff=0.8):
    """
    label:  "animal"/"portrait"/"landscape"
    sentence: original sentence to be corrected
    cutoff:   fuzzy Matching threshold,
    the lower the fault tolerance the stronger the original sentence to be corrected
    """
    if label == "others":
        return sentence
    else:
        keywords = load_keywords(label)
        tokens = re.findall(r"\w+|\W+", sentence)
        corrected = []
        for tok in tokens:
            # If it's a purely alphabetic word, try correcting
            if tok.isalpha():
                # not change what's already in the dictionary.
                if tok.lower() in keywords:
                    corrected.append(tok)
                else:
                    # fuzzy matches closest keywords
                    match = difflib.get_close_matches(tok.lower(), keywords, n=1, cutoff=cutoff)
                    if match:
                        # Retain original case styles
                        m = match[0]
                        if tok[0].isupper():
                            m = m.capitalize()
                        corrected.append(m)
                    else:
                        corrected.append(tok)
            else:
                # Spaces or punctuation, direct retention
                corrected.append(tok)

        return "".join(corrected)

if __name__ == "__main__":
    label = "landscape"
    orig = "a giant cliffft near the sea"
    fixed = correct_spelling(label, orig)
    print(f"original sentence: {orig}")
    print(f"corrected sentence: {fixed}")
