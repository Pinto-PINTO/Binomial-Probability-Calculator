
import math

# P ( X = x )
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

    
# P ( X > = x )
def binomial_greater_than(N,x):
    
    prob_greater_total = 0

    for val in range (int(x),int(N_increment)): 

        F = binomial_equal(N,val,p)
        prob_greater_total += float(F)        

    return prob_greater_total


# P (X < = x)
def binomial_lesser_than(x):

    prob_lesser_total = 0

    for val in range (0, int(x_increment)):
        
        G = binomial_equal(N,val,p)
        prob_lesser_total += float(G)

    return prob_lesser_total


################### User Input ###############

print("-----------------------------------------------------------------")
print("Binomial Distribution Calculator                 by: MENUKA PINTO")
print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
print("N = Number of opportunities an event X occur")
print("x = Number of times that event x occurs or is stipulated to occur")
print("p = Probability of success")
print("-----------------------------------------------------------------")
print("")

N = input("N : ")
x = input("x : ")
p = input("p : ")

N_increment = int(N) + 1
x_increment = int(x) + 1

##############################################


BE = binomial_equal(N,x,p)
BG = binomial_greater_than(N,x)
BL = binomial_lesser_than(x)


print("")
print("P(X =  "  + str(x) + ")  = ", BE)
print("")
print("P(X >= " + str(x) +  ")  = ", BG)
print("")
print("P(X <= " + str(x) +  ")  = ", BL)
print("")













