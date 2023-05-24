# Gebruikte Bibliotheken:

import time
from machine import Pin, PWM, ADC

# Algemene Instellingen

buzzerPin = 16 # GP16
Buzzer=PWM(Pin(buzzerPin))

groeneLED = Pin(1, Pin.OUT)
geleLED = Pin(5, Pin.OUT)
rodeLED = Pin(9, Pin.OUT)

aanraakDraadMeetPin = ADC(26) # GP26 analoge input
nieuwSpelKnopPin = Pin(17, Pin.IN, Pin.PULL_UP) # GP17
spelGehaaldSensorPin = Pin(18, Pin.IN, Pin.PULL_DOWN) # GP18

# Pin.PULL_UP trekt de draad standaard naar VIN / 3.3V
# Pin.PULL_DOWN trekt de draad standaard naar VIN / 3.3V
# Werkt hetzelfde als de 10kOhm weerstand uit het schema (die zit op 3.3V dus is PULL-UP)


# Variabelen waarmee we waardes bij kunnen houden.

conversion_factor = 3.3/(65536) # hiermee verdelen we 3.3V voltage bereik over 16-bit resolutie (advanced stuff x§§:))

kerenAangeraaktTeller = 0 # Teller hoe vaak de bibberdraad met het stokje is aangeraakt 
letopMaxBibbers = 5 # Na hoe veel bibbers krijg je penalty?
feestjeMaxBibbers = 10 # Na hoe veel bibbers heb je verloren?

geluidsFrequentie = 440 # frequentie in Hertz van de buzzer (midden C = 440)

# Een aantal muzieknoten:

notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
    'D5': 587.33,
    'E5': 659.26,
    'G3': 196.00
}

# Vader Jakob

song = [
    (notes['C4'], 0.5),    # C4 - 0.5 seconde
    (notes['D4'], 0.5),    # D4 - 0.5 seconde
    (notes['E4'], 0.5),    # E4 - 1 seconde (langere duur voor "Slaapt gij nog?")
    (notes['C4'], 0.5),    # C4 - 0.5 seconde
    (notes['C4'], 0.5),    # C4 - 0.5 seconde
    (notes['D4'], 0.5),    # D4 - 0.5 seconde
    (notes['E4'], 0.5),    # E4 - 1 seconde (langere duur voor "Slaapt gij nog?")
    (notes['C4'], 0.5),    # C4 - 0.5 seconde

    (notes['E4'], 0.5),    # E4 - 0.5 seconde
    (notes['F4'], 0.5),    # F4 - 0.5 seconde
    (notes['G4'], 1.0),    # G4 - 1 seconde (langere duur voor "Slaapt gij nog?")
    (notes['E4'], 0.5),    # E4 - 0.5 seconde
    (notes['F4'], 0.5),    # F4 - 0.5 seconde
    (notes['G4'], 1.0),    # G4 - 1 seconde (langere duur voor "Slaapt gij nog?")
    
    (notes['G4'], 0.5),    # G4 - 0.5 seconde
    (notes['A4'], 0.5),    # A4 - 0.5 seconde
    (notes['G4'], 0.5),    # G4 - 0.5 seconde
    (notes['F4'], 0.5),    # F4 - 0.5 seconde
    (notes['E4'], 0.5),    # E4 - 0.5 seconde
    (notes['C4'], 0.5),    # C4 - 0.5 seconde
    
    (notes['G4'], 0.5),    # G4 - 0.5 seconde
    (notes['A4'], 0.5),    # A4 - 0.5 seconde
    (notes['G4'], 0.5),    # G4 - 0.5 seconde
    (notes['F4'], 0.5),    # F4 - 0.5 seconde
    (notes['E4'], 0.5),    # E4 - 0.5 seconde
    (notes['C4'], 0.5),    # C4 - 0.5 seconde
    
    (notes['C4'], 0.5),    # E4 - 0.5 seconde
    (notes['G3'], 0.5),    # G4 - 0.5 seconde
    (notes['C4'], 1.0),
    (notes['C4'], 0.5),    # E4 - 0.5 seconde
    (notes['G3'], 0.5),    # G4 - 0.5 seconde
    (notes['C4'], 1.0)
]

# Helper functies:

def play_note(frequency, duration):
    Buzzer.duty_u16(512)  # Adjust the duty cycle to control the volume
    Buzzer.freq(int(frequency))
    time.sleep(duration)
    Buzzer.duty_u16(0)  # Stop the sound

def speelVaderJakob():
    # Play the song
    for note in song:
        play_note(note[0], note[1])
        time.sleep(0.1)  # Add a small delay between notes

def isDraadAangeraakt():
    meetwaarde = aanraakDraadMeetPin.read_u16() * conversion_factor
    time.sleep(0.01)
    return (meetwaarde < 0.5) # als we GND meten (bibberdraad is aangesloten op GND)

def buzzerAan():
    Buzzer.duty_u16(int(65536*0.2))
    Buzzer.freq(geluidsFrequentie)

def buzzerUit():
    Buzzer.duty_u16(int(65536*0))

def nieuwSpelKnopjeGedrukt():
    global kerenAangeraaktTeller
    return nieuwSpelKnopPin.value() == 0

def spelGehaald():
    return spelGehaaldSensorPin.value() == 1


def vierFeestje():
    # hier kun je leuke geluiden en LED effecten uitvoeren!
    print()
    print("Hoera!!! Tijd voor een feestje!")

def zetLEDAan(ledPin):
    ledPin.value(1)

def zetLEDUit(ledPin):
    ledPin.value(0)

def misschienTijdVoorFeestje():
    global kerenAangeraaktTeller
    if (kerenAangeraaktTeller < feestjeMaxBibbers):
        vierFeestje()
        
def zetStoplicht(keerAangeraakt):
    if(keerAangeraakt < letopMaxBibbers):
        alleenLEDAan(groeneLED)
    else:
        if(keerAangeraakt < feestjeMaxBibbers):
            alleenLEDAan(geleLED)
        else:
            if(keerAangeraakt == feestjeMaxBibbers):
                buzzerAan()
                time.sleep(0.5)
                buzzerUit()
                time.sleep(0.5)
                buzzerAan()
            alleenLEDAan(rodeLED)
            
def alleenLEDAan(ledAan):
    zetLEDUit(groeneLED)
    zetLEDUit(geleLED)
    zetLEDUit(rodeLED)
    zetLEDAan(ledAan)
        
# Hoofdfuncties:

def detecteerBibbers():
    global kerenAangeraaktTeller
    
    if (isDraadAangeraakt()):
      kerenAangeraaktTeller = kerenAangeraaktTeller + 1
      buzzerAan()
      
      while(isDraadAangeraakt()): # hiermee zorgen we dat een aanraking maar een keer telt!
          time.sleep(0.1)
          
      buzzerUit()  
      print("Aangeraakt: " + str(kerenAangeraaktTeller) + "x")
      
      zetStoplicht(kerenAangeraaktTeller)

def stelBibberTellerOpnieuwIn():
    global kerenAangeraaktTeller
    print("Reset")
    kerenAangeraaktTeller = 0 # we stellen de teller opnieuw in
    buzzerUit()
    
def beginNieuwSpel():
    stelBibberTellerOpnieuwIn()
    alleenLEDAan(groeneLED)
    print("Je mag nu beginnen!")
    print()
      
def leesNieuwSpelKnopje():
    if (nieuwSpelKnopjeGedrukt()):
      beginNieuwSpel()
      stelBibberTellerOpnieuwIn()
      
      while(nieuwSpelKnopjeGedrukt()): # hiermee zorgen we dat spel niet steeds opnieuw start!
          time.sleep(1) # heel ff wachten

def controleerSpelGehaald():
    if (spelGehaald()):
      print()
      print("Super! Je hebt het spel gehaald!")
      print("Keer geraakt: " + str(kerenAangeraaktTeller) + "x")
            
      while(spelGehaald()): 
          time.sleep(1) # ff wachten zodat spel niet te snel opnieuw start!
      
      beginNieuwSpel()
      speelVaderJakob()


# Hoofdprogramma

beginNieuwSpel() # begin nieuw spel

while True:
  
  detecteerBibbers()  
  leesNieuwSpelKnopje()
  controleerSpelGehaald()
          
Buzzer.deinit()
  


