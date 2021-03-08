import os
import math
import numpy
from collections import Counter

def ex1(text):
    """
    Returneaza ultimul cuvant lexicografic din text
    input: text - string
    ouput: string
            "nu exista cuvinte" daca textul e vid

    Complexitate O(n)
    """
    if len(text) == 0:
        return "nu exista cuvinte"
    #return sorted(text.split(" "), reverse=True)[0]
    text = text.split(" ")
    word = text[0]
    for w in text:
        if w > word:
            word = w
    return word

def testEx1():
    assert(ex1("alo sunt marcel") == "sunt")
    assert(ex1("zzzz eife de fefe") == "zzzz")
    assert(ex1("") == "nu exista cuvinte")


def ex2(x1, y1, x2, y2):
    """
    calculeaza dist euclidiana dintre doua puncte
    input: x1, y1, x2, y2 - doubles
    ouput: double

    complexitate: O(1)
    """
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def testEx2():
    assert(ex2(1,5,4,1) == 5.0)
    assert(ex2(0,1,0,4) == 3.0)


def ex3(v1, v2):
    """
    returneaza produsul scalar a doi vectori
    input: v1,v2- int arrays
    output: int

    complexitate: O(n)
    """
    produs = 0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            if isinstance(v1[i], list):
                produs = produs + ex3(v1[i], v2[i])
            else:
                produs = produs + (v1[i] * v2[i])
    
    return produs

def testEx3():
    assert(ex3([1,0,2,0,3,0,0,3], [1,2,0,3,1,1,4,3]) == 13)
    assert(ex3([1,[0,2],0,3,0,0,3], [1,[2,0],3,1,1,4,3]) == 13)
    assert(ex3([1,0,2,0,3], [1,2,0,3,1]) == 4)


def ex4v1(text):
    """
    returneaza o lista cu cuvintele care apar o singura data in text
    input: text - string
    output: list

    complexitate: O(n)
    """
    d = {}
    for word in text.split(" "):
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    
    return [word for word in d.keys() if d[word] == 1]

def ex4v2(text):
    """
    returneaza o lista cu cuvintele care apar o singura data in text
    input: text - string
    output: list

    complexitate: O(n)
    """
    word_counts = Counter(word for word in text.split())
    return [word for (word, count) in word_counts.items() if count == 1]

def ex4v3(text):
    """
    returneaza o lista cu cuvintele care apar o singura data in text
    input: text - string
    output: list

    complexitate: O(n)
    """
    words = []
    unique_words = []
    for w in (word for word in text.split()):
        if w in words:
            continue
        if w in unique_words:
            unique_words.remove(w)
            words.append(w)
        else:
            unique_words.append(w)
    return unique_words

def testEx4():
    assert(ex4v1("ana are ana are mere rosii ana") == ['mere', 'rosii'])
    assert(ex4v1("ana are ana are mere mere rosii rosii ana") == [])
    assert(ex4v1("ana are ana are mere mere rosii rosii ana abracadabra") == ['abracadabra'])

    assert(ex4v2("ana are ana are mere rosii ana") == ['mere', 'rosii'])
    assert(ex4v2("ana are ana are mere mere rosii rosii ana") == [])
    assert(ex4v2("ana are ana are mere mere rosii rosii ana abracadabra") == ['abracadabra'])

    assert(ex4v3("ana are ana are mere rosii ana") == ['mere', 'rosii'])
    assert(ex4v3("ana are ana are mere mere rosii rosii ana") == [])
    assert(ex4v3("ana are ana are mere mere rosii rosii ana abracadabra") == ['abracadabra'])


def ex5v1(sir):
    """
    returneaza valoaraea din sir care apare de 2 ori
    input: sir- array
    output: valoarea care se repeta de 2 ori - int
            -1 - daca nu exista o valoare care se repeta
    
    complexitate O(n)
    """
    fv = [0 for i in range(len(sir))]
    for i in sir:
        fv[i] += 1
        if fv[i] == 2:
            return i
    return -1

def ex5v2(sir):
    """
    returneaza valoaraea din sir care apare de 2 ori
    input: sir- array
    output: valoarea care se repeta de 2 ori - int
            -1 - daca nu exista o valoare care se repeta
    
    complexitate O(n)
    """
    duplicat = max((sir.count(x), x) for x in sir)
    return duplicat[1] if duplicat[0] == 2 else -1

def testEx5():
    assert(ex5v1([1,2,3,4,2]) == 2)
    assert(ex5v1([1,2,3,4,4]) == 4)
    assert(ex5v2([1,2,3,4,2]) == 2)
    assert(ex5v2([1,2,3,4,4]) == 4)

def ex6v1(arr):
    """
    varianta cu Counter
    returneaza elementul majoritar din arr
    input - array
    output: int
            -1 daca nu exista element majoritar
    
    complexitate O(n)
    """
    # counts = Counter(x for x in arr)
    # for (nr, cnts) in counts.items():
    #     if cnts > len(arr)/2:
    #         return nr
    # return -1

    # rez = [x for x in set(arr) if arr.count(x) > len(arr)/2]
    # return -1 if rez == [] else rez[0]

    # for x in set(arr):
    #     if arr.count(x) > len(arr)/2:
    #         return x
    # return -1

    #return max([(arr.count(x), x) for x in set(arr)])[1] if max([(arr.count(x), x) for x in set(arr)])[0] > len(arr)/2 else -1

    most_common = max([(arr.count(x), x) for x in set(arr)])
    return most_common[1] if most_common[0] > len(arr)/2 else -1

def ex6v2(arr):
    """
    varianta cu vector de frecventa
    returneaza elementul majoritar din arr
    input - array
    output: int
            -1 daca nu exista element majoritar
    
    complexitate O(n)
    """
    n = len(arr)
    fv = [0 for i in range(max(arr) + 1)]
    for i in arr:
        fv[i] += 1
        if (fv[i] > n/2):
            return i
    return -1

def ex6v3(arr):
    """
    varianta eficienta
    returneaza elementul majoritar din arr
    input - array
    output: int
            -1 daca nu exista element majoritar
    
    complexitate O(n)
    """
    n = len(arr)
    candidat = -1
    aparitii = 0
    for i in arr:
        if aparitii == 0:
            candidat = i
            aparitii += 1
        elif i != candidat:
            aparitii -= 1
        else:
            aparitii += 1
    
    return candidat if arr.count(candidat) > n/2 else -1

def testEx6():
    #print(ex6v1([2,8,7,2,2,5,2,3,1,2,2]))
    assert(ex6v1([2,8,7,2,2,5,2,3,1,2,2]) == 2)
    assert(ex6v2([2,8,7,2,2,5,2,3,1,2,2]) == 2)
    assert(ex6v3([2,8,7,2,2,5,2,3,1,2,2]) == 2)
    #print(ex6v1([1,2,3,4,5]))
    assert(ex6v1([1,2,3,4,5]) == -1)
    assert(ex6v2([1,2,3,4,5]) == -1)
    assert(ex6v3([1,2,3,4,5]) == -1)

def ex7(v, k):
    """
    returneaza al k-ulea cel mai mare element din v
    input: v- array, k - int
    ouput: integer

    Complexitate O(nlogn)
    """
    return sorted(v)[-k]


def testEx7():
    assert (ex7([7,4,6,3,9,1], 2) == 7)
    assert (ex7([7,4,6,3,9,1], 1) == 9)
    assert (ex7([7,4,6,3,9,1], 3) == 6)


def ex8(n):
    """
    returneaza un array cu reprezentarile binare alea numerelor pana la n
    input: n - integere
    ouput: array

    complexitate O(n)
    """
    v = [0 for i in range(n)]
    for i in range(n):
        v[i] = numpy.binary_repr(i+1)
    return v

def testEx8():
    rez = ex8(4)
    assert (rez[0] == numpy.binary_repr(1))
    assert (rez[1] == numpy.binary_repr(2))
    assert (rez[2] == numpy.binary_repr(3))
    assert (rez[3] == numpy.binary_repr(4))


def ex9(matrix, l):
    """
    returneaza o lista cu sumele submatricilor identificate de perechiile din l
    input: matix, lista de tupluri de tupluri
    output: lista de integers

    complexitate O(n^2)
    """
    sums = []
    for pair in l:
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]
        suma = 0
        for line in matrix[x1:x2+1]:
            suma += sum(line[y1:y2+1])
        sums.append(suma)
    return sums



def testEx9():
    m = [[0,2,5,4,1],[4,8,2,3,7],[6,3,4,6,2], [7,3,1,8,3], [1,5,7,9,4]]
    pairs = [((1,1), (3,3)), ((2,2), (4,4))]
    assert(ex9(m, pairs) == [38, 44])
    pairs.append(((0,0), (4,4)))
    assert(ex9(m, pairs) == [38, 44, 105])



def ex10(mat):
    """
    returneaza indexul liniei pe care se afla cele mai multe cifre de 1
    input: mat - matrix
    output: integer

    Complexitate O(n^2)
    """
    smax = 0
    index = 0
    x = 0
    for line in mat:
        if (sum(line) > smax):
            smax = sum(line)
            index = x
        x = x + 1
    
    return index


def testEx10():
    assert (ex10([[1, 0, 0], [1,1,1], [0,0,0]]) == 1)
    assert (ex10([[1, 0, 0], [1,0,1], [1,1,1]]) == 2)




testEx1() #
testEx2() #
testEx3()
testEx4()
testEx5()
testEx6()
testEx7() #
testEx8() #
testEx9()
testEx10() #
