
import csv
import sys
import re

def savefile(f_addr, w_str):
	fp = open(f_addr, "w")
	fp.write(w_str.encode("utf-8"))
	fp.close()

if __name__ == "__main__":
	cnt = 0;
	offset = 0
	w_str = "MIST32 Instruction Format\r\n==========\r\n\r\n";
	if(len(sys.argv) == 2):
		print("Parameter Error")
		sys.exit()

	fp = open(sys.argv[1], "r")

	for row in csv.reader(fp):
		# escape
		row = [re.sub(r"([\\\`\*\_\{\}\[\]\(\)\#\+\-\.\!])", r"\\\1",
			      i.decode("shift-jis").replace("|", "&#124;"))
		       if i else u" "
		       for i in row]

		if(row[offset+5] != u" "):
			if(cnt == 1):
				w_str = w_str + u"|"
				for i in range(17):
					w_str = w_str + u"---|"
				w_str = w_str + u"\r\n"

			w_str += u"|%s|\r\n" % (u"|".join(row[:17]))
			cnt = cnt + 1

	fp.close()

	savefile(sys.argv[2], w_str)
	print(str(cnt) + " Instructions")
	print("done.")
