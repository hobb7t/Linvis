import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Minimum required Python version
MIN_PYTHON_VERSION = (3, 7)

# Required libraries
REQUIRED_LIBRARIES = [
    'selenium',
    'webdriver-manager'
]


def check_python_version():
    """Ensures the Python version meets the minimum requirements."""
    if sys.version_info < MIN_PYTHON_VERSION:
        print("ERROR: Python " + ".".join(map(str, MIN_PYTHON_VERSION)) + " or higher is required.")
        sys.exit(1)
    print("INFO: Python version " + sys.version.split()[0] + " is compatible.")


def install_package(package_name):
    """Installs a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        logging.info(f"Successfully installed {package_name}.")
    except Exception as e:
        logging.error(f"Failed to install {package_name}: {e}")
        sys.exit(1)


def ensure_dependencies():
    """Checks and installs missing libraries."""
    for package in REQUIRED_LIBRARIES:
        try:
            __import__(package.replace('-', '_'))  # Convert names like 'webdriver-manager' for import
        except ImportError:
            logging.info(f"Package {package} not found. Attempting to install...")
            install_package(package)


# Run dependency check at the top of the script
check_python_version()
ensure_dependencies()

# Now import the dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# LinkedIn Visitor Class and Rest of the Code
class LinkedInVisitor:
    def __init__(self, username, password, keywords, max_pages):
        self.username = username
        self.password = password
        self.keywords = keywords
        self.max_pages = max_pages
        self.driver = None

    def setup_driver(self):
        """Initializes the Selenium WebDriver."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        logging.info("WebDriver initialized.")

    def login(self):
        """Logs into LinkedIn."""
        try:
            self.driver.get('https://www.linkedin.com/login')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(
                self.username)
            self.driver.find_element(By.ID, 'password').send_keys(self.password)
            self.driver.find_element(By.XPATH, '//*[@type="submit"]').click()
            logging.info("Successfully logged in.")
        except Exception as e:
            logging.error(f"Login failed: {e}")
            raise

    def visit_profiles(self):
        """Visits profiles based on the search keywords and page limits."""
        try:
            for page in range(1, self.max_pages + 1):
                search_url = f'https://www.linkedin.com/search/results/people/?keywords={self.keywords}&page={page}'
                self.driver.get(search_url)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'reusable-search__result-container')))

                profiles = self.driver.find_elements(By.CLASS_NAME, 'reusable-search__result-container')
                logging.info(f'Page {page}: Found {len(profiles)} profiles.')

                for profile in profiles:
                    try:
                        profile_link = profile.find_element(By.TAG_NAME, 'a').get_attribute('href')
                        self.driver.execute_script("window.open('');")
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        self.driver.get(profile_link)
                        logging.info(f"Visited profile: {profile_link}")
                        time.sleep(2)  # Simulate delay
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                    except Exception as e:
                        logging.warning(f"Error visiting profile: {e}")
        except Exception as e:
            logging.error(f"Error during profile visits: {e}")
            raise

    def cleanup(self):
        """Closes the WebDriver."""
        if self.driver:
            self.driver.quit()
            logging.info("WebDriver closed.")


def run_visitor(username, password, keywords, max_pages):
    """Runs the LinkedIn Visitor."""
    visitor = LinkedInVisitor(username, password, keywords, max_pages)
    try:
        visitor.setup_driver()
        visitor.login()
        visitor.visit_profiles()
    finally:
        visitor.cleanup()


# Main Entry Point
if __name__ == '__main__':
    # Run the LinkedIn visitor program
    username = input("Enter LinkedIn username: ")
    password = input("Enter LinkedIn password: ")
    keywords = input("Enter search keywords: ")
    max_pages = int(input("Enter the number of pages to visit: "))

    run_visitor(username, password, keywords, max_pages)
