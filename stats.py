import sys
from array import array

def stats(filename):
    ax = array('f')
    ay = array('f')
    az = array('f')
    lines = open(filename, encoding='ASCII').readlines()
    print(len(lines))
    for line in lines:
        x, y, z = (float(n) for n in line.split())
        ax.append(x)
        ay.append(y)
        az.append(z)


    print('min:', min(ax), min(ay), min(az))
    print('max:', max(ax), max(ay), max(az))
    print('delta:', max(ax)-min(ax), max(ay)-min(ay), max(az)-min(az))

if __name__=='__main__':
    source = sys.argv[1]
    stats(source)
