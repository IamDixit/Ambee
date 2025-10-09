'''
    Delhi -> Chennai
    Chennai -> Guwahati
    Mumbai -> pune
    bangalore -> Mumbai
    Guwahati -> Mumbai

    A travel agent have above tickets with him. Display the route for the traveller from any one location
'''
class node:
    def __init__(self, data):
        self.place = data
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

def createTree(root, data):
    newNode = node(data)
    if(root == None):
        print "1st Node added with data ->" + str(data)
        root = newNode
    else:
        print "Node added with data ->" + str(data)
        curr = root
        while(curr.left != None):
            curr = curr.left
        curr.left = newNode
    return root, data

def display(root):
    string = ""
    if(root.left == None):
        string = root.place + "->"
    else:
        while(root):
            string = string + (root.place) + "->"
            root = root.left
    print string + "X"

if __name__ == "__main__":
    tickets = [["delhi","chennai"],["chennai","guwahati"],["mumbai","bangalore"],["bangalore","pune"],["guwahati","mumbai"]]
    json = {}
    for route in tickets:
        json[route[0]] = route[1]

    tree = Tree()
    start = input("Enter your origin destination ")
    root, data = createTree(tree.root, start)
    while(data in json.keys()):
        root, data = createTree(root, json[data])
    print "My Journey Route"
    display(root)
    