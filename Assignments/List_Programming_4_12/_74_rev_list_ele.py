# Reverse list of elements and print in upper case
first_lst = ["mon","tue","thu","fri","sat"]
sec_lst = ["jan","feb","mar","apr","may"]
res = sec_lst+first_lst[::-1]
print("Reverse list of elements: ",res)
upper_case = [ele.upper() for ele in res]
print(upper_case)