from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can help you to do stuff on PDFs as well as convert images to PDF. Use /help to see features.

JUST SEND A PDF (or an image) to get started.

By @Bipin_Movies
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Bot Channel 📢", url="https://t.me/Bipin_Movies")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("☺️ About", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it
2) Send images to convert to PDFs

**Functions**
1) Rotate PDF Pages
2) Merge PDFs
3) Encrypt PDFs
4) Decrypt PDFs
5) Convert Images to PDF
"""

    # About Message
    ABOUT = """
**About This Bot** 

Channel : @Bipin_Movies 

Source Code : [Click Here](https://github.com/bipin8987/PDFBot.git)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @BipinX
    """
