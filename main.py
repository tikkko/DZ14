s1 = [1, 2, 3, 4, 5]

s2 = [4, 5, 6, 7, 8]


def list_sum():
    s3 = []
    for i in s1:
        for j in s2:
            if s1.index(i) == 0 and s2.index(j) == 0:
                s = i + j
                s3.append(s)
            if s1.index(i) == 2 and s2.index(j) == 2:
                s = i + j
                s3.append(s)
            if s1.index(i) == 4 and s2.index(j) == 4:
                s = i + j
                s3.append(s)
    print(s3)


if __name__ == '__main__':
    list_sum()

