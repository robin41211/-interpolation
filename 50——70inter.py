
#############################  3개 점으로 보간, 50~70
def temp1(x1):
    
   
    y1 = 0.029*x1 + 22.412-3.55     
    print(y1)


temp1(1078)     ####50도
temp1(1408)     ####60도
temp1(1767)     ####70도
temp1(4095)     ####adc 마지막 값
