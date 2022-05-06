# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: MULTIPLICATION TABLE
#
# NAME:         Julio Arias
# ASSIGNMENT:   Technical HW: Arrays & Maps

# Write a function called multiplication_table that
# takes a width, height, & scaling factor as parameters
# and returns a two-dimensional array multiplication
# table scaled by the scaling factor.
# You should not be using any functions other than range.


def multiplication_table(w, h, s):
    myarray = [ [ 0 for i in range(w)] for i in range(h)]
    #if the array has no high or wide return None
    if w==0 or h==0:
      return None

    #multiplies variable in top row by scaling factor and adds value for each row down
    high = 0
    while high<h:
      wide = 0
      while wide<w:
          myarray[high][wide]=((wide+1)*s)
          if high>0:
            
              
              myarray[high][wide]=(myarray[high][wide])+myarray[high-1][wide]
             
          wide+=1
      high+=1
        
    return myarray

def print_2D(b):
    for i in range(len(b)):
        print(b[i])

def main():
    print("5 3 1:")
    print_2D(multiplication_table(5, 3, 1))
    print("5 3 2:")
    print_2D(multiplication_table(5, 3, 2))

# Don't run main on import
if __name__ == "__main__":
    main()