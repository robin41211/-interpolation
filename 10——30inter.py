31.0546#############################  2개 점으로 보간 10~30도
def temp1(x1):
    
    # y=0.1012*x-9.2618-10.666            ######-10~10
    y1 = 0.0826*x1 - 12.302       
    print(y1)  
                                       


 ############################  20~30도
def temp2(x2):
    
    y2 =0.0632*x2-4.7166    
                                 
    print(y2)
  


    

# plt.plot(x,y)
# plt.show()
temp1(270)
temp1(391)

temp2(391)
temp2(566)

