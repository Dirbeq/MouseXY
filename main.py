import mouse,time


while True:
    try:
        pos = mouse.get_position
        print('             ',end='\r') # Clear the line
        print(pos(),end='\r')
        time.sleep(0.05) # Prevents the processor from exploding
    except:
        break