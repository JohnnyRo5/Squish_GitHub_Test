Feature: Captures

    This test is to verify that when the user clicks on the Manage Search Profile menu option ->
    the Manage Search Profile screen shop display.

    Steps:
    1. Launch DEI and navigate to Home Page -> Scan Setup & Key Management.
    2. Click on Manage Search Profiles
    3. Verify that user is redirected to Manage Search Profiles page as per requirement in FIV-3221

    Scenario: User can navigate to manage search profiles

        Given the user launches DEI
        And navigate to Home Page -> Scan Setup & Key Management
        When the user clicks on Manage Search Profiles
        Then user is redirected to Manage Search Profiles page