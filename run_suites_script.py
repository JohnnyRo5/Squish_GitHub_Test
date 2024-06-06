import os
import shutil
import subprocess
import configparser
import psutil
import parse_junit as add_skipped_to_junit_report

SQUISH_BIN_FOLDER_PATH = "C:\\Squish_for_Qt_6.7.2\\bin"
SUITES_DIR_PATH = "C:\\Squish_tests_suites\\autotests_dei_ui_local"
XML3_REPORTS_PATH = os.path.join("C:\\Report", "results", "xml")
HTML_REPORTS_PATH = os.path.join("C:\\Report", "results", "web_report")
# Path to folder for final results
FINAL_REPORTS_PATH = os.path.join("C:\\Report", "results", "final")

skipped_suites = [
    'suite_1st_setup_app',
    'suite_audit_trail',
    #'suite_captures',
    'suite_cky_creation_tests',
    #'suite_date_range_tests',
    'suite_export_tests',
    'suite_filtering',
    'suite_imaging',
    'suite_license_token_server',
    'suite_misc_tests',
    'suite_mobile_scan_tests',
    'suite_remote_agent',
    'suite_scan_results',
    'suite_scan_tests',
    'suite_search_button',
    'suite_settings',
    'suite_set_data_path',
    'suite_viewer',
]
def get_suites_paths(suites_dir_path):
    suites_list = []
    folders_list = os.listdir(suites_dir_path)
    for suite in folders_list:
        if str(suite).startswith("suite_"):
            if str(suite) in skipped_suites:
                continue
            suites_list.append(os.path.join(suites_dir_path, suite))

    for suite_name in suites_list:
        print(suite_name)
    return suites_list



def run_squish_tests(suites_list,xml3_reports_path,html_reports_path):
    squish_server = os.path.join(SQUISH_BIN_FOLDER_PATH, "squishserver")
    squish_runner = os.path.join(SQUISH_BIN_FOLDER_PATH, "squishrunner")

    # Run squish server
    subprocess.call([squish_server, "--verbose"])

    print(f"\nSUCCESSFULLY ADDED SUITES LIST: {suites_list}\n")
    for suite in suites_list:
        print(suite)
        print(squish_runner)
        path_elements = suite.split(os.sep)
        report_name = path_elements[-1][6:]
       # subprocess.call(f"{squish_runner} --testsuite {suite} --local --exitCodeOnFail 13  --reportgen junit,C:\\Report\\xml\\junit_report.xml --reportgen html,C:\\Report\\web_report",shell=True)


        subprocess.call(
            [
                squish_runner,
                "--debugLog",
                "alpw",
                "--testsuite",
                suite,
                "--reportgen",
                "junit," + xml3_reports_path + "\\" + report_name+".xml",
                "--reportgen",
                "html," + html_reports_path
            ])

if __name__ == "__main__":
    suites = get_suites_paths(SUITES_DIR_PATH)
    run_squish_tests(suites,XML3_REPORTS_PATH,HTML_REPORTS_PATH)
    add_skipped_to_junit_report.convert_test_results(XML3_REPORTS_PATH, FINAL_REPORTS_PATH)
