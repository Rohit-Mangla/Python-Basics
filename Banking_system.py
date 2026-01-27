Balance = 0.0
Kyc_documents = {}

def check_balance():
    print("Your current balance is: ", Balance)
    print("=======================")

def deposit(amount):
    global Balance
    if amount > 0:
        Balance += amount
    else:
        print("can't deposit negative or zero amount")
        print("=======================")

def withdraw(amount):
    global Balance
    if amount <= 0:
        print("can't withdraw negative or zero amount")
        print("========================")
    elif amount > Balance:
        print("can't withdraw. Insufficient balance.")
        print("========================")
    else:
        Balance -= amount

def update_kyc(docs):
    global Kyc_documents
    Kyc_documents.update(docs)

def check_kyc():
    if len(Kyc_documents) == 0:
        print("Kyc not done")
        print("========================")
    else:
        for doc in Kyc_documents:
            print(f"{doc}: {Kyc_documents[doc]}")

        print("========================")

if __name__ == "__main__":
    print("========================")
    print("Welcome to the ABC Bank!!!")
    print("========================")
    print()

while True:
    print("1. check your balance")
    print("2. Deposit an amount")
    print("3. Withdraw an amount")
    print("4. Check Kyc")
    print("5. Update Kyc")
    print("6. Quit")
    choice = input("Enter your choice(1-6): ")
    print("========================")

    if choice == "1":
        check_balance()
    elif choice == "2":
        amt = float(input("Enter the amount to be deposited: "))
        deposit(amt)
        print(f"Amount {amt} deposited successfully.")
        print("========================")
    elif choice == "3":
        amt = float(input("Enter the amount to be withdrawn: "))
        withdraw(amt)
        print(f"Amount {amt} withdrawn successfully.")
        print("========================")
    elif choice == "4":
        check_kyc()
    elif choice == "5":
        kyc_docs = {}
        n_documents = int(input("Enter the number of documents you want to add: "))
        for i in range(n_documents):
            key = input("Enter the document type: ")
            value = input("Enter the document number: ")
            kyc_docs[key] = value
        update_kyc(kyc_docs)
        print("Kyc updated successfully.")
        print("========================")
    elif choice == "6":
        print("Quiting. have a nice day.")
        break
    else:
        print("Invalid choice!!! Re-Try.")
        print("========================")

print()
print("Thank you for banking with us.")