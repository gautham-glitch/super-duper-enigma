import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = "login page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 400
    page.window.width = 400
    page.window.resizable = False

    #setup wigets
    text_username = TextField(label = "username", text_align = ft.TextAlign.LEFT, width = 200)
    text_pass = TextField(label = "pass", text_align = ft.TextAlign.LEFT, width = 200, password = True)
    checkbox_sign = Checkbox(label = "I agree to stuff", value = False)
    signup_button = ElevatedButton(text = "signup", width = 200, disabled = True)

    # validation
    def valid(e:ControlEvent) -> None:
        if all([text_pass.value, text_username.value, checkbox_sign.value]) == True:
            signup_button.disabled = False
        
        else:
            signup_button.disabled = True
        
        page.update()
    
    def submit(e:ControlEvent) -> None:
        print(f"username:{text_username.value}")
        print(f"pass:{text_pass.value}")

        page.clean()
        page.add(
            Row(
                controls = [Text(value = f"welcome, {text_username.value}",size = 20)],
                alignment = ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_sign.on_change = valid
    text_pass.on_change = valid
    text_username.on_change = valid
    signup_button.on_click = submit

    page.add(
        Row(
            controls = [
                Column([
                    text_username,
                    text_pass,
                    checkbox_sign,
                    signup_button
                ])
            ], alignment = ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target = main)