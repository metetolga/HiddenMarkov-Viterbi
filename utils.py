import string

punct = set(string.punctuation)

noun_suffix = ["action", "age", "ance", "cy", "dom", "ee", "ence", "er", "hood", "ion", "ism", "ist", "ity", "ling", "ment",
               "ness", "or", "ry", "scape", "ship", "ty"]
verb_suffix = ["ate", "ify", "ise", "ize"]
adj_suffix = ["able", "ese", "ful", "i", "ian", "ible", "ic", "ish", "ive", "less", "ly", "ous"]
adv_suffix = ["ward", "wards", "wise"]


def get_word_tag(line, vocab): 
    if not line.split():
        word = "--n--"
        tag = "--s--"
        return word, tag
    else:
        word, tag = line.split()
        if word not in vocab: 
            word = assign_unknown(word)
        return word, tag
    return None 


def preprocess(vocab, data_fp):
    orig = []
    prep = []

    with open(data_fp, "r") as data_file:

        for cnt, word in enumerate(data_file):

            if not word.split(): # end of sentence
                orig.append(word.strip())
                word = "--n--"
                prep.append(word)
                continue
            elif word.strip() not in vocab: # if word does not appear in vocabulary
                orig.append(word.strip())
                word = assign_unknown(word)
                prep.append(word)
                continue
            else:
                orig.append(word.strip())
                prep.append(word.strip())

    assert(len(orig) == len(open(data_fp, "r").readlines()))
    assert(len(prep) == len(open(data_fp, "r").readlines()))

    return orig, prep


def assign_unknown(tok):
    if any(char.isdigit() for char in tok): # integers/digit
        return "--unk_digit--"
    elif any(char in punct for char in tok): # punctuation
        return "--unk_punct--"
    elif any(char.isupper() for char in tok): # upper word
        return "--unk_upper--"
    elif any(tok.endswith(suffix) for suffix in noun_suffix): # nouns
        return "--unk_noun--"
    elif any(tok.endswith(suffix) for suffix in verb_suffix): # verbs
        return "--unk_verb--"
    elif any(tok.endswith(suffix) for suffix in adj_suffix): # adjectives
        return "--unk_adj--"
    elif any(tok.endswith(suffix) for suffix in adv_suffix): # adverb
        return "--unk_adv--"
    return "--unk--" # rather unknown

