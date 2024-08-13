
from flet_core.constrained_control import ConstrainedControl
from typing import Any, Optional
import flet as ft


class PdaListener(ConstrainedControl):
    """
    PdaListener 控件。
    """

    def __init__(self, pda_code = None, pda_action = None, data_tag = None):
        ConstrainedControl.__init__(self)
        self.pda_code = pda_code
        self.pda_action = pda_action
        self.data_tag = data_tag
    


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
    def pda_code(self):
        return self._get_attr("pda_code")
    
    @pda_code.setter
    def pda_code(self, value):
        self._set_attr("pda_code", value)
    
    

    

