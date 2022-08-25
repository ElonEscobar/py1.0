import threading
def earth():
        for i in range (5):
            print("I am great")

def sun():
        for x in range (5):
            print("Great")

d=threading.Thread(target=earth)
f= threading.Thread(target=sun)

d.start()
# use (d.join) to wait untill the first thread is full executed
f.start()     