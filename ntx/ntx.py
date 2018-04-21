import sys
from ntx.browser import Browser

__version__ = '0.1'


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    
    browser = Browser()
    browser.startup()
    try:
        browser.run()
    except (KeyboardInterrupt, SystemExit) as _:
        browser.exit()


if __name__ == "__main__":
    main()
    


