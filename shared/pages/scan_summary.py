# -*- coding: utf-8 -*-
from objectmaphelper import *
from action_methods import *
from .names import *


class ScanSummary:
    scan_information_rows = {"container": launcherQmlView_summary_SummaryPage, "id": "summaryDescriptions", "type": "PropertiesDelegate", "unnamed": 1, "visible": True}
    summary_container = {"container": launcherQmlView_summary_SummaryPage, "type": "Flickable", "unnamed": 1, "visible": True}
    
    scan_target_type_key = {"container": launcherQmlView_summary_SummaryPage, "text": "Target Type", "type": "Text", "unnamed": 1, "visible": True}
    pictures_and_videos_under_500mb_key = {"container": launcherQmlView_summary_SummaryPage, "text": "Pictures and Videos under 500MB Thorough ID", "type": "Text", "unnamed": 1, "visible": True}
    files_collected_key = {"container": launcherQmlView_summary_SummaryPage, "text": "Files Collected", "type": "Text", "unnamed": 1, "visible": True}
    pictures_in_cache_button = {"container": launcherQmlView_summary_SummaryPage, "text": "Pictures in Cache", "type": "Text", "unnamed": 1, "visible": True}
    
    search_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "keywordSearchButton", "type": "ToolBarButtonWithRoundProgress", "visible": True}
    
    classifier_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "classifierButton", "type": "ToolBarButtonWithRoundProgress", "visible": True}
    adult_age_group = {"container": launcherQmlView_scrollViewContainer_ScrollView, "occurrence": 3, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c5.sci", "type": "HoveredActivatedFilledBackground", "unnamed": 1, "visible": True}
    
    emails_btn = {"container": launcherQmlView_summary_SummaryPage, "text": "Emails", "type": "Text", "unnamed": 1, "visible": True}
    messages_button = {"container": launcherQmlView_summary_SummaryPage, "text": "Messages", "type": "Text", "unnamed": 1, "visible": True}
    browser_cache = {"container": launcherQmlView_summary_SummaryPage, "text": "Browser Cache", "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def age_group(photos: int) -> dict:
        return {"container": launcherQmlView_scrollViewContainer_ScrollView, "text": photos, "type": "Text", "unnamed": 1, "visible": True}

    @staticmethod
    def get_scan_target_type() -> str:
        scan_target_type_key_obj = get_object(ScanSummary.scan_target_type_key)
        scan_target_pair_obj = get_object(scan_target_type_key_obj.parent)
        scan_target_type_value_obj = object.children(scan_target_pair_obj)[2]
        return scan_target_type_value_obj.text;
        
    @staticmethod
    def get_pictures_and_videos_under_500mb_number() -> str:
        pictures_and_videos_under_500mb_key_obj = get_object(ScanSummary.pictures_and_videos_under_500mb_key)
        pictures_and_videos_under_500mb_pair_obj = get_object(pictures_and_videos_under_500mb_key_obj.parent)
        pictures_and_videos_under_500mb_value_obj = object.children(pictures_and_videos_under_500mb_pair_obj)[1]
        return pictures_and_videos_under_500mb_value_obj.text;
    
    @staticmethod
    def get_files_collected_number() -> str:
        files_collected_key_obj = get_object(ScanSummary.files_collected_key)
        files_collected_pair_obj = get_object(files_collected_key_obj.parent)
        files_collected_value_obj = object.children(files_collected_pair_obj)[2]
        return files_collected_value_obj.text;
