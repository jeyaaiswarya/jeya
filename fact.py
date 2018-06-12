def main():
    i=1
    fact=1
    n=input("Enter the number")
    if(n==0):
        fact=1
        print(fact)
    else:
        for i in range(1,n+1):
            fact*=i
        print("The factorial is")
        print(fact)


if __name__ == '__main__':
    main()
