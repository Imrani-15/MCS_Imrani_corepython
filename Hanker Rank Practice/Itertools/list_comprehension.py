x = int(input())
y = int(input())
z = int(input())
n = int(input())
ans=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(ans)

name = 'this is cow,cow has a baby and she give the milk to baby'
ans = name[::-1][0:10][::-1]
print(ans)