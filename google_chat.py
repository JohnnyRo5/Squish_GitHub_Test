import xml.etree.ElementTree as ET
import pathlib
import os
import json
import requests
import sys
from json import dumps
from datetime import datetime
from zoneinfo import ZoneInfo
from time import strftime
from time import gmtime



FILE_PATH = "C:\\Report\\results\\final"
WEBHOOK = 'https://chat.googleapis.com/v1/spaces/AAAAIMBcDDo/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=1z3JAI0M6VF0XfO38rG3Zgp9_r9FibupxpimNkLMnMY'
DATE = datetime.now(ZoneInfo('GMT')).strftime("%d %B %Y")

if __name__ == '__main__':
    total = 0
    errors = 0
    failures = 0
    skipped = 0
    successes = 0
    time = 0
    number_of_passes=0

    # Get test results from xml files
    for filename in os.listdir(FILE_PATH):
        if filename.endswith('.xml'):
            fullname = os.path.join(FILE_PATH, filename)
            testsuites = ET.parse(fullname)
            testsuite = testsuites.getroot()
            number_of_passes += int(testsuite.attrib['tests'])
            total += int(testsuite.attrib['hostname'])
            errors += int(testsuite.attrib['errors'])
            failures += int(testsuite.attrib['failures'])
            skipped += int(testsuite.attrib['skipped'])
            time += float(testsuite.attrib['time'])
    successes = total - errors - failures - skipped
    time_converted = strftime("%H:%M:%S", gmtime(time))
    # Post message to google chat
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    data = {
        'text': f'💻 *DESKTOP UI(DEI) TESTS* - {DATE}\n'
                f'Total Number of Test Cases: _{total}_\n'
                f'Number of verifications in Test Cases ✅: _{number_of_passes}_\n'
                f'Number of Fails ❌: _{failures}_\n'
                f'Number of Errors 🔥: _{errors}_\n'
                f'Number of Skipped ⏭️: _{skipped}_\n'
                f'Duration ⏱️: _{time_converted}_\n'
    }

    #response = requests.post(WEBHOOK, headers=headers, data=json.dumps(data))
    # if response.ok:
    #     print("Message posted.")
    # else:
    #     print(response.content)

