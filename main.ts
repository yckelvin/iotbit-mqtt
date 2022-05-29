ESP8266_IoT.MqttEvent("testtopic/2", ESP8266_IoT.QosList.Qos0, function (message) {
    basic.showString("" + (message))
})
input.onButtonPressed(Button.A, function () {
    if (ESP8266_IoT.wifiState(true)) {
        basic.showIcon(IconNames.Chessboard)
        basic.pause(500)
    }
    num = randint(0, 10)
    ESP8266_IoT.publishMqttMessage(convertToText(num), "testtopic/2", ESP8266_IoT.QosList.Qos2)
    basic.showNumber(num)
})
input.onButtonPressed(Button.AB, function () {
    control.reset()
})
input.onButtonPressed(Button.B, function () {
    if (ESP8266_IoT.isMqttBrokerConnected()) {
        basic.showIcon(IconNames.Yes)
    } else {
        ESP8266_IoT.connectMQTT("b01f5034387a4cb8a39f573af80d2958.s2.eu.hivemq.cloud", 8883, false)
        basic.showIcon(IconNames.SmallSquare)
    }
})
let num = 0
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("", "")
ESP8266_IoT.setMQTT(
ESP8266_IoT.SchemeList.TLS,
"clientId-PvewtMsW8P",
"852ebiz",
"k@yKAnFW9AdyRRH",
""
)
ESP8266_IoT.connectMQTT("b01f5034387a4cb8a39f573af80d2958.s2.eu.hivemq.cloud", 8883, false)
if (ESP8266_IoT.isMqttBrokerConnected()) {
    basic.showIcon(IconNames.Yes)
} else {
    basic.showIcon(IconNames.No)
}
