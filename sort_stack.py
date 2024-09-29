def sort_stack(stack):
    if len(stack) <= 1:
        return
    
    top = stack.pop()
    
    sort_stack(stack)
    
    insert_in_sorted_stack(stack, top)


def insert_in_sorted_stack(stack, element):
    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element)
    else:
        top = stack.pop()
        insert_in_sorted_stack(stack, element)
        
        stack.append(top)


stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack) 

stack = [7, 1, 5]
sort_stack(stack)
print(stack)  

stack = [-3, 14, 8, 2]
sort_stack(stack)
print(stack)  
stack = [5]
sort_stack(stack)
print(stack)  

stack = []
sort_stack(stack)
print(stack)  

stack = [3, 3, 3]
sort_stack(stack)
print(stack)  
