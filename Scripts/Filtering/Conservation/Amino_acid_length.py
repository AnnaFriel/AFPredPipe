file1=open("Fragment_Free_Bufavirus.fasta").readlines()
file2=open("BUV_Conservation_output.fasta", "w")
#result=[]
for i in file1:
	if ">" not in i:
		if len(i) > 569:
			file2.write(i)
