from lib.mylib import loadData

def look_and_say(seq: str) -> str:
	result = []
	n = 1
	c = seq[0]
	for i in range(1, len(seq)):
		if seq[i] == c:
			n += 1
		else:
			result.append(f'{n}{c}')
			n = 1
			c = seq[i]
	result.append(f'{n}{c}')
	return ''.join(result)

def main():
	txt = loadData()
	print(txt)
	for i in range(40):
		txt = look_and_say(txt)
	print("\nPart 1")
	print(txt)
	print(len(txt))

	for i in range(10):
		txt = look_and_say(txt)
	print("\nPart 2")
	print(len(txt))


if __name__ == "__main__":
	main()
