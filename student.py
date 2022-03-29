def main():
    #your code goes here
    num = int(input("CHOOSE THY NUMBA\n"))

    if num % 5 == 0 and num % 3 == 0:
        print ("FIZZBUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    elif num % 5 == 0:
        print("BUZZ")
    else:
        print(num)

if __name__ =='__main__':
    main()
