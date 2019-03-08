class Node:
    def __init__(self,val=-1):
        self.val = val
        self.left = None
        self.right = None


def makeBTree(List,root):
    for ele in List:
        cur = root
        while True:
            if ele > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(ele)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(ele)
                    break

def reverse(from_node , to_node):
    x = from_node
    y = from_node.right
    x.right = None # very important details
    while x!= to_node:
        z = y.right
        y.right = x
        x = y
        y = z

def reverseOutput(from_node, to_node):
    reverse(from_node , to_node)

    cur = to_node
    while True:
        print(cur.val)
        if cur == from_node:
            break
        cur = cur.right

    reverse(to_node,from_node)

def MorrisTraveralPostOrder(root):
    temp = Node(-1)
    temp.left = root
    cur = temp
    while cur:
        if cur.left is None:
            cur = cur.right
        else:
            temp= cur.left
            while temp.right and temp.right != cur:
                temp = temp.right
            if temp.right is None:
                temp.right = cur
                cur = cur.left
            else:
                temp.right = None
                reverseOutput(cur.left,temp)
                cur = cur.right

def MorrisTravelMidOrder(root):
    '''莫里斯中序遍历'''
    pre = None
    if root is None:
        return
    curr = root
    while curr is not None:
        if curr.left is None:
            print(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr #说明是第二次到达cur这个节点，是通过pre.right走到cur的这个节点的
                curr = curr.left
            elif pre.right == curr:
                pre.right = None
                print(curr.val)
                curr = curr.right

def PostOreder(root):
    last_visited = None
    #如果上一个被访问的元素是右子节点，那么下一个需要访问的就是当前节点
    cur = root
    stack = []
    while cur:
        stack.append(cur)
        cur = cur.left
    while stack:
        cur = stack.pop(-1)
        if cur.right is None or cur.right == last_visited:
            print(cur.val)
            last_visited = cur
        else:
            stack.append(cur)
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left


if __name__ == "__main__":
    List = [5, 8 , 3 , 2, 4, 1 , 6,7,9]
    root =Node(List[0])
    makeBTree(List[1:],root)
    MorrisTraveralPostOrder(root)
    print("*"*100)
    PostOreder(root)