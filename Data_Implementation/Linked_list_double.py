#DONE -  Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward).
#DONE Write a Python program to create a doubly linked list and print nodes from current position to first node.
#DONE Write a Python program to count the number of items of a given doubly linked list.
#DONE Write a Python program to print a given doubly linked list in reverse order.
#DONE Write a Python program to insert an item in front of a given doubly linked list.
#DONE Write a Python program to search a specific item in a given doubly linked list and return true if the item is found otherwise return false.
#14. Write a Python program to delete a specific item from a given doubly linked list.


class Node():
    def __init__(self, datavalue=None, nextelem=None, prevelem=None):
        self.datavalue = datavalue
        self.nextelem = nextelem
        self.prevelem = prevelem
    
    
class LinkedList():
    def __init__(self):
        pass

    def MakeNode(self, datavalue, nextelem, prevelem):
        return Node(datavalue, nextelem, prevelem)

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
        newlastelem = Node(val, None, temp)
        temp.nextelem = newlastelem
        return newlastelem

    def AddFirstElem(self, val, head):
        temp = head
        head = Node(val, temp, None)
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
        value = Node(val, None)
        
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
       

#linkylist = LinkedList()


#head = linkylist.MakeNode("1", None, None)
#tail = head
#tail = linkylist.AddFinalElem("2", tail)
#tail = linkylist.AddFinalElem("3", tail)
#tail = linkylist.AddFinalElem("4", tail)
#tail = linkylist.AddFinalElem("5", tail)

#linkylist.PrintList(head)
#print("____________________")
#linkylist.PrintFrom(2, head)
#print("____________________")
#linkylist.GetLength(head)
#print("____________________")
#linkylist.PrintListReverse(tail)
#print("____________________")
#head = linkylist.AddFirstElem("FIRST", head)
#linkylist.PrintList(head)
#print("____________________")
#linkylist.Find(3, head)
#print("____________________")
#linkylist.RemoveAtIndex(3, head)
#linkylist.RemoveCertainVal(2, head)
#linkylist.PrintList(head)

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