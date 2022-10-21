"This is return the length of word"

# res = max(len(ele) for ele in len_str)
# print("Length of longest string:",res)



"Length of lonest string "


class Len_Longest_Str:
    def __init__(self,len_str):
        self.len_str = len_str
    def result(self):
        max_len = 0
        for ele in len_str:
            if len(ele)>max_len:
                max_len = len(ele)
                res = ele
        print("Longest string in list:",res)
        print("length of longest string in list:",len(res))

len_str = ['john have 5 eggs5252','this is imrani@100','ele','jambo','kiran','imrani']
l = Len_Longest_Str(len_str)
l.result()