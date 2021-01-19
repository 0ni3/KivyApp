from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print("The user searched for '{}'".format(self.search_input.text))
        search_template = "http://api.openweathermap.org/data/2.5/" +
            "find?q={}&type=like"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self):
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
            for d in data['list']]:
                print("\n".join(cities))

class WeatherApp(App):
    pass

if __name__ == '__main__':
        WeatherApp().run()
