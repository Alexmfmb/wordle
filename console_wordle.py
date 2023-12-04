import random as rnd
import os



game_end = False

print(20*"-" + " WORDLE " + 20*"-")

#select number of characters to play with
char_num = input("Buchstabenanzahl: ")

umlaute_raus = input("Sollen im Spiel Umlaute (ä,ö,ü,ß) vorkommen? (N --> ä wird zu ae, ß wird zu ss) (Y/N): ")
if umlaute_raus == "N" or umlaute_raus == "n": umlaute_raus = True
else: umlaute_raus = False

#set data path
cwd = os.getcwd()
word_data_path = os.path.join(cwd,'worddata','worddata_de')

if umlaute_raus: 
    word_data_path += "_ae_ss"

word_data_path += '_' + char_num +'_char.txt'

#import data
with open(word_data_path, 'r') as word_file:
    words = word_file.read().splitlines()

#convert all words in list to lowercase
for i in range(len(words)):
    words[i] = words[i].lower()

#choose random solution
solution = words[rnd.randint(0,len(words)-1)]

#set custom solution
#solution = input("custom solution:")

#list of guessed characters
w_guess = []

counter = 0

#----------------------------------------------------------------------------

while(game_end != True):
    counter += 1
    inp = ""

    #check validity pf input
    while inp not in words:
        inp = input("↪ ").lower()

        #show solution with password
        if inp == "1234": 
            print("Das gesuchte Wort war " + solution.upper())

        #hint mechanism
        if inp in [str(x) for x in range(1,int(char_num) + 1)]:
            print(f"Tipp: An Position {inp} steht " + str(solution[int(inp)-1]))

    #feedback to guess
    s = ""
    for i in range(len(inp)):
        if inp[i] not in solution: 
            s += "🟥"
            if inp[i] not in w_guess: w_guess.append(inp[i])

        if inp[i] == solution[i]: s += "🟩"

        if inp[i] in solution and inp[i] != solution[i]: s += "🟨"
    print(" " + " ".join(inp).upper())

    #sort list of wrongly guessed characters
    w_guess.sort()

    #add list of wrongly guessed characters
    s += "   Wrong guesses: " 
    for character in w_guess:
        s += character.upper() + ", "

    #print feedback
    print(s)

    #check if guess is correct
    if (inp == solution): game_end = True

print("Richtige Lösung nach " + str(counter) + " Versuchen")

a = input("Press any key to exit")




    