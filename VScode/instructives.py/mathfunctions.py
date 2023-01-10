import math  #library the has a lot of math funtions

x = 2.9
print(round(x)) #round the float to result an int



x = -2.9
print(abs(x)) #abs function changes the int/float sign to positive



print(math.ceil(2.1))

print(math.floor(6.9))

print(math.copysign(1.3, -0.0)) #?

print(math.fabs(47.6/30)) #?

print(math.factorial(5)) #ValueError when float or is negative

print(math.fsum([3.15, 3.14, 4.7])) #gives an accurate floating point sum of the values in the iterable

print(math.gcd(129, 132)) #greatest common divisor, only integers

print(math.lcm(30,33,64)) #least common multiple, only integers

a = 1
b = 2
#tells if "a" and "b" are close
print(math.isclose(a, b, rel_tol=0, abs_tol=0.0)) #relative tolerance, absolute tolerance

#tells whether x is FINITE or not
print(math.isfinite(0.0)) #return False if x is either infinite or NaN (Not a Number)

print(math.isinf(0.1)) #tells if the value, whether positive or negative, is infinite or not

print(math.isnan(0)) #shows whether it's a NaN

print(math.isqrt(9)) #calculates the square foot of x (nonnegative integer)

print(math.modf(4.7)) #shows the fractional and the integer parts of x

print(math.prod([4.582 * 5.4 / 2])) #calculates the product of all the elements in the input ITERABLE

print(math.trunc(4.57)) #returns the integer part only, leaving out the floating point value

#returns the value of the least significant part of the float x
print(math.ulp(0)) #ULP - Unit in the Last Place