import time,pygame

def countdown(t):
    file = "C:\\Users\\kaart\\.vscode\\projects\\alarm\\alarm-327234.mp3" 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!')
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1) 

t = input("Enter the time in seconds: ") 

countdown(int(t)) 