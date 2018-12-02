#24 bits
#3 bytes
#take three letters, turn them each into binary, put them all together, then split into 4 parts, then convert them into ___ then output
#Htoo Min
#I'm pretty sure the alphabet variable is pretty much the caveman equivalent of coding
def arrConversion(arr):
	holder = ""
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' 
	for x in arr:
		var1 = int(x[0:6],2)
		var2 = int(x[6:12],2)
		var3 = int(x[12:18],2)
		var4 = int(x[18:24],2)
		holder += (alphabet[var1] + alphabet[var2] + alphabet[var3] + alphabet[var4])
	return holder

def main():
	file = input("Please enter the name of the file: ")
	counter = 0
	holder = ""
	arr = []
	f = open(file+".base64","w")
	with open(file,"rb") as binary_file:
		for line in binary_file:
			for x in line:\
				if (counter % 3 == 0 and counter != 0):
					arr.append(holder)
					if (len(bin(x)[2:]) < 8):
						temp = bin(x)[2:]
						while (len(temp) < 8):
							temp = '0' + temp
						holder=temp
					else:
						holder=bin(x)[2:]
					counter+=1
				else:
					if (len(bin(x)[2:]) < 8):
						temp = bin(x)[2:]
						while (len(temp) < 8):
							temp = '0' + temp
						holder+=temp
					else:
						holder+=bin(x)[2:]
					counter+=1
	f.write(arrConversion(arr))
main()

