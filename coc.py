ars=int(raw_input("Enter the army space"))
gold=int(raw_input("Enter the gold"))
br=int(raw_input("Enter the barbarians"))
gl=int(raw_input("Enter the goblins"))
gi=int(raw_input("Enter the giants"))
ar=int(raw_input("Enter the archers"))
if(ars<1):
    print("Army spacing is not enough")
elif(gold<50):
    print("Amount not enough")
else:
    if(br>0):
        ars=ars-(br*1)
        gold=gold-(br*50)
        if(ars>0):
            if(gold>0):
                print("%d barbarians added successfully" %br)
            else:
                print("Barbarians cannot be added")
        else:
            print("Barbarians cannot be added")
    if(gl>0):
        ars=ars-(gl*1)
        gold=gold-(gl*50)
        if(ars>0):
            if(gold>0):
                print("%d goblins added successfully" %gl)
            else:
                print("Goblins cannot be added")
        else:
            print("Goblins cannot be added")
    if(gi>0):
        ars=ars-(gi*5)
        gold=gold-(gi*1000)
        if(ars>0):
            if(gold>0):
                print("%d giants added successfully" %gi)
            else:
                print("Giants cannot be added")
        else:
            print("Giants cannot be added")
            
    if(ar>0):
        ars=ars-(ar*1)
        gold=gold-(ar*100)
        if(ars>0):
            if(gold>0):
                print("%d archers added successfully" %ar)
            else:
                print("archers cannot be added")
        else:
            print("Archers cannot be added")
print("Gold remaining %d" %gold)
print("Army space remaining %d" %ars)
            
                      
                 
                      
                 
    
    
