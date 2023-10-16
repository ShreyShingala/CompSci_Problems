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
        
    def copy(self):
        return File(self.name, self.data)
        
class Directory(): #This is a directory class to make a directory
    def __init__(self, name, previous=None):
        self.parent = previous
        self.name = name
        self.direcs = {}
        self.files = {}
        
    def add_file(self, file):
        name = file.name
        self.files[name] = file
        
    def add_directory(self, dir):
        name = dir.name
        self.direcs[name] = dir
        
    def find_directory(self, name):
        return self.direcs[name]
    
    def find_file(self, name):
        return self.files[name]
        
    def print_directory(self):
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
            
    def copy(self):
        new_dir = Directory(self.name, self.parent)
        for subdir_name, subdir in self.direcs.items():
            new_subdir = subdir.copy()
            new_dir.add_directory(new_subdir)
        for file_name, file in self.files.items():
            new_file = file.copy()
            new_dir.add_file(new_file)
        return new_dir

class file_explorer():
    def __init__(self):
        self.currentdir = Directory("root")
        self.home = self.currentdir
        self.curpath = ""
        self.addtopath()
        self.clipboard = None
     
    def copy(self, name):
        try:
            self.clipboard = self.currentdir.direcs[name].copy()
        except KeyError:
            self.clipboard = self.currentdir.files[name].copy()

    def paste(self):
        if self.clipboard:
            if isinstance(self.clipboard, Directory):
                new_dir = self.clipboard.copy()
                self.currentdir.add_directory(new_dir)
                new_dir.parent = self.currentdir
            elif isinstance(self.clipboard, File):
                new_file = self.clipboard.copy()
                self.currentdir.add_file(new_file)
        else:
            print("Copy something first")
        
    def addtopath(self):
        self.curpath += "/" + self.currentdir.name
        
    def remove(self, name):
        self.currentdir.remove(name)
            
        
    def removefrompath(self):
        betterstring = self.currentdir.name
        diff = len(self.curpath) - len(betterstring)
        self.curpath = self.curpath[0:diff - 1]
        
    def create_file(self, name, content=""):
        string = ""
        for i in range(2, len(content)):
            string += content[i] + " "
        newfile = File(name, string)
        self.currentdir.add_file(newfile)
        
    def create_directory(self, name):
        newdir = Directory(name, self.currentdir)
        self.currentdir.add_directory(newdir)
        
    def print_file(self, name):
        file = self.currentdir.find_file(name)
        print(file.data)
        
    def change_directory(self, input):
        if input == ".":
            pass
        elif input == "/":
            self.currentdir = self.home
            self.curpath = ""
            self.addtopath()
        elif input == ".." and self.currentdir.name != "root":
            self.removefrompath()
            self.currentdir = self.currentdir.parent
        else:
            newdir = self.currentdir.find_directory(input)
            self.currentdir = newdir
            self.addtopath()
        
        
    def run(self):
        while True:
            user_input = input(Fore.CYAN + self.curpath  + "$ " + Fore.RESET)
            command = user_input.split()
            
            if not command: #So my computer doesn't yell at me
                continue
            
            elif command[0] == "mf":
                #try:
                explorer.create_file(command[1], command)
                #except:
                #    print("Please try again.")
                #    print("Incorrect input: mf (file name) (file content)")
            
            elif command[0] == "rm":
                try:
                    explorer.remove(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: rm (file/directory name)")
                    
            elif command[0] == "copy":
                
                explorer.copy(command[1])
            
        
            elif command[0] == "paste":
                explorer.paste()
                
            
            elif command[0] == "mkdir":
                try:
                    explorer.create_directory(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: mkdir (directory name)")
            
            elif command[0] == "ls":
                self.currentdir.print_directory()
            
            elif command[0] == "exit":
                print("Goodbye!")
                break
                
            elif command[0] == "cd":
                try:
                    explorer.change_directory(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: cd (directory name)")
                    
            elif command[0] == "cat":
                try:
                    explorer.print_file(command[1])
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


#def edit_file(self, name):
#        if name == "":
#            print("Invalid name")
#            return
#        if name in self.current_directory.files:
#            self.wait_change_file = name
##            print(f"Editing file: `{name}`, enter content or submit exit to exit operation")
 #       else:
#            print("File dosent exist")#

#    def set_edit_changes(self, name, content):
#        if content == "exit":
#            print("Exiting operation...")
#        else:
#            self.current_directory.files[name].content = content
#            print("Changes created")