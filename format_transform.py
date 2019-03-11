## Give the table format data, and outpout in another format

data = '123\tabc\nbcd\t345\nabc\t345\n123\thij\n'

lines = data.split('\n')[:-1]
U = dict()
counter = 0
for line in lines:
    cells = line.split('\t')
    for cell in cells:
        if cell not in U:
            U[cell] = counter
            counter += 1
            line += '\t' + str(U[cell])
        else:
            line += '\t' + str(U[cell])
    print(line)
