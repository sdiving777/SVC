#  pip3 install keras
#  python3 -m pip install -U pip
#  python3 -m pip install -U setuptools
# apt install nvidia-cuda-toolkit
#  pip3 install tensorflow  



import random
import sys
import joblib

from keras.models import Sequential
from keras import initializers 
from keras.layers import Dense


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


model = Sequential()
model.add(Dense(len(Y_arr_train[0]), input_dim=len(Y_arr_train[0]), activation='relu')) 
model.add(Dense(4, activation='relu')) 
#model.add(Dense(256, activation='relu')) 
#model.add(Dense(256, activation='relu')) 
#model.add(Dense(256, activation='relu')) 
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])




bGood = False

while (bGood!=True):
    
    model.fit(Y_arr_train, X_arr_train, epochs=10, batch_size=len(X_arr_train), verbose=0)

    # Prediction
    arr_predict = model.predict(Y_arr_check)

    if (len(arr_predict)!=len(X_arr_check)):
        print("len(arr_predict)!=len(X_arr_check)")
        sys.exit(0)

    iOK_train = 0
    iFl_train = 0
    for i in range(len(arr_predict)):
        iR = -1
        if (arr_predict[i][0]<0.5):
            iR = 0
        else:
            iR = 1

        if (iR==X_arr_train[i]):
            iOK_train += 1
        else:
            iFl_train += 1

        if (iR<0):
            print("iR<0")
            sys.exit(0)

    if (iFl_train==0):
        bGood=True
        
    print()
    print("check: "+str(iFl_train)+"/"+str(iOK_train))
    print()
    
    

#model.save('model_prod_v2.h5')

