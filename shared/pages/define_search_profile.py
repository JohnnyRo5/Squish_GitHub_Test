# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class DefineSearchProfile:
    edit_btn = {"caption": "Edit", "container": launcherQmlView_capturesScollArea_ScrollView, "objectName": "ToolBarActionItem#3", "type": "ActionItem", "visible": True}
    name_textbox = {"container": launcherQmlView_QQuickView, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    multimedia_checkbox = {"container": launcherQmlView_ScrollView, "id": "checkbox", "occurrence": 8, "source": "qrc:/common_skin_default/graphics/checkbox_related_items/checkbox_background_5_5.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    next_btn = {"container": launcherQmlView_QQuickView, "text": "NEXT", "type": "Text", "unnamed": 1, "visible": True}
    proceed_btn = {"container": launcherQmlView_QQuickView, "text": "PROCEED", "type": "Text", "unnamed": 1, "visible": True}
    new_capture_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "newFileCaptureButton", "type": "ToolBarButton", "visible": True}
    