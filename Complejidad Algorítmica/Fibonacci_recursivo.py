def fibonacci_recursivo(n):                 
    if n <= 1:                             
        return n                            
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)  
    

num = 5                                   
resultado = fibonacci_recursivo(num)      
print("Fibonacci recursivo de", num, "es:", resultado)   