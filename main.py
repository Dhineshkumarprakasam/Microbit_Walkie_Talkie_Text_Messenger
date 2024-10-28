def encode(message: str):
    global shift_amount, encoded_message2
    shift_amount = len(message)
    for char in message:
        if char_list.index_of(char) >= 0:
            position = char_list.index(char)
            new_position = (position + shift_amount) % len(char_list)
            encoded_message2 = "" + encoded_message2 + char_list[new_position]
        else:
            encoded_message2 = "" + encoded_message2 + char
    return encoded_message2
def decode(encoded_message: str):
    global shift_amount, decoded_message
    shift_amount = len(encoded_message)
    for char2 in encoded_message:
        if char_list.index_of(char2) >= 0:
            position2 = char_list.index(char2)
            new_position2 = (position2 - shift_amount) % len(char_list)
            decoded_message = "" + decoded_message + char_list[new_position2]
        else:
            decoded_message = "" + decoded_message + char2
    return decoded_message

def on_button_pressed_a():
    global index
    index += 1
    basic.show_string("" + (characters[index]))
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function():
    global characters, index
    if characters == alphabets:
        characters = numbers
        index = 0
    else:
        characters = alphabets
        index = 0
    basic.show_icon(IconNames.YES)
buttonClicks.on_button_held(buttonClicks.AorB.B, my_function)

def on_received_string(receivedString):
    global msg, encoded_message2, encoded_message22, decoded_message, decoded_message2, index
    basic.show_icon(IconNames.HAPPY)
    basic.pause(1000)
    basic.clear_screen()
    basic.show_string("" + (decode(receivedString)))
    basic.pause(100)
    basic.clear_screen()
    msg = ""
    encoded_message2 = ""
    encoded_message22 = ""
    decoded_message = ""
    decoded_message2 = ""
    index = 0
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global index
    index = abs((index + -1) % len(characters))
    basic.show_string("" + (characters[index]))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global msg, encoded_message2, encoded_message22, decoded_message, decoded_message2, index
    radio.send_string("" + (encode(msg)))
    basic.show_icon(IconNames.YES)
    msg = ""
    encoded_message2 = ""
    encoded_message22 = ""
    decoded_message = ""
    decoded_message2 = ""
    index = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def my_function2():
    basic.clear_screen()
    basic.pause(200)
    basic.show_string("=" + msg)
buttonClicks.on_button_double_clicked(buttonClicks.AorB.B, my_function2)

def my_function3():
    global msg, index
    msg = "" + msg + characters[index]
    index = 0
    basic.clear_screen()
buttonClicks.on_button_held(buttonClicks.AorB.A, my_function3)

index = 0
decoded_message = ""
encoded_message2 = ""
characters = ""
alphabets = ""
numbers = ""
shift_amount = 0
char_list: List[str] = []
msg = ""
encoded_message22 = ""
decoded_message2 = ""
decoded_message2 = ""
encoded_message22 = ""
msg = ""
char_list = ["A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"]
shift_amount = 3
numbers = " 0123456789"
alphabets = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = alphabets
radio.set_group(1)