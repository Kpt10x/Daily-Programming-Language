def evaluate_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.lstrip('-').isdigit(): 
            stack.append(int(token))
        else: 
            b = stack.pop() 
            a = stack.pop()  
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = int(a / b)  
            
            stack.append(result)  
    
    return stack[0]  

# Test cases
print(evaluate_postfix("2 1 + 3 *"))  
print(evaluate_postfix("5 6 +"))      
print(evaluate_postfix("3 4 2 * 1 5 - 2 3  / +")) 
print(evaluate_postfix("-5 6 -"))     
print(evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -"))  
print(evaluate_postfix("5"))           
