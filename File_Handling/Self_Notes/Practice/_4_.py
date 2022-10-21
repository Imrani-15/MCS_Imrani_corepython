# Write a Python program to read last n lines of a file
def lastline(fname,N):
    with open('doc.txt') as f:
        for line in (f.readlines() [-N:]):
            print(line,end="")
if __name__=='__main__':
    fname = 'doc.txt'
    N = 3
    try:
        lastline(fname,N)
    except:
        print("File not found")