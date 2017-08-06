import numpy as np


def ConstructC(A):
    C=np.array(np.arange(12))
    for i in range(9):
        for j in range(9):
            if (A[i,j]==0):
                row=A[i,0:9]
                col=A[0:9,j]
                nbox = get_nBox(i, j)
                box = get_matBox(nbox, A)
                newrow = newCLine(row,col,box)
                newrow[9] = i
                newrow[10] = j
                newrow[11] = nbox
                C = np.vstack([C, newrow])

    C=np.delete(C,0,0)
    return C


def SudoInput1(A,C):
    t=False
    nrows=C.shape[0]
    delrows=np.array([])
    for i in range(nrows):
        row=C[i,0:9]
        if (row[np.nonzero(row)].size==1):
            arr=row[np.nonzero(row)]
            t=True
            A[C[i,9],C[i,10]]=arr[0]
            C=clearC(C,C[i,9],C[i,10],C[i,11],arr.item(0))
            delrows=np.append(delrows,i)
    
    C=np.delete(C,delrows,0)
    return A, C, t


def SudoInput2(A,C):
    t=False
    
    for i in range(9):
        for j in range(9):
            a=C[C[:,9]==i,:]
            delrows=np.array(np.where(C[:,9]==i))
            b=a[:,j]
            if(b[np.nonzero(b)].size==1):
                t=True
                whrows=np.array(np.where(b!=0))[0,0]
                c=a[b!=0,:]
                A[c[0,9],c[0,10]]=j+1
                C=clearC(C,c[0,9],c[0,10],c[0,11],j+1)
                C=np.delete(C,delrows[0,whrows],0)

    for i in range(9):
        for j in range(9):
            a=C[C[:,10]==i,:]
            delrows=np.array(np.where(C[:,10]==i))
            b=a[:,j]
            if(b[np.nonzero(b)].size==1):
                t=True
                #whrows.append(np.array(np.where(b!=0))[0,0])
                whrows=np.array(np.where(b!=0))[0,0]
                c=a[b!=0,:]
                A[c[0,9],c[0,10]]=j+1
                C=clearC(C,c[0,9],c[0,10],c[0,11],j+1)
                C=np.delete(C,delrows[0,whrows],0)

    for i in range(9):
        for j in range(9):
            a=C[C[:,11]==i+1,:]
            delrows=np.array(np.where(C[:,11]==i+1))
            b=a[:,j]
            if(b[np.nonzero(b)].size==1):
                t=True
                whrows=np.array(np.where(b!=0))[0,0]
                c=a[b!=0,:]
                A[c[0,9],c[0,10]]=j+1
                C=clearC(C,c[0,9],c[0,10],c[0,11],j+1)
                C=np.delete(C,delrows[0,whrows],0)

    return A, C, t


#------------------------------------------------------------
def CandLineEr(C):    #Determine Medium   (3)
    nrows=C.shape[0]
    t=False
    
    for i in range(9):
        a=C[C[:,11]==i+1,:]
        for j in range(9):
            b=a[:,j]
            if(b[np.nonzero(b)].size==2 or b[np.nonzero(b)].size==3):
                c=a[b!=0,9]
                if (np.unique(c).size==1):
                    row=c[0]
                    for k in range(nrows):
                        if (C[k,9]==row and C[k,11]!=i+1):
                            if (C[k,j]!=0):
                                t=True
                            C[k,j]=0
                c=a[b!=0,10]
                if (np.unique(c).size==1):
                    col=c[0]
                    for k in range(nrows):
                        if (C[k,10]==col and C[k,11]!=i+1):
                            if (C[k,j]!=0):
                                t=True
                            C[k,j]=0
    
    for i in range(9):
        a=C[C[:,10]==i,:]
        for j in range(9):
            b=a[:,j]
            if(b[np.nonzero(b)].size==2 or b[np.nonzero(b)].size==3):
                c=a[b!=0,11]
                if (np.unique(c).size==1):
                    #t=True
                    box=c[0]
                    #print(j+1,"col ",i)
                    for k in range(nrows):
                        if (C[k,11]==box and C[k,10]!=i):
                            if (C[k,j]!=0):
                                #print(a)
                                #print(k,j)
                                t=True
                            C[k,j]=0
    
    for i in range(9):
        a=C[C[:,9]==i,:]
        for j in range(9):
            b=a[:,j]
            if(b[np.nonzero(b)].size==2 or b[np.nonzero(b)].size==3):
                c=a[b!=0,11]
                if (np.unique(c).size==1):
                    #t=True
                    #print(j+1,"row ",i)
                    box=c[0]
                    for k in range(nrows):
                        if (C[k,11]==box and C[k,9]!=i):
                            if (C[k,j]!=0):
                                #print(a)
                                #print(k,j)
                                t=True
                            C[k,j]=0
    return C, t
#-------------------------------------------------------


#-------------------------------------------------------
def multLineEr(C):    #Determine Medium  (4)
    nrows=C.shape[0]
    t=False
    for i in xrange(1,8,3):     #Take every combination of two by row-contigous boxes
        for j in xrange(i,i+2,1):
            for k in xrange(j+1,i+3,1):
                a=np.array(np.arange(12))
                add=False
                for l in range(nrows):
                    if (C[l,11]==j or C[l,11]==k):
                        a=np.vstack([a,C[l,:]])
                        add=True
                a=np.delete(a,0,0)
                if (add):
                    for l in range(9):
                        b=a[:,l]
                        c=a[b!=0,9:12]
                        if (np.unique(c[:,0]).size==2 and np.unique(c[:,2]).size==2):
                            thirdBox=getThirdBox(i,j,k,1)
                            rows=np.unique(c[:,0])
                            for n in range(nrows):
                                if (C[n,11]==thirdBox and (C[n,9]==rows[0] or C[n,9]==rows[1])):
                                    if (C[n,l]!=0):
                                        t=True
                                    C[n,l]=0
    
    
    for i in xrange(1,4,1):         #Take every combination of two by col-contigous boxes
        for j in xrange(i,i+7,3):
            for k in xrange(j+3,i+7,3):
                a=np.array(np.arange(12))
                add=False
                for l in range(nrows):
                    if (C[l,11]==j or C[l,11]==k):
                        a=np.vstack([a,C[l,:]])
                        add=True
                a=np.delete(a,0,0)
                if (add):
                    for l in range(9):
                        b=a[:,l]
                        c=a[b!=0,10:12]
                        #print(c)
                        if (np.unique(c[:,0]).size==2 and np.unique(c[:,1]).size==2):
                            thirdBox=getThirdBox(i,j,k,2)
                            cols=np.unique(c[:,0])
                            #print(c[:,0])
                            #print(np.unique(c[0,:]))
                            #print(cols)
                            for n in range(nrows):
                                if (C[n,11]==thirdBox and (C[n,10]==cols[0] or C[n,10]==cols[1])):
                                    if (C[n,l]!=0):
                                        t=True
                                    C[n,l]=0
    return C, t
#-------------------------------------------------------


#-------------------------------------------------------
def nakedPairEr(C):       # Determine Difficult   (5)
    nrows=C.shape[0]
    #print(C)
    t=False
    for i in range(nrows):
        a=np.unique(C[i,0:9])
        a=np.delete(a,np.array(np.where(a==0)))
        if (a.size==2):
            cell=C[i,0:9]
            #print(C[i,:])
            #print(cell)
            nums=a
            row=C[i,9]
            col=C[i,10]
            box=C[i,11]
            for j in range(nrows):
                if (np.array_equal(cell,C[j,0:9]) and j!=i):
                    #print(C[j,:])
                    if (C[j,9]==row):
                        for k in range(nrows):
                            if (C[k,9]==row and j!=k and i!=k):
                                if (C[k,nums[0]-1]!=0):
                                    t=True
                                    C[k,nums[0]-1]=0
                                if (C[k,nums[1]-1]!=0):
                                    t=True
                                    C[k,nums[1]-1]=0
                    if (C[j,10]==col):
                        for k in range(nrows):
                            if (C[k,10]==col and j!=k and i!=k):
                                if (C[k,nums[0]-1]!=0):
                                    t=True
                                    C[k,nums[0]-1]=0
                                if (C[k,nums[1]-1]!=0):
                                    t=True
                                    C[k,nums[1]-1]=0
                    if (C[j,11]==box):
                        for k in range(nrows):
                            if (C[k,11]==box and j!=k and i!=k):
                                if (C[k,nums[0]-1]!=0):
                                    t=True
                                    C[k,nums[0]-1]=0
                                if (C[k,nums[1]-1]!=0):
                                    t=True
                                    C[k,nums[1]-1]=0    
    return C, t
#-------------------------------------------------------


#-------------------------------------------------------
def nakedTuplesEr(C):         #Determine Difficult (6)
    t=False
    nrows=C.shape[0]
    for i in range(9):
        cells=C[C[:,9]==i,:]
        crows=cells.shape[0]
        for j in range(crows):
            a1=np.unique(cells[j,0:9])
            a1=np.delete(a1,np.array(np.where(a1==0)))
            if (a1.size==2 or a1.size==3):
                for k in xrange(j+1,crows,1):
                    a2=np.unique(cells[k,0:9])
                    a2=np.delete(a2,np.array(np.where(a2==0)))
                    u1=np.union1d(a1,a2)
                    if (u1.size==2 or u1.size==3):
                        for l in xrange(k+1,crows,1):
                            a3=np.unique(cells[l,0:9])
                            a3=np.delete(a3,np.array(np.where(a3==0)))
                            u2=np.union1d(u1,a3)
                            if (u2.size==3):
                                for n in range(crows):
                                    if (n!=j and n!=k and n!=l):
                                        if (cells[n,u2[0]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[0]-1]=0
                                        if (cells[n,u2[1]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[1]-1]=0
                                        if (cells[n,u2[2]-1]!=0):
                                            #print(cells)
                                            #rint(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[2]-1]=0
        C[C[:,9]==i,:]=cells
            
    for i in range(9):
        cells=C[C[:,10]==i,:]
        crows=cells.shape[0]
        for j in range(crows):
            a1=np.unique(cells[j,0:9])
            a1=np.delete(a1,np.array(np.where(a1==0)))
            if (a1.size==2 or a1.size==3):
                for k in xrange(j+1,crows,1):
                    a2=np.unique(cells[k,0:9])
                    a2=np.delete(a2,np.array(np.where(a2==0)))
                    u1=np.union1d(a1,a2)
                    if (u1.size==2 or u1.size==3):
                        for l in xrange(k+1,crows,1):
                            a3=np.unique(cells[l,0:9])
                            a3=np.delete(a3,np.array(np.where(a3==0)))
                            u2=np.union1d(u1,a3)
                            if (u2.size==3):
                                for n in range(crows):
                                    if (n!=j and n!=k and n!=l):
                                        if (cells[n,u2[0]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[0]-1]=0
                                        if (cells[n,u2[1]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[1]-1]=0
                                        if (cells[n,u2[2]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[2]-1]=0
        C[C[:,10]==i,:]=cells
        
    for i in range(9):
        cells=C[C[:,11]==i+1,:]
        crows=cells.shape[0]
        for j in range(crows):
            a1=np.unique(cells[j,0:9])
            a1=np.delete(a1,np.array(np.where(a1==0)))
            if (a1.size==2 or a1.size==3):
                for k in xrange(j+1,crows,1):
                    a2=np.unique(cells[k,0:9])
                    a2=np.delete(a2,np.array(np.where(a2==0)))
                    u1=np.union1d(a1,a2)
                    if (u1.size==2 or u1.size==3):
                        for l in xrange(k+1,crows,1):
                            a3=np.unique(cells[l,0:9])
                            a3=np.delete(a3,np.array(np.where(a3==0)))
                            u2=np.union1d(u1,a3)
                            if (u2.size==3):
                                for n in range(crows):
                                    if (n!=j and n!=k and n!=l):
                                        if (cells[n,u2[0]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[0]-1]=0
                                        if (cells[n,u2[1]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[1]-1]=0
                                        if (cells[n,u2[2]-1]!=0):
                                            #print(cells)
                                            #print(u2)
                                            #print(n)
                                            t=True
                                            cells[n,u2[2]-1]=0
        C[C[:,11]==i+1,:]=cells
        
    return C, t
#-------------------------------------------------------


#-------------------------------------------------------
def hiddenPairEr(C):       #Determine difficult (7)
    t=False
    for i in range(9):
        cells=C[C[:,9]==i,:]
        for j in range(9):
            b1=cells[:,j]
            rc=[]
            if(b1[np.nonzero(b1)].size==2):
                c=cells[b1!=0,0:9]
                for k in range(b1.size):
                    if (b1[k]!=0):
                        rc.append(k)
                for k in xrange(j+1,9,1):
                    b2=cells[:,k]
                    if(b2[np.nonzero(b2)].size==2):
                        ispair=c[:,k]
                        if(ispair[np.nonzero(ispair)].size==2):
                            for l in range(9):
                                if (l!=j and l!=k):
                                    if (cells[rc[0],l]!=0):
                                        #print(cells)
                                        #print(c)
                                        #print(rc[0],l)
                                        t=True
                                        cells[rc[0],l]=0
                                    if (cells[rc[1],l]!=0):
                                        #print(cells)
                                        #print(c)
                                        #print(rc[1],l)
                                        t=True
                                        cells[rc[1],l]=0
        C[C[:,9]==i,:]=cells
    
    for i in range(9):
        cells=C[C[:,10]==i,:]
        for j in range(9):
            b1=cells[:,j]
            rc=[]
            if(b1[np.nonzero(b1)].size==2):
                c=cells[b1!=0,0:9]
                for k in range(b1.size):
                    if (b1[k]!=0):
                        rc.append(k)
                for k in xrange(j+1,9,1):
                    b2=cells[:,k]
                    if(b2[np.nonzero(b2)].size==2):
                        ispair=c[:,k]
                        if(ispair[np.nonzero(ispair)].size==2):
                            for l in range(9):
                                if (l!=j and l!=k):
                                    if (cells[rc[0],l]!=0):
                                        #print(cells)
                                        #print(c)
                                        #print(rc[0],l)
                                        t=True
                                        cells[rc[0],l]=0
                                    if (cells[rc[1],l]!=0):
                                        #print(cells)
                                        #print(c)
                                        #print(rc[1],l)
                                        t=True
                                        cells[rc[1],l]=0
        C[C[:,10]==i,:]=cells
    
    for i in range(9):
        cells=C[C[:,11]==i+1,:]
        for j in range(9):
            b1=cells[:,j]
            rc=[]
            if(b1[np.nonzero(b1)].size==2):
                c=cells[b1!=0,0:9]
                for k in range(b1.size):
                    if (b1[k]!=0):
                        rc.append(k)
                for k in xrange(j+1,9,1):
                    b2=cells[:,k]
                    if(b2[np.nonzero(b2)].size==2):
                        ispair=c[:,k]
                        if(ispair[np.nonzero(ispair)].size==2):
                            for l in range(9):
                                if (l!=j and l!=k):
                                    if (cells[rc[0],l]!=0):
                                        #print(cells)
                                        #print(c)
                                        #print(rc[0],l)
                                        t=True
                                        cells[rc[0],l]=0
                                    if (cells[rc[1],l]!=0):
                                        #print(cells)
                                        #print(c)
                                        #print(rc[1],l)
                                        t=True
                                        cells[rc[1],l]=0
        
        C[C[:,11]==i+1,:]=cells
    
    return C, t
#-----------------------------------------------------------


#-----------------------------------------------------------
def hiddenTupleEr(C):       #Determine difficult (8)
    t=False
    
    
    
    return C,t


def clearC(C,row,col,nbox,num):
    nrows=C.shape[0]
    for i in range(nrows):
        if (C[i,9]==row or C[i,10]==col or C[i,11]==nbox):
            C[i,num-1]=0
    return C


def FindMinRow(C):
    row=0
    arr=C[row,0:9]
    mini=arr[np.nonzero(arr)].size
    nrows=C.shape[0]
    for i in range(nrows-1):
        arr=C[i+1,0:9]
        if (mini>arr[np.nonzero(arr)].size):
            mini=arr[np.nonzero(arr)].size
            row=i+1
    return row


def get_nBox(row,col):
    box=row//3+1+2*(row//3)
    return box +col//3


def get_matBox(nbox,A):
    row=(nbox-1)//3+2*((nbox-1)//3)
    col=(nbox-1)%3+2*((nbox-1)%3)
    box=A[row:(row+3),col:(col+3)]
    return box


def newCLine(row,col,box):
    newrow=np.arange(12)+1
    nonZ=row[np.nonzero(row)]
    newrow[nonZ-1]=0
    nonZ = col[np.nonzero(col)]
    newrow[nonZ - 1] = 0
    nonZ = box[np.nonzero(box)]
    newrow[nonZ - 1] = 0
    return newrow


def FindPosNums(A,r,c):
    posnums=np.arange(9)+1
    nBox=get_nBox(r,c)
    Box=get_matBox(nBox,A)
    row=A[r,:]
    row=row[np.nonzero(row)]
    col=A[:,c]
    col=col[np.nonzero(col)]
    posnums[row-1]=0
    posnums[col-1]=0
    for i in range(3):
        for j in range(3):
            if (Box[i,j]!=0):
                posnums[Box[i,j]-1]=0
    posnums=np.delete(posnums,np.where(posnums==0))
    return posnums
 

def getThirdBox(i,j,k,n):
    if (n==1):
        if (i!=j):
            return i
        elif (k==i+1):
            return i+2
        else:
            return i+1
    else:
        if (i!=j):
            return i
        elif (k==i+3):
            return i+6
        else:
            return i+3
