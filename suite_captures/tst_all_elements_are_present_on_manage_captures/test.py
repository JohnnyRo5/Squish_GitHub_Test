from pages.home_page import HomePage
from pages.setup_scans_and_key_management import ScanSetupAndKeyManagement
from pages.manage_captures import ManageCaptures
from decorators import time_tracker
from application import application
from action_methods import *


@time_tracker
def main():
    
    """
   This test is to verify that:
   The Manage Captures screen should list all the Capture Groups and when a Capture Group is selected, 
   the Captures associated with that Capture Group should be displayed.
    Steps:
    1. Launch DEI and navigate to Home Page -> Scan Setup & Key Management.
    2. Click on Manage Captures
    3. Select a capture group in Capture group list
    4. Verify that Captures are valid for specific Capture Group
    """
    
    # Start DEI 
    application.start(to_home_page = True)
    
    # Navigate to Scan Setup & Key Management
    click(HomePage.scan_setup_and_key_management_button)
    
    # Click Manage Captures button
    click(ScanSetupAndKeyManagement.manage_captures_btn)
    
    # Verification point. Verify that Captures associated with that Capture Group is displayed
    capture_groups = ["APPLICATIONS", "CHILD EXPLOITATION", "COMMUNICATION", "DEVICE DATA", "DOCUMENTS", "INTEL KEYWORDS", "MULTIMEDIA", "USER DATA", "WEB BROWSERS"]
    captures = ["Anti-Forensics Traces", "CE - Keywords in Filenames", "Emails", "Database Files", "Referenced Files", "Domestic Security", "Audio Files", "Calendar", "Bookmarks"]
    snooze(0.5)
    for capture_group, capture in zip(capture_groups, captures):
        click(ManageCaptures.capture_groups(capture_group))
        test.verify(is_visible(ManageCaptures.captures(capture)))
        
