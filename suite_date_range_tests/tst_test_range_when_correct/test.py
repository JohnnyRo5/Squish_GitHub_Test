import datetime

from pages.names import *
from action_methods import is_visible
from application import application
from action_methods import click
from pages.investigate_device import InvestigateDevice
from pages.search_profile import SearchProfile
from pages.home_page import HomePage
from decorators import time_tracker

"""
Test that no error appears if we select a good time-range

Steps:
1. Navigate to the scan screen
2. Select a good time-range (eg starting from 2017 ending in 2019)
3. Check that no error appears
"""

FIRST_DATE = datetime.date(2017, 7, 7)
SECOND_DATE = datetime.date(2019, 7, 7)


@time_tracker
def main():
    # Start the start
    application.start(to_home_page=True)
    
    
    click(HomePage.investigate_device_button)
    click(InvestigateDevice.scan_button)
    
    click(SearchProfile.limit_data_collection_between_btn)

    # Test that if the interval is wrong an error will appear
    SearchProfile.define_timerange_for_scan(FIRST_DATE, SECOND_DATE)

    first_date_str = FIRST_DATE.strftime('%Y/%m/%d')
    first_date_error = {
        "container": launcherQmlView_QQuickView,
        "text": f"Set after {first_date_str}.",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    }

    second_date_str = SECOND_DATE.strftime('%Y/%m/%d')
    second_date_error = {
        "container": launcherQmlView_QQuickView,
        "text": f"Set after {second_date_str}.",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    }

    test.verify(not is_visible(first_date_error))
    test.verify(not is_visible(second_date_error))
