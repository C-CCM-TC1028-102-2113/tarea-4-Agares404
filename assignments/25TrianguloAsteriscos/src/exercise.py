
def main():
    #Escribe tu código debajo de esta línea
    alt=int(input("Enter triangle height: "))
    for n in range (alt+1):
        esp = alt - n
        print(" "*esp+"*"*n)
    pass


if __name__=='__main__':
    main()
