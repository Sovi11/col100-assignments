Entry_num="2021CS10075"
rem=75%4
# We use hadd directly as given in the Hint
def hadd(a,b):
    #This will add 2 binary numbers using logic gates
    # a and b are boolean inputs (either True or False)
    # Returns a tuple of 2 boolean output
    return ((a or b) and not(a and b), a and b)
def add(a,b,c):
    # This will add 3 binary numbers only using logic gates
    # a,b and c are boolian inputs (either True or False)
    (d,e) = hadd(a,b)
    # d is like a carry bit
    (f,g) = hadd(c,d)
    # Returns a tuple of 2 boolean outputs
    return ((f),(e or g))
def add4(a0,a1,a2,a3,b0,b1,b2,b3,c):
    # It will add two 4-bit numerals and a carry bit
    (d,e)= add(a0,b0,c)
    # e is a carry bit carried to next place
    (f,g)= add(a1,b1,e)
    # g is a carry bit carried to next place
    (h,i)= add(a2,b2,g)
    # i is a carry bit carried to next place
    (j,k)= add(a3,b3,i)
    # Returns a 5 tuple of boolean output
    return (d,f,h,j,k)
# operator assigned is >=
# We start by comparing 2 bits
def cmp1(a,b):
    #This compares 2 bits
    # Returns True if the first bit >= second bit
    return a or (not b)
def equality1(a,b):
    # This is equaliy function and compares 2 bits
    # Returns true if they are equal False if not
    return not(not (a and b) and (a or b))
def equality2(a0,a1,b0,b1):
    #This is equality function of two 2 bit numerals
    c = equality1(a0,b0)
    d = equality1(a1,b1)
    #Returns True if equal and False if not
    return c and d
def cmp2(a0,a1,b0,b1):
    # This compares two 2 bit numeral according to >=
    c= cmp1(a1,b1)
    d = cmp1(a0,b0)
    e = not equality1(a1,b1)
    f = d or e
    # Returns True if the equality is valid
    return(f and c)
def cmp(a0,a1,a2,a3,b0,b1,b2,b3):
    # This is what was required comparing w.r.t >= two 4 bit numerals
    c = cmp2(a2,a3,b2,b3)
    d = cmp2(a0,a1,b0,b1)
    e = equality2(a2,a3,b2,b3)
    f = c and not e
    (x,y)= add(c,d,f)
    # returns True if a>=b else False
    return y
def sub1(a,b):
    #This provides the magnitude of subtraction of 2 bits
    c=not equality1(a,b)
    # returns |a-b|
    return c
def cmpp1(a,b):
    # This is the operator logic of >
    return cmp1(a,b) and not equality1(a,b)
def cmpp2(a,b):
    # This is the operator logic of <
    return not cmp1(a,b)
def sub2(a0,a1,b0,b1):
    #This will give the value of a-b where a and b are 2- 2bit numeral only when a>=b
    c0=sub1(a0,b0)
    c1=cmpp2(a0,b0)
    c2=sub1(a1,c1)
    c3=sub1(c2,b1)
    # this returns the value in bool,bool format
    return(c0,c3)
def sub3(a0,a1,a2,b0,b1,b2):
    #This will give the value of a-b where a and b are 2- 3bit numeral a>=b
    c1=sub1(a0,b0)
    c2=cmpp2(a0,b0)
    if not c2:
        (d1,e1)=sub2(a1,a2,b1,b2)
    else:
        c3=cmpp2(a1,c2)
        if c3:
            d1=not b1
            e1=False
        else:
            c4=cmpp2(False,b1)
            if c4:
                d1=True
                e1=False
            else:
                d1=False
                e1=sub1(a2,b2)
    #This returns the value in bool,bool,bool format
    return (c1,d1,e1)
def bro2(a0,a1,a2,a3,b0,b1,b2,b3):
    #bro2 is a helper function which gives correct value of a-b when a>=b
    c0=sub1(a0,b0)
    c1=cmpp2(a0,b0)
    if not c1:
        (d1,e1,f1)=sub3(a1,a2,a3,b1,b2,b3)
    else:
        c2=cmpp2(a1,c1)
        if not c2:
            a1=False
            (d1,e1,f1)=sub3(a1,a2,a3,b1,b2,b3)
        else:
            c3=cmpp2(a2,c1)
            if not c3:
                a2=False
                (e1,f1)=sub2(a2,a3,b2,b3)
                d1=not b1
            else:
                f1=False
                e1=not b2
                d1=not b1
    return(c0,d1,e1,f1)

def sub4(a0,a1,a2,a3,b0,b1,b2,b3):
    #This gives the difference of a and b
    if cmp(a0,a1,a2,a3,b0,b1,b2,b3)==True :
        (w,x,y,z)= bro2(a0,a1,a2,a3,b0,b1,b2,b3)
        return (w,x,y,z,False)
    else:
        (w,x,y,z)= bro2(b0,b1,b2,b3,a0,a1,a2,a3)
        return (w,x,y,z,True)
        #Value returned is a-b in boolian 5 tuples

def add8(a,b,c):
    #The input is 2 4-tuples of boolean input and one carry bit
    (a0,a1,a2,a3,a4,a5,a6,a7)=a
    (b0,b1,b2,b3,b4,b5,b6,b7)=b
    (c0,c1,c2,c3,c4)=add4(a0,a1,a2,a3,b0,b1,b2,b3,c)
    (c5,c6,c7,c8,c9)=add4(a4,a5,a6,a7,b4,b5,b6,b7,c4)
    #It returns a 8tuple and a bit which when combined and read right to left represents the sum
    return (c0,c1,c2,c3,c5,c6,c7,c8),c9
def mul4(a,b):
    (a0,a1,a2,a3)=a
    (b0,b1,b2,b3)=b
    if equality1(b1,False) and equality1(b2,False) and equality1(b3,False) and equality1(b0,False):
        return (False,False,False,False,False,False,False,False)
    else:
        (x,y)=add8((a0,a1,a2,a3,False,False,False,False),mul4(a,bro2(b0,b1,b2,b3,True,False,False,False)),False)
        return x
