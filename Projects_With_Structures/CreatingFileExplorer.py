from colorama import Fore #This controls the color

#Hashmaps are used in order to efficently store the dictionaries
#We are using hashmaps in order to efficetly store subdirectories and files and to then access them in constant time.

#We are using trees through the overall strucutre of the file system. They are implemented through the subdirectories of subdirectories.
#MAKE A THING TO PRINT OUT HEIRACHHY 

#We are using linked lists through 

#ADD TOUCH TO MAKE EMPTY
#CHANGE INFO
#ADD INFO#EDIT
#exit

#possible functions cat, echo

class File(): #Class for a defualt text like file
    def __init__(self, name, data=""):
        self.name = name
        self.data = data
        
class Directory(): #This is a directory class to make a directory
    def __init__(self, name, previous=None):
        self.parent = previous
        self.name = name
        self.direcs = {}
        self.files = {}
        
    def addfile(self, file):
        name = file.name
        self.files[name] = file
        
    def adddir(self, dir):
        name = dir.name
        self.direcs[name] = dir
        
    def finddir(self, name):
        return self.direcs[name]
    
    def findfile(self, name):
        return self.files[name]
        
    def printdirectory(self):
        print(".")
        print("..")
        for name, directories in self.direcs.items():
            print(Fore.BLUE + name)
        for name, text in self.files.items():
            print(Fore.GREEN + name)            

    def remove(self, name):
        try:
            self.direcs.pop(name)
        except:
            self.files.pop(name)

class file_explorer():
    def __init__(self):
        self.currentdir = Directory("root")
        self.home = self.currentdir
        self.curpath = ""
        self.addtopath()
        self.clipboard = None
     
    def copy(self, name):
        try:
            temp = self.currentdir.finddir(name) 
        except:
            temp = self.currentdir.findfile(name) 
            
        self.clipboard = temp
        
    def paste(self):
        if self.clipboard != None:
            file = self.clipboard 
            try:
                if file.parent:
                    self.currentdir.adddir(file)
            except:
                self.currentdir.addfile(file)
            
        else:
            print("Copy something first")

        
    def addtopath(self):
        self.curpath += "/" + self.currentdir.name
        
    def remove(self, name):
        self.currentdir.remove(name)
            
        
    def removefrompath(self):
        betterstring = self.currentdir.name
        diff = len(self.curpath) - len(betterstring)
        print(diff)
        self.curpath = self.curpath[0:diff - 1]
        print(self.curpath)
        
    def createfile(self, name, content=""):
        newfile = File(name, content)
        self.currentdir.addfile(newfile)
        
    def createdir(self, name):
        newdir = Directory(name, self.currentdir)
        self.currentdir.adddir(newdir)
        
    def printfile(self, name):
        file = self.currentdir.findfile(name)
        print(file.data)
        
    def change_directory(self, input):
        if input == ".":
            pass
        elif input == "/":
            self.currentdir = self.home
            self.curpath = "/"
            self.addtopath()
        elif input == ".." and self.currentdir.name != "root":
            self.removefrompath()
            self.currentdir = self.currentdir.parent
        else:
            newdir = self.currentdir.finddir(input)
            self.currentdir = newdir
            self.addtopath()
        
        
    def run(self):
        while True:
            user_input = input(Fore.CYAN + self.curpath  + "$ " + Fore.RESET)
            command = user_input.split()
            
            if not command: #So my computer doesn't yell at me
                continue
            
            elif command[0] == "mf":
                try:
                    explorer.createfile(command[1], command[2])
                except:
                    print("Please try again.")
                    print("Incorrect input: mf (file name) (file content)")
            
            elif command[0] == "rm":
                try:
                    explorer.remove(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: rm (file/directory name)")
                    
            elif command[0] == "copy":
                try:
                    explorer.copy(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: copy (file/directory name)")
            
            elif command[0] == "paste":
                explorer.paste()
                
            
            elif command[0] == "mkdir":
                try:
                    explorer.createdir(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: mkdir (directory name)")
            
            elif command[0] == "ls":
                self.currentdir.printdirectory()
            
            elif command[0] == "exit":
                print("Goodbye!")
                break
                
            elif command[0] == "cd":
                #try:
                explorer.change_directory(command[1])
                #except:
                #    print("Please try again.")
                #    print("Incorrect input: cd (directory name)")
                    
            elif command[0] == "cat":
                try:
                    explorer.printfile(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: cat (file name)")
            
            elif command[0] == "help": #CONTINUE TO ADD
                listocommands = [("ls", "lists everything in the directory"), ("help", "gives you a list of all potential commands"), ("echo", "prints out whatever came next")]
            
            elif command[0] == "echo":
                string = ""
                for i in range(1, len(command)):
                    
                    string += command[i] + " "
                    
                print(string)
                
            
                    
            

    
explorer = file_explorer()
explorer.run()