file1=open("filtering_consensus_epitope_output.txt", "r").readlines()
file2=open("X_filtered_consensus_epitope_output.txt","w")
Sequence_X= ""
for i in file1:
	if i[2]=="X":
		Sequence_X=i[2]
		file2.write(Sequence_X)
