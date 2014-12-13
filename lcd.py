import lcddriver
from time import *

lcd = lcddriver.lcd()

# lcd.lcd_clear();
lcd.lcd_display_string("A Mama sprzata", 1)
lcd.lcd_display_string("Ha ha ha", 2)