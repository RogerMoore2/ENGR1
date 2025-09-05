#/*******************************************************************/
#/                    Engineering 1 Demonstration                   */
#/          Rev 1.0                             2025Sep04           */
#/                                                                  */
#/    This program is a simple program to be used in a lab          */
#/    experiment for Engineering 1.                                 */
#/*******************************************************************/



import utime
from machine import Pin

#/************************* Define I/O pins **************************/

#/**** Digital Outputs*******/

# Define 21 GPIO pins as outputs
pins = [Pin(i, Pin.OUT) for i in range(0, 22)]  # GPIO0–GPIO21

#def write_word(value):
#    for i in range(22):
#        pins[i].value((value >> i) & 1)  # set each bit
#/************ Main Loop ****************/

while True:
#    Start LED flashing sequence
    for LED_Select in range(22):
        pins[LED_Select].value(1)
        utime.sleep_us(1000)
        pins[LED_Select].value(0)
        utime.sleep_us(1)
    for LED_Select in range(22):
        pins[(21-LED_Select)].value(1)
        utime.sleep_us(1000)
        pins[(21-LED_Select)].value(0)
        utime.sleep_us(1)
    

#    print("Done" )
 
