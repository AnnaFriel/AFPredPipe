file1=open("Fragment_Free_Bufavirus.fasta").readlines()
file2=open("BUV_Conservation_output.fasta", "w")
file3=open("Fragment_Free_Cutavirus.fasta").readlines()
file4=open("CUV_Conservation_output.fasta", "w")
file5=open("Fragment_Free_Tusavirus.fasta").readlines()
file6=open("TUV_Conservation_output.fasta", "w")
sequence=""
header = ""
for i in file1:
	if ">" in i:
		if len(sequence) >= 569:
			file2.write(header)
			file2.write(sequence + "\n")
		header = i
		sequence =""
	else:
		sequence += i.strip()
if len(sequence)>=569:
	file2.write(header)
	file2.write(sequence + "\n")

cuv_sequence = ""
cuv_header = ""
for j in file3:
	if ">" in j:
                if len(cuv_sequence) >= 569:
                        file4.write(cuv_header)
                        file4.write(cuv_sequence + "\n")
                cuv_header = j
                cuv_sequence =""
        else:
                cuv_sequence += j.strip()
if len(cuv_sequence)>=569:
        file4.write(cuv_header)
        file4.write(cuv_sequence + "\n")

tuv_sequence = ""
tuv_header = ""
for k in file5:
	if ">" in k:
                if len(tuv_sequence) >= 565:
                        file6.write(tuv_header)
                        file6.write(tuv_sequence + "\n")
                tuv_header = k
                tuv_sequence =""
        else:
                tuv_sequence += k.strip()
if len(tuv_sequence)>=565:
        file6.write(tuv_header)
        file6.write(tuv_sequence + "\n")

#print sequence
#print len(sequence)
