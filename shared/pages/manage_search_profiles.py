# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class ManageSearchProfiles:
    first_profile_in_list = {"container": launcherQmlView_ScrollView, "id": "profileDelegate", "index": 0, "type": "ListItem", "unnamed": 1, "visible": True}
    edit_btn = {"caption": "Edit", "container": launcherQmlView_ScrollView, "objectName": "ToolBarActionItem#3", "type": "ActionItem", "visible": True}
    comprehensive_child_exploitation = {"container": launcherQmlView_ScrollView, "id": "profileDelegate", "index": 20, "type": "ListItem", "unnamed": 1, "visible": True}
    new_profile_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "newProfileButton", "type": "ToolBarButton", "visible": True}
    back_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "scanBasicLayoutBackButton", "type": "ToolBarButton", "visible": True}
    delete_btn = {"container": launcherQmlView_ScrollView, "text": "Delete", "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_search_profile(search_profile: str):
        return {"container": launcherQmlView_searchProfilesListScrollView_StyledScrollView, "text": search_profile, "type": "Text", "unnamed": 1, "visible": True}