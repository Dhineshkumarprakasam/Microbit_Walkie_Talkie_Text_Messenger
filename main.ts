function encode (message: string) {
    let position: number;
let new_position: number;
shift_amount = message.length
    for (let char of message) {
        if (char_list.indexOf(char) >= 0) {
            position = _py.py_array_index(char_list, char)
new_position = (position + shift_amount) % char_list.length
            encoded_message2 = "" + encoded_message2 + char_list[new_position]
        } else {
            encoded_message2 = "" + encoded_message2 + char
        }
    }
    return encoded_message2
}
function decode (encoded_message: string) {
    let position2: number;
let new_position2: number;
shift_amount = encoded_message.length
    for (let char2 of encoded_message) {
        if (char_list.indexOf(char2) >= 0) {
            position2 = _py.py_array_index(char_list, char2)
new_position2 = (position2 - shift_amount) % char_list.length
            decoded_message = "" + decoded_message + char_list[new_position2]
        } else {
            decoded_message = "" + decoded_message + char2
        }
    }
    return decoded_message
}
input.onButtonPressed(Button.A, function () {
    index += 1
    basic.showString("" + (characters[index]))
})
buttonClicks.onButtonHeld(buttonClicks.AorB.B, function () {
    if (characters == alphabets) {
        characters = numbers
        index = 0
    } else {
        characters = alphabets
        index = 0
    }
    basic.showIcon(IconNames.Yes)
})
radio.onReceivedString(function (receivedString) {
    basic.showIcon(IconNames.Happy)
    basic.pause(1000)
    basic.clearScreen()
    basic.showString("" + (decode(receivedString)))
    basic.pause(100)
    basic.clearScreen()
    msg = ""
    encoded_message2 = ""
    encoded_message22 = ""
    decoded_message = ""
    decoded_message2 = ""
    index = 0
})
input.onButtonPressed(Button.B, function () {
    index = Math.abs((index + -1) % characters.length)
    basic.showString("" + (characters[index]))
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString("" + (encode(msg)))
    basic.showIcon(IconNames.Yes)
    msg = ""
    encoded_message2 = ""
    encoded_message22 = ""
    decoded_message = ""
    decoded_message2 = ""
    index = 0
})
buttonClicks.onButtonDoubleClicked(buttonClicks.AorB.B, function () {
    basic.clearScreen()
    basic.pause(200)
    basic.showString("=" + msg)
})
buttonClicks.onButtonHeld(buttonClicks.AorB.A, function () {
    msg = "" + msg + characters[index]
    index = 0
    basic.clearScreen()
})
let index = 0
let decoded_message = ""
let encoded_message2 = ""
let characters = ""
let alphabets = ""
let numbers = ""
let shift_amount = 0
let char_list: string[] = []
let msg = ""
let encoded_message22 = ""
let decoded_message2 = ""
decoded_message2 = ""
encoded_message22 = ""
msg = ""
char_list = [
"A",
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
"9"
]
shift_amount = 3
numbers = " 0123456789"
alphabets = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = alphabets
radio.setGroup(1)
