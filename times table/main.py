def times():
    try:
        numberinitial = float(input("Enter a number..."))        
        numberfinal = float(input("Enter the number to want to multiply the first number with..."))
        print(numberfinal*numberinitial)
    except ValueError:
        times()

times()