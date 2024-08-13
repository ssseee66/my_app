import flet as ft
from extend.python.controls.pda_listener import PdaListener
import subprocess


def main(page: ft.Page):

    process = subprocess.Popen(['dart', 'hello.dart'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    pda_listener = PdaListener(
        pda_code="NULL", 
        pda_action="com.service.scanner.data", 
        data_tag="ScanCode"
    )
    output = process.stdout
    page.add(ft.Text("Hello, Flet!!!!!!!"))
    page.add(pda_listener)



    

ft.app(main)