import csv
import sys
import codecs


def savefile(f_addr, w_str):
	fp = open(f_addr, "w")
	fp.write(w_str)
	fp.close()

if __name__ == "__main__":
	cnt = 0;
	offset = 0
	w_str = "MIST32 Instruction Format\r\n==========\r\n\r\n";
	if(len(sys.argv) == 2):
		print("Parameter Error")
		sys.exit()

	fp = open(sys.argv[1])
	#fp = codecs.open(sys.argv[1], 'r', 'ascii')
	
	for row in csv.reader(fp):
		if(row[offset+5] != ""):
			if(cnt == 1):
				w_str = w_str + "|"
				for i in range(17):
					w_str = w_str + "---|"
				w_str = w_str + "\r\n"

			w_str = w_str + "|" + row[offset]
			w_str = w_str + "|" + row[offset+1]
			w_str = w_str + "|" + row[offset+2]
			w_str = w_str + "|" + row[offset+3]
			w_str = w_str + "|" + row[offset+4]
			w_str = w_str + "|" + row[offset+5]
			w_str = w_str + "|" + row[offset+7]
			w_str = w_str + "|" + row[offset+8]
			w_str = w_str + "|" + row[offset+9]
			w_str = w_str + "|" + row[offset+10]
			w_str = w_str + "|" + row[offset+11]
			w_str = w_str + "|" + row[offset+12]
			w_str = w_str + "|" + row[offset+13]
			w_str = w_str + "|" + row[offset+14]
			w_str = w_str + "|" + row[offset+15]
			w_str = w_str + "|" + row[offset+16]
			w_str = w_str + "|\r\n"
			cnt = cnt + 1

	savefile(sys.argv[2], w_str)
	print(str(cnt) + " Instructions")
	print("done.")
