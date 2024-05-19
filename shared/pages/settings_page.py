# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class SettingsPage:
    
    software_update_section = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "softwareUpdateSection", "type": "SoftwareUpdateSection", "unnamed": 1, "visible": True}
    
    delete_scan_information_field_button = {"container": table_rowitem_FocusScope, "text": "Delete", "type": "Text", "unnamed": 1, "visible": True}
    
    scan_results = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "scanResultsPathLabel", "type": "TextLabel", "unnamed": 1, "visible": True}
    exported_reports = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "exportedReportsPathLabel", "type": "TextLabel", "unnamed": 1, "visible": True}
    android_iOs = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "backupPathLabel", "type": "TextLabel", "unnamed": 1, "visible": True}
    licenses_back_up = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "licensesBackupPathLabel", "type": "TextLabel", "unnamed": 1, "visible": True}
    whitelists = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "whitelistsPathLabel", "type": "TextLabel", "unnamed": 1, "visible": True}
    search_pofiles = {"container": launcherQmlView_contentScrollView_ScrollView, "id": "searchProfilesPathLabel", "type": "TextLabel", "unnamed": 1, "visible": True}
    
    scan_result_text = {"container": launcherQmlView_contentScrollView_ScrollView, "text": "Scan results", "type": "Text", "unnamed": 1, "visible": True}
    exported_reports_text = {"container": launcherQmlView_contentScrollView_ScrollView, "text": "Exported reports", "type": "Text", "unnamed": 1, "visible": True}
    android_iOs_acquisitions = {"container": launcherQmlView_contentScrollView_ScrollView, "text": "Android/iOS acquisitions", "type": "Text", "unnamed": 1, "visible": True}
    licenses_text = {"container": launcherQmlView_contentScrollView_ScrollView, "text": "Licenses backup", "type": "Text", "unnamed": 1, "visible": True}
    whitelist_text = {"container": launcherQmlView_contentScrollView_ScrollView, "text": "Whitelists", "type": "Text", "unnamed": 1, "visible": True}
    search_profiles_text = {"container": launcherQmlView_contentScrollView_ScrollView, "text": "Search Profiles", "type": "Text", "unnamed": 1, "visible": True}
    
    ok_btn = {"caption": "OK", "container": launcherQmlView_QQuickView, "objectName": "okButton", "type": "CommonButton", "visible": True}
    browse_button = {"caption": "...", "container": launcherQmlView_contentScrollView_ScrollView, "objectName": "browseButton", "type": "CommonButton", "visible": True}

    @staticmethod
    def scan_result_tag(index: int):
        """
        index:
        0. 1st Tag
        1. 2nd Tag
        ...
        9. 10th Tag
        """
        return {"container": launcherQmlView_QQuickView, "id": "tagListItem", "index": index, "type": "TagsListDelegate", "unnamed": 1, "visible": True}
    
    @staticmethod
    def rename_tag_button(occurrence: int):
        """
        occurrence:
        1. Rename button for 1st Tag
        2. Rename button for 2nd Tag
        ...
        10. Rename button for 10th Tag
        """
        return {"container": launcherQmlView_QQuickView, "occurrence": occurrence, "text": "Rename", "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod        
    def tag_name_textfield(occurrence: int):
        """
        occurrence:
        1. Text field for 1st Tag
        2. Text field for 2nd Tag
        ...
        10. Text field for 10th Tag
        """
        return {"container": launcherQmlView_contentScrollView_ScrollView, "echoMode": 0, "id": "textField", "occurrence": occurrence, "type": "TextField", "unnamed": 1, "visible": True}
    
    @staticmethod
    def data_path_input_fields(occurance: int) -> dict:
        """
        occurance:
        8. Scan results
        9. Exported reports
        10. Android/iOS 
        11. licenses
        12. Whitelists
        13. Search Profiles
        """
        assert occurance in range(8, 14)
        return  {"container": launcherQmlView_contentScrollView_ScrollView, "echoMode": 0, "id": "textField", "occurrence": occurance, "type": "TextField", "unnamed": 1, "visible": True}
        
    @staticmethod
    def scan_information_fields_input_field(occurance: int) -> dict:
        """
        occurance:
        IF NO custom field:
        7. Enter new field name
        
        IF 1 custom field is added:
        7. Field Name for 1st custom field
        8. Field Value for 1st custom field
        9. Enter bew field name
        
        IF 2 custom fields are added:
        7. Field Name for 1st custom field
        8. Field Value for 1st custom field
        9. Field Name for 2nd custom field
        10. Field Value for 2nd custom field
        11. Enter bew field name
        
        etc.
        """
        
        return {"container": launcherQmlView_contentScrollView_ScrollView, "echoMode": 0, "id": "textField", "occurrence": occurance, "type": "TextField", "unnamed": 1, "visible": True}
        
    
    class Errors:
        
        @staticmethod
        def mandatory_field_error_msg(occurance: int) -> dict:
            """
            "Mandatory field. Enter a path." Dynamically displayed error message"
            occurance:
            1. Scan results error 
            2. Exported reports
            3. Android/iOS backups
            4. Licenses backup
            5. Whitelists
            6. Search profile
            
            """
            assert occurance in range(1,7)
            return {"container": launcherQmlView_contentScrollView_ScrollView,"occurrence": occurance, "text": "Mandatory field. Enter a path.", "type": "Text", "unnamed": 1, "visible": True}
            
        
        @staticmethod
        def unsupported_characters_error_msg(occurance: int) -> dict:
            """
            "Unsupported characters. Use only letters, numbers, and file system punctuation"
            occurance:
            1. Scan results error 
            2. Exported reports
            3. Android/iOS backups
            4. Licenses backup
            5. Whitelists
            6. Search profile
            
            """
            assert occurance in range(1,7)
            return {"container": launcherQmlView_contentScrollView_ScrollView, "occurrence": occurance, "text": "Unsupported characters. Use only letters, numbers, and file system punctuation.", "type": "Text", "unnamed": 1, "visible": True}
            
        
        @staticmethod
        def path_is_too_long_error_msg(occurance: int) -> dict:
            """
            "Path is too long. Maximum 200 characters."
         occurance:
        1. Scan results
        2. Exported reports
        3. Android/iOS 
        4. licenses
        5. Whitelists
        6. Search Profiles
        """
            assert occurance in range(1, 7)
            return   {"container": launcherQmlView_contentScrollView_ScrollView, "occurrence": occurance, "text": "Path is too long. Maximum 200 characters.", "type": "Text", "unnamed": 1, "visible": True}
