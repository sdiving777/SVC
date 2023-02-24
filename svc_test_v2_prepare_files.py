from sklearn import svm
import random
import sys


iRowNum = 1000
iRandBitsNum = 20
iColNum = iRandBitsNum*8

arrMetterBits = [5,22]#,93]#,157] # All numbers must be less then iColNum

for i in arrMetterBits:
    if (i>iColNum):
        print("Numbers in arrMetterBits must be less then iColNum.")
        sys.exit(0)
    
_random_source = open("/dev/random","rb")

def GetBin(the_num,sign_ammount):
    
    result_arr = []
        
    for i in range(0,sign_ammount):
        if (the_num&1 == 1):
            result_arr.append(1)
            #print("1",end="")
        else:    
            result_arr.append(0)
            #print("0",end="")
        the_num = the_num>>1
    
    return result_arr


hashRL = {}
for i in range(2**len(arrMetterBits)):
	if (i>=(2**len(arrMetterBits))/4 and i<((2**len(arrMetterBits))/4+(2**len(arrMetterBits))/2)):
		print("Class 0:",GetBin(i,len(arrMetterBits)))
		sTmp = ""
		for s in GetBin(i,len(arrMetterBits)):
			sTmp += str(s)
		hashRL[sTmp]=0
	else:	
		print("Class 1:",GetBin(i,len(arrMetterBits)))
		sTmp = ""
		for s in GetBin(i,len(arrMetterBits)):
			sTmp += str(s)
		hashRL[sTmp]=1


sTf = "svc_v2_train_file.txt"
fF = open(sTf,"w") 

for isn in range(iRowNum):
    
    rand_bytes = _random_source.read(iRandBitsNum)
    rand_num = int.from_bytes(rand_bytes,"big",signed=False)
    arrBin = GetBin(rand_num,iRandBitsNum*8)

    sTmp = ""
    for i in arrMetterBits:
        sTmp += str(arrBin[i])

    fF.write(str(hashRL.get(sTmp))+";")
    for i in arrBin:
        fF.write(str(i)+";")
    fF.write("\n")

fF.close()

sCf = "svc_v2_test_file.txt"
fF = open(sCf,"w") 

for isn in range(iRowNum):
    
    rand_bytes = _random_source.read(iRandBitsNum)
    rand_num = int.from_bytes(rand_bytes,"big",signed=False)
    arrBin = GetBin(rand_num,iRandBitsNum*8)

    sTmp = ""
    for i in arrMetterBits:
        sTmp += str(arrBin[i])

    fF.write(str(hashRL.get(sTmp))+";")
    for i in arrBin:
        fF.write(str(i)+";")
    fF.write("\n")

fF.close()

print()
print("Created files:")
print("   "+sTf)
print("   "+sCf)


