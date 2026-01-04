#alarm
import datetime,time,pygame

def set_alarm(alarm_time):
    print(f"alarm time set to {alarm_time}")
    sound_file = "C:\\Users\\kaart\\.vscode\\projects\\alarm\\alarm-327234.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time in alarm_time:
            print("wake up! 😫")
            is_running = not is_running
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
    
if __name__ == "__main__":
    alarm_time = input("enter the time you want to wake up in(HH:MM:SS): ")
    
    set_alarm(alarm_time)