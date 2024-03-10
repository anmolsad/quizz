from datetime import date

user_data = {}
login_user = None
file_data = []
def register():
    global user_data
    name = input("Enter your name: ")
    pwd = input("Enter your password: ")
    email = input("Enter your email address: ")
    cont = input("Enter your contact: ")
    enroll = input("Enter your Enrollment: ")

    user_data[enroll] = [name,enroll,pwd,email,cont]

    file = open('std_data.txt','a')
    file.write(f"{name},{pwd},{email},{enroll},{cont}")
    file.write("\n")
    ch = input("Do you want to login y/n: ")
    if ch == 'Y' or ch == 'y':
        login()
    else:
        main()



def login():
    global user_data
    global login_user
    global file_data
    user_p = {} #{'0103CS212121':'12345','':''}
    # file = open('std_data.txt','r')
    # data = file.readlines()
    # for i in data:
    #     res = i.split(',')
    #     user_p[res[3]] = [res[1],res[0]]
    # file.close()

    with open('std_data.txt','r') as file:
        data = file.readlines()
        file_data = data.copy()
        for i in data:
            res = i.split(',')
            #{enroll:[pass,name]
            user_p[res[3]] = [res[1],res[0]]

    if login_user is None:
        enroll = input("Enter your enroll: ")
        passw = input("Enter your password: ")
        if enroll in user_p:
            if user_p[enroll][0] == passw:
                print(f"WELCOME {user_p[enroll][1]}")
                login_user = enroll
            else:
                print("WRONG PASSWORD")
        else:
            print("WRONG USERNAME")
    else:
        print("""
        1. Attempt Quiz
        2. update Profile
        3. Result
        4. Logout
""")
    print("""
        1. Attempt Quiz
        2. update Profile
        3. Result
        4. Logout
""")
    ch = input("Enter your choice: ")
    if ch == '1':
        quiz()
    elif ch == '2':
        updateProfile()
    elif ch == '3':
        result()
    elif ch == '4':
        logout()
    else:
        print("Choose correct option: ")

def quiz():
    global login_user
    
    sub_on = date.today()

    print("QUIZ")
    print("""
        1. java
        2. python
        3. home
    """)
    
    ch=input("select topic: ")
  
                
    def topic(T):
        marks=0
        file=open(f'{T}.txt','r')
        data = file.readlines()
        for i in data:
            q=i.split(',')
            print(f"""
    Q.{q[0]}
    1. {q[1]}
    2. {q[2]}
    3. {q[3]}
    4. {q[4]}
            """)
            ans=int(input("select option: "))
            
            if q[ans] in q[5]:
                marks+=10
                print(q[ans])
            else:
                pass
        sub=input("do you want to submit:(y/n): ")
        if sub == 'Y' or sub == 'y':
            file = open('results.txt','a')
            file.write(f"{login_user},{T},{marks},{sub_on}")
            file.write("\n")
    if ch == '1':
        topic("java")
        main()
    elif ch== '2':
        topic("python")
        main()

def result():
    if login_user:
        file=open('results.txt','r')
        data = file.readlines()
        for i in data:
            q=i.split(',')
            if q[0] in login_user:
                print(f"""
                      result
            subject   marks    date 
             {q[1]}      {q[2]}   {q[3]}
                    """)
        main()


    

def updateProfile():
    global file_data
    
    for i in file_data:
        da = i.split(',')
        print(f"HEllo {da[0]} your username is {da[3]} contact number is {da[-1]}")
def logout():
    print("THANK YOU! VISIT AGAIN")
    exit()

def main():
    print("""
        ###########################
            WELCOME TO THE QUIZ
        1. Login
        2. Registration
        3. Attempt Quiz
        4. See Profile/Result
        5. EXIT

        ###########################
""")
    choice = input("Enter Your Choice: ")
    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        quiz()
    elif choice == '4':
        result()
    elif choice == '5':
        logout()
    else:
        print("CHOOSE CORRECT OPTION!")
        main()
    

if __name__ == "__main__":
    main()


#https://www.google.com (index/home/default)
    
    #PASSWORD VALIDATION (8-20, a, A, 0-9, @#$%)
