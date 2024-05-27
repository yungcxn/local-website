def with_opencv(filename):
    import cv2
    video = cv2.VideoCapture(filename)

    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    return duration, frame_count

def content(filelist, url):
  # generate xspf header
  # build array with title, videoduration and link
  # generate with vlc extension!!!
  header = '''<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/">
<title>Can's Video-Liste</title>
<trackList>
'''
  footer = '''  </trackList>
</playlist>
'''
  content = header
  for i, file in enumerate(filelist):
    duration, frame_count = with_opencv(f'video/{file}')
    content += f'''    <track>
      <title>{file}</title>
      <duration>{duration}</duration>
      <location>{url}/video/{file}</location>
      <extension application="http://www.videolan.org/vlc/playlist/0">
        <vlc:id>{str(i)}</vlc:id>
      </extension>
    </track>
'''
  content += footer

  return content
