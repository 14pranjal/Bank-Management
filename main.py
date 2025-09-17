import json
from pathlib import Path
import random
import string

class Bank:
    data = []
    __database = "data.json"

    # Load existing data
    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.load(fs)
    except Exception as err:
        print(f"An error occurred: {err}")

    @classmethod
    def __updatedata(cls):
        with open(cls.__database, "w") as fs:
            json.dump(cls.data, fs, indent=4, ensure_ascii=False)

    @classmethod
    def __Generate_Account_number(cls):
        alpha = random.choices(string.ascii_letters, k=5)
        numbers = random.choices(string.digits, k=5)
        acc_id = alpha + numbers
        random.shuffle(acc_id)
        return "".join(acc_id)

    def create_Account(self):
        info = {
            "Name": input("Name: "),
            "Age": int(input("Age: ")),
            "Email": input("Email: "),
            "AccountNo": self.__Generate_Account_number(),
            "PHONE": int(input("Phone Number: ")),
            "GENDER": input("Gender: "),
            "Pin": int(input("Pin (4 digits): ")),
            "Balance": 0
        }
        if info['Age'] < 18:
            print("Sorry, you cannot create an account (must be 18+)")
        elif len(str(info["PHONE"])) != 10:
            print("Invalid phone number")
        elif len(str(info["Pin"])) != 4:
            print("Invalid Pin (must be 4 digits)")
        else:
            Bank.data.append(info)
            Bank.__updatedata()
            print(f"Your Account No is {info['AccountNo']}, done")

    def deposit_money(self):
        Account_no = input("Account no: ")
        pin = int(input("Pin: "))
        user_data = [i for i in Bank.data if i["AccountNo"].lower() == Account_no.lower() and i["Pin"] == pin]

        if not user_data:
            print("No such user found")
        else:
            amount = int(input("Amount to deposit: "))
            if amount < 0:
                print("Cannot deposit negative amount")
            elif amount > 20000:
                print("Cannot deposit more than 20000 Rs")
            else:
                user_data[0]['Balance'] += amount
                Bank.__updatedata()
                print("Amount deposited successfully")

    def withdraw_money(self):
        Account_no = input("Account no: ")
        pin = int(input("Pin: "))
        user_data = [i for i in Bank.data if i["AccountNo"] == Account_no and i['Pin'] == pin]

        if not user_data:
            print("No such user found")
        else:
            amount = int(input("Amount to withdraw: "))
            if amount > 20000:
                print("Cannot withdraw more than 20000 Rs")
            elif amount > user_data[0]["Balance"]:
                print("Insufficient balance")
            else:
                user_data[0]['Balance'] -= amount
                Bank.__updatedata()
                print("Amount withdrawn successfully")

    def Account_detail(self):
        Account_no = input("Account no: ")
        pin = int(input("Pin: "))
        user_data = [i for i in Bank.data if i["AccountNo"] == Account_no and i['Pin'] == pin]

        if not user_data:
            print("No such user found")
        else:
            for key, value in user_data[0].items():
                print(f"{key} : {value}")

    def update_detail(self):
        account_no = input("Account no: ")
        pin = int(input("Pin: "))
        user_data = [i for i in Bank.data if i["AccountNo"] == account_no and i['Pin'] == pin]

        if not user_data:
            print("No such user found")
        else:
            print("You cannot change your account number. Update your details below (leave blank to keep current):")
            current = user_data[0]
            name = input(f"Name [{current['Name']}]: ") or current['Name']
            age = input(f"Age [{current['Age']}]: ") or current['Age']
            email = input(f"Email [{current['Email']}]: ") or current['Email']
            phone = input(f"Phone [{current['PHONE']}]: ") or current['PHONE']
            pin_new = input(f"Pin [{current['Pin']}]: ") or current['Pin']

            current['Name'] = name
            current['Age'] = int(age)
            current['Email'] = email
            current['PHONE'] = int(phone)
            current['Pin'] = int(pin_new)

            Bank.__updatedata()
            print("Details updated successfully")

    def delete_All_data(self):
        Bank.data.clear()
        Bank.__updatedata()
        print("All data deleted successfully")

    def show_all_data(self):
        for i in Bank.data:
            print(i)

    def Delete_account(self):
        account_no = input("Account no: ")
        pin = int(input("Pin: "))
        user_data = [i for i in Bank.data if i["AccountNo"] == account_no and i['Pin'] == pin]

        if not user_data:
            print("No such user found")
        else:
            Bank.data.remove(user_data[0])
            Bank.__updatedata()
            print("Account deleted successfully")


print("""
Press the following for your task:
1 - Create bank account
2 - Deposit money
3 - Withdraw money
4 - Account detail
5 - Update detail
6 - Delete account
7 - Delete ALL data
8 - Show ALL data
0 - Exit
""")

user = Bank()
check = input("Your choice: ")

if check == "1":
    user.create_Account()
elif check == "2":
    user.deposit_money()
elif check == "3":
    user.withdraw_money()
elif check == "4":
    user.Account_detail()
elif check == "5":
    user.update_detail()
elif check == "6":
    user.Delete_account()
elif check == "7":
    user.delete_All_data()
elif check == "8":
    user.show_all_data()
elif check == "0":
    exit()
else:
    print("Invalid input")