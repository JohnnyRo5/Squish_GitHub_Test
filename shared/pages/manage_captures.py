# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *
from object import *
from squish import *


class ManageCaptures:
    first_profile_in_list = {"container": launcherQmlView_ScrollView, "id": "profileDelegate", "index": 0, "type": "ListItem", "unnamed": 1, "visible": True}
    edit_btn = {"caption": "Edit", "container": launcherQmlView_ScrollView, "objectName": "ToolBarActionItem#3", "type": "ActionItem", "visible": True}
    comprehensive_child_exploitation = {"container": launcherQmlView_ScrollView, "id": "profileDelegate", "index": 20, "type": "ListItem", "unnamed": 1, "visible": True}
    new_profile_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "newProfileButton", "type": "ToolBarButton", "visible": True}
    back_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "scanBasicLayoutBackButton", "type": "ToolBarButton", "visible": True}
    delete_btn = {"container": launcherQmlView_ScrollView, "text": "Delete", "type": "Text", "unnamed": 1, "visible": True}
    
    new_capture_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "newFileCaptureButton", "type": "ToolBarButton", "visible": True}
    import_capture_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "importFileCaptureButton", "type": "ToolBarButton", "visible": True}
    search_for_files_by_properties = {"container": launcherQmlView_ScrollView, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "HoveredActivatedBackground", "unnamed": 1, "visible": True}
    search_for_files_by_hash_value_button = {"container": launcherQmlView_ScrollView, "occurrence": 3, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "HoveredActivatedBackground", "unnamed": 1, "visible": True}
    search_for_keywords = {"container": launcherQmlView_ScrollView, "id": "actionListItem", "index": 1, "type": "ListItem", "unnamed": 1, "visible": True}
    import_completed_msg = {"container": launcherQmlView_QQuickView, "text": "Import completed", "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def capture_groups(capture_group_name: str) -> dict:   
        return {"container": launcherQmlView_categoriesScollArea_ScrollView, "text": capture_group_name, "type": "Text", "unnamed": 1, "visible": True}
        
    @staticmethod
    def captures(capture_name: str) -> dict:
        return {"container": launcherQmlView_capturesScollArea_ScrollView, "text": capture_name, "type": "Text", "unnamed": 1, "visible": True}
    
