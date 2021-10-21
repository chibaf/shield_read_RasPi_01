def read_shield():

  import ADS1256
  import RPi.GPIO as GPIO

  ADC = ADS1256.ADS1256()
  ADC.ADS1256_init()
  adcv=[]
  ADC_Value = ADC.ADS1256_GetAll()

  for i in range(8):
    adcv.append(ADC_Value[i]*5.0/0x7fffff)

  GPIO.cleanup()
  return adcv
