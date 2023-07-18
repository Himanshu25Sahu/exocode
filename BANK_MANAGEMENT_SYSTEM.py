
#-------------------------------------------------------------------------------------------------CONNECTOR
import time
import mysql.connector
import pyfiglet
#--------------------------------------------------------------------------------------------------MODULES
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="your_password",
  database="your_database"
)
# create cursor object
mycursor = mydb.cursor()


#-------------------------------------------------------------------------------------------------CONNECTOR
def loan_calc(amt,time):
    rate=4.5/100
    month_rate=rate/12
    total_payment=time*12
    monthly_payment = (amt * month_rate) / (1 - (1 + month_rate) ** -total_payment)
    total_interest_paid = (monthly_payment * total_payment) - amt
    print("LOAN AMOUNT: ",amt,"\nTIME PERIOD: ",time,"\nMONTHLY PAYMENT: ",round(monthly_payment),"\nTOTAL INTEREST TO BE PAID: ",round(total_interest_paid))

def large_text(text):
    ascii_art = pyfiglet.Figlet().renderText(text)
    animation(ascii_art)

def animation(text):
    for char in text:
        print(char,end='',flush=True)
        time.sleep(0.01)
    print()

def welcome_screen(text):
    
    ascii_art = pyfiglet.Figlet().renderText(text)
    
    print(ascii_art)
     
def balance(user,store):
    query=f"SELECT balance FROM newusers WHERE name='{user}'"
    mycursor.execute(query)
    get=mycursor.fetchone()
    store=get[0]
    return store



welcome_screen("SAHU BANK\n")
flag=True
while(flag==True):
    
    animation("1.LOGIN\n2.SIGN UP\n3.EXIT")
    print("------------------------------------------")
    log=int(input())

    #-----------------------------------------------------------------------------------------------------LOGIN
    if log==1:
        animation("ENTER YOUR USERNAME")
        user=input()
        query1=f"SELECT*FROM newusers WHERE name='{user}'"
        mycursor.execute(query1)
        res=mycursor.fetchone()
        if res:  #--------------------------------------------------------------if user exists in database
            
            idc=f"select id from newusers where name='{user}'"
            animation("ENTER YOUR PASSWORD")
            pas=input()
            pascheck=f"select password from newusers where name='{user}'"
            mycursor.execute(pascheck)
            pasget=mycursor.fetchone()
            if pasget:
                pa=pasget[0]
                if pa==pas:
                    animation("LOGINNED SUCCESFULLY!")#------------------------------------------------------LOGIN END
                    while(flag==True):
                        animation("HELLO!!\n1.BALANCE\n2.DEPOSIT\n3.CREDIT\n4.DELETE USER\n5.UPDATE MOBILE NUMBER\n6.UPDATE PASSWORD\n7.TRANSFER MONEY\n8.LOAN CALCULATOR\n9.EXIT")
                        alog=int(input())
                        if alog==1:
                            #--------------------------------------------------------------------------balance
                            
                            query4=f"SELECT balance FROM newusers WHERE name='{user}'"
                            mycursor.execute(query4)
                            result1=mycursor.fetchone()
                            # if result1==' (None,)':
                            #     print("not yet deposited")
                            # print(user,"\nBALANCE=",result1[0],"/- RUPEES")
                            animation("----------"+user+"----------"+"\nBALANCE\n"+str(result1[0])+"\t/- RUPEES\n"),animation("balance")
                            if int(result1[0])<500:
                                print("!!!!BALANCE LOW! PLEASE DEPOSIT SOME MONEY!!!!")
                            
                        elif alog==2:
                            #----------------------------------------------------------------------------DEPOSIT
                            animation("ENTER PIN:")
                            pin=int(input())
                            qpin=f"SELECT pin FROM newusers WHERE name ='{user}'"
                            mycursor.execute(qpin)
                            result3=mycursor.fetchone()
                            # if result3[0]==pin:
                            if result3[0]==pin:
                                #---------------------------------------------------------------------------IF PIN IS CORRECT

                                animation("ENTER THE AMOUNT OF MONEY ")
                                add=int(input())
                                query6=f"update newusers set balance= balance + {int(add)} where name='{user}'"
                                mycursor.execute(query6)
                                mydb.commit()
                                animation("BALANCE UPDATED")
                            else :#--------------------------------------------------------------------------IF PIN IS NOT CORRECT
                                animation("WRONG PIN!")
                                continue



                            
                        elif alog==3:
                            #-------------------------------------------------------------------------------CREDIT
                            animation("PROCESSING.......")
                            animation("ENTER THE AMOUNT OF MONEY")
                            deduct=int(input())
                            
                            ndeduct=int(deduct)
                            query7=f"update newusers set balance=balance-{int(deduct)} where name='{user}'"
                            mycursor.execute(query7)
                            mydb.commit()
                            animation("AMOUNT OF :"+str(deduct)+"IS PROCESSING...\n")
                            animation("PLEASE COLLECT THE CASH FROM ATM\n")



                            
                        elif alog==4:
                            #----------------------------------------------------------------------------------DELETE USER
                            query5=f"delete from newusers where name='{user}'"
                            mycursor.execute(query5)
                            mydb.commit()

                        elif alog==5:
                            #-----------------------------------------------------------------------------------UPDATE MOBILE NUMBER
                            query7=f"select mobile from newusers where name = '{user}'"
                            mycursor.execute(query7)
                            result2=mycursor.fetchone()
                            
                            animation(f"YOUR CURRENT MOBILE NUMBER IS \n {result2[0]}")
                            newmob=int(input("ENTER YOUR NEW MOBILE NUMBER\n"))
                            
                            query8=f"update newusers set mobile ={newmob} where name='{user}'"
                            mycursor.execute(query8)
                            mydb.commit()
                            animation("UPDATED!")
                            
                        elif alog==6:
                            #---------------------------------------------------------------------------------UPDATE PASSWORD
                            animation("ENTER YOUR OLD PASSWORD")
                            opass=input()
                            if opass==pasget[0]:
                                animation("ENTER NEW PASSWORD")
                                npass=input()
                                
                                qery9=f"update newusers set password='{npass}' where name='{user}'"
                                mycursor.execute(qery9)
                                mydb.commit()
                                animation("UPDATED ! PLEASE LOGIN AGAIN\n")
                                break
                            else:
                                animation("PLEASE ENTER YOUR CORRECT OLD PASSWORD!\n")
                                    
                        elif alog==7:
                            #--------------------------------------------------------------------------------------TRANSFER
                            animation("ENTER THE NAME AND ACCOUNT NUMBER OF THE PERSON\n")
                            animation("NAME:\n")
                            trans_name=input()
                            animation("ACCOUNT NUMBER:\n")
                            trans_acc=input()
                            trans_name_exist=f"select name from newusers where name='{trans_name}'"
                            trans_acc_exist=f"select acc from newusers where acc='{trans_acc}'"
                            mycursor.execute(trans_name_exist)
                            nameres=mycursor.fetchone()

                            mycursor.execute(trans_acc_exist)
                            accres=mycursor.fetchone()
                            if nameres and accres:
                                animation("PROCESSING.........\n")
                                animation("ENTER THE AMOUNT OF MONEY\n")
                                trans_amt=int(input())

                                animation("ENTER PIN:\n")
                                pin=int(input())
                                qpin=f"SELECT pin FROM newusers WHERE name ='{user}'"
                                mycursor.execute(qpin)
                                result3=mycursor.fetchone()
                                # if result3[0]==pin:
                                if result3[0]==pin:
                                    stor=0
                                    bal_check=balance(user,stor)
                                    if trans_amt>bal_check:
                                        animation("!!TRANSFER AMOUNT EXCEEDING TRANSFER MONEY!!")
                                    else:
                                        trans_deduct=f"update newusers set balance=balance-{int(trans_amt)} where name = '{user}'"
                                        mycursor.execute(trans_deduct)
                                        mydb.commit()
                                        trans_add=f"update newusers set balance = balance + {int(trans_amt)} where name='{trans_name}'"
                                        mycursor.execute(trans_add)
                                        mydb.commit()
                                        animation("SENDING AMOUNT........")
                                        animation("AMOUNT OF : "+str(trans_amt)+" IS TRANSFERRED TO :"+trans_name+" SUCCESSFULLY!\n")
                                else:
                                    animation("WRONG PIN!\nPLEASE ENTER CORRECT PIN \n")
                            else:
                                animation("WRONG ENTRY OF NAME OR ACCOUNT NUMBER \n")
                                continue
                        elif alog==8:
                            animation("\nLOAN CALULATOR\n")        
                            loan=int(input("ENTER THE LOAN AMOUNT: "))
                            time=int(input("TIME IN YEARS: "))
                            loan_calc(loan,time)


                        elif alog==9:
                            animation("THANK YOU!")    
                            flag=False
                            break  
                        else:
                            animation("under devolepment")
                            continue
                        
                    else:
                        animation("WRONG LOGIN PASSWORD PLS ENTER CORRECT ONE!\n")
            
                        continue
                else:
                    animation("PLEASE ENTER THE CORRECT PASSWORD!")
            
        else:
            animation("USER NOT IN DATABASE")
            break

        
    elif log==2:
    #sign up
        animation("CREATE USERNAME\n")
        new=input()
        animation("CREATE PASSWORD\n")
        npas=input()
        animation("enter your mobile number\n")
        nmob=int(input())
        animation("ENTER ACCOUNT NUMBER\n")
        acc=int(input())
        
        query2=f"INSERT INTO newusers (name,mobile,password,acc) VALUES (%s,%s,%s,%s)"
        val2=(new,nmob,npas,acc)
        mycursor.execute(query2,val2)
        mydb.commit()
        continue
    else:
        animation("-----THANK YOU-----")
        break
#login end







    
