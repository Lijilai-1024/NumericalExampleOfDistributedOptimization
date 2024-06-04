import numpy as np
import matplotlib.pyplot as plt
import sys
def gamma_t(t):
    return (1/t)**0.8
def get_doubly_stochastic_matrix(n,rho):
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i,i] = 1
            if np.random.rand() < rho:
                A[i,j] = 1
                A[j,i] = 1
    for i in range(n):
        A[i,:] = A[i,:]/np.sum(A[i,:])
    return A
def get_points_and_labels(n,m,d):
    # m samples with feature space dimension d
    mean = np.zeros(d)
    cov = 2*np.eye(d)
    p = []
    l = []
    for i in range(n):
        p.append(np.random.multivariate_normal(mean,cov,int(m[i])))
        l.append(np.random.choice([1,-1],size=int(m[i]),p=[0.5,0.5]))
    return p,l
n = 30
rho = 0.2
gamma = 0.001
A = get_doubly_stochastic_matrix(n, rho)
m = 10*np.ones(n)
d = 5
p,l = get_points_and_labels(n,m,d) 
C = 0.01
