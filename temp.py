x=100;
print x;

def print_array(array):
    for i in array : 
        print i

str1 = ["Hello",  "World",  "Peace"]
print_array(str1)    

str1.append('123')
print_array(str1)    
    
str1.pop(0)
print_array(str1)    
