# subjects=["Math","Nepali","English","Science","Computer"]
# for subject in subjects:
#     print(f"{subject},this is the subject I study in my basic level schooling")
#     if "Math" in subjects:
#         print(subject.upper())    

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
    
Hello_Admin=["admin","john","robert","jaden","tom"]
for admins in Hello_Admin:
    # print(admins)
    if admins=="admin":
        print("Hello admin would you like to see a status report?")
    else:
        print(f"Hello {admins}, thank you for logging in again")    
    