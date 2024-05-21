import os
import shutil
import subprocess


SQUISH_BIN_FOLDER_PATH = "C:\\Squish_for_Qt_6.7.2\\bin"
SUITES_DIR_PATH = "C:\\Squish_tests_suites\\autotests_dei_ui_local"
def get_suites_paths(suites_dir_path):
    suites_list = []
    folders_list = os.listdir(suites_dir_path)
    for suite in folders_list:
        if str(suite).startswith("suite_"):
            suites_list.append(os.path.join(suites_dir_path, suite))

    for suite_name in suites_list:
        print(suite_name)
    return suites_list



def run_squish_tests(suites_list):
    #squish_server = os.path.join(SQUISH_BIN_FOLDER_PATH, "squishserver")
    squish_runner = os.path.join(SQUISH_BIN_FOLDER_PATH, "squishrunner")

    # Run squish server
    #subprocess.Popen([squish_server])

    print(f"\nSUCCESSFULLY ADDED SUITES LIST: {suites_list}\n")
    for suite in suites_list:
        print(suite)
        print(squish_runner)
        path_elements = suite.split(os.sep)
        report_name = path_elements[-1][6:]
        subprocess.call(
            [
                squish_runner,
                "--debugLog",
                "alpw",
                "--testsuite",
                suite,
                "--reportgen",
                "junit," + xml3_reports_path + "\\" + report_name+"\\results.xml",
                "--reportgen",
                "html," + html_reports_path
            ])

if __name__ == "__main__":
    suites = get_suites_paths(SUITES_DIR_PATH)
    run_squish_tests(suites)
