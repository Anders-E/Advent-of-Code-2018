### At close to 500 iterations, the resource value becomes
### periodical with an interval of 28 iterations.
### Any iteration from there on with an i value where
### (1000000000 - i) % 28 == 0 will return the correct
### value for i = 1000000000.
###
### Since i = 496 => (1000000000 - 496) % 28, we can
### simply use the value of the 496th iteration which
### is 190820.

print(190820)
