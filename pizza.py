


def read_file(filename):
    with open(filename, "r")as f:
        line = f.readline()
        R, C, L, H = [int(n) for n in line.split()]
        matrix = [0 for x in range(R)]
        for i in range(R):
            line = f.readline()
            matrix[i] = [x for x in line]
        return matrix, R, C, L, H


def generate_forms(area):
    list = []
    for i in range(1, area + 1):
        if area % i == 0:
            list.append([i,(area // i)])
    return list


def valid_slice(pizza, x, y, lung, lat, min,out):
    tom = 0
    mush = 0
    if len(pizza)>x+lat:
        for i in range(x, x + lat):
            if len(pizza[i])>y+lung:
                for j in range(y, y + lung):
                    if out[i][j]==1:
                        return False
                    else:
                        if pizza[i][j] == "M":
                            mush += 1
                        elif pizza[i][j] == "T":
                            tom += 1
            else:
                return False
        if mush < min or tom < min:
            return False
        return True
    return False


def mark_slice(out, x, y, lung, lat):
    for i in range(x, x + lat):
        for j in range(y, y + lung):
            out[i][j] += 1


def generate_slices(pizza, x, y, minIngr, maxArea, out,result):
    if out[x][y] == 0:
        for i in range(maxArea,1,-1):
            slices = generate_forms(i)
            for i in slices:
                if valid_slice(pizza, x, y, i[0], i[1], minIngr,out):
                    result.append([x,y,x+i[1]-1,y+i[0]-1])
                    mark_slice(out, x, y, i[0], i[1])


def compute(pizza, r, c, l, h,result):
    out = [[0 for i in range(c)] for j in range(r)]
    for x in range(r):
        for y in range(c):
            generate_slices(pizza, x, y, l, h, out,result)
    for i in range(r):
        print(out[i])


def write_file(result, filename):
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(result)))
        for slic in result:
            f.write(' '.join([str(item) for item in slic]) + '\n')


def run():
    infile = "big.in"
    pizza, r, c, l, h = read_file(infile)
    result=[]
    compute(pizza,r,c,l,h,result)
    write_file(result,"output.txt")


run()
