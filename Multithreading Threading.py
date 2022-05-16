import threading

def hello_world():
    print("Hello World")
    print("Hello World")

if __name__=="__main__":
    t1=threading.Thread(target=hello_world)
    t2=threading.Thread(target=hello_world)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    