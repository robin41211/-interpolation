#include <stdio.h>
void adc_convert()
{
//   int adc_value[4096];
//   for (int i=0;i<4096;i++)
//     {adc_value[i]=i;                            //adc 값 0~4095까지 배열 
//     }
//     printf("%d\n",adc_value[1079]);                // 값 확인  adc 1078일때 50.12
  
    
    for(int j=0;j<4096;j++)
    { float Temp =0;
       int adc_value= j;                    //실험을 위한 adc 0~4095까지 온도 값 확인 

    
        if (adc_value<187)
        {
        Temp =0.1887*adc_value-35.292;
        printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value,Temp);
        
        }
        else if (adc_value<270)
        {
        Temp=0.1205*adc_value-22.53;
        printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value,Temp);
        }
        else if (adc_value<391)
        {
        Temp=0.0826*adc_value-12.302;
        printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value,Temp);
        }
        else if (adc_value<566)
        {
        Temp=0.0632*adc_value-4.7166;
        printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value,Temp);
        }
        else if (adc_value<1078)
        {
        Temp=0.0373*adc_value+ 9.9049;
        printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value,Temp);
        }
        else if (adc_value<4096)
        {
        Temp=(0.029*adc_value+ 22.412-3.55);
        printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value,Temp);
        }
        else
        { printf("Value Error");

        } 
    
    }
}
    
int main()
{adc_convert();
return 0;
}