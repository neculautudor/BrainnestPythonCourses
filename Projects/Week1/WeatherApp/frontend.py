import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QHBoxLayout, QLineEdit, QLabel, QScrollArea

from WeatherApp.weatherAPI import WeatherGetter

# I chose pyqt6 instead of tkinter because i have more experience with it, and it fits better
# Creating classes instead of functions is necessary because i need persistent variables, and for a cleaner implementation
app = QApplication(sys.argv)


class WeatherApp(QWidget):
    def __init__(self):
        # Setting up the main app, consisting of 3 components: top buttons, middle info, bottom exit button
        super().__init__()
        self.setWindowTitle('WeatherApp')
        self.setGeometry(100, 100, 400, 400)
        self.layout = QVBoxLayout()
        self.weatherInfo = WeatherInfo()

        self.layout.addWidget(TopButtons(self.weatherInfo))
        # i give the whole object as a parameter because i need to call a method in weatherInfo from
        # TopButtons, but there were other ways of doing this
        self.layout.addWidget(self.weatherInfo)
        self.layout.addWidget(Button('quit', lambda: app.quit()))

        self.setLayout(self.layout)
        # created the layout, added the widgets to it, then set the layout to the main widget


class TopButtons(QWidget):
    def __init__(self, weatherInfoWidget):
        super().__init__()
        self.weatherInfoWidget = weatherInfoWidget
        self.weatherGetter = WeatherGetter()
        self.layout = QHBoxLayout()
        self.locationInput = QLineEdit()
        self.layout.addWidget(QLabel('City: '))
        self.layout.addWidget(self.locationInput)
        self.layout.addWidget(Button('Generate', lambda: self.handle_generate())) # using lambda to pass the action
        self.setLayout(self.layout)

    def handle_generate(self):
        city = self.locationInput.text()
        # fetching the actual data with the user input
        data = self.weatherGetter.get_weather(city)
        if type(data) == str:
            #print the error if there is one and don't do eanything else
            print(data)
            return
        # propagate the action further down the objects, with the data we got
        self.weatherInfoWidget.handle_generate(data)


class WeatherInfo(QScrollArea):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.temperatureField = WeatherField('Temperature:             ', '-')
        self.skyField = WeatherField('Sky:             ', '-')
        self.humidityField = WeatherField('Humidity:        ', '-')
        self.windField = WeatherField('Wind:            ', '-')

        self.layout.addWidget(self.temperatureField)
        self.layout.addWidget(self.skyField)
        self.layout.addWidget(self.humidityField)
        self.layout.addWidget(self.windField)


        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)

    def handle_generate(self, data):
        # updating the fields with the data
        self.temperatureField.update_value(f"{str(data['main']['temp'])}K")
        self.skyField.update_value(str(data['weather'][0]['main']))
        self.humidityField.update_value(str(data['main']['humidity']))
        self.windField.update_value(str(data['wind']['speed']))


class WeatherField(QWidget):
    def __init__(self, label, value):
        super().__init__()
        self.layout = QHBoxLayout()
        self.valueLabel = QLabel(value)
        self.layout.addWidget(QLabel(label))
        self.layout.addWidget(self.valueLabel)
        self.setLayout(self.layout)

    def update_value(self, value):
        # the "primal" method, the actual update of each field
        self.valueLabel.setText(value)


# useful for writing less code
class Button(QPushButton):
    def __init__(self, name, action):
        super().__init__()
        self.setText(name)
        self.clicked.connect(action)
