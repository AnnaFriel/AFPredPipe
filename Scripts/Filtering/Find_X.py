file1=open("filtering_consensus_epitope_output.txt", "r").readlines()
file2=open("X_filtered_consensus_epitope_output.txt","w")
Sequence_X= ""
filtered_id=set()
X_columns = ""
Filtered_lines=[]
for i in file1:
	columns= i.strip().split("\t")
#	print columns[0]
	if "X" in columns[2]:
		Sequence_X= i
		filtered_id.add(columns[0])
#		print Sequence_X
#		file2.write(i)
		X_columns = Sequence_X.strip().split("\t")
#	if X_columns[0] not in file1:
#		file2.write(i)
#		print X_columns[0]
for i in file1:
	columns = i.strip().split("\t")
	if columns[0] not in filtered_id:
		Filtered_lines.append(i)
file2.writelines(Filtered_lines)
file2.close()
#print("File updated")
