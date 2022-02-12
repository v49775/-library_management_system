# library management system

# create a library class
# methods is :
#     displaybooks
#     lend books
#     add books
#     return books

# harrylibrary = (listofboosks,library name)
# create a dictionary (books:user name)
#create a main function and run infinite while loop asking user for there input


import time

class Library:

    def __init__(self,list,lname):
        self.list = list
        self.lname = lname

    def displaybooks(self):
        return f"{self.list} ..."

    def lendBooks(self,string):
        self.string = string
        return self.list.remove(self.string)

    def addBooks(self,string):
        self.string = string
        return self.list.append(self.string)

    def returnBooks(self,dict):
        keys = dict.keys()
        value = dict.values()
        key1 = list(keys)[0]
        value1 = list(value)[0]
        return f"{value1} is {self.addBooks(key1)} return successfull"


if __name__ == '__main__':
    lib1 = Library(["c", "c++", "java", "python", "PHP", "database", "HTML", "javascript"], "Vinayak_library")
    i = 1
    user_name = input("Enter Username : ")
    lab_code = int(input("Enter Password : "))
    if lab_code == 1234:

        while(i<=10):
            print("Enter 1 to Display list of Books")
            print("Enter 2 to Lend a Books")
            print("Enter 3 to Add a Books in library")
            print("Enter 4 to Return a Books")
            print("Enter 0 to EXIT")
            ninput = int(input())


            if ninput == 1:
                print(lib1.displaybooks())
                print(" ")
                time.sleep(2)
                continue


            elif ninput == 2:
                akstolend = input("Emter a book name you want to lend it : ")
                print(lib1.lendBooks(akstolend))
                time.sleep(2)
                continue

            elif ninput == 3:
                asktoadd = input("Emter a book name you want to add it : ")
                print(lib1.addBooks(asktoadd))
                time.sleep(2)
                continue

            elif ninput == 4:
                rbooksname = input("Enter a books name you want return it : ")
                print(lib1.returnBooks({rbooksname: user_name}))
                time.sleep(2)
                continue

            elif ninput == 0:
                break


            else:
                print("Your are Enter Wrong input please choose one option")
                continue

            i = i+1

    else:
        print("logging Failed!!!, you enter wrong passsword and username")








