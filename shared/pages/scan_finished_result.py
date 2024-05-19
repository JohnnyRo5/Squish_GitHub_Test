# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *


class ScanFinishedResult:
    timeline = {"container": launcherQmlView_QQuickView, "id": "deletageBackground", "occurrence": 4, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    summary_btn = {"container": launcherQmlView_QQuickView, "id": "deletageBackground", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    close_btn = {"checkable": False, "container": LauncherQmlView_QQuickView, "objectName": "capturesSidePanelBackButton", "type": "ToolBarButton", "visible": True}
    launcherQmlView_Preview_Tab = {"container": launcherQmlView_QQuickView, "title": "Preview ", "type": "Tab", "unnamed": 1, "visible": True}

    preview_screen = {"container": launcherQmlView_Preview_Tab, "type": "QtWebEngineCore::RenderWidgetHostViewQtDelegateQuick", "unnamed": 1, "visible": True}
    preview_save_as_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "TollBarButton#Save as", "type": "ToolBarButton", "visible": True}
    preview_save_html_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "TollBarButton#Save HTML", "type": "ToolBarButton", "visible": True}
    
    first_artifact_row = {"container": launcherQmlView_viewScanResultsCaptureTable_CaptureTable, "id": "rowitem", "rowIndex": 0, "type": "FocusScope", "unnamed": 1, "visible": True}
    launcherQmlView_tabbar_TabBar = {"container": launcherQmlView_QQuickView, "objectName": "tabbar", "type": "TabBar", "visible": True}
    
    first_artifact_checkbox_check = {"container": first_artifact_row, "id": "checkImage", "source": "qrc:/common_skin_default/graphics/checkbox_related_items/checkbox_check_14_14.png", "type": "Image", "unnamed": 1, "visible": True}
   
    case_settings_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "viewerSettingsButton", "type": "ToolBarButton", "visible": True}
    automatically_uncheck_selected_records_after_tag_assignment_txt = launcherQmlView_Automatically_uncheck_selected_records_after_tag_assignment_Text = {"container": launcherQmlView_QQuickView, "text": "Automatically uncheck selected records after tag assignment", "type": "Text", "unnamed": 1, "visible": True}
    
    details_button = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "detailsModeButton", "type": "ToolBarButton", "visible": True}
    
    attachment_preview = {"container": launcherQmlView_QQuickView, "id": "previewImage", "type": "Image", "unnamed": 1, "visible": True}
   
    @staticmethod
    def get_artifact_by_row_index(index: int) -> dict:
        return {"container": launcherQmlView_viewScanResultsCaptureTable_CaptureTable, "id": "rowitem", "rowIndex": index, "type": "FocusScope", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_column_by_name(column_name: str):
        return {"container": launcherQmlView_viewScanResultsCaptureTable_CaptureTable, "text": column_name, "type": "Text", "unnamed": 1, "visible": True}

        
    @staticmethod
    def artifact_properties_tabs(text: str) -> dict:
        assert text in ['Properties', 'Metadata', 'Preview']
        return {"container": ScanFinishedResult.launcherQmlView_tabbar_TabBar, "text": f"{text} ", "type": "Text", "unnamed": 1, "visible": True}