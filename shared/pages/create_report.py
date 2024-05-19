import squish
from objectmaphelper import *
from .names import *

class CreateReport:
    
    export_btn = {"caption": "EXPORT", "container": launcherQmlView_QQuickView, "id": "exportButton", "type": "CommonButton", "unnamed": 1, "visible": True}
    
    all_records_checkbox = {"container": report_table, "objectName": "commonHeader_column#0", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "CommonHeaderDelegate", "visible": True}
    
    path_input_field = {"container": launcherQmlView_QQuickView, "echoMode": 0, "id": "textField", "type": "TextField", "unnamed": 1, "visible": True}
    
    export_completed_pop_up = {"container": launcherQmlView_QQuickView, "text": "Export completed", "type": "Text", "unnamed": 1, "visible": True}
    export_completed_ok_btn = {"container": launcherQmlView_QQuickView, "text": "OK", "type": "Text", "unnamed": 1, "visible": True}
    
    csv_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "csvFormatRadioButton", "text": "CSV", "type": "StyledRadioButton", "visible": True}
    html_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "htmlFormatRadioButton", "text": "HTML", "type": "StyledRadioButton", "visible": True}
    pdf_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "pdfFormatRadioButton", "text": "PDF", "type": "StyledRadioButton", "visible": True}
    vics_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "vicsFormatRadioButton", "text": "VICS", "type": "StyledRadioButton", "visible": True}
    standalone_viewer_radio_btn ={"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "standaloneViewerFormatRadioButton", "text": "Standalone viewer", "type": "StyledRadioButton", "visible": True}
    
    include_previews_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "previewsAndOriginalFilesRadioButton", "text": "Include previews and original files", "type": "StyledRadioButton", "visible": True}
    include_previews_tagged_only_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "previewsAndOriginalFilesForTaggedOnlyRadioButton", "text": "Include previews and original files of tagged records only", "type": "StyledRadioButton", "visible": True}
    sanitize_report_radio_btn = {"checkable": True, "container": launcherQmlView_QQuickView, "objectName": "sanitizeReportRadioButton", "text": "Sanitize report (no previews and no original files will be included) ", "type": "StyledRadioButton", "visible": True}
    
    no_tag_rectangle = {"container": report_table, "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
    report_table = {"container": launcherQmlView_QQuickView, "id": "contentTable", "type": "ReportSelectionTable", "unnamed": 1, "visible": True}
    
    checkbox_one = {"container": contentTable_rowitem_FocusScope_2, "id": "checkboxContainer", "type": "Item", "unnamed": 1, "visible": True}
    checkbox_two = {"container": contentTable_rowitem_FocusScope_3, "id": "checkboxContainer", "type": "Item", "unnamed": 1, "visible": True}
    checkbox_three = {"container": contentTable_rowitem_FocusScope, "id": "checkboxContainer", "type": "Item", "unnamed": 1, "visible": True}
    
    report_btn = {"container": launcherQmlView_QQuickView, "id": "deletageBackground", "source": "qrc:/common_skin_default/graphics/basic_backgrounds/background_c1.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    files_btn = {"container": launcherQmlView_QQuickView, "id": "deletageBackground", "occurrence": 6, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    
