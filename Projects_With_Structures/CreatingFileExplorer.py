#----------------------------------- Code for Linked lists Starts ----------------------------
class Data_Node():
    def __init__(self, name, nextelem=None, prevelem=None):
        self.storage = name
        self.nextelem = nextelem
        self.prevelem = prevelem
    
    
class LinkedList():
    def __init__(self):
        pass

    def MakeNode(self, datavalue, nextelem, prevelem):
        return Data_Node(datavalue, nextelem, prevelem)

    def ReturnPrintString(self, head):
        temp = head
        curstring = "["
        
        if head.nextelem == None:
            return temp.datavalue + ", "
        
        while temp:            

            if temp.nextelem != None: 
                curstring += str(temp.datavalue) + ", "
            else:
                curstring += str(temp.datavalue)
            temp = temp.nextelem
        curstring += "], "
        return curstring
        
    def PrintFrom(self, index, head):
        temp = head
        i = -1
        while temp:
            i += 1
            if i >= index:
                print(temp.datavalue)
                
            temp = temp.nextelem

    def PrintList(self, head):
        temp = head
        while temp:
            print(temp.datavalue)
            temp = temp.nextelem
            
    def PrintListReverse(self, tail):
        temp = tail
        while temp:
            print(temp.datavalue)
            temp = temp.prevelem

    def Find(self, val, head):
        temp = head
        i = -1
        while temp:
            i += 1
            data = temp.datavalue
            if str(data) == str(val):
                print("Found " + str(data) + " at index " + str(i))
                return None
            temp = temp.nextelem
        
        print(str(data) + " is not in the Linked List")
        
    def BetterFind(self, val, head):
        temp = head
        i = -1
        while temp:
            i += 1
            data = temp.datavalue
            if str(data) == str(val):
                return True
            temp = temp.nextelem
        
        
        return False
        
    def AddFinalElem(self, val, tail):
        temp = tail
        newlastelem = Data_Node(val, None, temp)
        temp.nextelem = newlastelem
        return newlastelem

    def AddFirstElem(self, val, head):
        temp = head
        head = Data_Node(val, temp, None)
        return head

    def RemoveFirstElem(self, head):
        temp = head.nextelem
        return temp

    def PrintTail(self, tail):
        temp = tail
        return temp.storage
    
    def FindSecondLastElem(self, tail):
        temp = tail
        newtail = temp.prevelem
        return newtail.storage

    def RemoveTail(self, tail):
        temp = tail
        newtail = temp.prevelem
        newtail.nextelem = None
        return newtail

    def RemoveCertainVal(self, val, head):
        temp = head
        val = str(val)
        
        while temp:
            
            if val == temp.datavalue:
                firstvalue = temp.prevelem
                secondvalue = temp.nextelem
            
            temp = temp.nextelem
        
        firstvalue.nextelem = secondvalue
        secondvalue.prevelem = firstvalue

    def RemoveAtIndex(self, index, head):
        temp = head
        i = 0
        
        while i < index + 2:
            if i == (index-1):
                firstvalue = temp
            if i == (index+1):
                secondvalue = temp
            temp = temp.nextelem
                
            i += 1
        
        firstvalue.nextelem = secondvalue
        secondvalue.prevelem = firstvalue
        
            
    def ChangeAtIndex(self, newval, index, head):
        temp = head
        i = 0
        
        while i < index + 1:
            if i == (index):
                temp.datavalue = newval
            temp = temp.nextelem
                
            i += 1

    def AppendAtIndex(self, val, index, head):
        temp = head
        value = Data_Node(val, None)
        
        i = 0
        
        while i < index:
            
            if i == (index - 1):
                prevelem = temp.prevelem
                nextnode = temp.nextelem
                temp.nextelem = value
                value.nextelem = nextnode
                value.prevelem = prevelem
                nextnode.prevelem = value
                break
            
            temp = temp.nextelem
            
            i += 1
            
        return value

    def GetLength(self, head):
        length = 0
        temp = head
        
        while temp:
            
            length += 1
            temp = temp.nextelem
            
        print("List is " + str(length) + " items long")
        return length


#----------------------------------- Code for Linked lists Ends ----------------------------


from colorama import Fore #This controls the color
import json # is used to actually interact with the json file

#Hashmaps are used in order to efficently information and are implemented via the dictionaries.
#We are using hashmaps as it will allow us to access data in constant time.

#We are using trees through the overall strucutre of the file system. 
# They are implemented through the subdirectories of subdirectories, etc.

#We are using Linked lists through the way that we are allowing the user to undo actions.
class File(): #Class for a defualt text like file
    def __init__(self, name, data=""):
        self.name = name # name of file
        self.data = data # data in file
        
    def copy(self): #makes a copy of itself
        return File(self.name, self.data)

        
class Directory(): #This is a directory class to make a directory
    def __init__(self, name, previous=None):
        self.parent = previous #parent directory
        self.name = name #name 
        self.direcs = {} #dictionary of all subdirectories | use of hashmap
        self.files = {} #dictionary of all files | use of hashmap
  
    def add_file(self, file): #adds a file to the directory
        name = file.name
        self.files[name] = file
        
    def add_directory(self, dir): #adds a subdirectory to the directory
        name = dir.name
        self.direcs[name] = dir
        
    def find_directory(self, name): #finds a certain directory and returns in
        return self.direcs[name]
    
    def find_file(self, name): #finds a certain file and returns in
        return self.files[name]
        
    def print_directory(self): #prints out the contents of the directory
        print(".")
        print("..")
        for name, directories in self.direcs.items():
            print(Fore.BLUE + name) #makes the directory names blue
        for name, text in self.files.items():
            print(Fore.GREEN + name) #makes the file names green

    def remove(self, name): #removes a subdirectory/file from the directory
        try: #there is a try here so that it automatically goes to the next one
            self.direcs.pop(name)
        except:
            self.files.pop(name)
            
    def copy(self): #makes a copy of the dircetory using recursion
        new_dir = Directory(self.name, self.parent)
        for subdir_name, subdir in self.direcs.items(): #makes a copy of all subdirectory
            new_subdir = subdir.copy()
            new_subdir.parent = new_dir
            new_dir.add_directory(new_subdir)
        for file_name, file in self.files.items(): #makes a copy of all files
            new_file = file.copy()
            new_dir.add_file(new_file)
        return new_dir #returns the copy
    
    def get_file_dictionary(self): #makes a dictionary of the file contents, used for undoing and loading
        dictionary = {}
        for name, directory in self.direcs.items():
            dictionary["/" + name] = directory.get_file_dictionary()

        for name, file in self.files.items():
            dictionary[name] = file.data

        return dictionary #returns the dictionary
    
    

class file_explorer(): #the file explorer class
    def __init__(self): 
        self.currentdir = Directory("root") #stores the current directory
        self.home = self.currentdir #stores the home root directory
        self.curpath = "" #stores the current path
        self.addtopath() #adds name to current path
        self.clipboard = None #clipboard used for copying
        self.edited_file = None #used to determine if a file is being edited
        self.history = LinkedList() #creates a linked list to store history 
        self.loadingfile = "storage.json" #name of the storage file
        self.tail = self.history.MakeNode(None, None, None) #the tail of the list
         
    def copy(self, name): #makes a copy of the directory/file
        try:
            temp = self.currentdir.find_directory(name) 
            self.clipboard = temp.copy()
        except KeyError:
            temp = self.currentdir.find_file(name) 
            self.clipboard = temp.copy()
        
    def paste(self): #pastes the directory/file
        if self.clipboard != None:
            if isinstance(self.clipboard, Directory):
                new_dir = self.clipboard
                new_dir.parent = self.currentdir
                self.currentdir.add_directory(new_dir)
            elif isinstance(self.clipboard, File):
                new_file = self.clipboard
                self.currentdir.add_file(new_file)
            
        else:
            print("Copy something first")
        
    def addtopath(self): #adds the current directory to the path
        self.curpath += "/" + self.currentdir.name
        
    def remove(self, name): #removes a file/directory
        self.currentdir.remove(name)
            
        
    def removefrompath(self): #finds a certain directory and returns in
        betterstring = self.currentdir.name
        diff = len(self.curpath) - len(betterstring)
        self.curpath = self.curpath[0:diff - 1]
        
    def create_file(self, name, content=""): #creates a file
        string = ""
        for i in range(2, len(content)):
            string += content[i] + " "
        newfile = File(name, string)
        self.currentdir.add_file(newfile)
        
    def create_directory(self, name): #creates a directory
        newdir = Directory(name, self.currentdir)
        self.currentdir.add_directory(newdir)
        
    def print_file(self, name): #prints out the file
        file = self.currentdir.find_file(name)
        print(file.data)
        
    def change_directory(self, input): #changes directory
        if input == ".": #in an actual linux terminal there is a .
            pass
        elif input == "/": # goes to home if the input is /
            self.currentdir = self.home
            self.curpath = ""
            self.addtopath()
        elif input == ".." and self.currentdir.name != "root": #goes back one directory
            self.removefrompath()
            self.currentdir = self.currentdir.parent
        else:
            newdir = self.currentdir.find_directory(input) #changes directory to new directory 
            self.currentdir = newdir
            self.addtopath()
            
    def edit(self, name): #allows you to edit a file
        file = self.currentdir.find_file(name)
        self.edited_file = file
        print(f"Editing file: `{name}`, print exit to leave")
        
    def set_changes(self, name, content): #allows you to set data to a file
        if content == "exit":
            print("Exiting")
        else:
            file = self.currentdir.find_file(name)
            file.data = content
            print("Changes saved")
        
    def store_data(self): #stores data in the json storage
        data = {"/root":self.home.get_file_dictionary()}

        with open(self.loadingfile, 'w') as lf:
            json.dump(data, lf)
        lf.close()
    
    def convert_json_to_directory(self, name, dictionary, previousdirectory): #converts json to a directory, used for both undo and loading
        directory = Directory(name, previousdirectory)
        
        for key, value in dictionary.items():
            if "/" in key:
                directory.direcs[key.replace("/", "")] = self.convert_json_to_directory(key.replace("/", ""), value, directory)
            else:
                directory.files[key] = File(key, value)

        return directory

    def load_dict(self, string, dict): #loads a dictionary 
        for key, value in dict.items():
            nroot = self.convert_json_to_directory(key, value, None)

        self.curpath = string
        self.home = nroot

        if string == "/root":
            self.currentdir = self.home
        else:
            curdirectory = self.home
            for d in string.replace("/root", "")[1:].split("/"):
                curdirectory = curdirectory.direcs[d]

            self.currentdir = curdirectory

    def import_json(self): #allows you to import the storage json file
        with open(self.loadingfile, 'r') as lf:
            data = json.load(lf)
        lf.close()

        for key, value in data.items():
            nroot = self.convert_json_to_directory(key, value, None)

        self.curpath = "/root"
        self.home = nroot
        self.currentdir = self.home

    def snapshot_history(self, snapshot=None): #makes a snapshor of the history 
        if snapshot:
            self.tail = self.history.AddFinalElem(snapshot, self.tail)
            return
        self.tail = self.history.AddFinalElem((self.curpath, {"/root":self.home.get_file_dictionary()}), self.tail)
          
    def undo(self): #undoes previous command
        previous = self.history.FindSecondLastElem(self.tail)
        if previous != None:
            laststring, lastdict = previous
            explorer.load_dict(laststring, lastdict)
            self.tail = self.history.RemoveTail(self.tail)
        else:
            print("Do something first")
            
    def run(self): #runs the actual terminal
        
        explorer.snapshot_history() #takes a snapshot for history
        
        while True: #is while true so it always run
            if explorer.edited_file != None: #checks if a file is being edited
                text = input()
                explorer.set_changes(explorer.edited_file.name, text)
                explorer.edited_file = None
            
            user_input = input(Fore.CYAN + self.curpath  + "$ " + Fore.RESET) #gets command input
            command = user_input.split()
            
            if not command: #So my computer doesn't yell at me
                continue
            
            elif command[0] == "mf": #makes a file
                try:
                    explorer.create_file(command[1], command)
                except:
                    print("Please try again.")
                    print("Incorrect input: mf (file name) (file content)")
                    
            elif command[0] == "undo": #undoes a command
                explorer.undo()

            
            elif command[0] == "rm": #removes a file
                try:
                    explorer.remove(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: rename (orignial name) (new name)")
            elif command[0] == "copy": #copies a file
                try:
                    explorer.copy(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: copy (file/directory name)")
            elif command[0] == "edit": #allows you to edit a file
                try:
                    explorer.edit(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: copy (file/directory name)")
            elif command[0] == "paste": #pastes something
                explorer.paste()
            elif command[0] == "mkdir": #makes directory
                try:
                    explorer.create_directory(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: mkdir (directory name)")
            
            elif command[0] == "ls": #lists all directories
                self.currentdir.print_directory()
            
            elif command[0] == "exit": #exits
                print("Goodbye!")
                break
                
            elif command[0] == "cd": #changes directory
                try:
                    explorer.change_directory(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: cd (directory name)")
                    
            elif command[0] == "cat": #prints content of file
                try:
                    explorer.print_file(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: cat (file name)")
            
            elif command[0] == "help": #prints list of all commands
                listocommands = [("mf", "makes a file"), ("undo", "Undoes your previous edit"), ("rm", "removes a directory"), ("copy", "copies a directory/file to your clipboard"), ("paste", "pastes your clipboard into the current directory"), ("edit", "allows you to edit a file"), ("mkdir", "makes a directory"), ("ls", "lists everything in the directory"), ("help", "gives you a list of all potential commands"), ("echo", "prints out whatever came next"), ("cd", "allows you to change your directory"), ("cat", "prints out the contents of a file"), ("exit", "exit this wonderful program")]
                for i in range(len(listocommands)):
                    print(listocommands[i][0] + " | " + listocommands[i][1])
            
            elif command[0] == "echo": #repeates what we did
                string = ""
                for i in range(1, len(command)):
                    
                    string += command[i] + " "
                print(string)   
                
            elif command[0] == "load": #loads a new file
                explorer.import_json()
                
            explorer.store_data() #stores data
            if (snap := (explorer.curpath, {"/root":explorer.home.get_file_dictionary()})) != explorer.history.PrintTail(self.tail): #if it is different
                explorer.snapshot_history(snap)
            
explorer = file_explorer()
explorer.run()