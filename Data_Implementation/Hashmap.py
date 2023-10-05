#index = key%available adresses

#Objectives, Minimize collisions, uniform distribution, easy to calculate, resolve solutions

from Linked_list import *

def AddPrefectData():
    Hashmap.AddData("Mia")
    Hashmap.AddData("Tim")
    Hashmap.AddData("Bae")
    Hashmap.AddData("Zoe")
    Hashmap.AddData("Jan")
    Hashmap.AddData("Ada")
    Hashmap.AddData("Leo")
    Hashmap.AddData("Sam")
    Hashmap.AddData("Lou")
    Hashmap.AddData("Max")
    Hashmap.AddData("Ted")

def AddImperfectData():
    Hashmap.AddData("Mia")
    Hashmap.AddData("Tim")
    Hashmap.AddData("Bae")
    Hashmap.AddData("Zoe")
    Hashmap.AddData("Sue")
    Hashmap.AddData("Len")
    Hashmap.AddData("Moe")
    Hashmap.AddData("Lou")
    Hashmap.AddData("Rae")
    Hashmap.AddData("Max")
    Hashmap.AddData("Tod")
    

class Hashmap():
    def __init__(self, size):
        self.size = size
        self.Hashtable = [None] * size 
        
    def PrintTable(self):
        currstring = "["
        for i in range(len(self.Hashtable)):
            if self.Hashtable[i] == None:
                currstring += "None, "
            else:
                linkylist = LinkedList()
                currstring += linkylist.ReturnPrintString(self.Hashtable[i])
                
        print(currstring)
        
    def HashFunc(self, Data):
        key = 0
        for chr in Data:
            key += ord(chr)

        key = key % self.size
        return key
                
    def AddData(self, Data):
        key = self.HashFunc(Data)
        if self.Hashtable[key] == None:
            linkylist = LinkedList()
            self.Hashtable[key] = linkylist.MakeNode(Data, None)
        else:
            linkylist = LinkedList()
            linkylist.AddFinalElem(Data, self.Hashtable[key])

    def FindData(self, Data):
        key = self.HashFunc(Data)
        linkylist = LinkedList()
        temp = self.Hashtable[key]
        if Data == temp.datavalue:
            print("Found " + str(Data) + " at index " + str(key))
        else:
            if linkylist.BetterFind(Data, self.Hashtable[key]):
                print("Found " + str(Data) + " at index " + str(key))
            else:
                print(str(Data) + " was not found in the Hashmap")

Hashmap = Hashmap(11)

#AddPrefectData()
AddImperfectData()

Hashmap.PrintTable()

