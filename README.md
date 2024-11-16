# pLetters - Text to Image Generator Bot

`pLetters` is a Telegram bot that allows users to generate images from formatted text. The bot uses LaTeX to format text and convert it into images, which it then sends to the user through Telegram.

The bot performs the following steps:
1. **Receive input** from the user via Telegram.
2. **Generate LaTeX code** for the input text.
3. **Compile LaTeX to PDF** and convert it into image(s).
4. **Send the image(s)** to the user.
5. **Clean up** generated files after sending the images.



## Table of Contents

- [pLetters - Text to Image Generator Bot](#pletters---text-to-image-generator-bot)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
    - [Python 3.7+](#python-37)
    - [Required Packages](#required-packages)
  - [Setup and Installation](#setup-and-installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Set Up `.env` File](#3-set-up-env-file)
    - [4. Generate Your Telegram Bot Token](#4-generate-your-telegram-bot-token)
  - [Usage](#usage)
    - [Running the Bot](#running-the-bot)
  - [How to Generate a Telegram Bot Token](#how-to-generate-a-telegram-bot-token)
  - [Example](#example)
  - [Contributing](#contributing)
  - [License](#license)
  - [More About Me](#more-about-me)
  - [Remember to Star the Repository ⭐](#remember-to-star-the-repository-)



## Features

- Converts formatted text into LaTeX and generates images.
- Allows dynamic insertion of user handle.
- Cleans up temporary files after sending images.
- Supports handling of headings, bolded text, and bullet points.
- Sends generated images to users via Telegram.


## Requirements

Make sure to install the following dependencies before running the bot:

### Python 3.7+

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Required Packages

1. `python-telegram-bot` - Python wrapper for the Telegram Bot API.
2. `latexmk` - For compiling LaTeX files.
3. `pdf2image` - To convert PDFs into images.
4. `python-dotenv` - To load environment variables from `.env` file.


## Setup and Installation

Follow these steps to get your bot running:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pLetters.git
cd pLetters
```

### 2. Install Dependencies

Make sure you have all the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set Up `.env` File

Create a `.env` file by copying the contents of `.env.example`:

```bash
cp .env.example .env
```

Modify the `.env` file to include your **Telegram Bot Token** and **User Handle**:

- `TELEGRAM_BOT_TOKEN`: The token for your Telegram bot. You can get this by talking to `@BotFather` on Telegram.
- `USER_HANDLE`: The handle or username that will be used in the LaTeX document (this is displayed as the author).


```env
# .env

TELEGRAM_BOT_TOKEN=your-telegram-bot-token
USER_HANDLE=your-username-or-handle
```

### 4. Generate Your Telegram Bot Token

To create a Telegram bot and get the `TELEGRAM_BOT_TOKEN`, follow these steps:

1. **Open Telegram** and search for `@BotFather`.
2. Start a conversation and send the command `/newbot`.
3. Follow the prompts to create a new bot. BotFather will give you the `TELEGRAM_BOT_TOKEN`.
4. Paste the token into the `.env` file as shown above.


## Usage

Once the environment is set up, you can start the bot. The bot will respond to messages containing text formatted with specific tags such as:

- `[Heading]` to specify the heading.
- `bt[Bold Text]` for bold text.
- `Items[Item1, Item2, Item3]` for bullet points.

For example, a user can send the following message to the bot:

```
[Heading] Example Heading
[Content]
This is a simple paragraph.
bt[Bold Text Example]
Items[Item 1, Item 2, Item 3]
```

The bot will process this message, generate LaTeX code, compile it into a PDF, convert the PDF into images, and then send the images back to the user.

### Running the Bot

To run the bot, simply execute the `main.py` script:

```bash
python main.py
```

The bot will start polling for messages. It will respond to text messages, process them, and send back images generated from the LaTeX code.


## How to Generate a Telegram Bot Token

1. Open Telegram and search for `@BotFather`.
2. Start a conversation and send the command `/newbot`.
3. Follow the prompts to create a new bot, such as:
   - Choose a name for your bot.
   - Choose a unique username (must end in `bot`).
4. BotFather will generate a **bot token** and send it to you.
5. Copy the token and paste it into your `.env` file under `TELEGRAM_BOT_TOKEN`.


## Example

**Message**

```
[Heading]
Reflux: Art Of Focus 

[Content]
I began my journey from a place many might find familiar—a modest bt[\$376/month] 9-to-5 job, where I felt like any other ordinary person. For months, I was captivated by Dan Koe's work, not just his writing skills, but also his unique visual aesthetics. His letters were more than just words; they were a visual experience that resonated deeply with me.

But life had other plans. My five-year-old laptop, which I depended on for my creative projects, broke down. Suddenly, I was left without a crucial tool. My situation seemed dire. I wasn’t hustling; instead, I found solace in listening to the audiobook bt[Art of Focus]. The book instilled in me a glimmer of courage, and with it, I decided to forge ahead, despite the odds.

I was determined to emulate Dan Koe's impactful letters. I knew I had the potential, but I faced significant hurdles. Without a computer, generating these letters through conventional means was impossible. Even if I managed to get my hands on one, the exhaustion from my daily grind would likely stifle my creativity.

In this moment of adversity, I chose to leverage my two greatest assets: programming skills and a keen eye for visual design. I took my Pixel 3, with its modest 5.5-inch screen

st[Crafted a solution]
Items[I wrote LaTeX code to create the letter’s structure, Python script to process and refine the content and converted the output to images, A telegram bot to input data and a Discord channel to receive the generated letters]

Working late into the nights after my job, I navigated the constraints of my small screen and limited resources. It was a labor of love, driven by a vision and an unwavering belief in my potential. Despite the challenges, I managed to produce results that I found deeply satisfying.

My story might have been different if I had chosen to accept the setbacks. But I didn’t let the circumstances define my path. Instead, I used them as a catalyst for innovation and personal growth. The book "Art of Focus" was my beacon, guiding me through the darkness of doubt and helping me create something meaningful.

I want to express my gratitude to Dan Koe, whose work inspired me to push beyond my limitations. My journey is a testament to the idea that with determination and the right mindset, we can overcome obstacles and turn our dreams into reality.

Thank you, bt[Dan Koe.]
```

**Output**
![Page_1](/sample_output/page_1.jpg)
![Page_2](/sample_output/page_2.jpg)


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## More About Me

For more information about my other projects, visit [my website](https://jagadeshronanki.com).



## Remember to Star the Repository ⭐

If you found this project useful or interesting, please star the repository at the top of the page. This helps others find it and motivates me to continue improving it. 

