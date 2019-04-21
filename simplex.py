# _*_ coding: utf-8 _*_
'''
	Author: Lucas Batista Fialho - 2018
	Writen in Python 2. But it can be converted to Python 3 (Easy Way)
	[no guarantees, educational purposes]
	Algoritmo Simplex - Passo A passo
	Simplex Algorithm - Step by step
	INPUT:
		nvar: number of decision variables.
		fo: objective function, it'll receive the coeficients for each decision variables.
		r: restrictions or constraits, they'll be the same way that objective function, but with semicolons for separate each them.  
	OUTPUT:
		result of problem, in text.
'''
MAX = -1
MIN = 1
obj = MAX
nvar = 2
fo = [1,1]
r = [
		[4,1,100],
		[1,1,80],
		[1,0,40]
	]
min_or_max = min if obj == MAX else max

def create_tableau():
	t = []
	nconst = len(r)
	first_line = [1]
	for i in fo:
		first_line.append((obj)*i)
	first_line.extend([0 for i in range(nconst+1)])
	t.append(first_line)
	for pos,c in enumerate(r):
		line = [0]
		line.extend([i for i in c[:-1]])
		line.extend([0 if pos!=i else 1 for i in range(nconst)])
		line.append(c[-1])
		t.append(line)
	return t
def enter_var(table):
	nt = [t*float(obj)*(-1) for t in table[0]]
	minimo = 0
	for i,_ in enumerate(nt):
		if nt[minimo]>nt[i]:
			minimo = i
	return minimo
	
def exit_var(table,enter_pos):
	menor = 0
	list_cand = []
	for i,_ in enumerate(r):
		list_cand.append(table[i+1][-1]/table[i+1][enter_pos])
		'''if(table[i+1][enter_pos]!=0 and (table[i+1][-1]/table[i+1][enter_pos])>0):'''
	sai = list_cand.index(min_or_max(filter(lambda x: x>0 if obj == MAX else x<0,list_cand)))
	return sai+1
def converge(table):
	return not(min_or_max(table[0])<0 if obj == MAX else min_or_max(table[0])>0)			
		
def solve():
	table = create_tableau()
	vb = [i+nvar+1 for i,_ in enumerate(r)]
	print vb
	#enter variable identify
	while not(converge(table)):
		enter_pos = enter_var(table)
		exit_pos = exit_var(table,enter_pos)
		pivot = table[exit_pos][enter_pos]
		nlp = [float(i)/pivot for i in table[exit_pos]]
		ntable = []
		for i,line in enumerate(table):
			if i == exit_pos: 
				ntable.append(nlp)
				continue
			p = table[i][enter_pos]
			nl = [float(i)-(p*nlp[c]) for c,i in enumerate(line)]
			ntable.append(nl)
		vb[exit_pos-1] = enter_pos-1	
		table = ntable
	nvb = {}
	for c,i in enumerate(vb):
		nvb[i] = table[c+1][-1]
		print 'x%d = %.2f'%(i,table[c+1][-1])
	nvb['z'] = table[0][-1]
	print 'z= %.2f'%nvb['z']
	return table,nvb
print solve()
