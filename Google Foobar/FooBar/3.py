SY2VA = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'A': 10,
         'B': 11,
         'C': 12,
         'D': 13,
         'E': 14,
         'F': 15,
         'G': 16,
         'H': 17,
         'I': 18,
         'J': 19,
         'K': 20,
         'L': 21,
         'M': 22,
         'N': 23,
         'O': 24,
         'P': 25,
         'Q': 26,
         'R': 27,
         'S': 28,
         'T': 29,
         'U': 30,
         'V': 31,
         'W': 32,
         'X': 33,
         'Y': 34,
         'Z': 35,
         'a': 36,
         'b': 37,
         'c': 38,
         'd': 39,
         'e': 40,
         'f': 41,
         'g': 42,
         'h': 43,
         'i': 44,
         'j': 45,
         'k': 46,
         'l': 47,
         'm': 48,
         'n': 49,
         'o': 50,
         'p': 51,
         'q': 52,
         'r': 53,
         's': 54,
         't': 55,
         'u': 56,
         'v': 57,
         'w': 58,
         'x': 59,
         'y': 60,
         'z': 61,
         '!': 62,
         '"': 63,
         '#': 64,
         '$': 65,
         '%': 66,
         '&': 67,
         "'": 68,
         '(': 69,
         ')': 70,
         '*': 71,
         '+': 72,
         ',': 73,
         '-': 74,
         '.': 75,
         '/': 76,
         ':': 77,
         ';': 78,
         '<': 79,
         '=': 80,
         '>': 81,
         '?': 82,
         '@': 83,
         '[': 84,
         '\\': 85,
         ']': 86,
         '^': 87,
         '_': 88,
         '`': 89,
         '{': 90,
         '|': 91,
         '}': 92,
         '~': 93}

def str2int(string, base):
    integer = 0
    for character in string:
        value = SY2VA[character]
        integer *= base
        integer += value
    return integer


def toBase(n,base):
   n = int(n)
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toBase(n//base,base) + convertString[n%base]

table = {}



def answer(n,b):
	counter = 1
	while 1:
		num = n
#		print(num)
		try:
			if table[num] == None:
				table[num] = counter
				counter += 1
			else:
				old_c = table[num]
				break
		except:
			table[num] = counter
			counter += 1
		
		l = len(n)
		a = ''.join(sorted(n))
		ba = a[::-1]
		a = str2int(a,int(b))
		ba = str2int(ba,int(b))
		z = int(ba) - int(a)
		z = str(z)
		z = toBase(z,b)
		z = z.zfill(l)
#		print (str(a) + " " + str(ba) + " " + str(z) +" " +str(l))
		n = z
		
	return counter - old_c
	
print(answer("210111",3))
#print(answer("122221",3))
#print(answer("1211",10))