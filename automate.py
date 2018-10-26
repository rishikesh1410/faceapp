def tofb(var,pass1):
    
    kb= Controller()


    kb.press(Key.ctrl)
    kb.press(Key.shift_l)
    kb.press('n')
    kb.release(Key.ctrl)
    kb.release(Key.shift_l)
    kb.release('n')

    time.sleep(0.1)
    fb="https://www.facebook.com/login/"

    for char1 in fb:
        kb.press(char1)
        kb.release(char1)
        time.sleep(0.0001)

    time.sleep(0.001)    
    kb.press(Key.enter)
    time.sleep(0.5)
    kb.release(Key.enter)    
    kb.press(Key.tab)
    kb.release(Key.tab)

    time.sleep(8)
    for char2 in var:
        kb.press(char2)
        kb.release(char2)
        time.sleep(0.0001)
    kb.press(Key.tab)
    kb.release(Key.tab)

    for char3 in pass1:
        kb.press(char3)
        kb.release(char3)
        time.sleep(0.0001)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.press(Key.enter)
    kb.release(Key.enter)




