*** Settings ***
Documentation               Check selenium hub and Webdriver
...
Metadata                    VERSION     0.1
Library                     Selenium2Library
Library                     Collections
Library                     OperatingSystem
Test Teardown              Close Browsers


*** Variables ***
${PAGE_URL}                 https://www.google.com
${HUB}                      http://127.0.0.1:4444/wd/hub

*** Keywords ***
Close Browsers
    Close All Browsers

*** Test Cases ***
Selenium hub Headless Chrome - Create Webdriver
    &{options} =	Create Dictionary	browserName=chrome	platform=ANY

    Create Webdriver    Remote   command_executor=${HUB}    desired_capabilities=${options}
    Go to     ${PAGE_URL}

    Maximize Browser Window
    Title Should Be         Google
    Capture Page Screenshot

Selenium hub Headless Chrome - Open Browser
    &{options} =	Create Dictionary	browserName=chrome	platform=ANY

    Open Browser    ${PAGE_URL}    browser=chrome    remote_url=${HUB}     desired_capabilities=${options}

    Maximize Browser Window
    Title Should Be         Google
    Capture Page Screenshot

Selenium hub Headless Firefox - Create Webdriver
    &{options} =	Create Dictionary	browserName=firefox  platform=ANY

    Create Webdriver    Remote   command_executor=${HUB}    desired_capabilities=${options}
    Go to     ${PAGE_URL}

    Maximize Browser Window
    Title Should Be         Google
    Capture Page Screenshot

Selenium hub Headless Firefox - Open Browser
    &{options} =	Create Dictionary	browserName=firefox  platform=ANY

    Open Browser    ${PAGE_URL}    browser=firefox    remote_url=${HUB}     desired_capabilities=${options}

    Maximize Browser Window
    Title Should Be         Google
    Capture Page Screenshot