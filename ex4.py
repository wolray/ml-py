from lib import *

X,y=load_mat('ex4data1.mat')
t1_trans,t2_trans=load_nn('ex4weights.mat')
n=[400,25,10]
lamb=1

t=append(t1_trans.T,t2_trans.T)
yk=yy(n,y)
J=ncost(t,n,X,yk,lamb)

print(J)
print('ex4: 0.383770')

t0=randt(n)
t=nfmin_cg(t0,n,X,yk,lamb)
npredict(t,n,X,y)
print('ex4: 95.3%')