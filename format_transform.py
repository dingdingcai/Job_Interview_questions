## Give the table format data, and outpout in another format


"""
123  abc
bcd  345
abc  345 
123  hij

==>

123	 abc 	0	1
bcd	 345	2	3
abc  345    1	3
123	 hij    0	4

strs, index
123    0
abc    1
bcd    2
345    3
hij    4
"""

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
