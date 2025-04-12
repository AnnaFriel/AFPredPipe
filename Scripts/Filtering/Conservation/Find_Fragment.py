#If the term fragment is found the sequence is removed
file1=open("Uniprot_Bufavirus-1.fasta").readlines()
File2=open("Fragment_Free_Bufavirus.fasta", "w")
not_fragment=[]
Fragments = []
nextline = False
result = []
rows =[]
for i in file1:
	if ">" in i:
		if "(Fragment)" in i:
			Fragments.append(i)
			nextline = False
		else:
			not_fragment.append(i)
			nextline =True
			File2.write(i)
	elif nextline:
		File2.write(i)


