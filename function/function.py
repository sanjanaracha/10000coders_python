#function is a block of code which can be reused multiple times whenever calling it.
#def fn_name():
    #block code to ec=xecute
#fn_name()  #calling/invoke
#fn_name()
#fn_name()


'''def add():
    a=10
    b=20
    print(a+b)
add()
add()
add()'''


'''def mul():
    a=10
    b=20
    print(a*b)
mul()'''


'''rigister dashboard
login
dashboard access'''

#register
'''def register():
    n=input("enter name:")
    e=input("enter email:")
    p=input("enter password:")
    cp=input("enter password again:")
    if p==cp:
        print("rigistration successful")
    else:
        print("pls provide matched values for p and cp")
register()'''


#dashboard access

def dashboard():
    print("dashborad access successful")


#login

def login():
    e="sanj@g"
    le=input("enter email:")
    lp=input("enter password:")
    p="000"
    if p==lp and le==e:
        print("login successful")
        dashboard()
    else:
        print("pls provide matched values")
login()


