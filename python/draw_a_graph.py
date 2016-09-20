#A  student's packages
from mpl_toolkits.mplots3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

# B student's packages


# B student's function

def eval_func():

    return X,Y,Z

# A student's function

def plot_func(X,Y,Z):
    fig = plt.figure()
    ax  = fig.gca(projection='3d')
    
    surf ax.plot_surface(x, Y, Z, rstribe=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialised=Flase)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
    return
    return

# B student writes the main

if __name__=="__main__":

    X,Y,Z = eval_func()
    plot_func(X,Y,Z)
