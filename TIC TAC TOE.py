from random import randint

nome = input("Hey, what's your name? ")
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
print(f"Hi {nome}, Ready for a match?")
print(f"{a}|{b}|{c}")
print("-----")
print(f"{d}|{e}|{f}")
print("-----")
print(f"{g}|{h}|{i}")
print("Insert a number from 1 to 9 and you will enter an X in the box provided")

while True:
    pos = input("Choose the position ")
    match pos:
        case "1":
            if a != " ":
                print("Position already occupied")
                continue
            else:
                a = "X"
        case "2":
            if b != " ":
                print("Position already occupied")
                continue
            else:
                b = "X"
        case "3":
            if c != " ":
                print("Position already occupied")
                continue
            else:            
                c = "X"
        case "4":
            if d != " ":
                print("Position already occupied")
                continue
            else:            
                d = "X"
        case "5":
            if e != " ":
                print("Position already occupied")
                continue
            else:            
                e = "X"
        case "6":
            if f != " ":
                print("Position already occupied")
                continue
            else:            
                f = "X"
        case "7":
            if g != " ":
                print("Position already occupied")
                continue
            else:            
                g = "X"
        case "8":
            if h != " ":
                print("Position already occupied")
                continue
            else:            
                h = "X"
        case "9":
            if i != " ":
                print("Position already occupied")
                continue
            else:            
                i = "X"
        case _:
            print("Invalid number")
            continue
    print(f"{a}|{b}|{c}")
    print("-----")
    print(f"{d}|{e}|{f}")
    print("-----")
    print(f"{g}|{h}|{i}")
    if (a=="X" and b=="X" and c=="X") or (a=="X" and d=="X" and g=="X") or (a=="X" and e=="X" and i=="X") or (b=="X" and e=="X" and h=="X") or (c=="X" and f=="X" and i=="X") or (d=="X" and e=="X" and f=="X") or (g=="X" and h=="X" and i=="X") or (c=="X" and e=="X" and g=="X"):
        print (f"Great {nome}, you're the winner!")
        break
    print("It's my turn...")
    while True:
        ia = randint(1,9)
        match str (ia):
            case "1":
                if a != " ":
                   continue
                else:
                    a = "O"
                    break
            case "2":
                if b != " ":
                    continue
                else:
                    b = "O"
                    break
            case "3":
                if c != " ":
                    continue
                else:
                    c = "O"
                    break
            case "4":
                if d != " ":
                    continue
                else:
                    d = "O"
                    break
            case "5":
                if e != " ":
                    continue
                else:
                    e = "O"
                    break
            case "6":
                if f != " ":
                    continue
                else:
                    f = "O"
                    break
            case "7":
                if g != " ":
                    continue
                else:
                    g = "O"
                    break
            case "8":
                if h != " ":
                    continue
                else:
                    h = "O"
                    break
            case "9":
                if i != " ":
                    continue
                else:
                    i = "O"
                break
    print(f"{a}|{b}|{c}")
    print("-----")
    print(f"{d}|{e}|{f}")
    print("-----")
    print(f"{g}|{h}|{i}")
    if (a=="O" and b=="O" and c=="O") or (a=="O" and d=="O" and g=="O") or (a=="O" and e=="O" and i=="O") or (b=="O" and e=="O" and h=="O") or (c=="O" and f=="O" and i=="O") or (d=="O" and e=="O" and f=="O") or (g=="O" and h=="O" and i=="O") or (c=="O" and e=="O<" and g=="O"):
        print("The victory is mine")
        break
