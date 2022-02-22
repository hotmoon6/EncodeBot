from pyrogram import filters
from bot import app, data, sudo_users
from bot.helper.utils import add_task

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "application/x-mpegURL",
  "video/MP2T",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]

@app.on_message(filters.incoming & filters.command(['start', 'help']))
def help_message(app, message):
    message.reply_text(f"Hi {message.from_user.mention()}\nI can encode Telegram files, just send me a video.\nThen See The Magic.\n\nDeveloped By @HeimanSupports", quote=True)

@app.on_message(filters.incoming & filters.command(['donate']))
def donate_message(app, message):
    message.reply_text(f"**Hello User, It's Our Privilege to respond to your Big Heart, if your Wishing To Donate Us Some Penny. Click Below.** ```After Donating DM your ScreenShot``` **@HeimanSSProof_bot** ", quote=True)

@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.video | filters.document))
def encode_video(app, message):
    if message.document:
      if not message.document.mime_type in video_mimetype:
        message.reply_text("⚠️ ```Invalid Video !\nMake sure its a valid video file.```", quote=True)
        return
    message.reply_text("```Added to Queue ⏰...```", quote=True)
    data.append(message)
    if len(data) == 1:
      add_task(message)

app.run()
