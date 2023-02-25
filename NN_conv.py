
#  pip3 install keras
#  python3 -m pip install -U pip
#  python3 -m pip install -U setuptools
# apt install nvidia-cuda-toolkit
#  pip3 install tensorflow  



import random
import sys
import joblib
import numpy as np

from keras.models import Sequential
from keras import initializers 
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D


_random_source = open("/dev/random","rb")

def GetBin(the_num,sign_ammount):
    
    
    result_arr = []
    
    #print(the_num,"- ",end="")
    
    for i in range(0,sign_ammount):
        if (the_num&1 == 1):
            result_arr.append(1)
            #print("1",end="")
        else:    
            result_arr.append(0)
            #print("0",end="")
        the_num = the_num>>1
    
    #for i in range(sign_ammount-1,-1,-1):
    #    print (result_arr[i],end="")
    #print("")    
    return result_arr


arrMetterBits = [93,218,230,177]
hashRL = {}
for i in range(2**4):
	if (i>3 and i<12):
		#print("R:",GetBin(i,4))
		sTmp = ""
		for s in GetBin(i,4):
			sTmp += str(s)
		hashRL[sTmp]=0
	else:	
		#print("L:",GetBin(i,4))
		sTmp = ""
		for s in GetBin(i,4):
			sTmp += str(s)
		hashRL[sTmp]=1


fF = open("svc_v2_test_file.txt","r") 

X_arr_check = []
Y_arr_check = []

for sLine in fF:
    arrTmp = sLine.split(";")
    arrTmp.pop(-1) 

    X_arr_check.append(int(arrTmp[0]))
    
    arrY = []
    for i in range(1,len(arrTmp)):
        arrY.append(int(arrTmp[i]))

    Y_arr_check.append(arrY)

fF.close()



fF = open("svc_v2_train_file.txt","r") 

X_arr_train = []
Y_arr_train = []

for sLine in fF:
    arrTmp = sLine.split(";")
    arrTmp.pop(-1) 

    X_arr_train.append(int(arrTmp[0]))
    
    arrY = []
    for i in range(1,len(arrTmp)):
        arrY.append(int(arrTmp[i]))

    Y_arr_train.append(arrY)
    
fF.close()

if (len(X_arr_train)!=len(X_arr_check)):
    print("len(X_arr_train)!=len(X_arr_check)")
    sys.exit(0)



y_train = np.array(Y_arr_train)
x_train = np.array(X_arr_train)

print()
print(y_train.shape)
print(x_train.shape)
print()
print(type(y_train))
print(type(x_train))


y_train = y_train.reshape(y_train.shape[0], y_train.shape[1], 1)


y_check = np.array(Y_arr_check)
x_check = np.array(X_arr_check)
y_check = y_check.reshape(y_check.shape[0], y_check.shape[1], 1)


model = Sequential()
model.add(Conv1D(64, 2, activation="relu", input_shape=(160,1)))
model.add(Dense(16, activation="relu"))
model.add(MaxPooling1D())
model.add(Flatten())
#model.add(Dense(1, activation = 'softmax'))
model.add(Dense(1, activation = 'sigmoid')) 
model.compile(loss = 'binary_crossentropy',optimizer = "adam", metrics = ['accuracy'])
#model.compile(loss = 'sparse_categorical_crossentropy',optimizer = "adam", metrics = ['accuracy'])

#model.summary()

model.fit(y_train, x_train, batch_size=1, epochs=10, verbose=0)

acc = model.evaluate(y_train,x_train)
print("Loss:", acc[0], " Accuracy:", acc[1])


arr_predict_train = model.predict(y_train)


if (len(X_arr_train)!=len(arr_predict_train)):
    print("len(X_arr_train)!=len(arr_predict_train)")
    sys.exit(0)
    
iG = 0
iF = 0
for i in range(len(arr_predict_train)):
    iR = -1
    
    if (arr_predict_train[i]>0.5):
        iR=1
    else:
        iR=0
        
    if (iR==X_arr_train[i]):
        iG += 1
    else:    
        iF += 1

print("Train F/G: "+str(iF)+"/"+str(iG)+" = "+str(iF/iG))        


arr_predict_test = model.predict(y_check)

if (len(X_arr_check)!=len(arr_predict_test)):
    print("len(X_arr_train)!=len(arr_predict_train)")
    sys.exit(0)
    
iG = 0
iF = 0
for i in range(len(arr_predict_test)):
    iR = -1
    
    if (arr_predict_test[i]>0.5):
        iR=1
    else:
        iR=0
        
    if (iR==X_arr_check[i]):
        iG += 1
    else:    
        iF += 1

print("Test F/G: "+str(iF)+"/"+str(iG)+" = "+str(iF/iG))        

#model.save('model_prod_v2.h5')
