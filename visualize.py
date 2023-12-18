import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

def visualize(function, xx,r, save_file = False, gif=False, fps=1):
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = function.objective((X,Y))
    fig, ax = plt.subplots()
    fig.set_figheight(14)
    fig.set_figwidth(16)
    cp = ax.contour(x,y,Z)
    color = ['red','blue','green','yellow']
    frames = []
    filename = 'tmp.png'  # Temporary filename for gif generation
    for i in range(len(xx)):
        x1 = first_elements = list(map(lambda arr: arr[0], xx[:i+1]))
        x2 = first_elements = list(map(lambda arr: arr[1], xx[:i+1]))
        ax.plot(x1,x2, '-o', color='black', markersize=4)
        
        if i != len(r):
            circle1 = plt.Circle(xx[i], radius=r[i],facecolor = color[i%len(color)],alpha = 0.2)
            ax.add_artist(circle1)

        # create gif
        if gif:
            plt.savefig(filename)  # Save the plot as a PNG file
            frames.append(imageio.imread(filename))  # Append the PNG file to the frames list
            # frames.append(fig) 
    if gif:
        imageio.mimsave('animation.gif', frames, fps=fps)
        os.remove(filename)

    ax.clabel(cp, inline=True, fontsize=10)
    ax.set_title('Визуализация trust region', fontsize = 18,fontweight='bold')
    ax.set_xlabel('X_1',fontsize=16,fontweight='bold')
    ax.set_ylabel('X_2',fontsize=16,fontweight='bold')
    ax.annotate(f'точка минимума [{"%.2f" % round(xx[-1][0],2)},{"%.2f" % round(xx[-1][1],2)}]',
            xy=(xx[-1][0], xx[-1][0]+0.1), xycoords='data',
            xytext=(-15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom',fontsize = 18)
    if save_file:
        fig.savefig('fig.png')
    plt.show()