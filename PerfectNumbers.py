#scripts enter to loop
while True:
    #input number from console
    number=int(input("Enter number: "))
    toplam=0
    #get element till number
    for i in range(1,number):
        #check split up or not
        if(number%i==0):
            toplam=toplam+i
    if(toplam==number):
        print number,"is perfect number"
    else:
        print number,"isn't perfect number"
