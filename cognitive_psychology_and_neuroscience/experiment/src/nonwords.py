import random
import nltk
import sys
from nltk.corpus import words

# Function to check if a word is valid using WordsAPI
def generate_nonword_strings(num_strings):
    nltk.download('words')

    nonword_list = []
    existing_words = set()  # A set to store generated nonwords

    # Get a set of all valid English words
    real_words = set(words.words())

    consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y",
                      "z", "ch", "th", "sh", "st", "ph", "sp", "sc", "sk", "sm", "sch",]

    onset_only_list = [
        "qu", "bl", "cl", "gl", "kl", "pl", "sl", "zl",  # existing onsets
        "br", "cr", "dr", "fr", "gr", "pr", "tr",  # new onsets with "r"
        "wh",  # digraphs
        "fl", "gl", "pl", "bl", "sl", "cl",  # common two-letter clusters with "l"
        "sn", "sp", "sw", "tw", "wr",  # new initial blends
        "shr", "spl", "spr", "str", "thr"  # three-letter onsets
    ]

    coda_only_list = [
        "ct", "ft", "lk", "lp", "lt", "mp", "nd", "nt", "pt", "rt", "ng",  # new common coda clusters
        "ld", "rd", "rch", "lch", "nch", "mch", "rch", "rth", "nth", "rsh",  # new ending blends
    ]

    vowel_list = [
        "a", "e", "i", "o", "u", "oo", "ou", "ee", "ea",  # existing vowels
        "ai", "au", "aw", "ea", "ee", "ei", "ie", "oa", "oe", "oi",  # new vowel digraphs
        "ou", "ow", "ue", "ui",  # more vowel combinations
    ]

    # Combine consonant list and onset-only list for possible onsets
    onset_list = consonant_list + onset_only_list
    # Combine consonant list and coda-only list for possible codas
    coda_list = consonant_list + coda_only_list

    while len(nonword_list) < num_strings:
        # Generate a random onset, vowel, and coda
        onset = random.choice(onset_list)
        vowel = random.choice(vowel_list)
        coda = random.choice(coda_list)

        # Form the nonword string
        nonword = onset + vowel + coda

        # Check if the nonword is already in the list or is a real word
        if nonword not in existing_words and nonword.lower() not in real_words:
            nonword_list.append(nonword)
            existing_words.add(nonword)  # Add to dictionary to avoid duplicates

    return nonword_list

def main():
    n = int(sys.argv[1])
    nonword_list = generate_nonword_strings(n)
    for word in nonword_list:
        print(word)

if __name__ == '__main__':
    main()