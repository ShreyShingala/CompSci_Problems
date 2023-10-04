# we could turn the entire list itself into a class?

class Node():
    def __init__(self, datavalue=None, nextelem=None):
        self.datavalue = datavalue
        self.nextelem = nextelem

def PrintList(head):
    temp = head
    while temp:
        print(temp.datavalue)
        temp = temp.nextelem

def Find(val, head):
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

def AddFinalElem(val, head):
    temp = head
    while temp.nextelem != None:
        temp = temp.nextelem
    newlastelem = Node(val, None)
    temp.nextelem = newlastelem
    return newlastelem

def AddFirstElem(val, head):
    temp = head
    head = Node(val, temp)
    return head

def RemoveFirstElem(head):
    temp = head.nextelem
    return temp

def RemoveFinalElem(head):
    temp = head
    temp1 = None
    while temp.nextelem != None:
        temp1 = temp
        temp = temp.nextelem
    temp1.nextelem = None
    return temp1

def RemoveAtIndex(index, head):
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
        
def ChangeAtIndex(newval, index, head):
    temp = head
    i = 0
    
    while i < index + 1:
        if i == (index):
            temp.datavalue = newval
        temp = temp.nextelem
            
        i += 1

def AppendAtIndex(val, index, head):
    temp = head
    value = Node(val, None)
    
    i = 0
    
    while i < index:
        
        if i == (index - 1):
            nextnode = temp.nextelem
            temp.nextelem = value
            value.nextelem = nextnode
            break
        
        temp = temp.nextelem
        
        i += 1
        
    return value

def GetLength(head):
    length = 0
    temp = head
    
    while temp:
        
        length += 1
        temp = temp.nextelem
        
    print("List is " + str(length) + " items long")
    return length

def Reverse(head):
    temp = head
    previous = head
    nextelem = head.nextelem
    head.nextelem = None
    
    while temp:
        
        temp = nextelem
        nextelem = temp.nextelem 
        temp.nextelem = previous
        previous = temp
        
        if nextelem == None:
            break

        
        
    return temp        

elem5 = Node("5", None)    
elem4 = Node("4", elem5)
elem3 = Node("3", elem4)
elem2 = Node("2", elem3)
elem1 = Node("1", elem2)

head = elem1

head = AddFirstElem("FIRST", head)
head = AddFirstElem("BETTERFIRST", head)

tail = AddFinalElem("LAST", head)
tail = AddFinalElem("better Last", head)

RemoveAtIndex(4, head)
ChangeAtIndex("Guacamole", 4, head)

head = RemoveFirstElem(head)

tail = RemoveFinalElem(head)

PrintList(head)

AppendAtIndex("Appended", 2, head)

PrintList(head)

GetLength(head)

head = Reverse(head)

PrintList(head)