file_ = open('sequence.txt','r') #read from text file

fwd = False #initialize boolean variables regarding forward or backward sequences as false
bwd = False

for line in file_:
    starts = []
    for i in range(0,len(line)):
        if line[i:i+6] == 'AGGAGG': #look for AGGs as potential starting points
            starts.append(i)
    ATGs = []
    for k in starts: #look for ATGs 6 or 7 bases after the 'AGGAGG'
        if line[k+12:k+15] == 'ATG':
            ATGs.append(k+12)
        elif line[k+13:k+16] == 'ATG':
            ATGs.append(k+13)
    print('forward starting pts', ATGs) #print the starting points, if any
    if len(ATGs) > 0: #iterate over all starting pts
        for j in ATGs: 
            for i in range(j+3,len(line),3): #and search for ending codons (TAG, TAA, TGA) with a stride of 3 bases
                if line[i:i+3] == 'TAG' or line[i:i+3] == 'TAA' or line[i:i+3] == 'TGA':
                    fwd = True #set the boolean variable as true after finding one valid gene
                    print('forward sequence',line[j:i+3],'limits',j,i+3) #print all you find
                    break
    else:
        print('nada regarding forward')

    #reverse + complement
    #1) revert all elements of the input sequence
    #2) replace bases w/ their complementary: A->T, T->A, C->G, G->C
    invline = ''
    for i in range(0,len(line)):
        if line[len(line)-1-i] == 'A':
            invline += 'T'
        elif line[len(line)-1-i] == 'T':
            invline += 'A'
        elif line[len(line)-1-i] == 'C':
            invline += 'G'
        else: #G
            invline += 'C'

    #repeat the above procedure w/ the reverted and complementary seq

    starts = []
    for i in range(0,len(line)):
        if invline[i:i+6] == 'AGGAGG':
            starts.append(i)
    ATGs = []
    for k in starts:
        if invline[k+12:k+15] == 'ATG':
            ATGs.append(k+12)
        elif invline[k+13:k+16] == 'ATG':
            ATGs.append(k+13)
    print('backward starting pts', ATGs)
    if len(ATGs) > 0:
        for j in ATGs: 
            for i in range(j+3,len(line)):
                if invline[i:i+3] == 'TAG' or invline[i:i+3] == 'TAA' or invline[i:i+3] == 'TGA':
                    bwd = True
                    print('reverse+complementary sequence',invline[j:i+3],'(inverted) limits',j,i+3)
                    break
    else:
        print('nada regarding backward')

    if not fwd and not bwd: #if both the forward and inverted sequence yield no genes, print as such
        print('nada generally')
    else:
        print('there is some sequence in some direction')

