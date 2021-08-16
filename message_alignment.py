#!/usr/bin/python

"""
This programme will align to the right, left and center 
the message "Welcome to Python" in a 50 character variable

"""

if __name__ == "__main__":
    message="Welcome to Python!\n"

    print (f"{message:>50}") 
    print(f"{message}".rjust(70)) # Or you can use a method 
    print (f"{message:^50}") 
    print(f"{message}".center(70)) # Or you can use a method    
    print (f"{message:<50}") 
    print(f"{message}".ljust(70)) # Or you can use a method    

    """
Result:
                               Welcome to Python!

                                                   Welcome to Python!

               Welcome to Python!
                
                         Welcome to Python!
                          
Welcome to Python!
                               
Welcome to Python!
"""