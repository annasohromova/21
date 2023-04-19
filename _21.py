import random
deck=[6,7,8,9,10,2,3,4,11]*4
random.shuffle(deck)
arv=0
while True:
    choice=input("kas te võtate kaardi?  jah/ei: ")
    if choice == "jah":
        number=deck.pop()
        print("teie kaardi number on %d" %number)
        arv+=number
    if arv>21:
        print("Mul on kahju, aga te olete kaotanud.")
        break
    elif arv==21:
        print("õnnitlused, te olete jõudnud numbrini 21!")
        break
    else:
        if choice == "ei":
             print("teil on %d punkti, kahjuks te kaotate" %arv)
             break
