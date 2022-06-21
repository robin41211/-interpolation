def convert_temp(adc_value):                                    ####### adc값을 변수로 결과값으로 adc,온도 print


    while True:
        if 0<=adc_value<187 :
                Temp =0.1887*adc_value-35.292
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')        
        elif 187<=adc_value<270 :
                Temp=0.1205*adc_value-22.53
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
        elif 270<=adc_value<391 :
                Temp=0.0826*adc_value-12.302
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')    
        elif 391<=adc_value<566 :
                Temp=0.0632*adc_value-4.7166
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
        elif 566<=adc_value<1078 :
                Temp=0.0373*adc_value + 9.9049
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
        elif 1078<=adc_value<4095 :
                Temp=0.029*adc_value + 22.412-3.55
                print('\033[91m'+"ADC_value(mv):"+str(adc_value)+","+"Temp(C):"+str(Temp)+ '\033[0m')
                  
        else: ValueError
                

while True:
    convert_temp(1)

