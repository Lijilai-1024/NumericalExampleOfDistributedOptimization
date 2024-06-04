import numpy as np
def DistributedSubgradientMethod(f,x_initial,A,gamma,t_terminal,args):
    '''
    Distributed Subgradient Method
    Args:
        f: list of functions
        x_initial: initial point
        A: doubly stochastic matrix
        gamma: step size(related to time)
        t_terminal: terminal time
        Args: list of arguments for functions
    Returns:
        x: final point
    '''
    n = len(f)
    x = x_initial
    t = 0
    while t <= t_terminal:
        t += 1
        v = A @ x
        for i in range(n):
            print()
            if args == None:
                x[i] = x[i] - gamma(t) * subgradient(f[i],v[i])
            else:
                x[i] = x[i] - gamma(t) * subgradient(f[i],v[i],args[i])
    return x

def subgradient(f,x,args=None):
    '''
    Compute the subgradient of f at x
    Args:
        f: function
        x: point
    Returns:
        subgrad: subgradient of f at x
    '''
    print(np.size(x))
    ans = 0
    return ans

        
        


