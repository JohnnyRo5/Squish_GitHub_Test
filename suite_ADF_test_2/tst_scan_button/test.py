# -*- coding: utf-8 -*-

import names


def main():
    startApplication("adf-dei")
    mouseClick(waitForObject(names.itemsScrollView_Scan_hard_drives_storage_media_data_containers_or_connected_Android_iOS_devices_Text))
    mouseClick(waitForObject(names.searchProfilesView_RadioButtonIndicator), 10, 13, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.searchProfilesView_USE_ONLY_ON_THE_SYSTEM_DRIVE_OF_COMPUTERS_Runs_all_Artifact_Captures_excluding_Email_and_P2P_searches_for_anti_forensic_traces_social_media_traces_remote_access_traces_files_in_the_Skype_caches_and_pictures_and_videos_in_the_browser_cache_and_carves_pictures_from_system_cache_files_Text).text), "USE ONLY ON THE SYSTEM DRIVE OF COMPUTERS - Runs all Artifact Captures excluding Email and P2P, searches for anti forensic traces, social media traces, remote access traces, files in the Skype caches and pictures and videos in the browser cache and carves pictures from system cache files.")
