def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

stack = [1, 2, 3, 4]
print("Original Stack:", stack)

reverse_stack(stack)
print("Reversed Stack:", stack)

stack = [3, 2, 1]
reverse_stack(stack)
print(stack)  

stack = [5]
reverse_stack(stack)
print(stack)  

stack = [-5, -10, -15]
reverse_stack(stack)
print(stack)  

stack = []
reverse_stack(stack)
print(stack)  

stack = [3, 3, 3]
reverse_stack(stack)
print(stack) 

