def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip()) #將換行符號去除後再加進lines清單
		return lines


def convert(lines):
	new = []
	person = None
	Allen_word_count = 0
	Allen_sticker_count = 0
	Allen_image_count = 0
	Viki_word_count = 0
	Viki_sticker_count = 0
	Viki_image_count = 0
	
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]

		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count += 1
			elif s[2] == '圖片':
				Allen_image_count += 1
			else: 
				for m in s[2:]:
					Allen_word_count += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			elif s[2] == '圖片':
				Viki_image_count += 1
			else :
				for m in s[2:]:
					Viki_word_count += len(m)
	print('Allen說了',Allen_word_count, '個字',)
	print(Allen_sticker_count, '個貼圖')	
	print(Allen_image_count, '個圖片')	
	print('Viki說了', Viki_word_count, '個字')
	print(Viki_sticker_count, '個貼圖')
	print(Viki_image_count,'個圖片')		



	return(new)

def write_file(filename,lines):
		with open(filename, 'w') as f:
			for line in lines:
				f.write(line + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()