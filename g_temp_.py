import time
x=list(range(4096))
y=[]
for adc_value in range(4096):               #############################x,y list(array처리)
    if 0<=adc_value<187 :
                Temp =0.1887*adc_value-35.292
                y.append(Temp)
                
    elif 187<=adc_value<270 :
                Temp=0.1205*adc_value-22.53
                y.append(Temp)
                
    elif 270<=adc_value<391 :
                Temp=0.0826*adc_value-12.302
                y.append(Temp)
    elif 391<=adc_value<566 :
                Temp=0.0632*adc_value-4.7166
                y.append(Temp)
    elif 566<=adc_value<1078:
                Temp=0.0373*adc_value+9.9049
                y.append(Temp)
    elif 1078<=adc_value<4096 :
                Temp=0.029*adc_value + 22.412-3.55
                y.append(Temp)
    
    else:
         pass
###############################x,y list(array처리)
print(type(x))              #### x(adc)값 0~4095 리스트 타입 확인
print(type(y))              #### y(temp)값 리스트 타입 확인
print(len(x))               #### list(x)안 int 갯수 확인
print(len(y))               #### list(y)안 float 갯수 확인 //list(y)와 갯수 동일 하여야 함



def convert_temp(adc_value):                                    ######### adc값을 변수로 결과값으로 adc,온도 print

        if 0<=adc_value<187 :
                Temp =0.1887*adc_value-35.292
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m') 
                time.sleep(0.5)
        elif 187<=adc_value<270 :
                Temp=0.1205*adc_value-22.53
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
                time.sleep(0.5)
        elif 270<=adc_value<391 :
                Temp=0.0826*adc_value-12.302
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
                time.sleep(0.5)    
        elif 391<=adc_value<566 :
                Temp=0.0632*adc_value-4.7166
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
                time.sleep(0.5)
        elif 566<=adc_value<1078 :
                Temp=0.0373*adc_value + 9.9049
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
                time.sleep(0.5)
        elif 1078<=adc_value<4095 :
                Temp=0.029*adc_value + 22.412-3.55
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
                time.sleep(0.5)
        else: ValueError
    
            

for i in x:
    convert_temp(i)

# while True:
#     convert_temp(adc_value)