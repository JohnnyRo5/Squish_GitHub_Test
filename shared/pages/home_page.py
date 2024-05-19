# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *


class HomePage:
    
    investigate_device_button = {"container": launcherQmlView_homePageScrollView_StyledScrollView, "id": "homePageDelegate", "type": "HomePageListItem", "unnamed": 1, "visible": True}
    review_scan_results_button = {"container": launcherQmlView_homePageScrollView_StyledScrollView, "id": "homePageDelegate", "occurrence": 2, "type": "HomePageListItem", "unnamed": 1, "visible": True}
    scan_setup_and_key_management_button = {"container": launcherQmlView_homePageScrollView_StyledScrollView, "id": "homePageDelegate", "occurrence": 3, "type": "HomePageListItem", "unnamed": 1, "visible": True}
    
    right_plane_panel = {"container": launcherQmlView_QQuickView, "id": "mouseArea", "type": "MouseArea", "unnamed": 1, "visible": True}
    back_btn = {"container": launcherQmlView_QQuickView, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c8.sci", "type": "CommonToolBarButtonStyle", "unnamed": 1, "visible": True}
    
    settings_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "settingsButton", "type": "ToolBarButton", "visible": True}

    guides_btn = {"container": launcherQmlView_homePageScrollView_StyledScrollView, "text": "User Guides", "type": "Text", "unnamed": 1, "visible": True}
    
    user_guides = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "userGuidesButton", "type": "ToolBarButton", "visible": True}
    
    launcher_object = {"container": launcherQmlView_QQuickView, "objectName": "launcherQML", "type": "LauncherQML", "visible": True}
    
    class ErrorPopUp:
        error_accessing_data_pop_up = {"container": launcherQmlView_QQuickView, "id": "background", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
        settings_btn = {"caption": "SETTINGS", "container": launcherQmlView_QQuickView, "id": "genericActionButton", "type": "CommonButton", "unnamed": 1, "visible": True}
