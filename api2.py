import requests
username=input("Enter the username you would like to show details of ")

url = f"https://api.github.com/users/{username}"
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print("GITHUB API PROJECT :")
import requests


headers = {}  
payload = {}

while True:
    print("\nWhat operation would you like to perform to fetch from GITHUB?")
    print("1: Following")
    print("2: Followers")
    print("3: Basic info")
    print("4: Repository details")
    print("5: Exit")
    
    option = input("Enter the choice (1-5): ")

    if option == "1":
        following_url = f"https://api.github.com/users/{username}/following"
        response_following = requests.get(following_url, headers=headers, data=payload)
        data_following = response_following.json()
        
        if response_following.status_code == 200:
            print(f"\n{username} is following the following users:")
            for following in data_following:
                print(f"{following['login']}")
        else:
            print(f"Failed to fetch the following list for {username}")

    elif option == "2":
        followers_url = f"https://api.github.com/users/{username}/followers"
        response_follower = requests.get(followers_url, headers=headers, data=payload)
        data_followers = response_follower.json()
        
        if response_follower.status_code == 200:
            print(f"\n{username} has the following followers:")
            for follower in data_followers:
                print(f"{follower['login']}")
        else:
            print(f"Failed to fetch the followers list for {username}")
    elif(option=="3"):
        basic_info_url=f"https://api.github.com/users/{username}"
        response_basic_url=requests.get(basic_info_url,headers=headers,data=payload)
        data_basic_info=response_basic_url.json()
        if response_basic_url.status_code==200:
            print(f"\n{username}has the basic info : ")
            print("Name:",(data_basic_info['name']))
            print("Login:",(data_basic_info['login']))
            print("Total followers:",(data_basic_info['followers']))
            print("Total  following: ",(data_basic_info['following']))
        else:
            print(f"Failed to fetch the basic info {username}")
    elif(option=="4"):
        repo_url=f"https://api.github.com/users/{username}/repos"
        reponse_repo_url=requests.get(repo_url,headers=headers,data=payload)
        data_repos=reponse_repo_url.json()
        if reponse_repo_url.status_code==200:
            print(f"\n{username} has the repository details:")
            for reps in data_repos:
                print("Repo name:",(reps['name']))
                print("Visibiltiy :",(reps['private']))
                print("Fork status:",(reps['fork']))
                print("Default branch:",(reps['default_branch']))
        else:
            print(f"Failed to fetch the repos info {username}")           
    elif option == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please try again.")
