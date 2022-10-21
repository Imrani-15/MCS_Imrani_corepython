Ip = input("Enter your IP address:").split(".")
for zero in Ip:
   result = (''.join(str(int(zero))))
   print(result,end=".")

# 200.006.020.900
