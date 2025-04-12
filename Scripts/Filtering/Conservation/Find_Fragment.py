file1=open("Uniprot_Bufavirus-1.fasta").readlines()
#file2=open("uniprotkb_Cutavirus-1.fasta").readlines()
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
                       #print Fragments			nextline = False
		else:
			not_fragment.append(i)
			nextline =True
			File2.write(i)
	elif nextline:
		File2.write(i)
#		if nextline:
#			if ">" in i:
#				nextline = False
#			else:
#				result.append(i.strip())
#		 
#		if "(Fragment)" not in i:
#			nextline = True	
#print result
#File2.writelines(not_fragment)
#File2.writelines(result)
#	elif nextline:
#		result.append(not_fragment
#		result.append(i)
#		nextline = False
#		File2.writelines(result)

