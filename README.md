# Part of Speech Tagger with Hidden Markov Models and Viterbi Algorithm

This project implements a Hidden Markov Model (HMM) for natural language processing tasks, specifically for part-of-speech tagging.

## Files

### `markov.py`
Contains the implementation of key HMM components:
- **`get_counters`**: Processes a labeled corpus to compute the transition, emission, and tag counts.
- **`get_transition_mat`**: Generates the transition probability matrix using Laplace smoothing.
- **`get_emission_mat`**: Generates the emission probability matrix using Laplace smoothing.

### `utils.py`
Provides utility functions used throughout the project:
- **`get_word_tag`**: Extracts a word and its tag from a corpus line, handling unknown words.
- **`preprocess`**: Prepares a dataset by replacing unknown words with specialized tokens.
- **`assign_unknown`**: Classifies unknown words based on their characteristics (e.g., digits, punctuation, suffixes).

### `main.ipynb`
This file likely contains the main workflow for training and evaluating the HMM tagger using the above implementations.

## How It Works
1. **Data Preparation**: The corpus is preprocessed using `utils.py` to handle unknown words.
2. **Training**: The `markov.py` functions compute:
   - Transition probabilities: The likelihood of transitioning between tags.
   - Emission probabilities: The likelihood of a word being associated with a specific tag.
3. **Evaluation**: The generated matrices can be used to predict tags for unseen sentences.


## Steps
1. Prepare your vocabulary file and labeled dataset.
2. Import the required functions from `markov.py` and `utils.py`.
3. Preprocess the dataset:
   ```python
   from utils import preprocess
   orig, prep = preprocess(vocab, "data.txt")
   ```
4. Compute the HMM parameters:
   ```python
   from markov import get_counters, get_transition_mat, get_emission_mat

   emission, transition, tag_count = get_counters(prep, vocab)
   A = get_transition_mat(transition, tag_count, alpha=0.1)
   B = get_emission_mat(emission, tag_count, vocab, alpha=0.1)
   ```
5. Use the matrices `A` and `B` for tag prediction.

### Example
An example workflow can be found in the `main.ipynb` file.

