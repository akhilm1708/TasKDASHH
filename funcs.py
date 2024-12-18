# import requests
# API = "https://cs-api.pltw.org/"


# # def get_user_input():
# #     user = input("Which user would you like to hack: ")
# #     return user

# def build_url(user):
#     my_response = requests.post(API+"newuser/"+user)
#     print(my_response.status_code)
#     print(my_response.headers)
#     print(my_response.text)
#     return API + user

# def POST(url):
#     post_response = requests.post(url)
    
#     print(post_response.status_code)
#     print(post_response.headers)
#     print(post_response.text)

# def INC(url):
#     id = "/increment?id="  
#     num = input("What task's priority would you like to increase: ")
#     count = int(input("How much of a priority would you like to increase it by? : "))
    
#     for _ in range(count):
       
#         inc_url = url + id + num
#         inc_response = requests.post(inc_url)
        
#         print(inc_response.status_code)
#         print(inc_response.headers)
#         print(inc_response.text)


# def GET(url):
#     get_response = requests.get(url)
#     print(get_response.status_code)
#     print(get_response.headers)
#     print(get_response.text)

# def CLEAR(url):
#     password = input("What is the user's password: ")
#     cString = "/reset?password="
#     clear_response = requests.post(url+cString+password)
#     print(clear_response.status_code)
#     print(clear_response.headers)
#     print(clear_response.text)





# # user = get_user_input()
# # url = build_url(user)


# # user_response = requests.get(url)
# # check_user = user_response.text

# # if "Error: No such user." in check_user:
# #     answer = input("Do you want to create this user (Y/N): ")
# #     if answer.lower() == "y":
# #         my_response = requests.post(API+"newuser/"+user)  
# #         print(my_response.status_code)
# #         print(my_response.headers)
# #         print(my_response.text)