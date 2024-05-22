import datetime
from pages.home_page import HomePage
from pages.names import *
from action_methods import is_visible
from application import application
from action_methods import click
from pages.investigate_device import InvestigateDevice
from pages.search_profile import SearchProfile
from decorators import time_tracker

"""
Test that an error appears if we try to select a faulty time-range

Steps:
1. Navigate to the scan screen
2. Select a faulty time-range (eg starting from 2019 ending in 2017)
3. Check that an error appears
"""

FIRST_DATE = datetime.date(2017, 7, 7)
SECOND_DATE = datetime.date(2019, 7, 7)


@time_tracker
def main():
    # Start DEI
    application.start(to_home_page=True)
    
    
    click(HomePage.investigate_device_button)
    
    click(InvestigateDevice.scan_button)
    click(SearchProfile.limit_data_collection_between_btn)

    # Test that if the interval is wrong an error will appear
    SearchProfile.define_timerange_for_scan(SECOND_DATE, FIRST_DATE)

    second_date_str = SECOND_DATE.strftime('%Y/%m/%d')
    second_date_error = {
        "container": launcherQmlView_QQuickView,
        "text": f"Set after {second_date_str}.",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    }

    test.verify(is_visible(second_date_error))
