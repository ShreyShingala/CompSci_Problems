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

    def RemoveFinalElem(self, tail):
        temp = tail
        newtail = temp.prevelem
        newtail.nextelem = 0
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

from colorama import Fore #This controls the color
import os

#Hashmaps are used in order to efficently store the dictionaries
#We are using hashmaps in order to efficetly store subdirectories and files and to then access them in constant time.

#We are using trees through the overall strucutre of the file system. They are implemented through the subdirectories of subdirectories.

#We are using Linked lists through the way that we are allowing the user to undo actions.
#UNDO AND ADD JSON



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
            new_subdir.parent = new_dir
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
        self.edited_file = None
         
    def copy(self, name):
        try:
            temp = self.currentdir.find_directory(name) 
            self.clipboard = temp.copy()
        except KeyError:
            temp = self.currentdir.find_file(name) 
            self.clipboard = temp.copy()
        
    def paste(self):
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
            
    def edit(self, name):
        file = self.currentdir.find_file(name)
        self.edited_file = file
        print(f"Editing file: `{name}`, print exit to leave")
        
    def set_changes(self, name, content):
        if content == "exit":
            print("Exiting")
        else:
            file = self.currentdir.find_file(name)
            file.data = content
            print("Changes saved")
        
    def run(self):
        while True:
            if explorer.edited_file != None:
                text = input()
                explorer.set_changes(explorer.edited_file.name, text)
                explorer.edited_file = None
            
            user_input = input(Fore.CYAN + self.curpath  + "$ " + Fore.RESET)
            command = user_input.split()
            
            if not command: #So my computer doesn't yell at me
                continue
            
            elif command[0] == "mf":
                try:
                    explorer.create_file(command[1], command)
                except:
                    print("Please try again.")
                    print("Incorrect input: mf (file name) (file content)")
                    
            elif command[0] == "undo":
                pass

            
            elif command[0] == "rm":
                try:
                    explorer.remove(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: rename (orignial name) (new name)")
                    
            elif command[0] == "copy":
                try:
                    explorer.copy(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: copy (file/directory name)")
            elif command[0] == "edit":
                try:
                    explorer.edit(command[1])
                except:
                    print("Please try again.")
                    print("Incorrect input: copy (file/directory name)")
            
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
            
            elif command[0] == "help":
                listocommands = [("mf", "makes a file"), ("undo", "Undoes your previous edit"), ("rm", "removes a directory"), ("copy", "copies a directory/file to your clipboard"), ("paste", "pastes your clipboard into the current directory"), ("edit", "allows you to edit a file"), ("mkdir", "makes a directory"), ("ls", "lists everything in the directory"), ("help", "gives you a list of all potential commands"), ("echo", "prints out whatever came next"), ("cd", "allows you to change your directory"), ("cat", "prints out the contents of a file"), ("exit", "exit this wonderful program")]
                for i in range(len(listocommands)):
                    print(listocommands[i][0] + " | " + listocommands[i][1])
            
            elif command[0] == "echo":
                string = ""
                for i in range(1, len(command)):
                    
                    string += command[i] + " "
                    
                print(string)

                
            
explorer = file_explorer()
explorer.run()