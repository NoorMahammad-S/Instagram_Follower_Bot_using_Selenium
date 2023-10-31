
# Instagram Follower Bot

This Python script is a Instagram follower bot that uses Selenium to automate following the followers of a specified Instagram account. 
It is intended for educational purposes and should be used responsibly and in compliance with Instagram's terms of service.

## Prerequisites

Before using this bot, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Google Chrome
- Chrome WebDriver
- Selenium (You can install it using `pip install selenium`)

## Getting Started

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/NoorMahammad-S/instagram-follower-bot.git
   ```

2. Download the Chrome WebDriver and provide its path in the `chromedriver.exe` file variable in the code.

3. Customize the following variables in the code:
   - `USERNAME`: Your Instagram username
   - `PASSWORD`: Your Instagram password
   - `SIMILAR_ACCOUNT`: The username of the Instagram account whose followers you want to follow.

4. Run the Python script:

   ```
   python instagram_follower_bot.py
   ```

5. The script will open a Chrome browser, log in to your Instagram account, navigate to the specified account's followers page, and start following the followers. Be sure to keep the script running until you've followed the desired number of followers.

6. You may need to adjust the number of followers to follow by modifying the loop in the `find_followers` method.

7. Please use this script responsibly and be aware of Instagram's policies regarding automated actions on their platform.

## Disclaimer

This script is for educational purposes only, and its usage may be subject to Instagram's terms of service. 

## Caution

- Be careful when automating actions on Instagram to avoid getting your account banned or restricted.
- Use this script responsibly and within the limits of Instagram's terms of service.

## Contributing

Feel free to contribute to this project by opening issues or pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is for educational purposes and should be used responsibly.

Happy botting!

**Note:** The code provided here is meant for educational purposes and should be used responsibly and in compliance with Instagram's terms of service. 
Unauthorized or excessive automation on Instagram may lead to account restrictions or bans.
