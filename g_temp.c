#include <stdio.h>


void adc_convert()
{

  int adc_value[4096];
  for (int i=0;i<4096;i++)
    {adc_value[i]=i;                            ////adc 값 0~4095까지 배열 
    }
    // printf("%d\n",adc_value[2]);                 값 확인
    for(int j=0;j<1000;j++)
    { float Temp =0;
  if (0<=adc_value[j]<187)
  {
    Temp =0.1887*adc_value[j]-35.292;
    printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value[j],Temp);

  }
  else if (187<=adc_value[j]<270)
  {
    Temp=0.1205*adc_value[j]-22.53;
    printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value[j],Temp);
  }
  else if (270<=adc_value[j]<391)
  {
    Temp=0.0826*adc_value[j]-12.302;
    printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value[j],Temp);
  }
  else if (391<=adc_value[j]<566)
  {
    Temp=0.0632*adc_value[j]-4.7166;
    printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value[j],Temp);
  }
  else if (566<=adc_value[j]<1078)
  {
    Temp=0.0373*adc_value[j] + 9.9049;
    printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value[j],Temp);
  }
  else if (1078<=adc_value[j]<4095)
  {
    Temp=(0.029*adc_value[j]+ 22.412-3.55);
    printf("ADC_VALUE: %d, TEMP: %.2f\n",adc_value[j],Temp);
  }
  else
  {

  } 
    
    }
    }
int main()
{adc_convert();
return 0;
}