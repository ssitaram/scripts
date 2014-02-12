#LDC - Festival format or LDC - Sphinx format
#option to either read from a mapping file or convert to buckwalter
#option to convert to festival format or sphinx format
#option to generate phoneset file

LEX = open("../data/ar_lex.utf8")
lex = LEX.read()
LEX.close()

#word in native script
NATIVE_FIELD = 2

#prounciation of word
PRON_FIELD = 3

#morphological decomposition of word
#MORPH_FIELD = 4


OUTF = open("festival_lex", "w")
OUTF.close()

PHONE_MAP = open("phone_table", "r")
ph_map_file = PHONE_MAP.read()
PHONE_MAP.close()

ph_map = {}

for line in ph_map_file.split("\n")[1:-1]:
	mapped = line.split("\t")[0]
	orig = line.split("\t")[1]
	ph_map[orig] = mapped

print(ph_map)

for line in lex.split("\n")[:-1]:
	native_word = line.split("\t")[NATIVE_FIELD-1]
	pron_word_mult = line.split("\t")[PRON_FIELD-1]
	if pron_word_mult.find("/") != -1:
		#for cases when the lexicon has two or more pronunciations for the word
		#print("mult words")
		pron_word = pron_word_mult.split("//")
	else:
		pron_word = [pron_word_mult]
	for pw in pron_word:
		#print(native_word+" "+pw)
		phoneme_string = ""
		for letter in pw:
			if letter != "ay" or letter != "aw":
				try:
					mapped_letter = ph_map[letter]
					phoneme_string += " "+mapped_letter
				except KeyError:
					print("Key not found for "+letter)
					#fix for Egyptian, may be wrong
					if letter == "B":
						mapped_letter = "B"
						phoneme_string += " "+mapped_letter
		#print(phoneme_string)
		OUTF = open("festival_lex", "a")
		OUTF.write(native_word+" "+phoneme_string[1:]+"\n")
		OUTF.close()
OUTS = open("sphinx_dic", "w")		
OUTS.close()

