import numpy as np
from collections import defaultdict
from utils import get_word_tag

def get_counters(corpus, vocab):
    transition = defaultdict(int)
    emission = defaultdict(int)
    tagcount = defaultdict(int)
    
    prev_tag = '--s--'
    for i, word_tag in enumerate(corpus):
        word, tag = get_word_tag(word_tag, vocab)
        transition[(prev_tag, tag)] += 1
        emission[(tag, word)] += 1
        tagcount[tag] += 1
        
        prev_tag = tag 
    return emission, transition, tagcount

def get_transition_mat(transition_counts, tag_counts, alpha):
    states = sorted(tag_counts.keys())
    ntags = len(tag_counts)
    A = np.zeros((ntags,ntags))
    for i in range(ntags):
        for j in range(ntags):
            key = (states[i], states[j])
            count = 0
            if key in transition_counts:
                count = transition_counts[key]
            prev_tag_count = tag_counts[states[i]]
            A[i,j] = (count+alpha) / (prev_tag_count + ntags * alpha)
    return A

def get_emission_mat(emission_counts, tag_counts, vocab, alpha):
    states = sorted(tag_counts.keys())
    ntags = len(tag_counts)
    nwords = len(vocab)
    B = np.zeros((ntags, nwords))
    for i in range(ntags):
        for j in range(nwords):
            key = (states[i], vocab[j])
            count = 0
            if key in emission_counts:
                count = emission_counts[key]
            tag_count = tag_counts[states[i]]
            B[i, j] = (count + alpha) / (tag_count + nwords * alpha)
    return B
    