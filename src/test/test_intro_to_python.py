import numpy as np

def main():
    mat = createMat()
    printMat(mat)
    print()
    mat = addThree(mat)
    printMat(mat)
    print()
    mat = removeLastCol(mat)
    printMat(mat)


def createMat():
    return np.identity(3)

def printMat(mat):
    print(mat)

def addThree(mat):
    mat = mat * (-2)
    return (mat + 3)

def removeLastCol(mat):
    return np.delete(mat, np.s_[-1:], axis=1)

if __name__ == "__main__":
    main()