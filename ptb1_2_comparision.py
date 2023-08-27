import time
import math

#new version

def decorator(func):
    def wrapper():
        print(f"Running {func.__name__}...")
        time.sleep(2)
        func()
        print(f"Complete running {func.__name__}")
    return wrapper

@decorator
def ptb1():
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    loi_giai(a, b)


def loi_giai(a, b):
    x = -a/(2*b)
    print("x = ", x)


@decorator
def ptb2():
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    c = int(input("nhap c: "))
    print(f"phuong trinh cua ban la: y = {a}x^2 + {b}x + {c}")
    if a + b + c == 0:
        truong_hop_1_ptb2(a, c)
    elif a + b - c == 0:
        truong_hop_2_ptb2(a, c)
    else:
        truong_hop_con_lai_ptb2(a, b, c)
    

def truong_hop_1_ptb2(a, c):
    print("x1 = 1")
    print("x2 = ", c/a)


def truong_hop_2_ptb2(a, c):
    print("x1 = -1")
    print("x2 = ", -c/a)


def truong_hop_con_lai_ptb2(a, b, c):
    delta = b**2 - 4*a*c
    delta_squared = math.sqrt(delta)
    x1 = (-delta_squared + b)/(2*a)
    x2 = (-delta_squared - b)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)


def quit():
    say = print 
    say("Shutting down...")
    time.sleep(2)
    exit()

while True:
    match input("ptb1 hay ptb2 (quit de thoat): "):
        case "ptb1":
            ptb1()
        case "ptb2":
            ptb2()
        case "quit":
            quit()
        case _:
            print("Invalid Input")

#old version

import math

while True:
    pheptoan = input("chon phep toan(ptb1 hoac ptb2 hoac thoat): ")

    if pheptoan == "ptb2":
        def ptb2():
            while True:
                try:
                    a = float(input("nhap a: "))
                    b = float(input("nhap b: "))
                    c = float(input("nhap c: "))
                except ValueError:
                    print("a, b, c phai la cac so thuc")
                    continue
                if a != 0:
                    print(f"phuong trinh cua ban la: {a}x^2+{b}x+{c} = 0")
                    denta = (b**2)-(4*a*c)
                    if a+b+c == 0:
                        print("phuong trinh co dang a+b+c = 0")
                        print("x1= 1")
                        print("x2 =", c/a)
                        break
                    elif a-b+c == 0:
                        print("phuong trinh co dang a-b+c = 0")
                        print("x1 = -1")
                        print("x2 = ", -c/a)
                        break
                    elif denta < 0:
                        print("phuong trinh vo nghiem")
                        break
                    elif denta > 0:
                        print("phuong trinh co hai nghiem phan biet")
                        print("x1 = ", (-b+math.sqrt(denta))/2*a)
                        print("x2 = ", (-b-math.sqrt(denta))/2*a)
                        break
                    elif denta == 0:
                        print("phuong trinh co nghiem kep")
                        print("x1 = x2 = ", b/(2*a))
                        break
                else:
                    print("a phai khac 0")
        ptb2()


    elif pheptoan == "ptb1":
        def ptb1():
            while True:
                try:
                    a = float(input("nhap a: "))
                    b = float(input("nhap b: "))
                except ValueError:
                    print("a, b phai la cac so thuc")
                print(f"phuong trinh cua ban la: y = {a}x + {b}")
                if a and b == 0:
                    print("phuong trinh co vo so nghiem")
                elif a == 0 and b != 0:
                    print("phuong trinh vo nghiem")
                elif a and b != 0:
                    print("phuong trinh co nghiem kep")
                    print("x1 = x2 = ", -a/b)
        ptb1()
    elif pheptoan == "thoat":
        break
    else:
        quit()
  


    


