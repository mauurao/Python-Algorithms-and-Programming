#!/usr/bin/python

"""
This program will calculate
- 4+3*(15-2);
- 2^3;
- 40 divide by 9
- The remainder of the division of 40 by 3
- The integer division of 30 by 4

"""

if __name__ == "__main__":
    E1, E2, E3 = 4+3*(15-2), 2**3, 40/9
    print(f"{E1:3d}")
    print(f"{E2:3d}")
    print(f"{E3:.2f}")
    
    E4, E5 = 40%3, 30//4
    print(f"{E4:3d}")
    print(f"{E5:3d}")

"""
Result:

43
  8
4.44
  1
  7

"""