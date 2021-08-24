
import math


def binomial_equal(N,x,p):

    q = 1 - float(p)
    difference = int(N) - int(x)
    
    A = math.factorial(int(N))
    B = pow(float(p),int(x))
    C = pow(float(q),int(difference))
    Numerator = int(A) * float(B) * float(C)


    D = math.factorial(int(x))
    E = math.factorial(int(difference))
    Denominator = int(D) * int(E)


    Result = float(Numerator) / int(Denominator)
    return Result

    

def binomial_greater_than(N,x):
    
    prob_greater_total = 0

    for val in range (int(x),int(N_increment)):  # 2,3,4,5,6

        r_r = binomial_equal(N,val,p)
        prob_greater_total += float(r_r)        

    return prob_greater_total


###############################################
N = input("N : ")
x = input("x : ")
p = input("p : ")


N_increment = int(N) + 1

##############################################


BE = binomial_equal(N,x,p)
BG = binomial_greater_than(N,x)


print("")
print("P(X =  "  + str(x) + ")  = ", BE)
print("")
print("P(X >= " + str(x) +  ")  = ", BG)
print("")
print("P(X <  "  + str(x) + ")  = ", 1 - BG)
print("")













