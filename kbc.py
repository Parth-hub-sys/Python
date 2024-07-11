print("------------------------------>> KBC <<----------------------------------- ")
wallet = 0


q = ["(A) Yes"," (B) No"]
print(q)
q[0] = "A"
q[1] = "B"
A = str(input("enter your answer to start your KBC for Start or No for conformation :"))
if A == q[0]:
    print("\n wellcome in KBC ")
    print("1. what is a capital of india")
    l = ["(A) Delhi","(B) Gujarat","(C) Mumbai","(D) cheenai"]
    print(l)
    l[0] = "A"
    l[1] = "B"
    l[2] = "C"
    l[3] = "D"
    
    
    a = str(input("enter your answer : "))
    if a == l[0]:
        print("congratulation you won 1 lacs ")
        wallet = wallet + 1
        print("Total value : ",wallet)
    else:
        print("sorry you lost the game")
        print("Total value : ",wallet)
 
    print("--------------------------------------------->>") 
    print("--------------------------------------------->>")   
    print("2. what is a capital of Gujrat")
    l = ["Surat","Ahmdabad","Rajkot","Amreli"]
    print(l)
    l[0] = "A"
    l[1] = "B"
    l[2] = "C"
    l[3] = "D"
    a = str(input("enter your answer : "))
    if a == l[1]:
        print("congratulation you won 1.5 lacs ")
        wallet = wallet + 1.5
        print("Total value : ",wallet)

    else:
        print("sorry you lost the game")
        print("Total value : ",wallet)
        
    print("--------------------------------------------->>") 
    print("--------------------------------------------->>")   
    print("3. where is a born of Swaminarayan")
    l = ["Chapaiya","gudgav","gadhda","gondal"]
    print(l)
    l[0] = "A"
    l[1] = "B"
    l[2] = "C"
    l[3] = "D"
    a = str(input("enter your answer : "))
    if a == l[0]:
        print("congratulation you won 2 lacs ")
        wallet = wallet + 2
        print("Total value : ",wallet)

    else:
        print("sorry you lost this qustion")
        print("Total value : ",wallet)
        
    print("--------------------------------------------->>") 
    print("--------------------------------------------->>")   
    print("4. what is your birth date")
    l = ["19/04/2006","2/06/2004","17/06/2005","20/06/2005"]
    print(l)
    l[0] = "A"
    l[1] = "B"
    l[2] = "C"
    l[3] = "D"
    a = str(input("enter your answer : "))
    if a == l[2]:
        print("congratulation you won 4 lacs ")
        wallet = wallet + 4
        print("Total value : ",wallet)

    else:
        print("sorry you lost this qustion")
        print("Total value : ",wallet)
    
    print("--------------------------------------------->>") 
    print("--------------------------------------------->>")   
    print("5.who is most richest person name")
    l = ["Adani","Elon","tate","ambani"]
    print(l)
    l[0] = "A"
    l[1] = "B"
    l[2] = "C"
    l[3] = "D"
    a = str(input("enter your answer : "))
    if a == l[3]:
        print("congratulation you won 8 lacs ")
        wallet = wallet + 8
        print("Total value : ",wallet)
        print("congratulation you won a ",wallet,"Rs.")

    else:
        print("sorry you lost this question")
        print("Total value : ",wallet)
        print("congratulation you won a ",wallet,"Rs.")
else:
    print("Ok")
    





