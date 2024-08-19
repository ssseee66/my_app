import flet as ft
from extend.python.controls.pda_listener import PdaListener
import subprocess


def main(page: ft.Page):
    listener_num = 0
    def change_text(e):
        lists.controls.append(ft.Text("sucess"))
        # lists.controls.append(ft.Text(e))
        # lists.controls.append(ft.Text(e.control))
        # lists.controls.append(ft.Text(pda_listener._get_attr("pda_code")))
        lists.controls.append(ft.Text(f"数据变动：{pda_listener.pda_code}"))
        page.update()
    
    def listener_text(e):
        my_text_field.value += 1
        my_text_field_1.value = e.control.pda_code
        lists.controls.append(ft.Text(e))
        # lists.controls.append(ft.Text("sucess_2"))
        # lists.controls.append(ft.Text(my_text_field.value))
        # lists.controls.append(ft.Text(e))
        # lists.controls.append(ft.Text(e.control))
        # lists.controls.append(ft.Text(pda_listener._get_attr("pda_code")))
        # lists.controls.append(ft.Text(f"监听数据：{pda_listener.pda_code}"))
        page.update()
    lists = ft.ListView(height=450)
    
    my_text_field = ft.Text(0)
    my_text_field_1 = ft.Text()
    pda_listener = PdaListener(
        pda_action="com.service.scanner.data", 
        data_tag="ScanCode",
        hint_text="输入单号：",
        on_change=change_text,
        on_listener=listener_text,
    )
    
    def button_click(e):
        if e.control.text == "开始监听":
            e.control.text = "停止监听"
            pda_listener.start_listener = True
            # pda_listener._set_attr("onChange", False)
            # pda_listener._set_attr("start_listener", True)
            # pda_listener._set_attr("onChange", False)
        else:
            e.control.text = "开始监听"
            pda_listener.start_listener = False
            # pda_listener._set_attr("onChange", True)
            # pda_listener._set_attr("start_listener", False)
            # pda_listener._set_attr("onChange", True)
        page.update()
    
    page.add(ft.Text("Hello, Flet!!!!!!!"))
    page.add(pda_listener)   # I want to get this control's datia
    page.add(ft.FilledButton(text="停止监听", on_click=button_click))
    page.add(my_text_field)
    page.add(my_text_field_1)
    page.add(lists)



    

ft.app(main)
