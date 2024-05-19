# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *
from squish import *
from object import *
import builtins


class ScanSearchRibbon:
    input_container = {"container": launcherQmlView_QQuickView, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    error_text = {"container": launcherQmlView_QQuickView, "text": "Unsupported characters. Use only letters and numbers.", "type": "Text", "unnamed": 1, "visible": True}
    search_btn = {"container": launcherQmlView_QQuickView, "id": "buttonIcon", "source": "qrc:/common_skin_default/graphics/main_toolbar_icons/keyword_search_icon_32_32.png", "type": "Image", "unnamed": 1, "visible": True}
    number_of_results_text = {"container": launcherQmlView_QQuickView, "objectName": "currentTotalText", "type": "Text", "visible": True}
    right_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "forwardButton", "type": "ToolBarButton", "visible": True}
    left_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "backwardButton", "type": "ToolBarButton", "visible": True}
    combo_box = {"container": launcherQmlView_QQuickView, "id": "searchResultsComboBox", "type": "ComboBox", "unnamed": 1, "visible": True}
    
    @staticmethod  
    def get_number_of_results() -> int:
        obj = waitForObject(ScanSearchRibbon.number_of_results_text)
        number_of_results = (str(obj.text)).split("/")[1]
        return builtins.int(number_of_results)
    
    @staticmethod  
    def get_current_result_number() -> int:
        obj = waitForObject(ScanSearchRibbon.number_of_results_text)
        current_result_number = (str(obj.text)).split("/")[0]
        return builtins.int(current_result_number)
