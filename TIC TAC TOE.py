from random import randint

nome = input("Ciao, come ti chiami? ")
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
print(f"Ciao {nome}, pronto per una partita?")
print(f"{a}|{b}|{c}")
print("-----")
print(f"{d}|{e}|{f}")
print("-----")
print(f"{g}|{h}|{i}")
print("Ti spiego le regole, ovviamente non quelle del tris, ma per come giocare")
print("Inserisci un numero da 1 a 9 e inserirai una X nella casella apposita")

while True:
    pos = input("Scegli la posizione ")
    match pos:
        case "1":
            if a != " ":
                print("Posizione già occupata")
                continue
            else:
                a = "X"
        case "2":
            if b != " ":
                print("Posizione già occupata")
                continue
            else:
                b = "X"
        case "3":
            if c != " ":
                print("Posizione già occupata")
                continue
            else:            
                c = "X"
        case "4":
            if d != " ":
                print("Posizione già occupata")
                continue
            else:            
                d = "X"
        case "5":
            if e != " ":
                print("Posizione già occupata")
                continue
            else:            
                e = "X"
        case "6":
            if f != " ":
                print("Posizione già occupata")
                continue
            else:            
                f = "X"
        case "7":
            if g != " ":
                print("Posizione già occupata")
                continue
            else:            
                g = "X"
        case "8":
            if h != " ":
                print("Posizione già occupata")
                continue
            else:            
                h = "X"
        case "9":
            if i != " ":
                print("Posizione già occupata")
                continue
            else:            
                i = "X"
        case _:
            print("Numero non valido")
            continue
    print(f"{a}|{b}|{c}")
    print("-----")
    print(f"{d}|{e}|{f}")
    print("-----")
    print(f"{g}|{h}|{i}")
    if (a=="X" and b=="X" and c=="X") or (a=="X" and d=="X" and g=="X") or (a=="X" and e=="X" and i=="X") or (b=="X" and e=="X" and h=="X") or (c=="X" and f=="X" and i=="X") or (d=="X" and e=="X" and f=="X") or (g=="X" and h=="X" and i=="X") or (c=="X" and e=="X" and g=="X"):
        print (f"Complimenti {nome}, hai vinto!")
        break
    print("Adesso tocca a me...")
    while True:
        ia = randint(1,9)
        match str (ia):
            case "1":
                if a != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    a = "O"
                    break
            case "2":
                if b != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    b = "O"
                    break
            case "3":
                if c != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    c = "O"
                    break
            case "4":
                if d != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    d = "O"
                    break
            case "5":
                if e != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    e = "O"
                    break
            case "6":
                if f != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    f = "O"
                    break
            case "7":
                if g != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    g = "O"
                    break
            case "8":
                if h != " ":
                    print("Posizione già occupata")
                    continue
                else:
                    h = "O"
                    break
            case "9":
                if i != " ":
                    print("Posizione già occupata")
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
        print("Questa volta ho vinto io")
        print("Ti andrà meglio la prossima volta")
        break
