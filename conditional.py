
#creating our first password checker

#defining variables

user_name="Shloka"
password="Xy1234"


#define inputs

input_user_name=input("User name: ")
input_password=input("password: ")



#conditions

if input_user_name == user_name and input_password == password:
    print(f"Login successful, welcome {user_name}!")
elif input_user_name != user_name and input_password == password:
    print("Username is incorrect")
elif input_user_name == user_name and input_password != password:
    print("Incorrect password")
else:
    print("Sorry, user not found")
     
     