import matplotlib.pyplot as plt
import imageio as img
from os import remove
from mpl_toolkits.mplot3d import Axes3D

def wide_perspective(plt,ax,fr):
    ang, pls, png = 0, (360 / fr), []
    for i in range(int(fr)):
        ax.view_init(elev=22., azim=ang)
        png.append(str(ang) + '.png')
        plt.savefig(str(ang) + '.png')
        print("img number ", i + 1, " from ", fr, " created")
        ang += pls
    return png

def create_3d_graph(x,y,z,colors,fr=36):
    fig= plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, marker='.', color=colors)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    return wide_perspective(plt,ax,fr)

def create_gif(img_lst, name):
    img.mimsave(name+'.gif', [img.imread(i) for i in img_lst])
    print("the gif '",name, "' created\n")

def clean_workspace(lst):
    for i in lst:
        remove(i)

def pd_to_gif(data ,xyz ,name ,clrs=None):
    """
    convert pandas dataframe to 3d gif
    :param data: pandas dataframe
    :param xyz: x, y & z field names
    :param clrs: color field name
    :param name: output filename
    """

    x, y, z = list(data[xyz[0]]), list(data[xyz[1]]), list(data[xyz[2]])
    clrs = list(data[clrs]) if clrs != None else ['blue']*len(x)

    lst = create_3d_graph(x, y, z, colors=clrs, fr=36)
    create_gif(lst, name)
    clean_workspace(lst)