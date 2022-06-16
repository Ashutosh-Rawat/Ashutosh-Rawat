def cal_arrays():
    import numpy

    print("Enter the value for dimension: ")
    input1 = input()
    a, b = input1.split()
    n, m = int(a), int(b)
    array = [[0 for i in range(m)]for j in range(n)]

    if m == 2:
        for i in range(0, n):
            print("Enter values: ")
            input2 = input()
            c, d = input2.split()
            c, d = int(c), int(d)
            array[i] = [c, d]

    elif m == 3:
        for i in range(0, n):
            input3 = input()
            e, f, g = input3.split()
            e, f, g = int(e), int(f), int(g)
            array[i] = [e, f, g]

    print("Mean of values: ", numpy.mean(array, axis=1).tolist())
    print("Variance of values: ", numpy.var(array, axis=0).tolist())
    std = numpy.std(array)
    std = round(std, 11)
    print("Standard deviation: ", std)


cal_arrays()
