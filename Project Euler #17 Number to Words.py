unit_number = {1:'One ',2:'Two ',3:'Three ',4:'Four ',5:'Five ',6:'Six ',7:'Seven ',8:'Eight ',9:'Nine ',10:'Ten ',
11:'Eleven ',12:'Twelve ',13:'Thirteen ',14:'Fourteen ',15:'Fifteen ',16:'Sixteen ',17:'Seventeen ',18:'Eighteen ',
19:'Nineteen ',20:'Twenty ',30:'Thirty ',40:'Forty ',50:'Fifty ',60:'Sixty ',70:'Seventy ',80:'Eighty ',90:'Ninety ',
100:'Hundred ',1000:'Thousand ',1000000:'Million ',1000000000:'Billion ',1000000000000:'Trillion ',
1000000000000000:'Quadrillion ',1000000000000000000:'Quintillion ',1000000000000000000000:'Sextillion ',
1000000000000000000000000:'Septillion ',1000000000000000000000000000:'Octillion ',
1000000000000000000000000000000:'Nonillion ',1000000000000000000000000000000000:'Decillion '}

def number_word(string):
    w = ''
    rev = string[::-1]
    lis = [rev[0+i:3+i] for i in range(0, len(string), 3)]
    lis.reverse()
    lis = [map(int,list(j[::-1])) for j in lis]
    for x in xrange(-1,(len(lis)+1)*-1,-1):
        if x < -1:
            if sum(lis[x]) != 0:
                w = w[:0]+unit_number[10**(3*((x*-1)-1))]+w[0:]
        if len(lis[x]) == 3:
            if lis[x][-2] == 0:
                if lis[x][-1] != 0:
                    w = w[:0]+unit_number[lis[x][-1]]+w[0:]
            elif lis[x][-2] == 1:
                n = int(str(1)+str(lis[x][-1]))
                w = w[:0]+unit_number[n]+w[0:]
            else:
                if lis[x][-1] != 0:
                    w = w[:0]+unit_number[lis[x][-1]]+w[0:]
                n = int(str(lis[x][-2])+str(0))
                w = w[:0]+unit_number[n]+w[0:]
            if lis[x][-3] != 0:
                w = w[:0]+unit_number[100]+w[0:]
                w = w[:0]+unit_number[lis[x][-3]]+w[0:]
        elif len(lis[x]) == 2:
            if lis[x][-2] == 0:
                if lis[x][-1] != 0:
                    w = w[:0]+unit_number[lis[x][-1]]+w[0:]
            elif lis[x][-2] == 1:
                n = int(str(1)+str(lis[x][-1]))
                w = w[:0]+unit_number[n]+w[0:]
            else:
                if lis[x][-1] != 0:
                    w = w[:0]+unit_number[lis[x][-1]]+w[0:]
                n = int(str(lis[x][-2])+str(0))
                w = w[:0]+unit_number[n]+w[0:]
        else:
            if lis[x][-1] != 0:
                w = w[:0]+unit_number[lis[x][-1]]+w[0:]
    return w
    
T = int(raw_input())
for _ in xrange(T):
    N = str(raw_input())
    print number_word(N)