test.log("skipped")


import re
import pathlib

from datetime import datetime, date
from action_methods import *
from common_actions import input_path_to_folder
from pages.timeline import Timeline
from pages.investigate_device import InvestigateDevice
from pages.search_profile import SearchProfile
from pages.target_devices import TargetDevices
from pages.scan_progress import ScanProgress
from pages.scan_finished_result import ScanFinishedResult
from pages.names import *
from decorators import time_tracker
from application import application
from names import *

# !!!!!!!!!!!!!!!!!!!!!!!
# SOMETIMES PROPERTIES TAB DOES NOT SHOW UP, that's why it crashes

""""
Test that when we select a time-range to scan within, records respect the time-range rules
and are only within the time-range

Pre-requisites: Intel.E01 image placed in the "test_data" folder

Steps:
1. Navigate to the scan screen
2. Select the E01 image and an appropriate time-range, and scan
3. Wait for the scan to complete, access the results
4. Go to the timeline page
5. Sort the timeline by date asc
6*. Check that all the records in the upper part of the screen respect the time-range
7*. Check that all the records in the bottom part of the screen respect the time-range

* We check this using the "properties" of the record, where we can find dates (like capture date,
installation date etc). For each type of capture, we look at different dates. Refer to the story.
For more info on which dates are chosen check FIV-2192
"""

# Time-range dates
FIRST_CAPTURE_DATE = date(2018, 3, 12)
LAST_CAPTURE_DATE = date(2018, 3, 14)
# Properties that contain a date
DATE_PROPERTIES = [
    "Last Written", "File Created", "Last Accessed", "Installed",
    "Installation Date", "Last Shutdown", "Event Time"
]
# Regex for finding a date, compile only once for optimization
DATE_REGEX = re.compile("([0-9]{4}/[0-9]{2}/[0-9]{2})")
DRIVE_NAME = "Demo_Intel.E01"
DRIVE_PATH = str(
    pathlib.Path(__file__).parent.parent.parent.resolve() / 
    "shared/big_test_data/Demo_Intel.E01")


def start_scan(firstCaptureDate: datetime, lastCaptureDate: datetime) -> None:
    application.start()
    click(InvestigateDevice.scan_button)
    click(SearchProfile.limit_data_collection_between_btn)
    # Test that if the interval is right no error will appear
    SearchProfile.define_timerange_for_scan(firstCaptureDate, lastCaptureDate)
    click(TargetDevices.add_image_btn)
    press_key("<Down>")
    press_key("<Down>")
    press_key("<Return>")

    input_path_to_folder(DRIVE_PATH)

    click(SearchProfile.search_profile("Quick - General Profiling"))
    click(SearchProfile.scan_button)
    mouseClick(waitForObject(ScanProgress.ok, 1000000))
    click(ScanProgress.view_results)
    click(ScanFinishedResult.timeline)


# Get a date out of a text
def parse_date(text: str) -> datetime:
    date_str = DATE_REGEX.findall(str(text))[0]
    date = datetime.strptime(date_str, '%Y/%m/%d').date()
    return date


# Sort the timelapse rows by y value
def sort_rows(reverse: bool) -> list:
    rows = [i for i in object.children(get_object(Timeline.rows_container))]
    rows.sort(key=lambda a:-a.y if reverse else a.y)
    return rows


# Get the date out of a property
def get_property_date(propertyDelegate) -> datetime:
    detailsPanePropertyValueLoader = object.children(propertyDelegate)[1]
    propertyTextValueColumn = object.children(
        detailsPanePropertyValueLoader)[0]
    if propertyTextValueColumn.id == "propertyTextValueColumn":
        valueRow = object.children(propertyTextValueColumn)[0]
    else:
        valueRow = propertyTextValueColumn
    propertyTextSingleLineValue = object.children(valueRow)[1]
    return parse_date(propertyTextSingleLineValue.text)


# Get the date from the timelapse for a row
def get_date(row):
    # Reach the text in the object tree
    rowitem_0 = object.children(row)[0]
    itemrow_1 = object.children(rowitem_0)[1]
    TableViewItemDelegateLoader_4 = object.children(itemrow_1)[4]
    autoTypeItem = object.children(TableViewItemDelegateLoader_4)[0]
    delegatesLoader = object.children(autoTypeItem)[0]
    multiline = object.children(delegatesLoader)[0]
    itemText = object.children(multiline)[1]
    displayText = object.children(itemText)[0]
    return parse_date(displayText.text)


# Check if a date is within the timerange
def check_timerange(date: datetime) -> bool:
    if date >= FIRST_CAPTURE_DATE and date <= LAST_CAPTURE_DATE:
        return True
    return False


# Check if all the dates from an artifact's properties are within the timerange
def check_row_date(properties: dict) -> bool:
    # We only want to include a file if the Last Written or File created timestamps are within the range
    if properties["isFile"]:
        if "Last Written" in properties:
            if check_timerange(properties["Last Written"]):
                return True
        if "File Created" in properties:
            if check_timerange(properties["File Created"]):
                return True
        return False
    # Else, if any property is within the range we include it
    for propertyName, propertyValue in properties.items():
        if propertyName is not "isFile":
            if check_timerange(propertyValue):
                return True
    return False


# Get all properties from a row
def get_row_properties():
    container = get_object(Timeline.row_properties)
    frameLoader = object.children(container)[2]
    stack = object.children(frameLoader)[0]
    Tab = object.children(stack)[0]
    propertiesListView = object.children(Tab)[0]
    propertiesTabScrollView = object.children(propertiesListView)[0]
    propertiesTabFlickable = object.children(propertiesTabScrollView)[0]
    Item_0 = object.children(propertiesTabFlickable)[0]
    propertiesTabLayout = object.children(Item_0)[0]
    propertyDelegate = object.children(propertiesTabLayout)
    return propertyDelegate[:-1]


# Select the needed properties of a row (from all the properties it has) and map them in a dictionary
def map_properties() -> dict:
    properties = {"isFile": False}
    for propertyDelegate in get_row_properties():
        propertyName = str(object.children(propertyDelegate)[0].text)
        if propertyName == "File Type":
            properties["isFile"] = True
        if propertyName in DATE_PROPERTIES:
            properties[propertyName] = get_property_date(propertyDelegate)
    return properties


# Click on the first row
def click_first_row(rows: list) -> None:
    for i in range(len(rows)):
        if rows[i].id == "rowItemContainer":
            click(rows[i])
            return


# Check the upper boundary of the timerange
def check_top() -> bool:
    mouseWheel(get_object(Timeline.scan_results_container), 0, 0, 0, 1100000,
               Qt.NoModifier)
    snooze(1)
    rows = sort_rows(False)
    while True:
        rows = sort_rows(False)
        rowCount = 0
        for row in rows:
            if rowCount == 15:
                break
            if row.id == "rowItemContainer":
                rowCount += 1
                row_date = get_date(row)
                if row_date <= LAST_CAPTURE_DATE:
                    return True
                else:
                    return False
        mouseWheel(get_object(Timeline.scan_results_container), 0, 0, 0, -221,
                   Qt.NoModifier)


# Check the lower boundary of the timerange
def check_bottom() -> bool:
    mouseWheel(get_object(Timeline.scan_results_container), 0, 0, 0, -1100000,
               Qt.NoModifier)
    snooze(1)
    rows = sort_rows(True)
    while True:
        rows = sort_rows(True)
        rowCount = 0
        for row in rows:
            if rowCount == 15:
                break
            if row.id == "rowItemContainer":
                rowCount += 1
                row_date = get_date(row)
                if row_date >= FIRST_CAPTURE_DATE:
                    return True
                elif row_date not in {date(2018, 2, 1), date(2018, 2, 7), date(2018, 2, 12), date(2018, 2, 14), date(2018, 2, 15)}:
                    return False
        mouseWheel(get_object(Timeline.scan_results_container), 0, 0, 0, 221,
                   Qt.NoModifier)


@time_tracker
def main():
    test.skip("skipped")
    # Go to a historic report
    start_scan(FIRST_CAPTURE_DATE, LAST_CAPTURE_DATE)

    # If the time-line is not sorted, sort it
    sort_object = Timeline.sorted_image
    if not is_visible(sort_object):
        click(Timeline.sort_button)
    
    snooze(1)
#     
#     expected_dates = ["2018/02/01 14:35:27", "2018/02/07 12:47:28", "2018/02/12 13:50:06",
#                       "2018/02/14 13:43:50", "2018/02/14 13:43:50", "2018/02/15 17:18:08"]
#     
#     for expected_date in expected_dates: 
#         should_be_visible({"container": viewScanResultsCaptureTable_rowitem_FocusScope, "text": expected_date, "type": "Text", "unnamed": 1, "visible": True})
#         
#     mouseWheel(get_object(Timeline.scan_results_container), 0, 0, 0, 1100000, Qt.NoModifier)

# mouseWheel(get_object(Timeline.scan_results_container), 0, 0, 0, 1100000,
#                Qt.NoModifier)
#     last_scan_row = {"container": launcherQmlView_viewScanResultsCaptureTable_CaptureTable, "id": "rowitem", "rowIndex": 0, "type": "FocusScope", "unnamed": 1, "visible": True}
#     double_click(last_scan_row)
#     
    # Go to the top and check elements with the upper limit
    test.verify(check_top())
    # Go to the bottom and check elements with the lower limit
    test.verify(check_bottom())
