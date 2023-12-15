
#from list solution
#END cases
def hackingLanguage():
    
    text = "javier el habil zapatero trabajaba con destreza en su pequeño taller su bufanda azul ondeaba mientras tarareaba alegremente una cancion antigua con una taza de te caliente en la mano examinaba cuidadosamente cada zapato buscando imperfecciones de repente un zumbido interrumpio su rutina tranquila un abejorro curioso exploraba las flores de un jardin cercano javier asombrado observo como el insecto se movia entre las violetas y los girasoles llevando consigo la esencia de la primavera con una sonrisa retomo su labor disfrutando de la paz que le brindaba su oficio y la naturaleza circundante"
    
    # list = []
    # i = 0
    listing = text.replace(" ","")
    # for letter in text:
    #     list.append(letter)
    #     return list
    return listing
    # for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    # for i in range(len(list)):

def gettingHack(input):
    
    # for i in range(input):
    for i in input:
    
        if i == "a":
            letter1 = "4"
            i = letter1
            print(i)
        elif i == "b":
            letter2 = "13"
            i = letter2
            print(i)
        elif i == "c":
            letter3 = "["
            i = letter3
        elif i == "d":
            letter4 = ")"
            i = letter4
            print(i)
        elif i == "e":
            letter5 = "3"
            i = letter5
            print(i)
        elif i == "f":
            letter6 = "|="
            i = letter6
            print(i)
        elif i == "g":
            letter7 = "&"
            i = letter7
            print(i)
        elif i == "h":
            letter8 = "#"
            i = letter8
            print(i)
        elif i == "i":
            letter9 = "1"
            i = letter9
            print(i)
        elif i == "j":
            letter10 = ",_|"
            i = letter10
            print(i)
        elif i == "k":
            letter11 = ">|"
            i = letter11
            print(i)
        elif i == "l":
            letter12 = "1"
            i = letter12
            print(i)
        elif i == "m":
            letter13 = '"/\/\"'
            i = letter13
            print(i)
        elif i == "n":
            letter14 = "^/"
            i = letter14
            print(i)
        elif i == "o":
            letter15 = "0"
            i = letter15
            print(i)
        elif i == "p":
            letter16 = "|*"
            i = letter16
            print(i)
        elif i == "q":
            letter17 = "(_,)"
            i = letter17
            print(i)
        elif i == "r":
            letter18 = "i2"
            i = letter18
            print(i)
        elif i == "s":
            letter19 = "5"
            i = letter19
            print(i)
        elif i == "t":
            letter20 = "7"
            i = letter20
            print(i)
        elif i == "u":
            letter21 = "(_)"
            i = letter21
            print(i)
        elif i == "v":
            letter22 = "\/"
            i = letter22
            print(i)
        elif i == "w":
            letter23 = "\/\/"
            i = letter23
            print(i)
        elif i == "x":
            letter24 = "><"
            i = letter24
            print(i)
        elif i == "y":
            letter25 = "j"
            i = letter25
            print(i)
        elif i == "z":
            letter26 = "2"
            i = letter26
            print(i)
        else:
            print(i)
            
gettingHack(hackingLanguage())

#from string solution
#convert a string to a list and iterate it