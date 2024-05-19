from objectmaphelper import *
from .names import *
from object import *
from squish import *


class DefineKeywordCapture:
    
    import_list_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "importButton", "type": "ToolBarButton", "visible": True}
    ok_modal_button = {"container": launcherQmlView_QQuickView, "occurrence": 2, "text": "OK", "type": "Text", "unnamed": 1, "visible": True}
    warnings_errors_message = {"container": launcherQmlView_QQuickView, "id": "progressbarTextSecondLine", "type": "Text", "unnamed": 1, "visible": True}
    import_log_area = {"container": launcherQmlView_QQuickView, "id": "importLogArea", "type": "TextAreaItem", "unnamed": 1, "visible": True}
    import_errors_area = {"container": launcherQmlView_calcErrorsArea_TextAreaItem, "id": "textArea", "type": "TextArea", "unnamed": 1, "visible": True}
    ok_modal_after_import_button = {"container": launcherQmlView_QQuickView, "occurrence": 2, "text": "OK", "type": "Text", "unnamed": 1, "visible": True}
    cancel_top_button = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "editFileCaptureLayoutCornerButton", "type": "ToolBarButton", "visible": True}
    