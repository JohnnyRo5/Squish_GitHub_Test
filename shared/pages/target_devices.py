# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *
from squish import *

class TargetDevices:
    
    add_remote_agent = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "addRemoteAgentButton", "type": "ToolBarButton", "visible": True}
    add_folder_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "addFolderButton", "type": "ToolBarButton", "visible": True}
    add_device_acquisition_btn = {"container": launcherQmlView_QQuickView, "id": "addDeviceAcquisitionComboBox", "type": "ComboBox", "unnamed": 1, "visible": True}
    add_image_btn = {"container": launcherQmlView_QQuickView, "id": "addImageComboBox", "type": "ComboBox", "unnamed": 1, "visible": True}
    add_phone_backup_popup = {"container": launcherQmlView_Overlay, "type": "Rectangle", "unnamed": 1, "visible": True}
    adf_phone_popup_option_dialog = {"container": select_the_ADF_mobile_device_acquisition_Dialog, "text": "Select Folder", "type": "Button"}
    no_itunes_backup_found_error_message = {"container": launcherQmlView_QQuickView, "text": "No iTunes backup found.", "type": "Text", "unnamed": 1, "visible": True}
    itunes_backup_is_encrypted_warning_message = {"container": launcherQmlView_QQuickView, "text": "The selected iTunes backup is encrypted. Please enter the password to proceed.", "type": "Text", "unnamed": 1, "visible": True}
    password_text_field_popup = {"container": launcherQmlView_QQuickView, "occurrence": 3, "source": "qrc:/common_skin_default/graphics/basic_backgrounds/transparent_background.sci", "type": "BorderImage", "unnamed": 1, "visible": True}
    ok_button_popup = {"container": launcherQmlView_QQuickView, "text": "OK", "type": "Text", "unnamed": 1, "visible": True}
    proceed_button_popup = {"container": launcherQmlView_QQuickView, "text": "PROCEED", "type": "Text", "unnamed": 1, "visible": True}
    checking_password_text_popup = {"container": launcherQmlView_QQuickView, "text": "Checking Password...", "type": "Text", "unnamed": 1, "visible": True}
    entered_password_not_accepted_text_popup = {"container": launcherQmlView_QQuickView, "text": "The entered password is not accepted. Please try again.", "type": "Text", "unnamed": 1, "visible": True}
    
    back_btn = {"checkable": False, "container": launcherQmlView_QQuickView, "objectName": "scanPageBackButton", "type": "ToolBarButton", "visible": True}
    
    @staticmethod
    def hard_disk_icon(icon_number: int) -> dict:
        return {"container": launcherQmlView_scanTargetsScrollView_StyledScrollView, "id": "typeIcon", "occurrence": icon_number, "source": "qrc:/common_skin_default/graphics/target_icons/hard_drive_icon_48_48.png", "type": "Image", "unnamed": 1, "visible": True}
    
    
    @staticmethod
    def usb_icon(icon_number: int) -> dict:
        return {"container": launcherQmlView_scanTargetsScrollView_StyledScrollView, "id": "typeIcon", "occurrence": icon_number, "source": "qrc:/common_skin_default/graphics/target_icons/flash_drive_icon_48_48.png", "type": "Image", "unnamed": 1, "visible": True}
    
    
    @staticmethod
    def folder_icon(icon_number: int) -> dict:
        return {"container": launcherQmlView_scanTargetsScrollView_StyledScrollView, "id": "typeIcon", "occurrence": icon_number, "source": "qrc:/common_skin_default/graphics/target_icons/folder_icon_48_48.png", "type": "Image", "unnamed": 1, "visible": True}
    
    @staticmethod
    def get_target_device_by_text(text: str):
        return {"container": launcherQmlView_scanTargetsScrollView_StyledScrollView, "text": text, "type": "Text", "unnamed": 1, "visible": True}
    
    @staticmethod
    def select_device_acquisition(option_name: str):
        options = {
                "ADF Android": (360, 160),
                "ADF iOS": (360, 210),
                "ADF ChromeOS": (360, 250),
                "iTunes backup": (360, 300),
                "GrayKey": (360, 340),
                "UFED": (360, 390),
            }

        snooze(1)
        import pyautogui
        x, y = options[option_name]
        pyautogui.click(x, y)
        
    @staticmethod
    def remote_agent_name(pc_name, ip):
        return {"container": launcherQmlView_QQuickView, "text": f"{pc_name} - {ip}", "type": "Text", "unnamed": 1, "visible": True}