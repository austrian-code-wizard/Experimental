from math import sqrt
import matplotlib.pyplot as plt

sq3 = sqrt(3)

def draw_triangle(x, y, l, plt, up=True):
    plt.plot([x, x+l], [y, y], 'k-', lw=0.5)
    if up:
        plt.plot([x, x+l/2], [y, y+l/2*sq3],'k-', lw=0.5)
        plt.plot([x+l/2, x+l], [y+l/2*sq3, y],'k-', lw=0.5)
    else:
        plt.plot([x, x+l/2], [y, y-l/2*sq3],'k-', lw=0.5)
        plt.plot([x+l/2, x+l], [y-l/2*sq3, y],'k-', lw=0.5)
    


def sierpinski(x, y, l, depth, plt):
    if depth == 0:
        return True
    draw_triangle(x+l/4, y-l/4*sq3, l/2, plt)
    sierpinski(x, y, l/2, depth-1, plt)
    sierpinski(x+l/2, y, l/2, depth-1, plt)
    sierpinski(x+l/4, y-l/4*sq3, l/2, depth-1, plt)
    return True

draw_triangle(0, 20, 2000, plt, up=False)
sierpinski(0, 20, 2000, 5, plt)
plt.show()
