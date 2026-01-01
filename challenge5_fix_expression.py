from collections import deque

def fix_expression(expr):
    def is_valid(s):
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
            elif ch == ')':
                if balance == 0:
                    return False
                balance -= 1
        return balance == 0

    result = []
    visited = set()
    queue = deque([expr])
    visited.add(expr)

    found_valid = False

    while queue:
        curr = queue.popleft()

        # If current string is valid → record it
        if is_valid(curr):
            result.append(curr)
            found_valid = True

        # If valid strings found at this level → do NOT go deeper
        if found_valid:
            continue

        # Generate all strings by removing ONE parenthesis
        for i in range(len(curr)):
            if curr[i] not in "()":
                continue

            next_str = curr[:i] + curr[i+1:]
            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)

    return result



print(fix_expression("()())()"))  # Output: "(())()" or "()()()"
print(fix_expression("(a)())()"))  # Output: "(a())()" or "(a)()()"
print(fix_expression(")("))        # Output: ""
print(fix_expression("()"))        # Output: "()"
print(fix_expression("abc"))       # Output: "abc"
print(fix_expression("((("))       # Output: ""
print(fix_expression("(()"))       # Output: "()"
print(fix_expression("())"))       # Output: "()"

