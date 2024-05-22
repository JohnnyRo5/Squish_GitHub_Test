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

    # Get test results from xml files
    for filename in os.listdir(FILE_PATH):
        if filename.endswith('.xml'):
            fullname = os.path.join(FILE_PATH, filename)
            testsuites = ET.parse(fullname)
            testsuite = testsuites.getroot()
            total += int(testsuite.attrib['tests'])
            errors += int(testsuite.attrib['errors'])
            failures += int(testsuite.attrib['failures'])
            skipped += int(testsuite.attrib['skipped'])
            time += float(testsuite.attrib['time'])
    successes = total - errors - failures - skipped
    time_converted = strftime("%H:%M:%S", gmtime(time))
    print(f'💻 *DESKTOP UI(DEI) TESTS* - {DATE}')
    print(f'Successes: {successes}')
    print(f'Total number of tests: {total}')
    print(f'Errors: {errors}')
    print(f'Failures: {failures}')
    print(f'Skipped: {skipped}')
    print(f'Total time: {time_converted}')
    # Post message to google chat
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    data = {
        'text': f'💻 *DESKTOP UI(DEI) TESTS* - {DATE}\n'
                f'Total number of tests: _{total}_\n'
                f'Passed ✅: _{successes}_\n'
                f'Failed ❌: _{failures}_\n'
                f'Errors 🔥: _{errors}_\n'
                f'Skipped ⏭️: _{skipped}_\n'
                f'Total time ⏱️: _{time_converted}_\n'
    }

    # response = requests.post(WEBHOOK, headers=headers, data=json.dumps(data))
    # if response.ok:
    #     print("Message posted.")
    # else:
    #     print(response.content)

