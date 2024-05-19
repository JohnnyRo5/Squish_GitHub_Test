# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *


class ScanFilesSection:
    tags_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "tagsButton", "type": "ToolBarButton", "visible": True}
    report_btn = {"container": launcherQmlView_QQuickView, "id": "deletageBackground", "occurrence": 8, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    first_item_in_list = {"container": launcherQmlView_viewScanResultsCaptureTable_CaptureTable, "id": "rowitem", "rowIndex": 0, "type": "FocusScope", "unnamed": 1, "visible": True}
    records_count = {"container": launcherQmlView_QQuickView, "id": "recordsCountText", "type": "Text", "unnamed": 1, "visible": True}

    @staticmethod
    def get_artifact_by_row_index(index: int) -> dict:
        return {"container": launcherQmlView_viewScanResultsCaptureTable_CaptureTable, "id": "rowitem", "rowIndex": index, "type": "FocusScope", "unnamed": 1, "visible": True}