# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class PrepareCollectionKeys:
    no_predefined_search_radio_btn = {"container": launcherQmlView_profilesFullContentScrollArea_ScrollView, "type": "RadioButtonIndicator", "unnamed": 1, "visible": True}
    predefined_search_radio_btn = {"container": launcherQmlView_profilesFullContentScrollArea_ScrollView, "occurrence": 2, "type": "RadioButtonIndicator", "unnamed": 1, "visible": True}
    first_search_profile = {"container": launcherQmlView_profilesFullContentScrollArea_ScrollView, "occurrence": 4, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "HoveredActivatedBackground", "unnamed": 1, "visible": True}
    deselect_all_profiles = {"container": launcherQmlView_profilesFullContentScrollArea_ScrollView, "text": "Deselect all", "type": "Text", "unnamed": 1, "visible": True}
    select_all_profiles = {"container": launcherQmlView_profilesFullContentScrollArea_ScrollView, "text": "Select all", "type": "Text", "unnamed": 1, "visible": True}
    error_select_profiles = {"container": launcherQmlView_QQuickView, "text": "Select one or more Search Profiles", "type": "Text", "unnamed": 1, "visible": True}
    
    container = launcherQmlView_ScrollView = {"container": launcherQmlView_QQuickView, "occurrence": 2, "type": "ScrollView", "unnamed": 1, "visible": True}
    first_collection_key = {"container": container, "id": "collectionKeyTargetDelegate", "index": 0, "type": "CollectionKeyTargetDelegate", "unnamed": 1, "visible": True}
    
    prepare_btn = {"container": launcherQmlView_QQuickView, "id": "background", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c8.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    
    usb_icon = {"container": launcherQmlView_colectionKeysSelectionLsitScrollArea_StyledScrollView, "id": "iconItem", "source": "qrc:/common_skin_default/graphics/target_icons/flash_drive_icon_48_48.png", "type": "Image", "unnamed": 1, "visible": True}
    
    proceed_btn = {"container": launcherQmlView_QQuickView, "text": "Proceed", "type": "Text", "unnamed": 1, "visible": True}
    
    ready_txt = {"container": launcherQmlView_preparationTargetsListScrollArea_StyledScrollView, "text": "Ready. Please unplug.", "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_drive_by_name(drive_name: str):
        return {"container": launcherQmlView_colectionKeysSelectionLsitScrollArea_StyledScrollView, "text": drive_name, "type": "Text", "unnamed": 1, "visible": True}

