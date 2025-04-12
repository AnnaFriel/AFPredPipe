file1=open("./filtering_consensus_epitope_input.txt", "r").readlines()
file2=open("./filtering_consensus_epitope_output.txt", "w")
flag1=0
pred=[]
clust_numb=[]
#setting a for loop to look for the word Consensus in column 2
for i in range (0, len(file1)):
	if file1[i].split("\t")[1] == "Consensus":
# if Consensus is there flag is equal to 1
		flag1=flag1+1
# If Consensus is there the list pred will be appended with column 5 which is separated by tabs
	if flag1==1:
		pred.append(file1[i].split("\t")[5].split()[0])
# If we reach another Consnsus or a Singleton
	if flag1==2 or file1("\t")[1]=="Singleton":
		if "-" in pred:
			pred.remove("-")
		pred=list(set(pred))
		if len(pred)>1:
			clust_numb.append(file1[i-1].split("\t")[0])
		flag=1
		pred=[]
file2.write(file1[0])
for j in clust_numb:
	for k in file1:
		if j.strip()==k.split("\t")[0].strip():
		file2.write(k.strip()+"\n")
