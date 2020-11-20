# rename this to "config.py" after configuration

from colors import *

class Config:
    # retrieve homework from n number of days ahead
    days = 5
    # webdriver: firefox or chrome
    # when this is set to chrome, you also need to provide chromedriver path
    driver = "chrome"
    chrome = "/path/to/chromedriver"
    # most likely your school's website link
    provider = "https://provider.edupage.org"
    # your edupage username
    username = "FirstLast"
    # your edupage password
    password = "PASSWORD"

    # format configuration for "-f" or "--formatted" output
    class Format:
        # number of spaces before newline
        newline = 10
        # title color
        title = blue
        # due date format, [0] contains color and [1] contains datetime format
        date = (green, "%a %d %b")
