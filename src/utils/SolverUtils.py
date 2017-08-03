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
