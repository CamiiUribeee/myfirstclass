def fibonacci(n):                       
    a, b = 0, 1                         
    
    for i in range(n):                  
        a, b = b, a + b                
    
    return a                          

num = 10                      
resultado = fibonacci(num)              
print("Fibonacci de", num, "es:", resultado)  
