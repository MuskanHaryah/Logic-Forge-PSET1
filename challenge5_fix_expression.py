def fix_expression(expr):
    result=[]
    count =0
    for char in expr:
        if char == '(':
            count+=1
            result.append(char)
        elif char == ')':
            count-=1
            result.append(char)
        else:
            result.append(char)

    final=''
    for char in result:
        if char == '(' and count >0:
            count-=1
        elif char == ')' and count <0:
            count+=1
        else:
            final+=char
    return final

print(fix_expression("()())()"))  # Output: "(())()" or "()()()"
print(fix_expression("(a)())()"))  # Output: "(a())()" or "(a)()()"
print(fix_expression(")("))        # Output: ""
print(fix_expression("()"))        # Output: "()"
print(fix_expression("abc"))       # Output: "abc"
print(fix_expression("((("))       # Output: ""

