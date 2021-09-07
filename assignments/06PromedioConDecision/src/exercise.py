def main():
    #escribe tu código abajo de esta línea
    total = 0
    cont = 0
    num = 1
    while num > 0:
        num = float(input())
        if num > 0:
            total = total + num
            cont = cont + 1
    
    prom = total/cont
    print(prom)
    pass
if __name__=='__main__':
    main()
