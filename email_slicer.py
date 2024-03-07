def email_slicer(email):
    # Split the email address into username and domain
    username, domain = email.split('@')
    
    # Print the username and domain
    print(f"Username: {username}")
    print(f"Domain: {domain}")

def main():
    email = input("Enter your email address: ")
    email_slicer(email)

if __name__ == "__main__":
    main()
