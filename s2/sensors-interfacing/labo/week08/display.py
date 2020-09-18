#pylint: skip-file
from RPi import GPIO as io
import time

rs = 21
e = 20
# a) Stop alle 8 de databits in de correcte volgorde in een list.
databits = [13, 19, 26, 23, 24, 25, 12, 16]

def setup():
    io.setwarnings(False)
    io.setmode(io.BCM)
    # b) Initialiseer alle GPIO pinnen.
    io.setup(rs, io.OUT)
    io.setup(e, io.OUT)
    for bit in databits:
        io.setup(bit, io.OUT)
    init_LCD()
        
# d) Schrijf de send_instruction(value).
def send_instruction(value):
    #rs laag: voor instruction
    io.output(rs, io.LOW)
    #enable hoog
    io.output(e, io.HIGH)
    set_data_bits(value)
    #enable terug laag
    io.output(e, io.LOW)
    time.sleep(0.01)

# e) Schrijf de send_character(value).
def send_character(character):
    #rs hoog: voor data
    io.output(rs, io.HIGH)
    #enable hoog
    io.output(e, io.HIGH)
    #data klaarzetten
    set_data_bits(character)
    #enable laag
    io.output(e, io.LOW)
    #wait
    time.sleep(0.2)

# c) Schrijf de set_data_bits(value).
def set_data_bits(byte):
    mask = 0x80
    for i in range(8):
        io.output(databits[i], byte & (mask >> i))


# i) Schrijf een def write_message(message).
def write_message(message):
    for char in message[0:16]:
        send_character(ord(char))
    for char in message[16:]:
        move_screen()
        send_character(ord(char))

# f) Schrijf een init_LCD()
def init_LCD():
    # set datalengte op 8 bit (= DB4 hoog), 2 lijnen (=DB3), 5x7 display (=DB2).
    send_instruction(0b00111000)
    # display on (=DB2), cursor on (=DB1), blinking on (=DB0)
    send_instruction(0b00001111)
    # clear display en cursor home (DB0 hoog)
    send_instruction(0b00000001)

def set_cursor(row, col):
    # byte maken: row (0 of 1) = 0x0* voor rij 0 of 0x4* voor rij 1. col = 0x*0 - 0x*F 
    byte = row << 6 | col
    # byte | 128 want DB7 moet 1 zijn
    send_instruction(byte | 128)

def move_screen():
    send_instruction(0b00011000)

if __name__ == "__main__":
    try:
        setup()
        #write_message("Hello World!")
        #send_instruction(0b11000000)
        write_message("Hello World!Hello World2")
        
        write_message("test")

        #set_cursor(0, 0xF)
        
        # j) Vraag een input van de gebruiker.
        #message = input("Choose a string to display: ")
        #write_message(message)
            
    except KeyboardInterrupt as e:
        print("quitting...")
        
