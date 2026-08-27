from pathlib import Path   #used to import path of used foler
import os

def confirm(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")

def readfileandfolder():  #created a function to show user the already present files and folders 
    path = Path('')       #path is empty to show the current folder as default
    items = list(path.rglob('*'))    #rglob() or recursive globe function created a list of present files and folders
    for i,items in enumerate(items):  #this is done to save index and values separately
        print(f"{i+1} : {items}")    #f " " used to write formatted string  i+1 to see from index 1 not 0



def createfile():
    try:    #did exception handling if any error occurs
        readfileandfolder()   # shows user the existing files and folders
        name = input ("Write your file name : ")
        p = Path(name)  #gave the path to the file using Path function

        if not p.exists():  #if p do not exist then the function runs if file exits it comes TRUE but not converts it to FALSE
            with open(p,"w") as fs:
                data = input("Enter file content:")
                fs.write(data)
            print(f"File created successfully")  
        else:
            print(f"This file already exists")
            
        
    except Exception as err:
        print(f"An error occured with {err}")


def readfile():

    try:
        readfileandfolder() #show existing files 
        name = input("enter name of file to read:")
        p = Path(name) #if name exist its path is taken if not exists its path is created
        if p.exists() and p.is_file():
            with open(p,'r') as fs :
                data = fs.read()
                print(f"Content of {name} is :",data)
        else:
            print("File does not exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file to update:")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the file name")
            print("press 2 for overwriting the file data")
            print("press 3 for appending data to the file")

            res = int(input("Enter option:"))

            if res == 1:
                name2 = input("Enter new file name:")
                p2 = Path(name2)
                p.rename(p2)  # p is renamed by path p2
            elif res == 2:
                if confirm(f"Overwrite the contents of {p}"):
                    with open(p,'w') as fs:
                        data = input("Tell what you want to overwrite :")
                        fs.write(data)
                else:
                    print("Overwrite cancelled")
            elif res == 3:
                with open(p,"a") as fs:
                    data = input ("Tell what you want to append :")
                    fs.write(" "+data)  #" " given to have a space between old and new  data
            else:
                print("Invalid update option")
    except Exception as err:
        print(f"An error occured as {err}")

def delete():
    try:
        readfileandfolder()
        name = input("Which file you want to delete:")

        p = Path(name)
        if p.exists() and p.is_file():

            if confirm(f"Delete {p}"):
                os.remove(name)  #with help of os the file is removed so os is imported for this function
                print("File removed successfully")
            else:
                print("Delete cancelled")
        else:
            print("No such file Exists")
    except Exception as err:
        print(f"An error occured as {err}")

    
        
    
while True:
    print("\npress 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 for exiting")

    try:
        response = int(input("Enter your response:"))
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue

    if response == 1:
        createfile()
    elif response == 2:
        readfile()
    elif response == 3:  #name change,overwrite or append
        updatefile()
    elif response == 4:
        delete()
    elif response == 5:
        print("Goodbye")
        break
    else:
        print("Invalid menu option")