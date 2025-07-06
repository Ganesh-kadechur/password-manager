import os


def add_password():
    website = input("Enter the website")
    username = input("Enter the username")
    password = input("Enter the password")

    entry = f"{website}|{username}|{password}\n"
    with open("data/vault.txt", "a") as f:
        f.write(entry)

def view_password():
    if not os.path.isfile("data/vault.txt"):
        print("No passwords saved  yet.")
        return
    with open("data/vault.txt", "r") as f:
        lines = f.readlines()

    if not lines:
        print("No passwords saved  yet.")
        return

    print("\n---Passwords saved  yet.---")
    for i,line in enumerate(lines,1):
        try:
            website, username, password = line.strip().split("|")
            hidden_pass = "*" * len(password)
            print(f"{i}.{website}|{username}|{hidden_pass}")
        except ValueError:
            print(f"{i}.Corrupted entry:{line.strip()}")


def delete_password():
    if not os.path.isfile("data/vault.txt"):
        print("vault file not found.")
        return
    with open("data/vault.txt", "r") as f:
         lines = f.readlines()

    if not lines:
        print("No passwords saved  yet.")
        return
    print("\n---Passwords saved  yet.---")
    for i,line in enumerate(lines,1):
        print(f"{i}{line.strip()}")

    try:
        choice = int(input("Enter number password to delete: "))
        if 1<= choice <= len(lines):
            deleted = lines.pop(choice-1)
            with open("data/vault.txt", "w") as f:
                f.writelines(lines)
            print(f"Deleted password: {deleted.strip()}")
        else:
            print(" Invalid choice.")
    except ValueError:
        print("Invalid input.please enter a number.")
        
def authenticate():
    master_key = "masterkey123"
    entered = input("Enter the master key")
    return entered == master_key

def main():
    if not authenticate():
        print("Access  denied")
        return

    while True:
        print("\n--- Password Manager ---")
        print("1. Add a new password")
        print("2. View your password")
        print("3. Delete your password")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
