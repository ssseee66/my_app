
from flet_core.constrained_control import ConstrainedControl
from typing import Any, Optional
import flet as ft
from flet_core.form_field_control import FormFieldControl, InputBorder
from flet_core.adaptive_control import AdaptiveControl
from flet_core.text_style import TextStyle
from flet_core.types import (
    AnimationValue,
    BorderRadiusValue,
    OffsetValue,
    PaddingValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
    TextAlign,
    VerticalAlignment,
    OptionalEventCallable,
)



class PdaListener(FormFieldControl, AdaptiveControl):
    """
    PdaListener 控件。
    """

    def __init__(
            self, 
            pda_code: Optional[str] = None, 
            pda_action = None, 
            data_tag = None,
            adaptive: Optional[bool] = None,
            on_change: OptionalEventCallable = None,
        ):
        FormFieldControl.__init__(self)
        AdaptiveControl.__init__(self, adaptive=adaptive)
        self.pda_code = pda_code
        self.pda_action = pda_action
        self.data_tag = data_tag
        self.on_change = on_change
    


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

    # on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._add_event_handler("change", handler)
        self._set_attr("onChange", True if handler is not None else None)
    
    

    

