import matplotlib.pyplot as plt
import numpy as np

# TODO: read from h5 file to get flow and fasta

flow = ['T', 'A', 'T', 'G', 'T', 'C', 'B', 'A', 'G', 'T', 'G', 'C', 'A', 'T', 'G', 'T', 'C', 'A', 'T', 'G', 'T', 'C', 'A']
fasta = 'TCAGGGCAGCGCAAAA'

def getIncorporations(flow, fasta):
    n = len(fasta)
    incorporations = [0]*len(flow)
    index = 0

    for count, letter in enumerate(flow):
        for i in range(index, n):
            if letter == fasta[i]:
                incorporations[count] += 1
            else:
                index = i
                break

    return incorporations

def barPlot(x, y):
    index = np.arange(len(x))
    plt.bar(index, y)
    plt.xticks(index, x, fontsize=10)
    plt.show()

if __name__ == '__main__':
    incorporations = getIncorporations(flow, fasta)
    print ' '.join(map(str,incorporations))
    print ' '.join(flow)
    barPlot(flow, incorporations)
