# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class ReviewScanResults:
    first_scan_result_in_list = {"container": launcherQmlView_scanResultsListView_ResultsListView, "id": "scanResultAdvancedListItem", "index": 0, "type": "ListItem", "unnamed": 1, "visible": True}
    
    report_btn = {"container": launcherQmlView_scanResultsListView_ResultsListView, "id": "actionItem", "occurrence": 2, "type": "Column", "unnamed": 1, "visible": True}
    delete_btn = {"caption": "Delete", "container": launcherQmlView_scanResultsListView_ResultsListView, "objectName": "ScanResultsActionItem#Delete", "type": "ActionItem", "visible": True}
    view_btn = {"container": launcherQmlView_scanResultsListView_ResultsListView, "id": "actionImage", "source": "qrc:/common_skin_default/graphics/common_icons/move_forward_arrow_icon_32_32.png", "type": "Image", "unnamed": 1, "visible": True}
    
    back_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "scanResultsListAdvancedBackButton", "type": "ToolBarButton", "visible": True}

    remove_mobile_device_acquisition_popup = {"container": launcherQmlView_QQuickView, "id": "background", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    acquisition_item = {"container": launcherQmlView_relatedAcquisitionsList_RelatedAcquisitionsList, "id": "acquisitionItem", "index": 0, "type": "ListItem", "unnamed": 1, "visible": True}
    yes_button = {"caption": "YES", "container": launcherQmlView_QQuickView, "id": "acceptQuitButton", "type": "CommonButton", "unnamed": 1, "visible": True}
    no_button = {"caption": "NO", "container": launcherQmlView_QQuickView, "id": "rejectQuitButton", "type": "CommonButton", "unnamed": 1, "visible": True}
    
    acquisition_name = {"container": launcherQmlView_relatedAcquisitionsList_RelatedAcquisitionsList, "text": "test_backup", "type": "Text", "unnamed": 1, "visible": True}
    acquisition_size = {"container": launcherQmlView_relatedAcquisitionsList_RelatedAcquisitionsList, "text": "227.4MB", "type": "Text", "unnamed": 1, "visible": True}
    
    undo_btn = {"container": launcherQmlView_scanResultsListView_ResultsListView, "id": "focusRectangle", "type": "Rectangle", "unnamed": 1, "visible": True}
    
    search_tables = launcherQmlView_buttonIcon_Image = {"container": launcherQmlView_QQuickView, "id": "buttonIcon", "source": "qrc:/common_skin_default/graphics/main_toolbar_icons/keyword_search_icon_32_32.png", "type": "Image", "unnamed": 1, "visible": True}
    
    enter_text_placeholder = {"container": launcherQmlView_QQuickView, "text": "Enter text...", "type": "PlaceholderText", "unnamed": 1, "visible": True}
    
    launcherQmlView_Properties_Tab = {"container": launcherQmlView_QQuickView, "title": "Properties ", "type": "Tab", "unnamed": 1, "visible": True}

    property_name_text = {"container": launcherQmlView_Properties_Tab, "id": "propertyTextValue", "type": "TextEdit", "unnamed": 1, "visible": True}

    
    tool_bar_search_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "searchButton", "type": "ToolBarButton", "visible": True}
    
    combo_box = {"container": launcherQmlView_QQuickView, "id": "searchResultsComboBox", "type": "ComboBox", "unnamed": 1, "visible": True}
    
    counter = {"container": launcherQmlView_QQuickView, "objectName": "currentTotalText", "type": "Text", "visible": True}

    tag_btn = {"container": launcherQmlView_scanResultsListView_ResultsListView, "objectName": "addTagComboBox", "type": "ScanResultsListItemTagComboBox", "visible": True}
    current_tag_of_first_scan = {"container": launcherQmlView_scanResultsListView_ResultsListView, "type": "Rectangle", "unnamed": 1, "visible": True}
    
    @staticmethod
    def tag(color: str):
        available_colors = ['white', 'gray', 'red', 'yellow', 'dark_green', 'light_green', 'dark_blue', 'ligth_blue',
                            'orange', 'purple', 'pink']
        occurrences = [i + 1 for i in range(len(available_colors))]
        assert color in available_colors
        color_occurrence = dict(zip(available_colors, occurrences))
        return {"container": launcherQmlView_Overlay, "occurrence": color_occurrence[color], "type": "Rectangle", "unnamed": 1, "visible": True}
    
    
    @staticmethod
    def combo_box_text(text: str) -> dict:
        return {"container": launcherQmlView_QQuickView, "text": text, "type": "Text", "unnamed": 1, "visible": True}
    
    
    @staticmethod
    def arrow(direction: str) -> dict:
        assert direction in ("back", "forward")
        arrow_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "forwardButton", "type": "ToolBarButton", "visible": True} if direction == 'forward' else {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "backwardButton", "type": "ToolBarButton", "visible": True}
        return arrow_button
        
    class ErrorMessage:
        
        @staticmethod
        def error(error: str) -> dict:
            return {"container": launcherQmlView_QQuickView, "text": error, "type": "Text", "unnamed": 1, "visible": True}

      
    class Views:
        
        @staticmethod
        def cross_capture_view(view_type: str) -> dict:
            assert view_type in ('summary', 'pictures', 'videos', 'keywords', 'timeline', 'files', 'scan log', 'tagged')
            types: dict = {'summary': 0, 'pictures': 1, 'videos': 2, 'keywords': 3, 'timeline': 4, 'files': 5,'scan log': 6, 'tagged': 7}
            
            return {"container": launcherQmlView_QQuickView, "id": "crossCapturesDelegate", "index": types[view_type], "type": "CrossCapturesListDelegate", "unnamed": 1, "visible": True}
          
    
    
    
