from WeatherApp.frontend import WeatherApp, app

if __name__ == '__main__':
    # we just run the front-end pyqt6 app
    window = WeatherApp()
    window.show()
    app.exec()
