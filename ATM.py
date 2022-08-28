print("welcome to ATM")
balance=10000
ATM_card=input("select your card:1.SBI,2.rupay :")
if ATM_card=="1" or ATM_card=="2":
    language=input("please choose the language:1,english,2.hindi:")
    if language=="1":
            option=input("choose the option:1.balance enqury,2.withdraw:")
            if option=="1":
                pin=int(input("enter your the pin:"))
                if pin<9999:
                    print("tatol balace is",balance)
                    print("your transaction is completed collect your card:")
                else:
                    print("invalid pin")
                    print("try again")
            elif option=="2":
                amount=int(input("enter your amount:"))
                if amount>500 or amount<10000:
                    if amount%100==0:
                        print("please collect your amount")
                        print("your current balance is ",balance-amount)
                    sleep=input("you want sleep:")
                    if sleep=="yes" or sleep=="no":
                        print("please collect your sleep")
                        print("thank you")
                    else:
                        print("your transaction is completed")
                else:
                    print("please enter valid amount")
    if language=="2":
        account=input("apna khata chune 1.vartman khata, 2.bachat khata:")
        if account=="1" or account=="2":
            len_den=input("apna len den chune1.balance puchtach, 2. paise nikalana:")
            if len_den=="1":
                pin=int(input("apna char ank pin dale:"))
                if pin<9999:
                    print("apka kul shesh hai",balance)
                    print("apka len den purn hua")
                    rasid=input("aapko rasid chahiye 1.ha 2. nahi")
                    if rasid=="1":
                        print("apka len den purn hua")
                        print("krupaya apni rasid aur apna card nikal le")
                    else:
                        print("apka len den purn hua krupaya apna card nikal le")
                else:
                    print("sahi pin dale")
            elif len_den=="2":
                pin=int(input("apna char ank pin dale:"))
                if pin<9999:
                    print("apka pin sahi hai")
                    rashi=int(input("enter your amount5: "))
                    if rashi>500 or rashi<=10000:
                        if rashi%100==0:
                            print("krupaya apni rashi nikal le")
                            print("apke khate me kul rashi",balance-rashi)
                        rasid=input("aapko rasid chahiye1.ha,2.nahi:")
                        if rasid=="1":
                            print("apka len den pura hua")
                            print("krupaya apni rashid aur apna card nikal le")
                        else:
                            print("apka len den pura hua kripaya apna card nikal le")
                    else:
                        print("krupaya manya rashi darj kare")
                else:
                    print("manya pin darj kare")              
else:
    print("please re-enter your card")


