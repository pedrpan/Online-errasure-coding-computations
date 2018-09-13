def fact(n):
    if n == 0:
        return 1
    elif n > 0:
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



def part(n,r,x,i):
    if(n<0 or r <0 or x< 0 or i< 0 or n*r < x):
        return [-1]
    p = [0]*(r+1)
    p[r] = x//r
    if (i == 1):
        if (x/r == x//r):
            p[0]=n-p[r]
            return p
        while (x> 0 and r>1):
            x = x -r*p[r]
            r = r-1
            p[r] = x//r
        p[0]=n-sum(p)
        return p
    k=1
    while(k!=i and p!=[-1]):
        p=nextpart(n,r,x,p)
        k=k+1
    return p


def nextpart(n,r,x,p = []):
    if(n<0 or r <0 or x< 0 or n*r < x):
        return [-1]
    if (p[1]==x):
        return [-1]
    l = list(p)
    j = 2
    while(j<r+1):
        while(l[j]<1):
            j=j+1
            if (j>r):
                return [-1]
        l[j]=l[j]-1
        t=x
        m=n
        u=r
        while (u>j-1):
            t=t-u*l[u]
            m=m-l[u]
            u=u-1
        s=part(m,j-1,t,1)
        if(s != [-1]):
            f=0
            while(f<j):
                l[f]=s[f]
                f=f+1
            return l
        l[j]=l[j]+1
        j=j+1
    return [-1]



print(part(8,3,16,2))




x = 23
n = 8
r = 3



Z = 0
y=1
while (part(n,r,x,y)!=[-1]):
    Z=Z+Post(n, r, x, part(n,r,x,y))
    y=y+1

def Prob(n, r, x, p = []):
    return Post(n, r, x, p)/Z


print("\n")

h=1
while (part(n,r,x,h)!=[-1]):
    print(part(n,r,x,h))
    print("here is the probability of parition #", h)
    print( Prob(n, r, x, part(n,r,x,h)))
    print("\n")
    h=h+1


def f(i):
    return Prob(n, r, x, part(n,r,x,i))


print(part(n,r,x,11))
