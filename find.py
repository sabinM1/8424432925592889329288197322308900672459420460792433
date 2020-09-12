# If you really want to find the nummber you can use this script
# (keep in mind the CPU usage of a 7th gen. i5 was 30%)

def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

x=1 # start from one or any number in Z
a = pow(x, 17) + 9   # for the initial operation
b = pow(x+1, 17) + 9 # ^

while (hcfnaive(a,b)==1):
    a = pow(x, 17) + 9    # magic formula
    b = pow(x+1, 17) + 9  # magic formula nr2
    print ("GCD is",hcfnaive(a,b),"x =",x,"\n") # print the GCD (should be 1) and the test number (x)
    x+=1
else:
    print ("GCD is",hcfnaive(a,b),"found it!\na =",a,"\nb =",b)
