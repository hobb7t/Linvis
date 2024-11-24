About this Project
(Lin)kedIn (Vis)itor is a simple Python-based automation tool that uses Selenium to:

- Log into LinkedIn and search for profiles based on specified keywords, then visit profiles automatically up to a specified number of pages.
It helps developers explore browser automation and Selenium scripting while adhering to ethical guidelines and LinkedIn's Terms of Service.

⚠️ Disclaimer
This project is for educational purposes only. Automating interactions on LinkedIn may violate their Terms of Service. Use responsibly, and avoid scraping sensitive information. 
By using this tool, you take full responsibility for complying with LinkedIn's policies.

🛠️ Features
Automated Login: The program checks if you're already logged in, skipping redundant logins.
Profile Search and Visit: Automatically searches for profiles using a keyword and visits them.
Error Handling: Gracefully handles slow-loading pages and unexpected issues.
Dependency Installation: Automatically installs missing Python libraries.
Customizable: Easily edit keywords, page limits, and behavior. (Sooner or later, a GUI will come out)

🖥️ How to Use
Prerequisites
Python 3.7 or higher is required.
Install Google Chrome (latest version) and ensure chromedriver is available.
Installation

Clone the repository:

git clone https://github.com/hobb7t/Linvis.git
cd Linvis

Run the program:

bash
python3 main.py

The script will:

Check your Python version.
Automatically install any missing dependencies (selenium, webdriver-manager).
Prompt for LinkedIn login credentials, search keywords, and the number of pages to visit. 
(Due to security implementations, the username and pass are not saved on a file, are just being sent to memory for as long you are using the program)


📝 How to Contribute
We welcome contributions to improve this project! Here's how you can get started:

1. Fork This Repository
Click the "Fork" button at the top right of this repository.

3. Clone Your Fork Locally
bash
Copy code
git clone https://github.com/yourusername/Linvis.git
cd Linvis

4. Create a New Branch
bash
Copy code
git checkout -b feature-your-feature-name

5. Make Your Changes
Edit the code to fix bugs, add features, or improve documentation.

7. Run Tests
Test your changes to ensure the program runs without issues.

8. Commit and Push
bash
Copy code
git add .
git commit -m "Add your message here"
git push origin feature-your-feature-name

9. Open a Pull Request
Go to the original repository and open a pull request with a detailed explanation of your changes.
⚙️ Customization
You can easily customize the following:

Search Keywords:

Update the keyword input prompt in main.py or hardcode the keyword if needed.
Page Limits:

Adjust the max_pages parameter when running the program.
Logging Behavior:

Modify logging settings for more detailed or concise logs.
Dependencies:

Add new Python libraries to the REQUIRED_LIBRARIES list for automatic installation.

🧩 Issues and Improvements
If you encounter bugs or have suggestions, please open an issue on the GitHub repository. Contributions are always welcome!

🌟 Acknowledgements
Selenium for browser automation.
Webdriver-Manager for managing ChromeDriver.
Open-source contributors and the Python community for their inspiration.
Let me know if you want me to:

Add additional sections (e.g., "FAQ", "Roadmap").
Format this for your GitHub repository specifically.
