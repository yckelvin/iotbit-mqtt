def on_mqtt_qos_list_qos0(message):
    basic.show_string("" + (message))
ESP8266_IoT.mqtt_event("testtopic/2",
    ESP8266_IoT.QosList.QOS0,
    on_mqtt_qos_list_qos0)

def on_button_pressed_a():
    global num
    if ESP8266_IoT.wifi_state(True):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.pause(500)
    num = randint(0, 10)
    ESP8266_IoT.publish_mqtt_message(convert_to_text(num),
        "testtopic/2",
        ESP8266_IoT.QosList.QOS2)
    basic.show_number(num)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if ESP8266_IoT.is_mqtt_broker_connected():
        basic.show_icon(IconNames.YES)
    else:
        ESP8266_IoT.connect_mqtt("b01f5034387a4cb8a39f573af80d2958.s2.eu.hivemq.cloud",
            8883,
            False)
        basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.B, on_button_pressed_b)

num = 0
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("KLHOME", "127214529")
ESP8266_IoT.set_mqtt(ESP8266_IoT.SchemeList.TLS,
    "clientId-PvewtMsW8P",
    "852ebiz",
    "k@yKAnFW9AdyRRH",
    "")
ESP8266_IoT.connect_mqtt("b01f5034387a4cb8a39f573af80d2958.s2.eu.hivemq.cloud",
    8883,
    False)
if ESP8266_IoT.is_mqtt_broker_connected():
    basic.show_icon(IconNames.YES)
else:
    basic.show_icon(IconNames.NO)