
puntuaciones = ["love", 15, 30, 40, "Deuce", "ventaja"]

secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

def tennisMatch(input):
    for i in range(0, len(input),1):
        
        match input[i]:
            case 0 if i == "P1": 
                print("15 - Love")
            case 1 if i == "P1": 
                print("30 - Love")
            case 2 if i == "P2": 
                print("15 - 30")
            case 3 if i == "P2": 
                print("Deuce")
            case 4 if i == "P1": 
                print("40 - 30")
            case 5 if i == "P2": 
                print("40 - 30")
            case 6 if i == "P1": 
                print("Ventaja P1")
            case 7 if i == "P1": 
                print("Ha ganado el P1")
            case _:
                print("No winner")
        # if input[0] == "P1":
        #     print("15 - Love")
        # else:
        #     print("No winner")
        

tennisMatch(secuencia)        