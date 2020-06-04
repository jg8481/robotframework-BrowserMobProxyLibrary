*** Settings ***
Documentation               BrowserMob Proxy with selenium hub
...
Metadata                    VERSION     0.1
Library                     Selenium2Library
Library                     Collections
Library                     OperatingSystem
Library                     BrowserMobProxyLibrary
Suite Teardown              Close Browsers

*** Variables ***
${PAGE_URL}                 https://www.google.com
${HUB}                      http://127.0.0.1:4444/wd/hub
${PROXY_HOST}               proxy

*** Keywords ***
Start Browser
    [Arguments]    ${BROWSER}
    Set Selenium Implicit Wait  10
    # Connect to BrowserMob-Proxy
    Connect To Remote Server  host=${PROXY_HOST}  port=8080

    # Create dedicated proxy on BrowserMob Proxy
    ${BrowserMob_Proxy}=    Create Proxy

    &{options}=	Create Dictionary	browserName=${BROWSER}	platform=ANY  acceptSslCerts=${TRUE}  acceptInsecureCerts=${TRUE}

    # Configure Webdriver to use BrowserMob Proxy
    add_to_webdriver_capabilities  ${options}

    Create Webdriver    Remote   command_executor=${HUB}    desired_capabilities=${options}

Close Browsers
    Close All Browsers
    Close Proxy

*** Test Cases ***
Create har file - chrome
    [Setup]                 Start Browser   chrome
    New Har                 google
    Go to                   ${PAGE_URL}
    Title Should Be         Google
    Capture Page Screenshot
    ${har}=                 Get Har As JSON
    create file             ${EXECDIR}${/}file.har     ${har}
    log to console          Browsermob Proxy HAR file saved as ${EXECDIR}${/}file.har

Create har file - firefox
    [Setup]                 Start Browser   firefox
    New Har                 google
    Go to                   ${PAGE_URL}
    Title Should Be         Google
    Capture Page Screenshot
    ${har}=                 Get Har As JSON
    create file             ${EXECDIR}${/}file.har     ${har}
    log to console          Browsermob Proxy HAR file saved as ${EXECDIR}${/}file.har
