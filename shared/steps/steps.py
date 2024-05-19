# -*- coding: utf-8 -*-
from pages import names

@Given("the user launches DEI")
def step(context):
    startApplication("adf-dei")

@Given("navigate to Home Page -> Scan Setup & Key Management")
def step(context):
    try:
        screen = waitForObject({"container": names.launcherQmlView_QQuickView, "objectName": "homePageProductName", "type": "Text", "visible": True},2)
        if screen.text=="ADF Digital Evidence Investigator PRO":
            test.log("Already in Home Page")
    except:
        screen = waitForObject({"container": names.launcherQmlView_QQuickView, "objectName": "productName", "type": "Text", "visible": True})
        if screen.text =="Scan Setup & Key Management":
            mouseClick(waitForObject({"container": names.launcherQmlView_QQuickView, "text": "Back", "type": "Text", "unnamed": 1, "visible": True}))
        elif screen.text =="Investigate Device":
            mouseClick(waitForObject({"container": names.launcherQmlView_QQuickView, "text": "Back", "type": "Text", "unnamed": 1, "visible": True}))          
    mouseClick(waitForObject({"container": names.launcherQmlView_homePageScrollView_StyledScrollView, "text": "Create and edit Search Profiles/Captures, Prepare USB collection keys and Initialize Authentication Keys", "type": "Text", "unnamed": 1, "visible": True}))

@When("the user clicks on Manage Search Profiles")
def step(context):
    mouseClick(waitForObject({"container": names.launcherQmlView_itemsScrollView_StyledScrollView, "text": "Manage Search Profiles", "type": "Text", "unnamed": 1, "visible": True}))

@Then("user is redirected to Manage Search Profiles page")
def step(context):
    test.compare(str(waitForObjectExists({"container": names.launcherQmlView_QQuickView, "objectName": "pageTitle", "type": "Text", "visible": True}).text), "Manage Search Profiles")
