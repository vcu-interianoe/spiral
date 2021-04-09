def spiralize(number):
    x = 1
    y = 2
    step = 0
    running_total = 0   
    while x <= (number**2):
      
        running_total += x
        x += y
        step += 1
        if step == 4:
            y += 2
            step = 0    
    return running_total

print(spiralize(501)) 
