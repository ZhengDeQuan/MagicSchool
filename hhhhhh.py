from typing import Dict , List, Tuple
ParaDict = Dict[str,str]
ParaList = List[ParaDict]

def function(a:str = "aa",b:str = "bb")-> ParaList:
    temp_dict = dict()
    temp_dict['para_title'] = 90
    temp_dict['bb'] = 90
    temp_dict['cc'] = 90
    return [temp_dict]


if __name__ == "__main__":
    l = function(10,20)
    print(l)

'''
可能那些标亮的信息就是提示吧
'''
