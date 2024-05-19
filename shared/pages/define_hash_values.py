from objectmaphelper import *
from .names import *
from object import *
from squish import *


class DefineHashValues:
    cancel_top_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "editFileCaptureLayoutCornerButton", "type": "ToolBarButton", "visible": True}
    import_list_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "importCsvButton", "type": "ToolBarButton", "visible": True}
    import_vics_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "importVicsJsonButton", "type": "ToolBarButton", "visible": True}
    import_caid_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "importCaidJsonButton", "type": "ToolBarButton", "visible": True}
    import_modal_button = {"caption": "IMPORT", "container": launcherQmlView_QQuickView, "id": "importOptionsAcceptButton", "type": "CommonButton", "unnamed": 1, "visible": True}
    ok_modal_button = {"caption": "OK", "container": launcherQmlView_QQuickView, "id": "tagsAndCommentsSettingsOkButton", "type": "CommonButton", "unnamed": 1, "visible": True}
    ok_modal_after_import_button = {"container": launcherQmlView_QQuickView, "text": "OK", "type": "Text", "unnamed": 1, "visible": True}
    hash_values_imported_message = {"container": launcherQmlView_QQuickView, "id": "progressbarTextFirstLine", "type": "Text", "unnamed": 1, "visible": True}
    warnings_errors_message = {"container": launcherQmlView_QQuickView, "id": "progressbarTextSecondLine", "type": "Text", "unnamed": 1, "visible": True}
    skipped_records_message = {"container": launcherQmlView_QQuickView, "id": "calcErrorsArea", "type": "TextAreaItem", "unnamed": 1, "visible": True}
    auto_comment_max_length_error = {"container": launcherQmlView_captureDataTable_CaptureDataTable, "text": "Text is too long. Maximum 1000 characters.", "type": "Text", "unnamed": 1, "visible": True}
    import_log_area = {"container": launcherQmlView_calcLogArea_TextAreaItem, "id": "textArea", "type": "TextArea", "unnamed": 1, "visible": True}
    import_errors_area = {"container": launcherQmlView_calcErrorsArea_TextAreaItem, "id": "textArea", "type": "TextArea", "unnamed": 1, "visible": True}
    export_errors_button = {"caption": "Export Errors", "container": launcherQmlView_QQuickView, "objectName": "exportErrorsButton", "type": "CommonButton", "visible": True}
    
    @staticmethod
    def get_category_by_name(category_name: str):
        return {"container": launcherQmlView_captureDataTable_CaptureDataTable, "text": category_name, "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_auto_comment_field_by_index(index: int):
        return {"container": launcherQmlView_captureDataTable_CaptureDataTable, "occurrence": index, "echoMode": 0, "id": "textField", "type": "TextField", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_include_hash_comments_by_index(index: int):
        return {"container": launcherQmlView_captureDataTable_CaptureDataTable, "id": "includeHashCommentsCheckBoxContainerItem", "occurrence": index, "type": "Item", "unnamed": 1, "visible": True}
    