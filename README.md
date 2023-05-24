# PiCo Bibberdraad Workshop

Tutorial for Raspberry Pi Pico 2040 workshops.
Workshop is (for now) only available in Dutch.


Tips:
- De aanraakdraad is verbonden met GND, het handigste is die draad ca 1,5 cm te strippen, voor te solderen, dan om de aanraakdraad te buigen en dan nogmaals te solderen zodat het voldoende contact maakt.
- Bordjes zijn van MDF, 3mm boorgat voor 3mm dik draad.
- Aluminium (meer soepel) en gegalvaniseerd (stugger) draad geleid goed. Die kleurtjes van het aluminium draad zijn leuk maar geleiden niet dus moeten eerst geschuurd worden, blank draad werkt op zich beter / levert minder werk op.
- Om ene paaltje heen zit zelfklevend kopertape, daar soldeer je de 'eindsensordraad' aan vast, wel uitkijken dat de PLA (3D print plastic) niet smelt.
- Er waren vier bordjes die niet correct werkten (waren toevallig afwijkend), die waren normally closed ipv normally open, "return nieuwSpelKnopPin.value() == 0" moest "return nieuwSpelKnopPin.value() == 1" worden en toen deed ie het ook voor die leerlingen, leerzaam weer met name voor de leerlingen.
- Leerlingen hadden twee verbeteringen: batterijhouder vertikaal erop lijmen met hot glue én de nieuwe-spel-knop aan zijkant van bordje, dat maakt het geheel meer robuust. Zorg wel dat de USB vrij blijft voor eventueel herprogrammeren. (zie ook: https://github.com/jakorten/pico_tutorial/blob/main/resultaat_leerling.png)

# Stand-alone

Stand-alone maken (dus zonder computer) is beetje gedoe. Sla bestand op als main.py en kopieer het dan naar je bordje. Op de Mac doe je dit als volgt:

rshell --buffer-size=30 -p /dev/tty.usbmodem21301

(usbmodemxxxxx naam kan iets afwijken).

Daarna:

cp main.py /pyboard/

Doe dit vanaf de folder waar je main.py bestand staat.