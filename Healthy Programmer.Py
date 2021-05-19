from pygame import mixer
import threading
import datetime
import time
def get_time():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
def up_water_log(text):
    with open("water_log.txt",'a') as op:
            op.write(f"{get_time()}-{text} \n")

def water_log():
    water = 0
    while True:
        if water==3500:
            break
        else:
            print("water drinking counting is shuru\n")
            time.sleep(15)
            mixer.init()
            mixer.music.load("water.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            d=input("Please write drank if you have drink the water\n").upper()
        if d=="DRANK":
            mixer.music.stop()
            up_water_log(d)
            water+=100
            print("Thankyou  for drinking water\n")
            continue
        elif d != "DRANK" :
            print("IT'S YOUR DRINKING TIME")           
                    
def r_water_log():
    with open("water_log.txt",'r') as op:
        for i in op:
            print(i,end=" ")

def up_eye_log(text):
    with open("eyes_log.txt",'a') as op:
            op.write(f"{get_time()}-{text} \n")
def eye_log():
    while True:
        print("Eye Rest  counting is shuru\n")
        time.sleep(30)
        mixer.init()
        mixer.music.load("eye.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play()
        d=input("Please write done if have Done Eye Exercise\n").upper()
        if d=="DONE":
            mixer.music.stop()
            up_eye_log(d)
            print("Thankyou  for \n")
            continue
        elif d != "DONE" :
            print("IT'S YOUR EYES EXERCISE TIME") 
def r_eye_log():
    with open("eye_log.txt",'r') as op:
        for i in op:
            print(i,end=" ")
def up_ex_log(text):
    with open("ex_log.txt",'a') as op:
            op.write(f"{get_time()}-{text} \n")
def ex_log():
    while True:
        print("Chal bosdike  counting is shuru\n")
        time.sleep(60)
        mixer.init()
        mixer.music.load("phy.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play()
        d=input("Please write done if have Done  Exercise\n").upper()
        if d=="DONE":
            mixer.music.stop()
            up_eye_log(d)
            print("Thankyou  for \n")
            continue
        elif d != "DONE" :
            print("IT'S YOUR  EXERCISE TIME") 
                    
def r_ex_log():
    with open("ex_log.txt",'r') as op:
        for i in op:
            print(i,end=" ")
if __name__ == '__main__':
    print("\n\t\t\t\t\t------| Healthy Programmer |------")
    print('\nYou want to read the previous log files or run the "Healthy Programmer" program?\n'
          'if check the previous files press "1"\nor Run the program press "2"\n''Press QUIT to exit the program')
user_choice = input('Press the key: ')
if user_choice == '1':
    read_choice = input("\nPress 1 for check the water drank logs\nPress 2 for check the eyes exercised logs\n"
                            "Press 3 for check the physical exercised logs\nPress the key: ")
    if read_choice == '1':
        r_water_log()

    elif read_choice == '2':
        r_eye_log()

    elif read_choice == '3':
        r_ex_log()
elif user_choice == '2':
        # targeting the threads
    t1 = threading.Thread(target=water_log)
    t2 = threading.Thread(target=eye_log)
    t3 = threading.Thread(target=ex_log)

        # starting the threads
    t1.start()
    t2.start()
    t3.start()

        #join the threads
    t1.join()
    t2.join()
    t3.join()
else:
    if user_choice == "QUIT":
        exit(0)
    

