
def add_x_Right(a,x):
    # This function adds x to the right of existing tuple a
    # and returns the new tuple
    return (a)+(x,)
a=(True,True,True)
def add_n_x_Right(a,n,x):
    # This function adds x n times to the right of existing tuple a
    if n==0:
        return a
    else:
        # and returns the new tuple
        return add_n_x_Right(add_x_Right(a,x),n-1,x)
def add_x_Left(a,x):
    # This function adds x to the right of existing tuple a
    # and returns the new tuple
    return (x,)+(a)
def add_n_x_Left(a,n,x):
    # This function adds x n times to the left of existing tuple a
    if n==0:
        return a
    else:
        # and returns the new tuple
        return add_n_x_Left(add_x_Left(a,x),n-1,x)
def add_ij_x_Left_Right(i,a,j,x):
    # This function adds x , i and j times to left and right respectively of a
    a=add_n_x_Left(a,i,x)
    a=add_n_x_Right(a,j,x)
    # and returns the new tuple
    return a
def scratch(a):
    # This operation removes on bit from a 4-bit tuple and replace one bit by false
    # after shifting on side. In effect a//2 or right shift
    (a0,a1,a2,a3)=a
    return(a1,a2,a3,False)
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
def add8(a,b,c):
    #The input is 2 4-tuples of boolean input and one carry bit
    (a0,a1,a2,a3,a4,a5,a6,a7)=a
    (b0,b1,b2,b3,b4,b5,b6,b7)=b
    (c0,c1,c2,c3,c4)=add4(a0,a1,a2,a3,b0,b1,b2,b3,c)
    (c5,c6,c7,c8,c9)=add4(a4,a5,a6,a7,b4,b5,b6,b7,c4)
    #It returns a 8tuple and a bit which when combined and read right to left represents the sum
    return ((c0,c1,c2,c3,c5,c6,c7,c8),c9)
def megaand(a,b):
    #It is an auxillary function
    #It gives multiplication of one bit and a 4-bit numeral
    (a0,a1,a2,a3)=a
    return (b and a0, b and a1, b and a2, b and a3)
def mul4(a,b):
    # This gives the value of a*b in binary numbers.
    # This takes 2 a=a0a1a2a3 , b=b0b1b2b3 numerals
    (a0,a1,a2,a3)=a
    (b0,b1,b2,b3)=b
    c0=megaand(a,b0)
    c1=megaand(a,b1)
    c2=megaand(a,b2)
    c3=megaand(a,b3)
    (x0,y0) =add8(add_ij_x_Left_Right(0,c0,4,False),add_ij_x_Left_Right(1,c1,3,False),False)
    (x1,y1) =add8(x0,add_ij_x_Left_Right(2,c2,2,False),False)
    (x2,y2) =add8(x1,add_ij_x_Left_Right(3,c3,1,False),False)
    # It returns a*b in a 8 bit numeral output
    return x2


def itera(a,b,temp,i):
    # This is a loop like way to multiply 2 bit binary numbers which can easily be extended
    # to more than 4 bits. It is recursive in nature but completes in less than 4 steps
    if b==(False,False,False,False):
        return temp
    else:
        (b0,b1,b2,b3)=b
        (temp,c)=add8(temp,add_ij_x_Left_Right(i,megaand(a,b0),4-i,False),False)
        return itera(a,scratch(b),temp,i+1)


def mul4i(a,b):
    # This is the final function returning a*b in binary form
    return(itera(a,b,(False,False,False,False,False,False,False,False),0))
