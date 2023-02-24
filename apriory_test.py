from apriori_python import apriori


fF = open("svc_v2_train_file.txt","r") 

Y_arr_train = []

for sLine in fF:
    arrTmp = sLine.split(";")
    arrTmp.pop(-1) 

    
    arrY = []
    for i in range(1,len(arrTmp)):
        if (int(arrTmp[i])==1):
            arrY.append(str(i))

    Y_arr_train.append(arrY)
    
fF.close()


freqItemSet, rules = apriori(Y_arr_train, minSup=<>, minConf=<>) 
for i in rules:
	print(i)

	
	
