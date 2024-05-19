# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *


class UserGuides:
    user_guides_page = {"container": launcherQmlView_QQuickView, "id": "userGuidesPage", "type": "UserGuidesPage", "unnamed": 1, "visible": True}
    
    back_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "scanBasicLayoutBackButton", "type": "ToolBarButton", "visible": True}
    user_guides_list = {"container": user_guides_page, "name": "userGuidesListView", "objectName": "userGuidesListView", "type": "ItemsListView", "visible": True}
    
    @staticmethod
    def user_guide(user_guide_name: str) -> dict:
        return {"container": launcherQmlView_homePageScrollView_StyledScrollView, "text": user_guide_name, "type": "Text", "unnamed": 1, "visible": True}
