import browser_cookie3
import os
import sys

def clear_cookies(browser_name):
    try:
        browser = browser_cookie3.load(browser_name)
        if browser:
            for cookie in browser:
                cookie.expires = 1  # Expire the cookie
            print(f"Cookies cleared for {browser_name.capitalize()}.")
        else:
            print(f"No cookies found for {browser_name.capitalize()}.")

    except FileNotFoundError:
        print(f"{browser_name.capitalize()} not found. Cookies could not be cleared.")
    except Exception as e:
        print(f"An error occurred while clearing cookies: {str(e)}")

def clear_cache(browser_name):
    try:
        if browser_name.lower() == 'chrome':
            if sys.platform.startswith('win'):
                # For Windows
                os.system("start chrome://settings/clearBrowserData")
            elif sys.platform.startswith('darwin'):
                # For macOS
                os.system("open -a 'Google Chrome' --args --clear-browser-data")
            else:
                print(f"Cache clearing not supported for {browser_name.capitalize()} on this platform.")
        else:
            print(f"Cache clearing not supported for {browser_name.capitalize()}.")
    except FileNotFoundError:
        print(f"{browser_name.capitalize()} not found. Cache could not be cleared.")
    except Exception as e:
        print(f"An error occurred while clearing cache: {str(e)}")

if __name__ == "__main__":
    browser_name = 'chrome'  # Change to your preferred browser if required
    clear_cookies(browser_name)
    clear_cache(browser_name)
