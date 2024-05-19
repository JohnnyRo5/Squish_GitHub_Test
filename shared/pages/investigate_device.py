# -*- coding: utf-8 -*-
from objectmaphelper import *
from pages.names import *


class InvestigateDevice:
    scan_button = {"container": launcherQmlView_itemsScrollView_StyledScrollView, "id": "homePageDelegate", "type": "HomePageListItem", "unnamed": 1, "visible": True}
    HDD = {"container": launcherQmlView_scanTargetsScrollView_ScrollView, "index": 0, "objectName": "targetItem#0", "type": "TargetItemDelegate", "visible": True}
    setup_scans = {"container": launcherQmlView_itemsScrollView_StyledScrollView, "id": "homePageDelegate", "occurrence": 5, "type": "HomePageListItem", "unnamed": 1, "visible": True}
    prepare_collection_key = {"container": launcherQmlView_itemsScrollView_StyledScrollView, "occurrence": 2, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "HoveredActivatedBackground", "unnamed": 1, "visible": True}
    review_scan_results = {"container": launcherQmlView_itemsScrollView_StyledScrollView, "id": "homePageDelegate", "occurrence": 4, "type": "HomePageListItem", "unnamed": 1, "visible": True}
    back_btn = {"checkable": False, "container": LauncherQmlView_QQuickView, "objectName": "backButton", "type": "ToolBarButton", "visible": True}    
    image_button = {"container": launcherQmlView_itemsScrollView_StyledScrollView, "id": "homePageItemIcon", "source": "qrc:/common_skin_default/graphics/home_page_icons/home_icon_image_attached_devices_48_48.png", "type": "Image", "unnamed": 1, "visible": True}
    