class Translation(object):
    START_TEXT = """
Hello,

I am Telegram URL Upload Bot! Created by @shreevish

Please send me any direct download URL Link, i can upload to telegram as File/Video

🚨 . . . Note : its support almost all direct Url's except torrent link & some links . . . 🚨
 
🚨 PRON video🔞 Links gives you PERMANENT BAN 🚨

┈┈┈••💙✿❤️✿💚••┈┈┈
       
URL-UPLOADER bot created by @shreevish

➼/start = To Check whether the bot is alive or not
➼/help = To Know how to use me! 
➼/about = To know what am I !

⚠️Note :- Join My Channel before paste the link"""
    
    HELP_USER = """
<b>1.<u>Link to Media or File</u></b>
➠ Send a link for upload to telegram file or media.

<b>2.<u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.

<b>3.<u>To download</u></b>
Select the button.
   🎞SVideo🎞 - Give File as video with Screenshots
   🗂️DFile🗂️  - Give File with Screenshots
   🎞Video🎞  - Give File as video without Screenshots
   🗂️DFile🗂️  - Give File without Screenshots
   
<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail.

Made by @shreevish
"""
    
    ABOUT_TEXT = """
- **Bot :** `URL Uploader`
- **Creator :** [꧁★HACKER★꧂](https://telegram.me/shreevish)
- **Channel :** [Aʟʟ Mᴏᴠɪᴇ Rᴏᴄᴋᴇʀs](https://telegram.me/FayasNoushad)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/Satyamurthi/AMR-Url_Uploader)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    
    
    
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔗Channel🔗', url='https://telegram.me/All_Movie_Rockers'),
        InlineKeyboardButton('Creator ♐️', url='https://telegram.me/shreevish')
        ],[
        InlineKeyboardButton('💡Help💡', callback_data='help'),
        InlineKeyboardButton('🏷About🏷', callback_data='about'),
        InlineKeyboardButton('🔐Close🔐', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home🏠', callback_data='home'),
        InlineKeyboardButton('🏷About🏷', callback_data='about'),
        InlineKeyboardButton('🔐Close🔐', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home🏠', callback_data='home'),
        InlineKeyboardButton('💡Help💡', callback_data='help'),
        InlineKeyboardButton('🔐Close🔐', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""    
    
    
    FORMAT_SELECTION = """📭 𝗦𝗲𝗹𝗲𝗰𝘁 𝗔𝗻𝗱 𝗖𝗵𝗼𝘀𝗲 𝗬𝗼𝘂𝗿 𝗙𝗼𝗿𝗺𝗮𝘁👇
    

🎞️ 𝗩𝗜𝗗𝗘𝗢 = Upload as Streamble.

📂 𝗙𝗜𝗟𝗘 = Upload as File.

•••••••••••••••••••

➼/delthum = To Delet thumbnail

➼pLease send photo to save Thumblail before you press any Below Button

👲Powered By: @All_Movie_Rockers."""
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos Follow the steps :-
    
➲For Custom Name
➼URL | FileName.Extension

➲For Premium Videos
➼URL | FileName.Extension | username | password"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = " 📤 Downloaded in {} seconds.\n\nDetected File Size: {}\n\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " Join :- @All_Movie_Rocker"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = " 📤 Downloaded in {} seconds. \n\nUploaded in {} seconds."
    SAVED_CUSTOM_THUMB_NAIL = "**Thumbnail saved successfully**"
    DEL_ETED_CUSTOM_THUMB_NAIL = "**✅ Custom Thumbnail cleared succesfully**"
    CUSTOM_CAPTION_UL_FILE = "@All_Movie_Rocker"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    FORCE_SUBSCRIBE_TEXT = "**Join My Updates Channel to use ME 😎 🤭**"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
    REPORT_SITE_TEXT = "🙅‍♂️Sorry not uploading in this site here because this site is reporting site.🙅‍"
    SOMETHING_WRONG = "Something Wrong. Try again."    
