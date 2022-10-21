'''
Given the participants' score sheet for your University Sports Day, you are required to find
the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input("Enter the the no of scores:"))
    arr = input().split(",")
    res = sorted(arr,reverse=True)
    for i in range(len(res)):
#        print(res[i]) # 6,6,5,3,2
#         print(res[0])  #6
        if res[i] == res[0]:
            continue
        else:
            print("Runner-up score",res[i])
            break
