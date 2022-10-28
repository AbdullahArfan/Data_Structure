def isBalanced(myStr):

  # if length of myStr is odd then it is not balanced
    if len(myStr)%2 != 0:
        return False

  # initializing parentheses with dict
    my_dict = {'(':')','{':'}','[':']'}
    stack = []
    for char in myStr:
    # push opening bracket in stack
        if char in my_dict.keys():
            stack.append(char)
        else:
            #checking whether the stack is empty or not
            if stack == []:
                return False
            open_bracket = stack.pop()
            # checking present item and previous/popped item
            if char != my_dict[open_bracket]:
                return False
    return stack == []

#sample input ({[]}), ({[)}]})

myStr = input("Enter Brackets : \t ")
if isBalanced(myStr):
    print("\t \t", myStr, " is Balanced.")
else:
    print("\t \t", myStr, " is not Balanced.")


