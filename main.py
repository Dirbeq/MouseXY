import mouse

while True:
    try:
        pos = mouse.get_position
        print(pos(),end='\r')
    except:
        break