import numpy as np
N = 5
R = 8.3
def calc_Energy(A):
    E = 0
    for i in range(1,N-1):
        E_i = 0
        for j in range(1,N-1):
            e = -A[i][j]*(A[i-1][j]+A[i+1][j]+A[i][j-1]+A[i][j+1])
            E_i = E_i + e
        E = E + E_i
    return E
def mcmc(A,RT,nstep):
    istep = 0
    E = calc_Energy(A)
    ii = 0
    jj = 0
    xx = []
    ee = []
    while istep<nstep:
        Einc = 0.0
        if ii>0:
            Einc += A[ii-1,jj]
        if ii<N-1:
            Einc += A[ii+1,jj]
        if jj>0:
            Einc += A[ii,jj-1]
        if  jj<N-1:
            Einc += A[ii,jj+1]
        Enew = E+2.0*A[ii,jj]*Einc
        itrans = 0
        if Enew<E:
            itrans = 1
        else:
            p = np.random.random_sample()
            if p<np.exp(-(Enew-E)/RT):
                itrans = 1
        if itrans == 1:
            A[ii,jj] = -A[ii,jj]
            E = Enew
        jj += 1
        if jj == N:
            jj = 0
            ii += 1
        if ii == N:
            ii = 0
        istep += 1
        xx.append(istep)
        ee.append(E)
    return xx,ee
A = np.ones((N,N),dtype=np.int)
for i in range(N):
    for j in range(0,N,2):
        A[i,j] = -1


