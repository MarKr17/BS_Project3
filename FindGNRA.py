#script for finding GNRA motive in json file
import json
import re
N=["U","A","C","G"]
R=["A", "G"]
f=open("dssr-data//1s72.json","r")
data=json.loads(f.read())
f.close()

pairs=[]
loops=[]
GNRA=[]
#print(data["pairs"])
for pair in data["pairs"]:
	nt1 = pair["nt1"]
	nt2 = pair["nt2"]
	s=re.search(r'\d+$', nt1)
	x = int(s.group())
	s=re.search(r'\d+$', nt2)
	y = int(s.group())
	if y-x ==5:
		pairs.append(pair)

for pair in pairs:
	nt1 = pair["nt1"]
	nt2 = pair["nt2"]
	#print(pair)
	s=re.search(r'\d+$', nt1)
	x = int(s.group())
	s=re.search(r'\d+$', nt2)
	y = int(s.group())
	chain = nt1[:1]
	loop=[]
	for n in data["nts"]:
		if n["index"] in range(x,y+1):
			loop.append({"index": n["index"], "chain_name": n["chain_name"], "nt_code": n["nt_code"]})
	loops.append(loop)
loops_copy=loops.copy()
for i in range(0, len(loops)):
	chain=loops_copy[i][0]["chain_name"]
	s="{} ".format(loops_copy[i][0]["index"])
	for n in loops_copy[i]:
		if n["chain_name"]!=chain:
			loops.remove(loops_copy[i])
			break
		s+="{}".format(n["nt_code"])
	if len(s)>6:
		s+=" {}".format(loops[i][5]["index"])
		GNRA.append(s)

#for s in GNRA:
#	print(s)

print("----------------------")
gnra=GNRA.copy()
for i in range(0, len(gnra)):
	if gnra[i][6] != "G":
		GNRA.remove(gnra[i])
	elif gnra[i][7] not in N:
		GNRA.remove(gnra[i])
	elif gnra[i][8]not in R:
		GNRA.remove(gnra[i])
	elif gnra[i][9] != "A":
		GNRA.remove(gnra[i])

#print(GNRA[0][9]=="A")


for s in gnra:
	print(s)

#print(loops[5])
#print(GNRA)