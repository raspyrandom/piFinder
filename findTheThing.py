

loading={
    "interval": 100,
    "frames":["3",".","1","4"]
}
pinary=open("digits/binaryPi.txt","r")
pinary=pinary.read()
num=input("how many characters: ")
location=input("what location to start at: ")
string=""

for i in range(int(num)):
    string+=pinary[int(location)+i]

print(string)