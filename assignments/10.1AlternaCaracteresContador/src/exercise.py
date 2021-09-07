def main():
    #escribe tu código abajo de esta línea
    dis = int(input())
    for n in range (1,dis+1):
        if n%2 == 0:
            print (n,"- %")
        else:
            print (n,"- #")
    pass

if __name__=='__main__':   
    main()
