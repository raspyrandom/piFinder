from string import digits
from tqdm import tqdm

file=open("digits/pi-billion.txt","r")
writeFile=open("digits/binaryPiBillion.txt","w")
final=""
with tqdm(total=1000000000) as pbar:
    while 1:
        
        # read by character
        char = file.read(1)  
        pbar.update(1)
        if char.isdigit():
            intermidiate=str(bin(int(char)))
            intermidiate=intermidiate.replace("0b","")
            final+=intermidiate
        if not char:
            break
writeFile.write(final)
file.close()