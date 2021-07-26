title: Convert mp3 files to audiobook for Apple Books
subtitle: ...youtube playlists, cds, and more...
date: 5/17/2021
image: eugenio-mazzone-6ywyo2qtaZ8-unsplash.jpg

The Mac/iPhone Books app has some issues.  Before switching the content out of iTunes into a separate app, audiobooks were housed in the same app as music.  You could edit the metadata on individual tracks, you could easily import an audiobook cd and just change the type to "Audiobook" and things would work.  If something was wrong with the title of a track, or the track number, you could go in and edit it.  Once they switched to Books, this level of editing was no longer possible.  Until recently I was doing the tedious task of editing in Music, copying to Books, seeing errors, copying back etc...  The errors were often things like Books breaking the audiobook into separate "books" because the track numbers weren't read right, or the tracks would be out of order, or the artwork wouldn't come through.  I was ok with this workaround tedium until recently, when I wanted to start following a youtube channel called [Digital Gnosis](https://www.youtube.com/channel/UCy63pdWnpupE8MfxpMNfRNg).  One of my favorite playlists is called [Bad Apologetics](https://www.youtube.com/playlist?list=PLggkCqSR7N1eq3UGURGKs9hcJNV-uIn4n), with 15 episodes so far with an average length **around 7 and a half hours a piece**!  So this state of affairs has forced me to retool my workflow, because I can't be at my computer to watch a 9 hour video, and I don't want to pay youtube to be able to listen while my phone is locked, and there are too many videos/playlists to deal with by hand.  So here goes my solution.

## Make a folder of mp3 files

Using the tool youtube-dl, installed with

```csh
pip install youtube-dl --upgrade
```

we download all of the videos in a playlist, convert to mp3, and put them in the current folder.  This playlist is called Open Conversations, so I put it in a folder named for that.

```csh
youtube-dl -i --extract-audio --audio-format mp3 "https://www.youtube.com/playlist?list=PLggkCqSR7N1dBxUjy51NdVGPJ78JXEdl-"
```

One can also do this by importing audiobook CDs and place the tracks in a folder.

## Get the book info correct

We continue with a script to get the track titles correct.  This part is a little manual, because the naming scheme for the tracks are individual to the playlist.  A little bit of string magic does the trick.

```python
from glob import glob
folder='Open Conversations'
fnames=sorted(glob(folder+"/*.mp3"))
display(fnames)
```
Output:

    ['Open Conversations/Open Conversation #001-vCEu612_tbc.mp3',
    'Open Conversations/Open Conversation #002-DW6LTgzxI2c.mp3',
    'Open Conversations/Open Conversation #003-yxF3OJpLW8w.mp3',
    'Open Conversations/Open Conversation #004-kBSczog9hjY.mp3',
    'Open Conversations/Open Conversation #005-Ba9JeLKLx4M.mp3',
    'Open Conversations/Open Conversation #006 _ Defining Terms and Open Conversation with JIL-ypzf9gCPMW4.mp3',
    'Open Conversations/Open Conversation #007-mrzHt60jaJ0.mp3',
    'Open Conversations/Open Conversation #008- Socially Distanced New Year Open Hangout - PineCreek, Cam, Erin, Autumn, Rob, etc-8yGK_yh-CTY.mp3',
    'Open Conversations/Open Conversation #009-T-V0VnGG_FI.mp3',
    'Open Conversations/Open Conversation #010-IcN-O-cbP80.mp3',
    'Open Conversations/Open Conversation #011-hfIJLjO7xss.mp3',
    'Open Conversations/Open Conversation #012-XD-Al7-_ezM.mp3',
    'Open Conversations/Open Conversation #013-WxwxA5I-pN4.mp3',
    'Open Conversations/Open Conversation #014-STmBT9OSNVw.mp3',
    'Open Conversations/Open Conversation #015-ClVDRgd29aY.mp3',
    'Open Conversations/Open Conversation #016-RjiSEfq4NJY.mp3',
    'Open Conversations/Open Conversation #017 - 500 Arguments Against Christianity Aftershow-TVEEgX6NqbE.mp3',
    'Open Conversations/Open Conversation #018 - James Fodor, Causation, Craig and more...-Kj3L8L3vXZI.mp3']



```python
album=folder
artist='Digital Gnosis'
artwork='Open Converstions Cover.png'
mime='image/png'

# this part has to be done by hand because each 
# person's playlist has a different naming format
titles=[_[:-16].replace('Open Conversations/Open Conversation ','Open Conversations - Ep ') 
                for _ in fnames]
display(titles)
```

Output:

    ['Open Conversations - Ep #001',
    'Open Conversations - Ep #002',
    'Open Conversations - Ep #003',
    'Open Conversations - Ep #004',
    'Open Conversations - Ep #005',
    'Open Conversations - Ep #006 _ Defining Terms and Open Conversation with JIL',
    'Open Conversations - Ep #007',
    'Open Conversations - Ep #008- Socially Distanced New Year Open Hangout - PineCreek, Cam, Erin, Autumn, Rob, etc',
    'Open Conversations - Ep #009',
    'Open Conversations - Ep #010',
    'Open Conversations - Ep #011',
    'Open Conversations - Ep #012',
    'Open Conversations - Ep #013',
    'Open Conversations - Ep #014',
    'Open Conversations - Ep #015',
    'Open Conversations - Ep #016',
    'Open Conversations - Ep #017 - 500 Arguments Against Christianity Aftershow',
    'Open Conversations - Ep #018 - James Fodor, Causation, Craig and more...']

**NOTE:** Having the album name in the track title, followed by " - " and the track name seems to be important for the Books app to get the title and tracks right for some reason.


## Write out the mp3 meta data with the [```mutagen```](https://mutagen.readthedocs.io/en/latest/) library.  

The docs are a bit sparse here, so between the docs and stackoverflow, I pieced together enough to set the titles, album, tracknumber, and album art for each mp3 file.

```python
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
import mutagen

write=True # for debugging

for i,name in enumerate(fnames):
    
    
    if write:
        try:
            meta = EasyID3(name)
        except mutagen.id3.ID3NoHeaderError:
            meta = mutagen.File(name, easy=True)
            meta.add_tags()
    else:
        meta={}


    title=titles[i]
    
    
    meta['album']=album
    meta['title']=title
    meta['artist']=artist
    meta['tracknumber']=str(i+1)
    
    print(meta)
    
    if write:
        meta.save(name)
    
        file = ID3(name) # Load the file
        file.delall("APIC") # Delete every APIC tag (Cover art)

        imagedata = open(artwork, 'rb').read()
        file.add(mutagen.id3.APIC(3, mime, 3, 'Front cover', imagedata))

        file.save() # Save the file    
```

Then *bingo!* you can copy the folder of mp3 to the Books app, and all will be well.  Now I just have to find time to listen to it all.
