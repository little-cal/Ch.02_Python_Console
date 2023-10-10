'''
2.0 Jedi Training (20pts)  Name:Caleb Little

UPLOAD YOUR CH 2 PDF LOG! (6pts)

1.) How do you enter a single line comment in a program? Give an example. (1pt)
# This is an example of a single line comment!

2.) If a=2 and b=5, predict all the following below and record your predictions. (9pts)
Then in the Python Console window, enter a=2 and b=5 and then all the following and record the actual output.
If the output is an error record the error and try to determine what the error is!
Comment about any of your predictions that didn't match the actual output

prediction - 2.5
b/a                 = 2.5
prediction - 2, floor division, rounds down to the nearest whole; 3
b//a                = 2
prediction - 25, 5 to the power of 2
b**a                = 25
prediction - getting the remainder of 5/2 which is 1
b%a                 = 1
prediction - 7
a+b                 = 7
prediction - returns int, 42 is an integer
type(42)            = int
prediction - 42.0 is a float variable, so it would return float
type(42.0)          = float
prediction - this is a string, running this would return str
type("C3PO")        = str
prediction - this is a boolean value, so it would return bool
type(True)          = bool


3.) Predict what would be the final output of (a) and type(a) if you enter the following 5 lines        (2pts)
into the Python Console Window? Then actually do it and record the output and comment on differences
between your predictions and the output.

a=2
a now equals 2
a*=10
multiplying a by 10, a now equals 20
a/=2
dividing a by 2, a now equals 10
a+=12
adding 12, a now equals 22
a-=7
subtracting 7, a equals 15
a             = 15.0
a should equal 15
type(a)       = float
the type should be an int

My predictions were mostly correct, the math was all right. However, I was wrong in my guess of the final type of a. I
had guessed it to be an int. When executing the code, it returned a float. I then wanted to know why, so I did each step
one at a time, getting the type of a every time. I then found that after dividing a by 2, it now returned as a float.

4.) What is the mistake in the following code? Comment it and fix it!  (1pt)

You can't multiply 3 by the addition of x+y like they are doing. You need to use the correct operator.
x,y = (4,5)
a = 3*(x + y)
a


5.) What is the mistake in the following code, so it will calculate the average? Comment it and fix it!  (1pt)

A more simple algebra mistake, should have parenthesis around the addition before dividing. This will assign the correct
value to ave, which is 4.0.
x,y,z =(3,4,5)
ave = (x+y+z)/3
ave


'''
