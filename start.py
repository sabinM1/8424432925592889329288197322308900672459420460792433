# Inspired by https://youtu.be/L4ArlAfKTLA
# Program made by Maxim Sabin
# See this project at https://github.com/sabinM1/8424432925592889329288197322308900672459420460792433
# Expected output: https://paste.ubuntu.com/p/3HfnPQJFCK/
# Expected output mirrors: https://pastebin.com/raw/zy2cLxAm || https://0bin.net/paste/YKLYJNKZ#vXocbSg7bwksMv6QXvhxDuCRqtY6tw3u5PF-wG3ctdX
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
# for x in range(8424432925592889329288197322308900672459420460792423, 8424432925592889329288197322308900672459420460792443):
for x in range(magic_number-10, magic_number+11): # in a range of 10 numbers around the number, you can modify this very easily to find the number
    a = pow(x, 17) + 9    # magic formula
    b = pow(x+1, 17) + 9  # magic formula nr2
    print ("GCD is",hcfnaive(a,b),";; a =",a,"b =",b)
