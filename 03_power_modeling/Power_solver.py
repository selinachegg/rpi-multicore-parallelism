import cvxopt
from cvxopt import glpk
print("Recherche mpcores - couple s,n")
c=cvxopt.matrix([-10,5],tc='d')
A=cvxopt.matrix([[1.2,-1],[-1,0],[0,1],[-1,0]],tc='d')
b=cvxopt.matrix([0,-1,8,-1],tc='d')
(status, x)=glpk.ilp(c,A.T,b,I=set([0,1]))
print (status)
print (x[0],x[1])
print (sum(c.T*x))
