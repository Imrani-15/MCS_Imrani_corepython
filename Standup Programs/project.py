def isBalanced(s):
    stack = []
    for letter in s:
        if letter == '(':
            stack.append(1)
            print(stack)
        elif letter == ')':
            if len(stack) == 0:
                return False
            if stack.pop() != 1:
                return False
            elif letter == str(s):
              return True
    return len(stack) == 0

if __name__ == "__main__":
    s = input("Enter the expression here: ").strip()
    result = isBalanced(s)
    if result is True:
        print('True')
    else:
        print('False')
