''' Potion Generator '''
#
# Title: Potion Generator
# Author: Anna Vahtera, Copyright (c) 2025
#
# Version History:
# Version: 1.3.5 - Updated to new libAnna and the colors module.
# Version: 1.3.4 - Changed to using libAnna and Python coding standards.
# Version: 1.3.3a - Removed the need for PyHyphen and changed into using a pre-formatted list.
# Version: 1.3.2a - Added support for past tense verbs.
# Version: 1.3.1a - Refined multi-combination support. Added support for more combinations.
# Version: 1.3.0a - Added support for different word combinations.
# Version: 1.2.3a - Refined grammar check for "ing" form of verbs.
# Version: 1.2.2a - Added Syllable Counting for Verbs (PyHyphen)
# Version: 1.2.1a - Added grammar check for "ing" form of verbs
# Version: 1.2.0a - Added support for Verbs
# Version: 1.1.2a - Added ANSI Color Support and removed the need for the colored module
# Version: 1.1.1a - Added 'colored' support for potion effectiveness
# Version: 1.1.0a - Added support for Adjectives
# Version: 1.0.0a - Initial Release
#
# Description: This script generates random potion names using a list of adjectives and nouns.
# For use in tabletop games, writing, or just for fun.

import random
import sys
from libAnna.functions import open_file, clear_screen
from libAnna.colors import *

random.seed()
arguments = len(sys.argv) # Get Number of Arguments Passed to the Script

def set_num_potions():
    '''Set Number of Entries to create'''
    t = 0
    if arguments > 1: # Check if Number of Entries is Passed as an Argument
        for i in range(1, arguments):
            if sys.argv[i].isnumeric():
                t = int(sys.argv[i])

    if t > 0: # Check if Number of Entries is Greater than 0 and Return that, otherwise Default to 5
        return t

    return 5

NUM_POTIONS = set_num_potions() # Set the Number of Entries to Create
FILE_NAME = "english_nouns.txt" # File Name to Read the Words from
ADJ_FILE_NAME = "english_adjectives.txt" # File Name to Read the Adjectives from
VRB_FILE_NAME = "english_verbs_ing.txt" # File Name to Read the Verbs from
PST_VERB_FILE_NAME = "english_verbs_past.txt" # File Name to Read the Past Tense Verbs from

ARR_VOWELS = ["a", "e", "i", "o", "u"] # Array of Vowels to Check Against
ARR_CONSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t",
                 "v", "w", "x", "y", "z"] # Array of Consonants to Check Against
ARR_DOUBLING_CONSONANTS = ["b", "d", "g", "l", "m", "n", "p", "r", "t"]
ARR_WORD_COMBINATION = ["Word", "AdjWord", "VerAdjWord", "VerbWord", "AdjVerbWord", "AdjVerb",
                        "Verb", "Adj", "WordWord", "VerbWordWord"] # Array of Word Combinations

ARR_COLORS = [WHITE, CYAN, YELLOW, GREEN, RED] # Array of Colors to Choose from
# Arrays of Containers and Liquids
ARR_CONTAIN = ["vial", "bottle", "potion", "flask", "ampoule", "ewer", "jar", "jug", "cup", "mug",
               "dose", "can", "chalice", "copita", "bowl", "goblet", "phial", "beaker", "carafe",
               "cruet", "decanter", "flagon", "gourd", "horn", "pewter", "porringer", "pot",
               "tankard", "tumbler", "urn", "vase", "vessel", "glass", "cask", "keg", "barrel",
               "canteen", "skin", "waterskin", "wineskin", "flagon"] # Array of Containers
ARR_LIQUID = ["juice", "sap", "fluid", "solution", "broth", "goop", "nectar", "elixir", "resin",
              "infusion", "essence", "brew", "drink", "concotion", "mixture", "beverage",
              "extract", "jelly", "soup", "oil", "syrup", "tonic", "tincture", "serum", "dew",
              "salve", "cream", "paste", "ointment", "balm", "lotion", "gel", "emulsion"]

ARR_WORD = open_file(FILE_NAME)
ARR_ADJECTIVE = open_file(ADJ_FILE_NAME)
ARR_VERB = open_file(VRB_FILE_NAME)
ARR_PAST_VERB = open_file(PST_VERB_FILE_NAME)

clear_screen()

# Print the Legend
print(BLACK + BOLD + "Legend: " + ENDC + WHITE + "Diluted" + ", " + ENDC + CYAN + "Mild" + ENDC +
      ", " + GREEN + "Moderate" + ENDC + ", " + YELLOW + "Strong" + ENDC + ", " + RED +
      "Very Strong" + ENDC + "\n")

for l in range(NUM_POTIONS):   # Loop through the Number of Entries to Randomly Select a Word
    # Randomly Select a Container, Adjective, Word, Liquid, and Color
    val_contain = ARR_CONTAIN[random.randint(0, (len(ARR_CONTAIN)-1))]
    val_adjective = ARR_ADJECTIVE[random.randint(0, (len(ARR_ADJECTIVE)-1))]
    val_liquid = ARR_LIQUID[random.randint(0, (len(ARR_LIQUID)-1))]
    val_word = ARR_WORD[random.randint(0, (len(ARR_WORD)-1))]
    val_word2 = ARR_WORD[random.randint(0, (len(ARR_WORD)-1))]
    val_color = ARR_COLORS[random.randint(0, (len(ARR_COLORS)-1))]
    val_verb = ARR_VERB[random.randint(0, (len(ARR_VERB)-1))]
    val_past_verb = ARR_PAST_VERB[random.randint(0, (len(ARR_PAST_VERB)-1))]
    val_word_comb = ARR_WORD_COMBINATION[random.randint(0, (len(ARR_WORD_COMBINATION)-1))]
    l_word = [] # List to Store the Word

    verb_form = random.randint(0, 1) # Randomly Select the Verb Form
    if verb_form == 0: # If the Verb Form is 0, Use the Past Tense
        fin_verb = val_past_verb
    else: # Otherwise, Use the "ing" Form
        fin_verb = val_verb # Get the "ing" Form of the Verb

    WORD = val_word.capitalize()
    WORD2 = val_word2.capitalize()
    ADJECTIVE = val_adjective.capitalize()
    VERB = fin_verb.capitalize()
    LIQUID = val_liquid.capitalize()
    CONTAINER = val_contain.capitalize()
    _EOL = " " + LIQUID + ENDC # End of Line
    _SOL = BLACK + BOLD + str(l+1).rjust(4, " ") + ": " + ENDC + val_color + CONTAINER + \
        " of " + BOLD # Start of Line

    # Print the Potion Name
    match(val_word_comb): # Select the Word Combination to Print
        case "Word":
            print(_SOL + WORD + NOBOLD + _EOL)
        case "AdjWord":
            print(_SOL + ADJECTIVE + " " + WORD + NOBOLD + _EOL)
        case "VerAdjWord":
            print(_SOL + VERB + " " + ADJECTIVE + " " + WORD + NOBOLD + _EOL)
        case "VerbWord":
            print(_SOL + VERB + " " + WORD + NOBOLD + _EOL)
        case "AdjVerbWord":
            print(_SOL + ADJECTIVE + " " + VERB + " " + WORD + NOBOLD + _EOL)
        case "AdjVerb":
            print(_SOL + ADJECTIVE + " " + VERB + NOBOLD + _EOL)
        case "Verb":
            print(_SOL + VERB + NOBOLD + _EOL)
        case "Adj":
            print(_SOL + ADJECTIVE + NOBOLD + _EOL)
        case "WordWord":
            print(_SOL + WORD + " " + WORD2 + NOBOLD + _EOL)
        case "VerbWordWord":
            print(_SOL + VERB + " " + WORD + " " + WORD2 + NOBOLD + _EOL)
        case _: # Default to Word
            print(_SOL + WORD + NOBOLD + _EOL)

print("\n")
