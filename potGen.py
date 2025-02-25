#
# Title: Potion Generator
# Author: Anna Vahtera, Copyright (c) 2025
#
# Version History:
# Version: 1.3.2a - Added support for past tense verbs.
# Version: 1.3.1a - Refined multi-combination support. Added support for "WordWord" and "VerbWordWord" combinations.
# Version: 1.3.0a - Added support for different word combinations.
# Version: 1.2.3a - Refined grammar check for "ing" form of verbs. Will remain unfinished, since there's no way to check syllable stress in English.
# Version: 1.2.2a - Added Syllable Counting for Verbs (PyHyphen)
# Version: 1.2.1a - Added grammar check for "ing" form of verbs
# Version: 1.2.0a - Added support for Verbs
# Version: 1.1.2a - Added ANSI Color Support and removed the need for the colored module
# Version: 1.1.1a - Added 'colored' support for potion effectiveness
# Version: 1.1.0a - Added support for Adjectives
# Version: 1.0.0a - Initial Release
#
# Description: This script generates random potion names using a list of adjectives and nouns. For use in tabletop games, writing, or just for fun.

import random
import string
import sys
from hyphen import Hyphenator # Import the Hyphenator Module for Syllable Counting
h_en = Hyphenator('en_US') # Set the Hyphenator to English
random.seed()
arguments = len(sys.argv) # Get Number of Arguments Passed to the Script

# Color Definitions
WHITE = "\033[37m" # White Text Color
BLUE = "\033[34m" # Blue Text Color
YELLOW = "\033[33m" # Yellow Text Color
GREEN = "\033[32m" # Green Text Color
RED = "\033[31m" # Red Text Color
CYAN = "\033[36m" # Cyan Text Color
PURPLE = "\033[35m" # Purple Text Color
BLACK = "\033[30m" # Black Text Color
BOLD = "\033[1m" # Bold Text
NOBOLD = "\033[22m" # No Bold Text
ENDC = "\033[0m" # Reset Text Color

def setNumPotions(): # Set Number of Entries to create
    t = 0
    if arguments > 1: # Check if Number of Entries is Passed as an Argument
        for l in range(1, arguments):
            if (sys.argv[l].isnumeric()):
                t = int(sys.argv[l])
    
    if t > 0: # Check if Number of Entries is Greater than 0 and Return that, otherwise Default to 5
        return t
    else:
        return 5

# Function to Generate the "ing" Form of the Verb
def ingForm(s):
    for x in s:
        lWord.append(x)
    if lWord[len(lWord)-1]=='e' and lWord[len(lWord)-2]!='i': # If the Last Letter is an 'e' and the Second to Last Letter is not an 'i'
        del lWord[len(lWord)-1] # Delete the Last Letter
        lWord.append("ing")
    elif lWord[len(lWord)-1]=='e' and lWord[len(lWord)-2]=='i': # If the Last Letter is an 'e' and the Second to Last Letter is an 'i'
        del lWord[len(lWord)-1]
        del lWord[len(lWord)-1]
        lWord.append("ying")
    elif lWord[len(lWord)-2] in 'aeiou' and lWord[len(lWord)-1] in arrDoublingConsonants and len(h_en.syllables(s)) < 2 and len(lWord) < 5: # If the Last Letter is a Consonant and the Second to Last Letter is a Vowel and the Syllable Count is Less than 2 and the Word is Less than 5 Letters
        #tWord = lWord[len(lWord)-1] # Store the Last Letter
        # del lWord[len(lWord)-1]
        # lWord.append(tWord)
        lWord.append(lWord[len(lWord)-1])
        lWord.append("ing")
    elif lWord[len(lWord)-1] in 'aeiouy': # If the Last Letter is a Vowel
        lWord.append("ing")
    else:
        lWord.append("ing")
    return "".join(lWord)


numPotions = setNumPotions() # Set the Number of Entries to Create
fileName = "english_nouns.txt" # File Name to Read the Words from
adjFileName = "english_adjectives.txt" # File Name to Read the Adjectives from
vrbFileName = "english_verbs.txt" # File Name to Read the Verbs from
pstVerbFileName = "english_verbs_past.txt" # File Name to Read the Past Tense Verbs from"

arrVowels = ["a", "e", "i", "o", "u"] # Array of Vowels to Check Against
arrConsonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] # Array of Consonants to Check Against
arrDoublingConsonants = ["b", "d", "g", "l", "m", "n", "p", "r", "t"] # Array of Consonants that Double when Adding "ing"
arrWordCombination = ["Word", "AdjWord", "VerAdjWord", "VerbWord", "AdjVerbWord", "AdjVerb", "Verb", "Adj", "WordWord", "VerbWordWord"] # Array of Word Combinations

arrColors = [WHITE, CYAN, YELLOW, GREEN, RED] # Array of Colors to Choose from
# Arrays of Containers and Liquids
arrContain = ["vial", "bottle", "potion", "flask", "ampoule", "ewer", "jar", "jug", "cup", "mug", "dose", "can", "chalice", "copita", "bowl", "goblet", "phial", "beaker", "carafe", "cruet", "decanter", "flagon", "gourd", "horn", "pewter", "porringer", "pot", "tankard", "tumbler", "urn", "vase", "vessel", "glass", "cask", "keg", "barrel", "canteen", "skin", "waterskin", "wineskin", "flagon"] # Array of Containers to Choose from
arrLiquid = ["juice", "sap", "fluid", "solution", "broth", "goop", "nectar", "elixir", "resin", "infusion", "essence", "brew", "drink", "concotion", "mixture", "beverage", "extract", "jelly", "soup", "oil", "syrup", "tonic", "tincture", "serum", "dew", "salve", "cream", "paste", "ointment", "balm", "lotion", "gel", "emulsion"] # Array of Liquids to Choose from

with open(fileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrWord = [line.strip() for line in f]

with open(adjFileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrAdjective = [line.strip() for line in f]

with open(vrbFileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrVerb = [line.strip() for line in f]

with open(pstVerbFileName, "r", encoding="utf-8") as f: # Open the File and Read the Lines into an Array
    arrPastVerb = [line.strip() for line in f]

# Print the Legend
print(BLACK + BOLD + "Legend: " + ENDC + WHITE + "Diluted" + ", " + ENDC + CYAN + "Mild" + ENDC + ", " + GREEN + "Moderate" + ENDC + ", " + YELLOW + "Strong" + ENDC + ", " + RED + "Very Strong" + ENDC + "\n")

for l in range(numPotions):   # Loop through the Number of Entries to Create and Randomly Select a Word from the List
    # Randomly Select a Container, Adjective, Word, Liquid, and Color
    valContain = arrContain[random.randint(0, (len(arrContain)-1))]
    valAdjective = arrAdjective[random.randint(0, (len(arrAdjective)-1))]
    valLiquid = arrLiquid[random.randint(0, (len(arrLiquid)-1))]
    valWord = arrWord[random.randint(0, (len(arrWord)-1))]
    valWord2 = arrWord[random.randint(0, (len(arrWord)-1))]
    valColor = arrColors[random.randint(0, (len(arrColors)-1))]
    valVerb = arrVerb[random.randint(0, (len(arrVerb)-1))]
    valPastVerb = arrPastVerb[random.randint(0, (len(arrPastVerb)-1))]
    valWordComb = arrWordCombination[random.randint(0, (len(arrWordCombination)-1))]
    lWord = [] # List to Store the Word 

    verbForm = random.randint(0, 1) # Randomly Select the Verb Form
    if verbForm == 0: # If the Verb Form is 0, Use the Past Tense
        finVerb = valPastVerb
    else: # Otherwise, Use the "ing" Form
        finVerb = ingForm(valVerb) # Get the "ing" Form of the Verb

    WORD = valWord.capitalize()
    WORD2 = valWord2.capitalize()
    ADJECTIVE = valAdjective.capitalize()
    VERB = finVerb.capitalize()
    LIQUID = valLiquid.capitalize()
    CONTAINER = valContain.capitalize()
    _EOL = " " + LIQUID + ENDC # End of Line
    _SOL = BLACK + BOLD + str(l+1).rjust(4, " ") + ": " + ENDC + valColor + CONTAINER + " of " + BOLD # Start of Line

    # Print the Potion Name
    match(valWordComb): # Select the Word Combination to Print
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