# Video Encoder Bot
A Telegram bot to convert videos into x265/x264 format via ffmpeg.

### Configuration
Add values in environment variables or add them in [config.env.template](./config.env.template) and rename file to `config.env`.
- `API_ID` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` - Get it by creating a bot on [https://t.me/BotFather](https://t.me/BotFather)
- `SUDO_USERS` - Chat identifier of the sudo user. For multiple users use space as seperator.
- `DOWNLOAD_DIR` - (Optional) Temporary download directory to keep downloaded files.

### Configuring Encoding Format
To change the ffmpeg profile edit them in [ffmpeg_utils.py](/bot/helper/ffmpeg_utils.py)

### Installing Requirements

### The Easy Way

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/BotZ-TG/Encode-Bot)

#### The Hard Way
Install the required Python Modules in your machine.
```sh
apt-get -qq install ffmpeg
pip3 install -r requirements.txt
```
### Deployment
With python3.7 or later.
```sh
python3 -m bot
```

### Credits
*Thanks To [ShannonScott](https://gist.github.com/ShannonScott) for [transcode_h265.py](https://gist.github.com/ShannonScott/6d807fc59bfa0356eee64fad66f9d9a8)*
*Thanks To [Adnan Ahmed's](https://github.com/viperadnan-git/) [Encoder-Bot](https://github.com/viperadnan-git/video-encoder-bot)
*Thanks To [Heiman-BotZ](https://github.com/HEIMAN-BOTZ/) For Adding Heroku Support

### [License](./LICENSE)

```
Copyright (c) 2021 HEIMAN BOTZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
