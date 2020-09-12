# Inspired by https://youtu.be/L4ArlAfKTLA
# Program made by Maxim Sabin
# See this project at https://github.com/sabinM1/8424432925592889329288197322308900672459420460792433
# Code:
# --GCD--
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
# --GCD end--
# the one and only:
magic_number = 8424432925592889329288197322308900672459420460792433
# if you want to have more GCDs of the numbers lower and greater than the one given, uncomment the following 4 lines and comment lines 21, 22 and 23:
# for x in range(magic_number-10, magic_number+11): # in a range of 10 numbers around the number
#     a = pow(x, 17) + 9    # magic formula
#     b = pow(x+1, 17) + 9  # magic formula nr2
#     print ("GCD is",hcfnaive(a,b),"\na =",a,"\nb =",b,"\n\n\n")
# ---
# Calculate GCD with the formulas with only the given number (see comment on line 14)
a = pow(magic_number, 17) + 9    # magic formula
b = pow(magic_number+1, 17) + 9  # magic formula nr2
print ("GCD is",hcfnaive(a,b),"\na =",a,"\nb =",b)
