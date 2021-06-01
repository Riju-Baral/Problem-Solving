string = "Hello World" 
reverse_String = ""   
count = len(string)
while count > 0:   
    reverse_String += string[count-1] 
    count = count - 1 
print (reverse_String)