file1=open("X_filtered_consensus_epitope_output.txt", "r").readlines()
file2=open("Subclusters_filtered_consensus_epitope_output.txt", "w")
Main_cluster = {}
subclusters= []
Filtered_subclusters = []
#Setting each needed column as a variable
for i in file1:
	columns= i.strip().split("\t")
	cluster_id = columns[0]
	subcluster_id = columns[1]
	sequence = columns[2]
	allele_info = columns[5]
#Check if the line is a main cluster (Consensus)
	if subcluster_id =="Consensus":
		Main_cluster[cluster_id]=sequence
#		print Main_cluster
	else: 
		subclusters.append(i)
#		print subclusters
for j in subclusters:
	column = j.strip().split("\t")
	cluster_ID = column[0]
	alleleinfo = column[5]
#	print alleleinfo
	if cluster_ID in Main_cluster and alleleinfo in Main_cluster[cluster_id]:
		Filtered_subclusters.append(j)
	
#	if subclusters.issubset(Main_clusters):
#		Filtered_subclusters.append(j)
#		Filtered_subclusters.append(i)
#Check if alleles in subcluster match the main cluster
#	if allele_info == Main_cluster.get(cluster_id,""):
#		Filtered_subclusters.append(i)
file2.writelines(Filtered_subclusters)
file2.close()
