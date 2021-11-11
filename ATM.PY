print("welcome to ATM")
total_balance=50000
atm=input ("enter the card:")
if atm =="credit card" or atm =="debit card":
    print("after")
    language= input ("please enter your language:")
    if language =="english" and "hindi":
        print("english")
        pin = int(input("enter the pin:"))
        if pin >=0 or pin <=9 :
            print("ok")
            type=input("enter the type:")
            if type == "current" or "saving":
                print("in proese")
                trancsection=input("enter the trancsection:")
                if trancsection =="withdrawal" and "balance enquiry":
                    print("ok")
                    balance=int(input("enter the balance:"))
                    if balance >=0 or balance <=50000 :
                        print("go next")
                        if total_balance%100==0: 
                            print(total_balance - balance)
                            recipt=input("enter do you have receipt:")
                            if recipt =="yes":
                                print("next")
                                atm=input("take your atm back:")
                                if atm =="yes":
                                   print("ok thank you")
                                else:
                                    print("no")
                            else:
                                print("nothing") 
                        else:
                            print("anything") 
                    else:
                        print("never")        
                else:
                    print("noooo")
            else:
                print("noo")      
    elif language== "hindi":
         pin = int(input("apne 4 anko ka pin dale :"))
         if pin >=0 or pin <=9 :
            print("ha")
            khata=input("apna khata ka parkar dale dale:")
            if type == "chalu" or "bachat":
                print("prakriya")
                trancsection=input(" apne len den  ka prkar chune:")
                if trancsection =="nikashi" or "blance ki puch tach kare":
                    print("ok")
                    balance=int(input("apni rashi dale:"))
                    if balance >=0 or balance <=50000 :
                        print("agli prakriya m jae")
                        if total_balance%100==0: 
                            print(total_balance - balance)
                            recipt=input("kya apko rashid prapt hui h")
                            if recipt =="ha":
                                print("agli ")
                                atm=input("apna card wapas le:")
                                if atm =="ha":
                                    print("dhaniywad") 
                                else:  
                                    print("no")              
                            else:
                                print("nothing")        
                        else:
                            print("anything")  
                    else:
                        print("never") 
                else:
                     print("noo")                   
            else:
                print("go") 
        
