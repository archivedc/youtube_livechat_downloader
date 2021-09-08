# YouTube Live Chat Download/Converter
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Farchivedc%2Fyoutube_livechat_downloader.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Farchivedc%2Fyoutube_livechat_downloader?ref=badge_shield)


## Usage

### livechat.py
```bash
$ python livechat.py <Source URL> <Destination>
# Example: python livechat.py https://www.youtube.com/watch?v=-d8NPJ8ShfI livechat.json
```

This will export live chat data as json file.

You have to install Chat-Downloader before using it.
```bash
$ pip install chat-downloader
```

### jsonchat_tocsv.py
```bash
$ python jsonchat_tocsv.py <Json File> <Destination>
# Example: python jsonchat_tocsv.py livechat.json livechat.csv
```

This will convert json live chat data to csv file.

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Farchivedc%2Fyoutube_livechat_downloader.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Farchivedc%2Fyoutube_livechat_downloader?ref=badge_large)