# Shades

This project is inspired by the [Piet programming language](https://www.dangermouse.net/esoteric/piet.html).

It uses the Python Image Library.


## Language rules
Meaning is in the degree of difference between shades of a color.  

_Black and white have special meanings:_
- **black**: toggle * on/off (it is off initially) AND resets counter
- **white**: empty space - marks the end of the program

_Shades (from light to dark):_

| Steps/ shades|  * toggle     | Result   |
| :---------------------: |:-------------:| :-------:|
| 1                       |  False        | push     |
| 1                       |  True         | pop      |
| 2                       |  False        | add      |
| 2                       |  True         | subtract |
| 3                       |  False        | multiply |
| 3                       |  True         | divide   |
| 4                       |  False        | mod      |
| 4                       |  True         | not      |
| 5                       |  False        | greater or equal |
| 5                       |  True         | duplicate |
| 6                       |  False        | out (number) |
| 6                       |  True         | out (char) |
| 7                       |  False        | swap |


## To do:
- Currently only using red to distinguish between shades - should use all 
- Test greater or equal and not thoroughly