import torch
import torch.nn.functional as F
a = [[1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9]]
def func(ele):
    return 1.0 * ele
a =[list(map(func , ele)) for ele in a]
a = torch.tensor(a)
b = [[0]*10] * 2
b= torch.tensor(b)

a = F.softmax(a , dim = 1)
print(a)