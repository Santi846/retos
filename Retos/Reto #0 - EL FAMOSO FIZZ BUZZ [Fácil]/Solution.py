
def fizzbuzz():
    for i in range(1,101,1):
        if ((i % 3 == 0) and (i % 5 == 0)):
            msg1 = "fizzbuzz"
            i = msg1
            print(i)
        elif (i % 3 == 0):
            msg2 = "fizz"
            i = msg2
            print(i)
        elif (i % 5 == 0):
            msg3 = "buzz"
            i = msg3
            print(i)
        else:
            print(i)
fizzbuzz()