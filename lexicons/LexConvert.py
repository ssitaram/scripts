#LDC - Festival format or LDC - Sphinx format
#also add a buckwalter option

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
		print("mult words")
		pron_word = pron_word_mult
	else:
		pron_word = pron_word_mult
	print(native_word+" "+pron_word)
	phoneme_string = ""
	for letter in pron_word:
		if letter != "ay" or letter != "aw":
			mapped_letter = ph_map[letter]
			phoneme_string += " "+mapped_letter
	print(phoneme_string)

OUTS = open("sphinx_dic", "w")		
OUTS.close()

