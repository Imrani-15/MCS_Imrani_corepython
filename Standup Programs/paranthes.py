def isBalanced(s):
    stack = []

    for letter in s:
        if letter == '{':
            stack.append(1)
        elif letter == '[':
            stack.append(2)
        elif letter == '(':
            stack.append(3)
        elif letter == '}':
            if len(stack) == 0:
                return False
            if stack.pop() != 1:
                return False
        elif letter == ']':
            if len(stack) == 0:
                return False
            if stack.pop() != 2:
                return False
        elif letter == ')':
            if len(stack) == 0:
                return False
            if stack.pop() != 3:
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


# input1 = ")(()))"
# input2 = "("
# input3 = "()"
# input4= "(())((()())())"
# input5 = ")"
# input6= "hi())("
# input7 = "(hello))"
# input8 = "hello"
# input9 = "(hell(0))"

