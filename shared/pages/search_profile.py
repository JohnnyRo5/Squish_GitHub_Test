# -*- coding: utf-8 -*-
import datetime

from objectmaphelper import *
from .names import *


class SearchProfile:
    
    exclude_folder_radio_btn = {"container": launcherQmlView_searchProfilesView_ProfilesView, "id": "profileDelegate", "index": 0, "type": "ProfileDelegateItem", "unnamed": 1, "visible": True}
    scan_button = {"caption": "SCAN", "container": launcherQmlView_QQuickView, "objectName": "scanPageScanButton", "type": "CommonButton", "visible": True}
    limit_data_collection_between_btn = {"container": launcherQmlView_QQuickView, "text": "Limit data collection between", "type": "Text", "unnamed": 1, "visible": True}
    
    first_search_profile_radio_btn = {"container": launcherQmlView_searchProfilesView_ProfilesView, "type": "RadioButtonIndicator", "unnamed": 1, "visible": True}
    
    year_text_field_1 = {"container": launcherQmlView_QQuickView, "id": "yearTextField", "type": "TextField", "unnamed": 1, "visible": True}
    month_text_field_1 = {"container": launcherQmlView_QQuickView, "id": "monthTextField", "type": "TextField", "unnamed": 1, "visible": True}
    day_text_field_1 = {"container": launcherQmlView_QQuickView, "id": "dayTextField", "type": "TextField", "unnamed": 1, "visible": True}
    year_text_field_2 = {"container": launcherQmlView_QQuickView, "id": "yearTextField", "occurrence": 2, "type": "TextField", "unnamed": 1, "visible": True}
    month_text_field_2 = {"container": launcherQmlView_QQuickView, "id": "monthTextField", "occurrence": 2, "type": "TextField", "unnamed": 1, "visible": True}
    day_text_field_2 = {"container": launcherQmlView_QQuickView, "id": "dayTextField", "occurrence": 2, "type": "TextField", "unnamed": 1, "visible": True}
    
    @staticmethod
    def search_profile(profile_name: str) -> dict:
        return  {"container": launcherQmlView_searchProfilesView_ProfilesView, "text": profile_name, "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def define_timerange_for_scan(date1: datetime, date2: datetime) -> None:
        from action_methods import send_keys
        # Complete the dates
        send_keys(SearchProfile.year_text_field_1, date1.year)
        send_keys(SearchProfile.month_text_field_1, date1.month)
        send_keys(SearchProfile.day_text_field_1, date1.day)
        send_keys(SearchProfile.year_text_field_2, date2.year)
        send_keys(SearchProfile.month_text_field_2, date2.month)
        send_keys(SearchProfile.day_text_field_2, date2.day)
