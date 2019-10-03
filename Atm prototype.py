Pin=["111", "222", "333"]
Users=['Deepak Kumar', 'xyz', 'abc']
Amount=['10000','200','300']
a= input('Enter your Pin:')
x= a in Pin
if(x== True):
    b=Pin.index(a)
    c=Users[b]
    print("hello",c)
    y=input('Choose transaction:')
    if(y=='Withdraw amount'):
        w= input('Enter amount:')
        if(w>'0' and w<Amount[b]):
            print('Collect cash')
            Restamount =int(Amount[b])-int(w)
            print('Restamount',Restamount)   
        else:
            print('Insufficienrt amount')
    elif(y=='Deposit amount'):
        m= input('Enter amount to be deposit:')
        if(m>'0'):
            print('Deposit successfully')
        else:
            print('Enter valid amount to deposit')
    else:
        print('invalid transaction')
else:
    print('Wrong Pin')
