
from flet_core.constrained_control import ConstrainedControl
from typing import Optional

class PdaListener(ConstrainedControl):
    """
    PdaListener 控件。
    """

    def __init__(
            self, 
            pda_code: Optional[str] = None, 
            pda_action: Optional[str] = None, 
            data_tag: Optional[str] = None,
            start_listener: Optional[bool] = False,    # 初始为不监听广播
            hint_text: Optional[str] = None,
            on_change = None,
            on_listener = None,
            qr_data: Optional[str] = None,
            qr_data_tag: Optional[str] = None,
            image_data: Optional[str] = None,
            image_data_tag: Optional[str] = None,
            ocr_data: Optional[str] = None,
            ocr_data_tag: Optional[str] = None,
        ):
        ConstrainedControl.__init__(self)
        self.pda_code = pda_code
        self.pda_action = pda_action
        self.data_tag = data_tag
        self.start_listener = start_listener
        self.hint_text = hint_text
        self.on_change = on_change
        self.on_listener = on_listener
        self.qr_data = qr_data
        self.qr_data_tag = qr_data_tag
        self.image_data = image_data
        self.image_data_tag =image_data_tag
        self.ocr_data = ocr_data
        self.ocr_data_tag = ocr_data_tag
    


    def _get_control_name(self):
        return "pda_listener"

    @property
    def pda_action(self):
        return self._get_attr("pda_action")
    
    @pda_action.setter
    def pda_action(self, value):
        self._set_attr("pda_action", value)

    @property
    def data_tag(self):
        return self._get_attr("data_tag")
    
    @data_tag.setter
    def data_tag(self, value):
        self._set_attr("data_tag", value)
       
    @property
    def pda_code(self) -> Optional[str]:
        return self._get_attr("pda_code", def_value="")
    
    @pda_code.setter
    def pda_code(self, value):
        self._set_attr("pda_code", value)

    @property
    def start_listener(self):
        return self._get_attr("start_listener", def_value=False)

    @start_listener.setter
    def start_listener(self, value):
        self._set_attr("start_listener", value)

    @property
    def hint_text(self):
        return self._get_attr("hint_text")
    
    @hint_text.setter
    def hint_text(self, value):
        self._set_attr("hint_text", value)

    # on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._add_event_handler("change", handler)
        self._set_attr("onChange", True if handler is not None else None)

    
    @property
    def on_listener(self):
        return self._get_event_handler("listener")

    @on_listener.setter
    def on_listener(self, handler):
        self._add_event_handler("listener", handler)
        self._set_attr("start_listener", True if handler is not None else None)

    
    @property
    def qr_data(self):
        return self._get_attr("qr_data")
    @qr_data.setter
    def qr_data(self, value):
        self._set_attr("qr_data", value)

    @property
    def qr_data_tag(self):
        return self._get_attr("qr_data_tag")
    @qr_data_tag.setter
    def qr_data_tag(self, value):
        self._set_attr("qr_data_tag", value)

    @property
    def image_data(self):
        return self._get_attr("image_data")
    @image_data.setter
    def image_data(self, value):
        self._set_attr("image_data", value)

    @property
    def image_data_tag(self):
        return self._get_attr("image_data_tag")
    @image_data_tag.setter
    def image_data_tag(self, value):
        self._set_attr("image_data_tag", value)

    @property
    def ocr_data(self):
        return self._get_attr("ocr_data")
    @ocr_data.setter
    def ocr_data(self, value):
        self._set_attr("ocr_data", value)
    
    @property
    def ocr_data_tag(self):
        return self._get_attr("ocr_data_tag")
    @ocr_data_tag.setter
    def ocr_data_tag(self, value):
        self._set_attr("ocr_data_tag", value)


    
     

    

