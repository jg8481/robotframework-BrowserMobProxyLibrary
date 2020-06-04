[![Build Status](https://travis-ci.org/s4int/robotframework-BrowserMobProxyLibrary.svg?branch=master)](https://travis-ci.org/s4int/robotframework-BrowserMobProxyLibrary)
[![Build Status](https://img.shields.io/pypi/v/robotframework-browsermobproxylibrary.svg?label=version)](https://pypi.python.org/pypi/robotframework-browsermobproxylibrary)

# Robot Framework BrowserMob Proxy
## Introduction
BrowserMobProxyLibrary is a [Robot Framework](http://robotframework.org/) library ro interface with [BrowserMob Proxy](https://bmp.lightbody.net/).

BrowserMob Proxy is a simple utility to capture performance data for web apps (via the HAR format),
as well as manipulate browser behavior and traffic, such as whitelisting and blacklisting content,
simulating network traffic and latency, and rewriting HTTP requests and responses.

More information about this library can be found in the [Keyword Documentation](https://rawgit.com/s4int/robotframework-BrowserMobProxyLibrary/master/doc/BrowserMobProxyLibrary.html).

## Installation
### Using pip
```bash
      pip install -U robotframework-browsermobproxylibrary
```

### Manual installation
1. Make sure you have [Robot Framework installed](http://code.google.com/p/robotframework/wiki/Installation).
2. Download source distributions (`*.tar.gz`) for the library and its dependencies:
      - https://pypi.python.org/pypi/robotframework-browsermobproxylibrary
3. Extract each source distribution to a temporary location.
4. Go each created directory from the command line and install each project using:

```bash
      python setup.py install
```

## Keywords

Robot Framework keyword documentation is located [Here](https://rawgit.com/s4int/robotframework-BrowserMobProxyLibrary/master/doc/BrowserMobProxyLibrary.html)

## Example
Install Robot Framework library for selenium
```bash
      pip install -U robotframework-selenium2library
```

Download and extract [BrowserMob Proxy](https://bmp.lightbody.net/)

Basic example:
```robotframework

      *** Settings ***
      Documentation               This is just a BrowserMob Proxy Library tutorial
      ...
      Metadata                    VERSION     0.1
      Library                     Selenium2Library
      Library                     Collections
      Library                     OperatingSystem
      Library                     BrowserMobProxyLibrary
      Suite Setup                 Start Browser
      Suite Teardown              Close Browsers
      
      
      *** Variables ***
      ${PAGE_URL}                 https://www.google.com
      ${BROWSER}                  Firefox
      
      *** Keywords ***
      Start Browser
          [Documentation]         Start firefox browser
          Set Selenium Implicit Wait  10
          ## Init BrowserMob Proxy
          Start Local Server      <path to browsermob-proxy>
      
          ## Create dedicated proxy on BrowserMob Proxy
          ${BrowserMob_Proxy}=    Create Proxy
      
          ## Configure Webdriver to use BrowserMob Proxy
          Create Webdriver        ${BROWSER}    proxy=${BrowserMob_Proxy}
      
      Close Browsers
          Close All Browsers
          Stop Local Server
      
      *** Test Cases ***
      Check something
          [Documentation]         Check the page title
          New Har                 google
          Go to                   ${PAGE_URL}
          Title Should Be         Google
          ${har}=                 Get Har As JSON
          create file             ${EXECDIR}${/}file.har     ${har}
          log to console          Browsermob Proxy HAR file saved as ${EXECDIR}${/}file.har
```
