def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    elif n > 1:
        return n*fact(n-1)

def ffact(x, k):
    if (x < 1):
        return 1
    elif (k==0):
        return 1
    else:
        u = x
        y=1
        while (x > u-k):
            y=y*x
            x = x-1
    return y

def mfact(n, m = []):
    z = fact(n)
    for u in m:
        z = z / (fact(u))
    return z

def Post(n, r, x, p = []):
    w = [0]*(r+1)
    d = 0
    for q in p:
        w[d] = q
        d = d+1
    a = mfact(n, w)
    b = ffact(n*(n-r), x)
    m = [0]*n
    j = 1
    for i, l in enumerate(w):
        while(w[i] > 0):
            m[j-1]=i
            j=j+1
            w[i]=w[i]-1
    c = mfact(x, m)
    for s in m:
        b = b/ffact(n-r,s)
    return (a*c)/b


x = 16
n = 8
r = 3
p1 = [2,1,0,5]
p2 = [2,0,2,4]
p3 = [1,2,1,4]
p4 = [0,4,0,4]
p5 = [1,1,3,3]
p6 = [0,3,2,3]
p7 = [1,0,5,2]
p8 = [0,2,4,2]
p9 = [0,1,6,1]
p10 =[0,0,8,0]

Z = Post(n, r, x, p1)+Post(n, r, x, p2)+Post(n, r, x, p3)+Post(n, r, x, p4)+Post(n, r, x, p5)+Post(n, r, x, p6)+Post(n, r, x, p7)+Post(n, r, x, p8)+Post(n, r, x, p9)+Post(n, r, x, p10)

def Prob(n, r, x, p = []):
    return Post(n, r, x, p)/Z


print("\n")
print(p1)
print("here is the probability of p1", Post(n, r, x, p1))
print("\n")

print(p2)
print("here is the probability of p2", Post(n, r, x, p2))
print("\n")

print(p3)
print("here is the probability of p3", Post(n, r, x, p3))
print("\n")

print(p4)
print("here is the probability of p4", Post(n, r, x, p4))
print("\n")

print(p5)
print("here is the probability of p5", Post(n, r, x, p5))
print("\n")

print(p6)
print("here is the probability of p6", Post(n, r, x, p6))
print("\n")

print(p7)
print("here is the probability of p7", Post(n, r, x, p7))
print("\n")

print(p8)
print("here is the probability of p8", Post(n, r, x, p8))
print("\n")

print(p9)
print("here is the probability of p9", Post(n, r, x, p9))
print("\n")

print(p10)
print("here is the probability of p10", Post(n, r, x, p10))
print("\n")

print("here is Z", Z)
print("\n")

print("The configuration of the most probable congiguration is")
print(Post(n, r, x, p8)/Z)
print("where where the configuration is ", p8)
print("\n")


print("If you only are only allowed to move at most 2 balls from the configuration")
print(p10)
print("the probability of the configuration is")
print(Prob(n, r, x, p7)+Prob(n, r, x, p8)+Prob(n, r, x, p9)+Prob(n, r, x, p10))
print("corresponding to the configurations")
print(p7, p8, p9, p10)
print("\n")

def f(i):
    if (i==1):
        return Prob(n, r, x, p1)
    elif (i==2):
        return Prob(n, r, x, p2)
    elif (i==3):
        return Prob(n, r, x, p3)
    elif (i==4):
        return Prob(n, r, x, p4)
    elif (i==5):
        return Prob(n, r, x, p5)
    elif (i==6):
        return Prob(n, r, x, p6)
    elif (i==7):
        return Prob(n, r, x, p7)
    elif (i==8):
        return Prob(n, r, x, p8)
    elif (i==9):
        return Prob(n, r, x, p9)
    elif (i==10):
        return Prob(n, r, x, p10)
    else:
        return 0
