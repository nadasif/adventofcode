import re

from lib.mylib import loadData

def is_valid(password: str) -> bool:
	if re.match(r'i|o|l', password):
		return False
	#if re.match():

def main():
	txt = loadData()
	print(txt)
	print("\nPart 1")
	print(is_valid(txt))
	
	print("\nPart 2")


if __name__ == "__main__":
	main()
