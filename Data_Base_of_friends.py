import pandas as pd

# create the information for each Contact
name = ["William", "Spiros", "Haris"]
surname = ["", "", ""]
age = [20, 21, 22]
country = ["Poland", "Greece", "Greece"]
contact = ["+48 884173343", "+30 6930114769", "+30 6981568450"]
# information made to Series
data = {"Name:": pd.Series(data=name),
        "Surname:": pd.Series(data=surname),
        "Contact:": pd.Series(data=contact),
        "Age:": pd.Series(data=age),
        "Country:": pd.Series(data=country)
        }
# creating/printing the DataFrame
data_base = pd.DataFrame(data=data)
print(data_base)

while input("Whould you like to add a contact? Y/N: ") == "Y":
    # create the new DataFrame
    new_info = {"Name:": pd.Series(data=input("What's his/her name?")),
                "Surname:": pd.Series(data=input("What's his/her surname?")),
                "Contact:": pd.Series(data=input("What's his/her phone number? ")),
                "Age:": pd.Series(data=input("What's his/her age? ")),
                "Country:": pd.Series(data=input("Where is he/she from? ")),
                }
    new_contact = pd.DataFrame(data=new_info)
    data_base = data_base.append(new_contact, ignore_index=True)
    print(data_base)
