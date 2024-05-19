# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class ScanInformation:
    scan_name_textfield = {"container": scanNameSection, "echoMode": 0, "id": "textField", "type": "TextField", "unnamed": 1, "visible": True}
    custom_fields_container = {"container": launcherQmlView_scrollViewScanInformation_ScrollView, "id": "customFieldsListLoader", "type": "Loader", "unnamed": 1, "visible": True}
    
    
    @staticmethod
    def custom_field_by_name(text: str):
        return {"container": launcherQmlView_scrollViewScanInformation_ScrollView, "text": text, "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def field_value(occurrence: int):
        """
        occurrence:
        2. Custom field value 1
        3. Custom field value 2
        etc. 
        """
        return {"container": launcherQmlView_scrollViewScanInformation_ScrollView, "echoMode": 0, "id": "textField", "occurrence": occurrence, "type": "TextField", "unnamed": 1, "visible": True}
        