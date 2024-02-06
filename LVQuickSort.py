import random
import numpy
import matplotlib.pyplot as plt

Xr = 0

def switch(v, i, j):
    tmp = v[j]
    v[j] = v[i]
    v[i] = tmp

def partition(v, start, end):
    pivot_idx = random.randrange(start, end)
    switch(v, pivot_idx, start)
    i = start + 1

    for j in range(start + 1, end + 1):
        global Xr
        Xr += 1

        if(v[j] < v[start]):
            switch(v, i, j)
            i += 1
    
    switch(v, start, i-1)
    return i - 1

def LVQuickSort(v, start, end):
    if(start < end):
        pivot = partition(v, start, end)
        LVQuickSort(v, start, pivot-1)
        LVQuickSort(v, pivot+1, end)

if __name__ == "__main__":
    R = pow(10, 5)
    numConfronti = numpy.zeros(R)

    N = pow(10, 4)
    s = []

    for i in range(1, N+1):
        s.append(i)

    random.shuffle(s)

    for i in range(0, R):
        tmp = numpy.copy(s)
        LVQuickSort(tmp, 0, len(tmp) - 1)
        numConfronti[i] = Xr
        Xr = 0

    u = 0
    u = numpy.mean(numConfronti)
    print("Il valore medio è: ", u)

    d = 0
    d = numpy.std(numConfronti)
    print("La deviazione standard empirica è: ", d)

    plt.hist(numConfronti, bins = 50, edgecolor = 'blue', linewidth = 1.5)
    plt.axvline(x=u, color='g', linestyle='solid')
    plt.axvline(x=u - d, color='r', linestyle='dashdot')
    plt.axvline(x=u + d, color='r', linestyle='dashdot')
    plt.title('LVQuickSort')
    plt.xlabel('Numero di confronti')
    plt.ylabel('Frequenza')
    plt.show()