import os
from xml.dom.minidom import parse
from junitparser import TestCase, TestSuite, JUnitXml, Skipped, Error, Attr ,TestCase, Attr, IntAttr, FloatAttr,Element
from lxml.etree import XMLParser, parse


def parse_func(xml_file1):
    xml_parser = XMLParser(huge_tree=True)
    return parse(xml_file1, xml_parser)

def convert_test_results(src_result_path,dst_result_path):
    if not os.path.exists(dst_result_path):
        os.mkdir(dst_result_path)
    for suite in os.listdir(src_result_path):
        # get location of JUnit report is not a folder anymore is just the xml file directly
        res_file_path = src_result_path + "\\" + suite
        print(res_file_path)
        # open JUnit report
        xml = JUnitXml.fromfile(res_file_path, parse_func)

        list_of_logs_from_report = []

        # Create the new element 'skipped'
        # and add custom attributes to it :
        # <skipped type="skipped" message="skipped"/>


        skipped = "skipped"
        number_of_skipped_tests = 0
        number_of_testcases = 0

        # parse the XML to get to the <system-out> logs where all the information is stored (e.g. skipped tests )
        for testcase in xml:
            number_of_testcases+=1
            for log in testcase:
                if log.text == None:
                    continue
                # search every log for skipped ( use test.log("skipped") , test.skip(message) in squish tests )
                #list_of_logs_from_report.append(log.text)
                find_skipped = log.text
                if skipped in find_skipped:
                    # if skipped found append new element 'skipped' to it
                    class CustomElement(Element):
                        _tag = 'skipped'
                        type = Attr('skipped')
                        message = Attr("skipped")

                    custom = CustomElement()
                    custom.type = 'skipped'
                    custom.message = 'skipped'
                    testcase.append(custom)
                    print("Found!")
                number_of_skipped_tests += find_skipped.count(skipped)
        # count the total number of skipped tests ( use test.log("skipped") , test.skip(message) in squish tests )
        #for log in list_of_logs_from_report:
        #    number_of_skipped_tests+=log.count(skipped)

        # get total number of tests (is equal to number of PASS verifications in tests) ,skipped,failures,errors from squish generated xml report file
        print(f"Number of Skipped tests : {number_of_skipped_tests}")
        print(f"Number of Test Cases : {number_of_testcases}")
        print(f"Number of Fails : {xml.failures}")
        print(f"Number of Errors : {xml.errors}")
        print(f"Number of Passes in one test : {xml.tests}")
        #
        # # get any attribute from testsuite header from xml report file
        #print(xml.__getattribute__("time"))
        #
        # # set any attribute from testsuite header from xml report file
        xml.__setattr__("skipped",number_of_skipped_tests)

        xml.__setattr__("hostname", number_of_testcases)
        #
        # # save new xml that has skipped attribute to new location
        dst_file_path = dst_result_path + "\\" + suite
        xml.write(dst_file_path)
