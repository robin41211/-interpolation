#include <stdio.h>


void adc_convert(int adc_value)
{
    
    
    { float Temp =0;
       

    
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
{adc_convert(792);    ////adc 인풋값 할당
return 0;
}