#Required Libraries
from machine import Pin, ADC 
import utime 
 
#Initialize Prepherials
POT_Value = ADC(26) 
conversion_factor = 3.3/(65536)

keren_aangeraakt = 0

  
def isDraadAangeraakt():
    meetwaarde = POT_Value.read_u16() * conversion_factor
    return (meetwaarde < 0.5)
 
#Main Application loop 
while True: 
  utime.sleep(0.1)
  
  if (isDraadAangeraakt()):
      keren_aangeraakt += 1
      
      while(isDraadAangeraakt()):
          utime.sleep(0.1)
      
      print("Aangeraakt: " + str(keren_aangeraakt) + "x")
  
