from objectmaphelper import *
from .names import *


class DefineFilesToCollect:
    capture_group_name_textbox = {"container": launcherQmlView_QQuickView, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    capture_name_textbox = {"container": launcherQmlView_QQuickView, "occurrence": 2, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    save_btn = {"container": launcherQmlView_QQuickView, "id": "background", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c8.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    
    class FileTypes:
        all_files_radiobox = {"checkable": True, "container": launcherQmlView_contentAreaScrollView_StyledScrollView, "id": "allFilesRadioButton", "text": "All Files", "type": "StyledRadioButton", "unnamed": 1, "visible": True}


    class Options:
        excluded_folders_btn = {"container": launcherQmlView_ScrollView, "id": "excludedFoldersListItem", "type": "SettingsListItem", "unnamed": 1, "visible": True}
        view_btn = {"container": launcherQmlView_ScrollView, "id": "actionItem", "occurrence": 23, "type": "Column", "unnamed": 1, "visible": True}
        
        # File identification methods
        thorough_identification_for_all_files_radiobox = {"checkable": True, "container": launcherQmlView_contentAreaScrollView_StyledScrollView, "id": "thoroughIdentificationOnAllFileTypesRadioButton", "text": "Thorough identification for all files", "type": "CaptureOptionRadioButton", "unnamed": 1, "visible": True}
    
    class FileSources:
        entire_file_system_checkbox = {"container": launcherQmlView_contentAreaScrollView_StyledScrollView, "occurrence": 18, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "HoveredActivatedBackground", "unnamed": 1, "visible": True}
        
    
    class ExcludedFolders:
        exclude_folder_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "exludeFolderButton", "type": "ToolBarButton", "visible": True}
        empty_directory_field = {"container": launcherQmlView_scrollView_ScrollView, "echoMode": 0, "id": "textField", "occurrence": 2, "type": "TextField", "unnamed": 1, "visible": True}
        delete_btn = {"container": launcherQmlView_scrollView_ScrollView, "id": "actionItem", "occurrence": 2, "type": "Column", "unnamed": 1, "visible": True}
        
        #Validation error messages
        mandatory_value_error_message = {"container": launcherQmlView_scrollView_ScrollView, "text": "Mandatory value. Enter a folder.", "type": "Text", "unnamed": 1, "visible": True}
        invalid_expression_error_message = {"container": launcherQmlView_scrollView_ScrollView, "text": "Invalid regular expression.", "type": "Text", "unnamed": 1, "visible": True}


        
