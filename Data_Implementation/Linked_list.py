
class Node():
    def __init__(self, datavalue=None, nextelem=None):
        self.datavalue = datavalue
        self.nextelem = nextelem
    
class LinkedList():
    def __init__(self):
        pass

    def MakeNode(self, datavalue, nextelem):
        return Node(datavalue, nextelem)

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
        

    def PrintList(self, head):
        temp = head
        while temp:
            print(temp.datavalue)
            temp = temp.nextelem

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

    def AddFinalElem(self, val, head):
        temp = head
        while temp.nextelem != None:
            temp = temp.nextelem
        newlastelem = Node(val, None)
        temp.nextelem = newlastelem
        return newlastelem

    def AddFirstElem(self, val, head):
        temp = head
        head = Node(val, temp)
        return head

    def RemoveFirstElem(self, head):
        temp = head.nextelem
        return temp

    def RemoveFinalElem(self, head):
        temp = head
        temp1 = None
        while temp.nextelem != None:
            temp1 = temp
            temp = temp.nextelem
        temp1.nextelem = None
        return temp1

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

    def GetLength(self, head):
        length = 0
        temp = head
        
        while temp:
            
            length += 1
            temp = temp.nextelem
            
        print("List is " + str(length) + " items long")
        return length

    def Reverse(self, head):
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

#linkylist = LinkedList()

#elem5 = linkylist.MakeNode("5", None)    
#elem4 = linkylist.MakeNode("4", elem5)
#elem3 = linkylist.MakeNode("3", elem4)
#elem2 = linkylist.MakeNode("2", elem3)
#elem1 = linkylist.MakeNode("1", elem2)

#head = elem1

#head = linkylist.AddFirstElem("FIRST", head)
#head = linkylist.AddFirstElem("BETTERFIRST", head)

#tail = linkylist.AddFinalElem("LAST", head)
#tail = linkylist.AddFinalElem("better Last", head)

#linkylist.RemoveAtIndex(4, head)
#linkylist.ChangeAtIndex("Guacamole", 4, head)

#head = linkylist.RemoveFirstElem(head)

#tail = linkylist.RemoveFinalElem(head)

#linkylist.PrintList(head)

#linkylist.AppendAtIndex("Appended", 2, head)

#linkylist.PrintList(head)

#linkylist.GetLength(head)

#head = linkylist.Reverse(head)

#linkylist.PrintList(head)