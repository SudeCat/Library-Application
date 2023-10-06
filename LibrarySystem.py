class Library:
    def listAllbooks(self):
        ccfile = open("books.txt", "r")
        alines = ccfile.readlines()
        alist=[]
        for line in alines:
            line = line.rstrip()
            words = line.split(",")
            alist.append(words[1])
        return "\n".join(alist)

    def listCheckedBooks(self):
        ccfile = open("books.txt", "r")
        alines = ccfile.readlines()
        alist = []
        for line in alines:
            line = line.rstrip()
            words = line.split(",")
            if words[3]=="T":
                alist.append(words[1])
        return "\n".join(alist)

    def addNewBook(self):
        afile=open("books.txt","r")
        lines = afile.readlines()
        alist = []
        for line in lines:
            line = line.rstrip()
            words = line.split(",")
            alist.append(words[0])
        afile.close()
        ccfile = open("books.txt", "a")
        ISBNNO=input("Please enter the ISBN number:")
        bookName=input("Please enter the book name:")
        authorName=input("Please enter the author name:")

        if ISBNNO not in alist:
            ccfile.write("\n"+ISBNNO+","+bookName+","+authorName+",F\n")
            return("The book is added")
        else:
            return("This book is already exist")

    def searchBookISBN(self):
        isbn=input("Please enter the ISBN number to search:")
        ccfile = open("books.txt", "r")
        alines = ccfile.readlines()
        alist=[]
        for line in alines:
            line = line.rstrip()
            words = line.split(",")
            if words[0]==isbn:
                alist.append(words[1])
        if alist == []:
            print("Not found")
        return "".join(alist)

    def searchBookName(self):
        name = input("Please enter the name to search:")
        ccfile = open("books.txt", "r")
        alines = ccfile.readlines()
        alist=[]
        for line in alines:
            line = line.rstrip()
            words = line.split(",")
            if name in words[1].lower():
                alist.append(words[1])
        if alist==[]:
            print("Not found")
        return "\n".join(alist)

    def checkOutBook(self):
        student=input("Enter your ID:")
        bookName=input("Enter the book name to borrow (You can type in lower case):")
        ccfile =open("books.txt", "r")
        onfile = open("checkOutsAndStudents", "a")
        alines = ccfile.readlines()
        ccfile=open("books.txt","w")

        for line in alines:
            line = line.rstrip()
            words = line.split(",")
            if bookName==words[1].lower():
                if words[3]=="F":
                    words[3]=words[3].replace("F","T")
                    onfile.write("\n"+student+","+words[1]+"\n")
                else:
                    print("You can't borrow this book")
            line=",".join(words)
            ccfile.write(line+"\n")
        return("The book is checked out")


    def listStudents(self):
        ccfile = open("students.txt", "r")
        alines = ccfile.readlines()
        afile=open("checkOutsAndStudents","r")
        otherLines=afile.readlines()
        alist = []
        otherDic={}
        for otherLine in otherLines:
            otherLine=otherLine.rstrip()
            otherWords=otherLine.split(",")
            for i in otherWords:
                if i==otherWords[0]:
                    otherDic.setdefault(i,[]).append(otherWords[1])
        for line in alines:
            line = line.rstrip()
            words = line.split(" ")
            if words[0] in otherDic.keys():
                alist.append(words[1]+" "+words[2]+"\nThe books:"+str(otherDic.get(words[0])))
            else:
                alist.append(words[1] + " " + words[2])
        return "\n".join(alist)

    def listTop3Book(self):
        ccfile = open("checkOutsAndStudents", "r")
        lines = ccfile.readlines()
        dic={}
        sortedDic={}
        for line in lines:
            line = line.rstrip()
            words = line.split(",")
            for i in words:
                if i==words[1]:
                    if i in dic:
                        dic[i]=dic[i]+1
                    else:
                        dic[i]=1
        for i in sorted(dic.values(),reverse=True):
            for k in dic.keys():
                if dic[k]==i:
                    sortedDic[k]=dic[k]

        first=next(iter(sortedDic))
        del sortedDic[next(iter(sortedDic))]
        second=next(iter(sortedDic))
        del sortedDic[next(iter(sortedDic))]
        third=next(iter(sortedDic))
        del sortedDic[next(iter(sortedDic))]
        return [first,second,third]

    def listTop3Student(self):
        ccfile = open("checkOutsAndStudents", "r")
        lines = ccfile.readlines()
        dic = {}
        sortedDic = {}
        for line in lines:
            line = line.rstrip()
            words = line.split(",")
            for i in words:
                if i == words[0]:
                    if i in dic:
                        dic[i] = dic[i] + 1
                    else:
                        dic[i] = 1
        for i in sorted(dic.values(),reverse=True):
            for k in dic.keys():
                if dic[k]==i:
                    sortedDic[k]=dic[k]
        first = next(iter(sortedDic))
        del sortedDic[next(iter(sortedDic))]
        second = next(iter(sortedDic))
        del sortedDic[next(iter(sortedDic))]
        third = next(iter(sortedDic))
        del sortedDic[next(iter(sortedDic))]

        afile=open("students.txt","r")
        lines=afile.readlines()
        for line in lines:
            line=line.rstrip()
            words=line.split(" ")
            if first==words[0]:
                first=words[1] + " "+ words[2]+", "+str(dic.get(words[0]))
            elif second==words[0]:
                second= words[1] + " " + words[2]+", "+str(dic.get(words[0]))
            elif third==words[0]:
                third=words[1] + " " + words[2]+", "+str(dic.get(words[0]))

        return first,second,third


menu="""  Welcome to the Library Management System     
------------------------------------------------------
[1] List all the books in the library.
[2] List all the books that are checked out.
[3] Add a new book.
[4] Search a book by ISBN number.
[5] Search a book by name.
[6] Check out a book to a student.
[7] List all the students and the books if they are checked out.
[8] List top 3 most checked out books in the library
[9] List top 3 students with the highest checked out numbers in the library
[10] Exit"""

while True:
    print(menu)
    option=input("Please enter a number of the action you want to do:")
    if option=="1":
        print(Library.listAllbooks("books.txt"))
    elif option=="2":
        print(Library.listCheckedBooks("books.txt"))
    elif option=="3":
        print(Library.addNewBook("books.txt"))
    elif option=="4":
        print(Library.searchBookISBN("books.txt"))
    elif option=="5":
        print(Library.searchBookName("books.txt"))
    elif option=="6":
        print(Library.checkOutBook("books.txt"))
    elif option=="7":
        print(Library.listStudents("books.txt"))
    elif option=="8":
        print(Library.listTop3Book("books.txt"))
    elif option=="9":
        print(Library.listTop3Student("books.txt"))
    else:
        print("Have a good day!")
        break