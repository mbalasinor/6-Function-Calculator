import os
import time

ans = None
main_err = False

N = "\n" #universal variable for new line

B = "\033[1m" #universal variable to bold
UB = "\033[0m" #universal variable to unbold

U = "\x1B[4m" #universal variable to underline
UU = "\x1B[0m" #universal variable to un-underline


def add():
    global ans
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer (ans): {ans}{UB}{N}")
    print(f"{B}{U}Mode: Addition{UU}{UB}")
    
    lst = []
    while True:
        add_input = input(f"{N}Enter number (or \"=\" if finished): ")
        if add_input == "ans" and ans != None:
            add_input = str(ans)
        if add_input.lower() == "=":
            break
        
        try:
            float(add_input)
        except:
            print(f"{N}{B}Please enter a number.{UB}")
            continue
        else: lst.append(add_input)
    
    sm = 0
    for i in lst:
        sm += float(i)

    ans = sm

    print(f"{N}The sum is {B}{sm}{UB}.")

    return_home()


def sub():
    global ans
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer (ans): {ans}{UB}{N}")
    print(f"{B}{U}Mode: Subtraction{UU}{UB}")
    
    while True:
        minuend = input(f"{N}Enter minuend: ")
        if minuend == "ans" and ans != None:
            minuend = str(ans)
        try:
            float(minuend)
        except:
            print(f"{N}{B}Please enter a number for the minuend.{UB}")
            continue
        if len(minuend) == 0:
            print(f"{N}{B}Please enter a number for the minuend.{UB}")
            continue
        else: break

    while True:
        subtrahend = input(f"{N}Enter subtrahend: ")
        if subtrahend == "ans" and ans != None:
            subtrahend = str(ans)
        try:
            float(subtrahend)
        except:
            print(f"{N}{B}Please enter a number for the subtrahend.{UB}")
            continue
        if len(subtrahend) == 0:
            print(f"{N}{B}Please enter a number for the subtrahend.{UB}")
            continue
        else: break

    try:
        df = float(minuend) - float(subtrahend)
    except ValueError:
        print(f"{N}{B}Error, please try again.{N}{UB}")
        sub()

    ans = df

    print(f"{N}{B}{float(minuend)} - {float(subtrahend)}{UB} = {B}{df}{UB}")

    return_home()


def mult():
    global ans
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer (ans): {ans}{UB}{N}")
    print(f"{B}{U}Mode: Multiplication{UU}{UB}")
    
    lst = []
    while True:
        mult_input = input(f"{N}Enter number (or \"=\" if finished): ")
        if mult_input == "ans" and ans != None:
            mult_input = str(ans)
        if mult_input.lower() == "=":
            break
        try:
            float(mult_input)
        except:
            print(f"{N}{B}Please enter a number.{UB}")
            continue
        if len(mult_input) == 0:
            print(f"{N}{B}Please enter a number.{UB}")
            continue
        else: lst.append(mult_input)
    
    prd = 1
    for i in lst:
        prd *= float(i)

    print(f"{N}The product is {B}{prd}{UB}.")

    ans = prd

    return_home()


def div():
    global ans
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer (ans): {ans}{UB}{N}")
    print(f"{B}{U}Mode: Division{UU}{UB}")
    
    while True:
        dividend = input(f"{N}Enter dividend: ")
        if dividend == "ans" and ans != None:
            dividend = str(ans)
        try:
            float(dividend)
        except:
            print(f"{N}{B}Please enter a number for the dividend.{UB}")
            continue
        if len(dividend) == 0:
            print(f"{N}{B}Please enter a number for the dividend.{UB}")
            continue
        else: break

    while True:
        divisor = input(f"{N}Enter divisor: ")
        if divisor == "ans" and ans != None:
            divisor = str(ans)
        try:
            float(divisor)
        except:
            print(f"{N}{B}Please enter a number for the divisor.{UB}")
            continue
        if len(divisor) == 0:
            print(f"{N}{B}Please enter a number for the divisor.{UB}")
            continue
        else: break

    try:
        qt = float(dividend) / float(divisor)
    except ValueError:
        print(f"{B}Error, please try again.{UB}")
        div()

    print(f"{N}{B}{float(dividend)} / {float(divisor)}{UB} = {B}{qt}{UB}")

    ans = qt

    return_home()


def exp():
    global ans
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer (ans): {ans}{UB}{N}")
    print(f"{B}{U}Mode: Exponent{UB}{UU}")
    
    while True:
        base = input(f"{N}Enter base: ")
        if base == "ans" and ans != None:
            base = str(ans)
        try:
            float(base)
        except:
            print(f"{N}{B}Please enter a number for the base.{UB}")
            continue
        if len(base) == 0:
            print(f"{N}{B}Please enter a number for the base.{UB}")
        else: break

    while True:
        exponent = input(f"{N}Enter exponent: ")
        if exponent == "ans" and ans != None:
            exponent = str(ans)
        try:
            float(exponent)
        except:
            print(f"{N}{B}Please enter a number for the exponent.{UB}")
            continue
        if len(exponent) == 0:
            print(f"{N}{B}Please enter a number for the exponent.{UB}")
            continue
        else: break

    try:
        ex = float(base) ** float(exponent)
    except ValueError:
        print(f"{B}Error, please try again.{UB}")
        exp()

    print(f"{N}{B}{base} ^ {exponent}{UB} = {B}{ex}{UB}")

    ans = ex

    return_home()


def fact_shell():
    global ans
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer (ans): {ans}{UB}{N}")
    print(f"{B}{U}Mode: Factorial{UB}{UU}")
    
    while True:
        factorial = input(f"{N}Enter number: ")
        if factorial == "ans" and ans != None and str(ans).endswith(".0"):
            factorial = int(ans)
            factorial = str(factorial)
        if factorial.endswith("!"):
            factorial = factorial[:-1]
        if factorial.isdigit() and int(factorial) >= 0:
            break
        else:
            print(f"{N}{B}Please enter a valid number (positive integer).{UB}")
    
    print(f"{N}{B}{factorial}!{UB} = {B}{fact(int(factorial))}{UB}")

    ans = fact(int(factorial))

    return_home()


def fact(fact_inp):
    fact_inp = int(fact_inp)
    if fact_inp == 0 or fact_inp == 1:
        return 1 
    else:
        return fact_inp * fact(fact_inp - 1)


def return_home():
    global main_err
    main_err = False
    
    while True:
        return_ans = input(f"{N}Would you like to perform any more calculations (or just return home)? The current result will be saved as \"ans\" for further use. (Y/N): ")
        if return_ans.lower() == "y" or return_ans.lower() == "yes" or return_ans.lower() == "n" or return_ans.lower() == "no":
            break
        else:
            print(f"{N}{B}Please enter either \"yes\" or \"no\"{UB}.")
    
    if return_ans.lower() == "y" or return_ans.lower() == "yes":
        main()
    else:
        print(f"{N}{B}Thank you for using the Calculator!{UB}{N}")
        exit()


def main():
    global ans
    global main_err
    os.system("cls")

    if ans != None:
        print(f"{N}{B}Stored Answer: {ans}{UB}")

    if main_err == True:
        print(f"{N}Please enter a valid operation.")

    print(f"{N}{B}Please select an operation:{UB}{N}    Addition (+){N}    Subtraction (-){N}    Multiplication (*){N}    Division (/){N}    Exponent (^){N}    Factorial (!){N}{B}Or quit (q) to exit.{UB}")
    
    op = input(f"Your choice is: {B}")
    if op.lower() == "addition" or op.lower() == "+": add()
    elif op.lower() == "subtraction" or op.lower() == "-": sub()
    elif op.lower() == "multiplication" or op.lower() == "*": mult()
    elif op.lower() == "division" or op.lower() == "/": div()
    elif op.lower() == "exponent" or op.lower() == "^": exp()
    elif op.lower() == "factorial" or op.lower() == "!": fact_shell()
    elif op.lower() == "quit" or op.lower() == "q": 
        print(f"{N}Thank you for using the Calculator!{UB}{N}")
        exit()
    else: 
        main_err = True
        main()


main()
