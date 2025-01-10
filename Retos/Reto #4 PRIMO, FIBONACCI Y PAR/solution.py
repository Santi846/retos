
number1 = 25

def validation(input):
  
  if (input >= 2):

    par = input % 2

    if(par != 0):
        raiz_cuadrada = input ** 0.5
        raiz_decimal = round(int(raiz_cuadrada))
        
        for x in range(2, raiz_decimal + 1):
            par_interno = input % x
        if(par_interno != 0):
            print(input, "ES primo")
            print("valor de posicion", x)
        else:
            print(input, "NO es primo")
            print("valor de posicion", x)
  
validation(number1)