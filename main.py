import random

from kivy.app import App
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Window.clearcolor = (0.02, 0.03, 0.06, 1)

store = JsonStore("game_data.json")

FONT = "/system/fonts/NotoNaskhArabic-Regular.ttf"


class GuessGame(App):

    def build(self):
        if store.exists("game"):
            data = store.get("game")
            self.coins = data.get("coins", 100)
            self.record = data.get("record", 0)
        else:
            self.coins = 100
            self.record = 0
            self.save_data()

        self.secret = random.randint(1, 100)
        self.attempts = 0

        main = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=12
        )

        title = Label(
            text="بازی حدس عدد",
            font_name=FONT,
            font_size=34,
            bold=True,
            size_hint_y=0.16
        )

        self.coins_label = Label(
            text="سکه",
            font_name=FONT,
            font_size=24,
            color=(1, 0.8, 0.1, 1),
            size_hint_y=0.09
        )

        self.coins_number = Label(
            text=str(self.coins),
            font_size=28,
            bold=True,
            color=(1, 0.85, 0.2, 1),
            size_hint_y=0.09
        )

        self.record_label = Label(
            text="رکورد",
            font_name=FONT,
            font_size=24,
            color=(0.7, 0.6, 1, 1),
            size_hint_y=0.09
        )

        self.record_number = Label(
            text=str(self.record) if self.record else "-",
            font_size=28,
            bold=True,
            color=(0.75, 0.65, 1, 1),
            size_hint_y=0.09
        )

        self.info = Label(
            text="یک عدد بین ۱ تا ۱۰۰ حدس بزن",
            font_name=FONT,
            font_size=21,
            size_hint_y=0.14
        )

        self.input = TextInput(
            hint_text="1 - 100",
            font_size=28,
            multiline=False,
            halign="center",
            input_filter="int",
            size_hint_y=0.15
        )

        guess = Button(
            text="حدس بزن",
            font_name=FONT,
            font_size=25,
            background_normal="",
            background_color=(0.08, 0.35, 0.9, 1),
            size_hint_y=0.14
        )
        guess.bind(on_press=self.check_guess)

        again = Button(
            text="بازی دوباره",
            font_name=FONT,
            font_size=22,
            background_normal="",
            background_color=(0.15, 0.16, 0.22, 1),
            size_hint_y=0.12
        )
        again.bind(on_press=self.restart)

        creator = Label(
            text="Aliasgr",
            font_size=30,
            bold=True,
            color=(0.7, 0.7, 0.8, 1),
            size_hint_y=0.10
        )

        main.add_widget(title)
        main.add_widget(self.coins_label)
        main.add_widget(self.coins_number)
        main.add_widget(self.record_label)
        main.add_widget(self.record_number)
        main.add_widget(self.info)
        main.add_widget(self.input)
        main.add_widget(guess)
        main.add_widget(again)
        main.add_widget(creator)

        return main

    def save_data(self):
        store.put(
            "game",
            coins=self.coins,
            record=self.record
        )

    def check_guess(self, button):
        if not self.input.text:
            self.info.text = "یک عدد وارد کن"
            return

        number = int(self.input.text)

        if number < 1 or number > 100:
            self.info.text = "عدد باید بین ۱ تا ۱۰۰ باشد"
            return

        self.attempts += 1

        if number < self.secret:
            self.info.text = "عدد بزرگتر است"

        elif number > self.secret:
            self.info.text = "عدد کوچکتر است"

        else:
            self.coins += 10
            self.coins_number.text = str(self.coins)

            if self.record == 0 or self.attempts < self.record:
                self.record = self.attempts
                self.record_number.text = str(self.record)

            self.info.text = "آفرین، درست حدس زدی"
            self.save_data()

    def restart(self, button):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.input.text = ""
        self.info.text = "یک عدد بین ۱ تا ۱۰۰ حدس بزن"


GuessGame().run()
