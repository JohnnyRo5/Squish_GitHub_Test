# -*- coding: utf-8 -*-

import names


def main():
    startApplication("adf-dei")
    nativeType("<Alt+F4>")
    test.compare(waitForObjectExists(names.launcherQmlView_Do_not_display_this_warning_anymore_Text).visible, True)
    mouseClick(waitForObject(names.launcherQmlView_QUIT_Text))
    snooze(7)
