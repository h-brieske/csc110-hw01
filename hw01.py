# ------------------------------------------------------
#        Name: Helena Brieske
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------


def main():
    """
    This is a Docstring for the main function. This is the short description.
    
    
    
    This program lets you execute math with basic operations and powers, as well as integer division and modulo. 

    Here, after a blank line, you can add a longer paragraph description.
    
    In Part 1, you can execute addition, subtraction and multiplication.
    In Part 2, you can do a calculation using powers.
    In Part 3, you can do integer divsion.
    In Part 4, you can do a division using modulo.
    
    
    
    Docstrings are like long comments that we put right under the function definition.
    The Docstring goes from one set of "opening" three double-quotes to
    another set of "closing" three double-quotes. We also try to keep the lines short.
    The Docstring has 4 sections:
      - the short one-line description
      - the paragraph description
      - the Params section that indicates input parameters and return values
      - the "how to run" section called "Example Use".

    PARAMS:
        - None. If the function took an input int of "apples" called num, we would
                indicate it like this: - num: int with number of apples
    RETURNS:
        - None. If the function returned something (like the integer half of num),
                we would indicate it like this: int : integer half of num
    """

    # ========== Setup for HW. DO NOT MODIFY ======
    x=0
    y=0
    a=0
    b=0
    c=0
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    result5 = 0
    # End of Setup code ---------------------------



    # Part 1: Basic Operations
    # =============================================
    # Your code for part 1 under this line and before the print statements
    x = 27
    print(f"Part 1: x = {x}")
    y = 1
    print(f"Part 1: y = {y}")
    a = 1.5
    print(f"Part 1: a = {a}")
    b = 7
    print(f"Part 1: b = {b}")
    c = -1
    print(f"Part 1: c = {c}")
    
    numerator = 3*x - 9*y
    denominator = 2*a*(b-c)
    result1 = numerator // denominator
    print(f"Part 1: result = {result1}")


    # End of Part 1 ----------------------


    # Part 2: Power
    # =============================================
    # Your code for part 2 under this line and before the print statements
    x = 5
    print("Part 2: x = 5")
    y = -3
    print("Part 2: y = -3")
    result2 = x**2*y**4
    print(f"Part 2: result = {result2}")
    
    # End of Part 2 ----------------------



    # Part 3: Integer divide
    # =============================================
    # Your code for part 3 under this line and before the print statements
    a = 100
    print(f"Part 3: a = {a}")
    b = 13
    print(f"Part 3: b = {13}")
    result3 = a // b
    print(f"Part 3: result = {result3}")
   
   # End of Part 3 ----------------------


    # Part 4: Modulo
    # =============================================
    # Your code for part 4 under this line and before the print statements
    result4 = a % b
    print(f"Part 4: result = {result4}")
    # End of Part 4 ----------------------

if __name__ == "__main__":
    main()

