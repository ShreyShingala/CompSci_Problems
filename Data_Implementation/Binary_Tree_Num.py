#ordered data
#leaf node has no child
#depth
#far left as possible
#Build tree from array [2,4,1,5,9] | 2 | 4 1 | 5 9 None None
#learn some charactersistics of tree
#Do the number implementaion 
#insertion, deletion, and traversal.
#let nodes know their depth, and give print func
class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.depth = None
        self.value = value
        
        
class Binary_Tree():
    def __init__(self):
        pass
        
    def make_root_node(self, val):
        root = Node(val)
        root.depth = 0
        return root
    
    def find(self, val, head, depth=0, curpath=""):
        
        if head == None:
            print("Not in list: " + str(val))
        elif head.value == val:
            curpath += str(head.value)
            print("Found Value")
            print("Depth is: " + str(depth))
            print("The path is: " + curpath)
        else:
            curpath += str(head.value) + " -> "
            if val < head.value:
                depth += 1
                self.find(val, head.left, depth, curpath)
            elif val > head.value:
                depth += 1
                self.find(val, head.right, depth, curpath)
        
    
    def determineplace(self, valnew, valog):
        if valnew == valog:
            return None
        if valnew < valog:
            return True
        if valnew > valog:
            return False
      
    def print_tree(self, head, depth = 0):
        if head != None:
            self.print_tree(head.right, depth + 1)
            if depth == 0:
                print(str(head.value))
            else:
                print(' ' * 4 * depth + '-> ' + str(head.value))
            self.print_tree(head.left, depth + 1)
    
    def add_node(self, val, head, const=0):
        depth = const
        depth += 1
        valog = head.value
        whereplace = self.determineplace(val, valog)
        
        if whereplace == None:
            print("Bad Input")
        elif whereplace == True:
            if head.left == None:
                node = Node(val)
                node.depth = depth
                head.left = node
            else:
                self.add_node(val, head.left, depth)
        elif whereplace == False:
            if head.right == None:
                node = Node(val)
                node.depth = depth
                head.right = node
            else:
                self.add_node(val, head.right, depth)
            
BinTree = Binary_Tree()
Head = BinTree.make_root_node(12)
BinTree.add_node(6, Head)
BinTree.add_node(14, Head)
BinTree.add_node(3, Head)
BinTree.add_node(19, Head)
BinTree.add_node(1, Head)
BinTree.add_node(44, Head)
BinTree.add_node(9, Head)
BinTree.print_tree(Head)

BinTree.find(9, Head)