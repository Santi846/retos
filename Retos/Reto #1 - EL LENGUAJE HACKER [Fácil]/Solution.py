
#from list solution
#END cases
def hackingLanguage():
    
    for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        
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
        else:
            print("Otra letra")
                
hackingLanguage()

#from string solution
#convert a string to a list and iterate it