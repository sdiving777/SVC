from sklearn import svm
import random
import sys
import os
import joblib

if (os.path.exists("svc_test_v2_prepare_files.py")==False):
    print("Need information about arrMetterBits from file svc_test_v2_prepare_files.py")
    sys.exit(0)

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


arrMetterBits = []
fF = open("svc_test_v2_prepare_files.py","r")
for s in fF:
    iP1 = s.find("arrMetterBits")
    iP2 = s.find("[")
    iP3 = s.find("]")
    if (iP1>-1 and iP2>-1):
        for s2 in s[:iP3][iP2+1:].split(","):
            arrMetterBits.append(int(s2))
fF.close()

print(arrMetterBits)


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



# check on test sample   
fF = open("svc_v2_test_file.txt","r") 

arr_arr_Y = []
arr_right_answers = []

for sLine in fF:
    arrTmp = sLine.split(";")
    arrTmp.pop(-1) 

    arr_right_answers.append(int(arrTmp[0]))
        
    arrY = []
    for i in range(1,len(arrTmp)):
        arrY.append(int(arrTmp[i]))
    
    arr_arr_Y.append(arrY)
    
fF.close()



arr_simple_result = []
for arrTmp in arr_arr_Y:
    sTmp = ""
    for i in arrMetterBits:
        sTmp += str(arrTmp[i])
    arr_simple_result.append(hashRL.get(sTmp))
    
    
iOKCntr = 0
iFlCntr = 0
for i in range(len(arr_right_answers)):
    if (arr_simple_result[i]==arr_right_answers[i]):
        #print(" - OK")
        iOKCntr += 1
    else:
        #print(" - FAIL")
        iFlCntr += 1

print("Simple check (Good/Bad):",str(iOKCntr)+"/"+str(iFlCntr))

