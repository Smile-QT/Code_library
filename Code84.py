
# 将mp4文件转为mp3音频文件并返回其文件路径,生成路径仍在原路径中(需要先下载moviepy库)
def mp4_to_mp3(path):
    try:
       video = VideoFileClip(path)
       audio = video.audio
       # 设置生成的mp3文件路径
       newPath = path.replace('mp4', 'mp3')
       audio.write_audiofile(newPath)
       return newPath
    except Exception as e:
        print(e)
        return None
