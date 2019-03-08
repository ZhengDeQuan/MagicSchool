class Node():
    def __init__(self,left = None , right = None, val = None):
        super(Node,self).__init__()
        self.left = left
        self.right = right
        self.val = val


def LevelTravel(root):
    ListLeft= []
    ListRight = []
    ListRight.append(root)
    while True:
        for ele in ListRight:
            print(ele.val,end=" ")
            if ele.right:
                ListLeft.append(ele.right)
            if ele.left:
                ListLeft.append(ele.left)
        print("\n","This Level finished","*"*10)
        ListLeft = ListLeft[::-1]
        ListRight = []
        for ele in ListLeft:
            print(ele.val,end=" ")
            if ele.left:
                ListRight.append(ele.left)
            if ele.right:
                ListRight.append(ele.right)
        print("\n","This Level finished","*"*10)
        ListRight = ListRight[::-1]
        ListLeft = []

        if not ListRight and not ListLeft:
            break

def makeTree(List):
    root = Node()
    root.val = List[0]
    cur = root
    for ele in List[1:]:
        cur = root
        while True:
            if ele > cur.val:
                if cur.right is None:
                    cur.right = Node(val = ele)
                    break
                else:
                    cur = cur.right
            else :
                if cur.left is None:
                    cur.left = Node(val = ele)
                    break
                else:
                    cur = cur.left
    return root

if __name__ == "__main__":
    root = makeTree([15,
                    7,20,
                     3,10,18,22,
                     2,4,8,12,17,19,21,23])
    # print(root.val)
    # print(root.left.val)
    # print(root.right.val)
    LevelTravel(root)
