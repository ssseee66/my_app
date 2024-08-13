import flet as ft
from extend.python.controls.pda_listener import PdaListener
import subprocess


def main(page: ft.Page):

    pda_listener = PdaListener(
        pda_code="NULL", 
        pda_action="com.service.scanner.data", 
        data_tag="ScanCode"
    )
    page.add(ft.Text("Hello, Flet!!!!!!!"))
    page.add(pda_listener)   # I want to get this control's data



    

ft.app(main)