
from browser import Browser

browser = Browser()

browser.startup()

try:
    browser.run()
except (KeyboardInterrupt, SystemExit) as e:
    browser.exit()


    


