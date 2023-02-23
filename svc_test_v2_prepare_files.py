from sklearn import svm
import random
import sys

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


arrMetterBits = [93,218,230,177] # Just random numbers
hashRL = {}
for i in range(2**4):
	if (i>3 and i<12):
		sTmp = ""
		for s in GetBin(i,4):
			sTmp += str(s)
		hashRL[sTmp]=0
	else:	
		sTmp = ""
		for s in GetBin(i,4):
			sTmp += str(s)
		hashRL[sTmp]=1


fF = open("svc_v2_train_file.txt","w") 

for isn in range(108*5):
    
    rand_bytes = _random_source.read(128)
    rand_num = int.from_bytes(rand_bytes,"big",signed=False)
    arrBin = GetBin(rand_num,1024)

    sTmp = ""
    for i in arrMetterBits:
        sTmp += str(arrBin[i])

    fF.write(str(hashRL.get(sTmp))+";")
    for i in arrBin:
        fF.write(str(i)+";")
    fF.write("\n")

fF.close()

fF = open("svc_v2_test_file.txt","w") 

for isn in range(108*5):
    
    rand_bytes = _random_source.read(128)
    rand_num = int.from_bytes(rand_bytes,"big",signed=False)
    arrBin = GetBin(rand_num,1024)

    sTmp = ""
    for i in arrMetterBits:
        sTmp += str(arrBin[i])

    fF.write(str(hashRL.get(sTmp))+";")
    for i in arrBin:
        fF.write(str(i)+";")
    fF.write("\n")

fF.close()

