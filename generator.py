class Generator:

    def __init__(self,passlen):
        #the only attribute we need here is the password length
        self.passlen=passlen

    def pswrd(self):

        #will not accept from charlists import *
        from charlists import charslowercase
        from charlists import charuppercase
        from charlists import specialchars
        from charlists import numschars
        import random

        #1. create empty list with NONE elements (empty) with the length of the password and a list indexing it with numbers
        passlist=self.passlen*[None] #empty list with the length of password
        passlistnums=list(range(0,len(passlist))) #indexing from 0 to len of passlist

        #2. mandatory elements list randomly selected/ these are elements that must included in the password: one lower, one capital leter, a number and a special character.
        mandatoryelements=[random.choice(charslowercase),random.choice(charuppercase),random.choice(specialchars),random.choice(numschars)]
        #2a. elements that will fill the None positions
        elements=[charslowercase,charuppercase,specialchars,numschars]

        #3. assign every mandatory element on a letter possition of the empty password list
        mandatorychars=random.sample(range(0, len(passlist)), len(mandatoryelements))
        #gets random sample of numbers from list from 0 to length of pass (8,9 or whatever) list equal to the length of elements list (4 numbers)
        #so sample of 4 numbers

        #4. assigning the mandatory elements on the randomly selected position
        for i in range(0,len(mandatorychars)):
            passlist[mandatorychars[i]]=mandatoryelements[i]

        #5. assign random charachters from randomly selected element lists on None list posisionts that left.
        for i in range(0,len(passlist)):
            if passlist[i] is None:
                passlist[i]=(random.choice(random.choice(elements)))

        passwrd="".join(map(str,passlist))
        return passwrd

    #we create a static method that takes all the attributes we want to create the csv file
    @staticmethod
    def filewrite(servicename,sitename,username,pass_word):


        #create and/or append the file that will store the passwords
        f=open("password.csv","a+")
        #open file to append+ means to read and write too.

        f.seek(0)   #set cursor to the beggining of the file
        if f.readline()=="Service,Website,Username,Password\n":
            pass
            #if readline() which is the first line, is equal to the heading (must include the \n as the text has line sepparation)
        else:
            f.write("Service,Website,Username,Password")
            #if the first line is not the heading (means the file is empty or not existent)
            #then add the heading

        f.write(f"\n{servicename},{sitename},{username},{pass_word}")
        f.close()
