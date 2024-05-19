# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *


class ScanFiltersRibbon:
    
    apply_button = {"caption": "APPLY", "container": filterOptions, "objectName": "applyFilterButton", "type": "CommonButton", "visible": True}
    clear_filter_button = {"container": filterColumns, "id": "filterIcon", "source": "qrc:/common_skin_default/graphics/list_item_related_icons/filter_cross_icon_22_22_inverted.png", "type": "Image", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_filter_by_name(filter_name: str):
        return {"container": filterColumns, "text": filter_name, "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_filter_option_by_name(filter_option_name: str):
        return {"container": filterOptions, "id": "uniqueValueDelegate", "valueName": filter_option_name, "type": "CheckableValueDelegate", "unnamed": 1, "visible": True}