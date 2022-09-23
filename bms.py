#BMS--> banking mangement system
import mysql.connector
mydb=mysql.connector.connect(
                            host='localhost',
                            port=3325,
                            user='root',
                            password='12345',
                            database='bank2'
                            )

def OpenAcc():
    name=input('Enter the customer Name:')
    accNo=input('Enter the Ac/No:')
    dob=input('Enter the DOB:')
    Add=input('Enter the Address:')
    Cont_No=int(input('Enter the contact No:'))
    open_bal=int(input('enter the balance:'))

    data1=(name,accNo,dob,Add,Cont_No,open_bal)
    sql1=('insert into ACCOUNT values(%s,%s,%s,%s,%s,%s)')
    data2=(name,accNo,open_bal)
    sql2=('insert into Amount values(%s,%s,%s)')

    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print('Enter My Data Sucessfully')
    main()

def DepoAmo():
    amount=input('Enter the amount you want to deposit:')
    ac=input('Enter the Acc No:')
    a='select bal from amount where accNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+int(amount)
    sql=('update amount set bal=%s where accNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()
def main():
        print('''
            1. OPEN NEW ACOUNT
            2. DEPOSIT AMOUNT
            3. WITHDRAW AMOUNT
            4. BALANCE ENQUIRY
            5. DISPLAY CUSTOMER DETAILS
            6. CLOSE AN ACCOUNT''')
        choice = input('Enter the task you want to perfrom:')
        if (choice=='1'):
            OpenAcc()
        elif(choice=='2'):
            DepoAmo()
        elif(choice=='3'):
            WithdrawAmount()
        elif(choice=='4'):
            balEnq()
        elif(choice=='5'):
            Disdetails()
        elif(choice=='6'):
            CloseAcc()
        else:
            print('Invalid Choice')
            main()

main()
