import flet as ft
from extend.python.controls.pda_listener import PdaListener
import subprocess


def main(page: ft.Page):
    
    def change_text(e):
        page.add(ft.Text(pda_listener.pda_code))
        page.update()

    pda_listener = PdaListener(
        pda_code="NULL", 
        pda_action="com.service.scanner.data", 
        data_tag="ScanCode",
        on_change=change_text,
    )
    page.add(ft.Text("Hello, Flet!!!!!!!"))
    page.add(pda_listener)   # I want to get this control's data
    page.add(ft.TextField())



    

ft.app(main)