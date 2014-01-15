default: make_md

make_md:
	python instructions/csv2md.py instructions/mist32_isa.csv instructions.md

	