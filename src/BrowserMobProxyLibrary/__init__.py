from browsermobproxy import Server
from browsermobproxy import RemoteServer
import json
from .version import VERSION

__version__ = VERSION

LIMITS = {
    'upstream_kbps': 'upstreamKbps',
    'downstream_kbps': 'downstreamKbps',
    'latency': 'latency'
}

TIMEOUTS = {
    'request': 'requestTimeout',
    'read': 'readTimeout',
    'connection': 'connectionTimeout',
    'dns': 'dnsCacheTimeout'
}


class BrowserMobProxyLibrary(object):
    """BrowserMobProxyLibrary is a Robot Framework library ro interface with BrowserMob Proxy.
    BrowserMob Proxy is a simple utility to capture performance data for web apps (via the HAR format),
    as well as manipulate browser behavior and traffic, such as whitelisting and blacklisting content,
    simulating network traffic and latency, and rewriting HTTP requests and responses.

    = Before running tests =

    Prior to running test cases using BrowserMobProxyLibrary, BrowserMobProxyLibrary must be
    imported into your Robot test suite.
    """

    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        """BrowserMobProxyLibrary is a Robot Framework library ro interface with BrowserMob Proxy.
        """

        self.server = None
        self.client = None

    def get_proxy_url(self):
        """Gets the url that the proxy is running on. This is not the URL clients
        should connect to.
        """

        return self.server.url

    def create_proxy(self, params={}):
        """Creates proxy.

        :param params: Dictionary where you can specify params \
                    like httpProxy and httpsProxy
        """

        self.client = self.server.create_proxy(params=params)
        return self.client

    def start_local_server(self, path='browsermob-proxy', options={}):
        """Start local Browsermob Proxy Server instance

        :param path: Path to the browsermob proxy batch file
        :param options: Dictionary that can hold the port. \
        """

        self.server = Server(path=path, options=options)
        self.server.start()

    def stop_local_server(self):
        """This will stop the process running the Browsermob Proxy
        """

        if isinstance(self.server, Server):
            self.server.stop()

    def connect_to_remote_server(self, host='localhost', port=9090):
        """Connect to a Remote Browsermob Proxy Server

        :param host: The host of the proxy server.
        :param port: The port of the proxy server.
        """

        self.server = RemoteServer(host=host, port=int(port))

    def close_proxy(self):
        """shuts down the proxy and closes the port
        """

        return self.client.close()

    def get_selenium_proxy(self):
        """Returns a Selenium WebDriver Proxy with details of the HTTP Proxy
        """

        return self.client.selenium_proxy()

    def get_webdriver_proxy(self):
        """Returns a Selenium WebDriver Proxy with details of the HTTP Proxy
        """

        return self.client.webdriver_proxy()

    def add_to_capabilities(self, capabilities):
        """Adds an 'proxy' entry to a desired capabilities dictionary with the
        BrowserMob proxy information

        :param capabilities: The Desired capabilities object from Selenium WebDriver
        """

        self.client.add_to_capabilities(capabilities=capabilities)

    def add_to_webdriver_capabilities(self, capabilities):
        """Adds an 'proxy' entry to a desired capabilities dictionary with the
        BrowserMob proxy information

        :param capabilities: The Desired capabilities object from Selenium WebDriver
        """

        self.client.add_to_webdriver_capabilities(capabilities=capabilities)

    def get_har(self):
        """Returns the HAR that has been recorded
        """

        return self.client.har

    def get_har_as_json(self):
        """Returns the HAR that has been recorded as json
        """

        return json.dumps(self.client.har)

    def new_har(self, ref=None, options={}):
        """This sets a new HAR to be recorded

        :param ref: A reference for the HAR. Defaults to None
        :param options: A dictionary that will be passed to BrowserMob Proxy \
                   with specific keywords. Keywords are: \
                   captureHeaders - Boolean, capture headers \
                   captureContent - Boolean, capture content bodies \
                   captureBinaryContent - Boolean, capture binary content
        """

        return self.client.new_har(ref=ref, options=options)

    def new_page(self, ref=None):
        """This sets a new page to be recorded

        :param ref: A reference for the new page. Defaults to None
        """

        return self.client.new_page(ref=ref)

    def blacklist(self, regexp, status_code):
        """Sets a list of URL patterns to blacklist

        :param regexp: a comma separated list of regular expressions
        :param status_code: the HTTP status code to return for URLs that do not \
                       match the blacklist

        """

        return self.client.blacklist(regexp=regexp, status_code=status_code)

    def whitelist(self, regexp, status_code):
        """Sets a list of URL patterns to whitelist

        :param regex: a comma separated list of regular expressions
        :param status_code: the HTTP status code to return for URLs that do not \
                       match the whitelist
        """

        return self.client.whitelist(regexp=regexp, status_code=status_code)

    def basic_authentication(self, domain, username, password):
        """This add automatic basic authentication

        :param domain: domain to set authentication credentials for
        :param username: valid username to use when authenticating
        :param  password: valid password to use when authenticating
        """

        return self.client.basic_authentication(domain=domain, username=username, password=password)

    def set_headers(self, headers):
        """This sets the headers that will set by the proxy on all requests

        :param headers: this is a dictionary of the headers to be set
        """

        return self.client.headers(headers=headers)

    def set_response_interceptor(self, js):
        """Executes the javascript against each response

        :param js: the javascript to execute
        """

        return self.client.response_interceptor(js=js)

    def set_request_interceptor(self, js):
        """Executes the javascript against each request

        :param js: the javascript to execute
        """

        return self.client.request_interceptor(js=js)

    def set_limits(self, options):
        """Limit the bandwidth through the proxy.

        :param options: A dictionary with all the details you want to set. \
                        downstreamKbps - Sets the downstream kbps \
                        upstreamKbps - Sets the upstream kbps \
                        latency - Add the given latency to each HTTP request
        """

        return self.client.limits(options)

    def set_timeouts(self, options):
        """Configure timeouts in the proxy

        :param options: A dictionary with all the details you want to set. \
                        request - request timeout (in seconds) \
                        read - read timeout (in seconds) \
                        connection - connection timeout (in seconds) \
                        dns - dns lookup timeout (in seconds)
        """

        return self.client.timeouts(options=options)

    def remap_hosts(self, address, ip_address):
        """Remap the hosts for a specific URL

        :param address: url that you wish to remap
        :param ip_address: IP Address that will handle all traffic for the address passed in
        """

        return self.client.remap_hosts(address=address, ip_address=ip_address)

    def wait_for_traffic_to_stop(self, quiet_period, timeout):
        """Waits for the network to be quiet

        :param quiet_period: number of miliseconds the network needs to be quiet for
        :param timeout: max number of miliseconds to wait
        """

        return self.client.wait_for_traffic_to_stop(quiet_period=quiet_period, timeout=timeout)

    def clear_dns_cache(self):
        """Clears the DNS cache associated with the proxy instance
        """

        return self.client.clear_dns_cache()

    def rewrite_url(self, match, replace):
        """Rewrites the requested url.

        :param match: a regex to match requests with
        :param replace: unicode a string to replace the matches with
        """

        return self.client.rewrite_url(match=match, replace=replace)

    def retry(self, retry_count):
        """Retries.

        :param retry_count: the number of retries
        """

        return self.client.retry(retry_count=retry_count)
