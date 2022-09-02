filename=input("filename(input): ")

filename="input/"+filename
filename2="digits/binarypi.txt"

file=open(filename,"r")
binaryFile=open(filename2,"r")
file2=file.read()

search=file2.replace("\n","")
pinary=binaryFile.read()
print(pinary.find(search))
