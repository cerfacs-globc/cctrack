import sys

tracks = sys.argv[1]
input_files = open(tracks, "r")                                                              
out = sys.argv[2]
out_file = open(out, 'w+',encoding = 'ascii')

NCyclones = 0

for line in input_files :
	file = line.strip()
 
	sub_input_files = open(file, "r")
	for sub_line in sub_input_files :
		data = sub_line.strip().split(" ")
		data[0] = str( int(data[0]) + NCyclones)
		out_file.write(data[0]+" "+data[1]+" "+data[2]+" "+data[3]+" "+data[4]+" "+data[5]+" "+data[6]+" "+data[7]+" "+data[8]+"\n")
	NCyclones = int(data[0])
	print(NCyclones)
	sub_input_files.close()

input_files.close()
out_file.close()
