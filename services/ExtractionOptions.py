import subprocess
import re
import yt_dlp
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))



def extract_video_info(url):
    cmd = ['yt-dlp',url, "--no-download", "--parse-metadata", "title:%(title)s", "--parse-metadata", "uploader:%(uploader)s", "--parse-metadata", "view_count:%(view_count)s", "--parse-metadata", "like_count:%(like_count)s","--parse-metadata", "upload_date:%(upload_date)s", "--parse-metadata", "description:%(description)s","--parse-metadata", "duration:%(duration)s"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    # process = subprocess.run(cmd, capture_output=True, text = True)
    return process
    
def extract_playlist_info(url):
    playlist_info_cmd = ['yt-dlp', url, "--no-download","-I","1", "--parse-metadata", "playlist_count:%(playlist_count)s", "--parse-metadata", "playlist_uploader:%(playlist_uploader)s","--parse-metadata", "playlist_title:%(playlist_title)s","--parse-metadata", "playlist_description:%(description)s"]
    playlist_info = subprocess.Popen(playlist_info_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    # playlist_info = subprocess.run(playlist_info_cmd, capture_output=True, text = True)
    # yield playlist_info
    cmd = ['yt-dlp', url, "--no-download", "--parse-metadata", "title:%(title)s", "--parse-metadata", "uploader:%(uploader)s", "--parse-metadata", "view_count:%(view_count)s", "--parse-metadata", "like_count:%(like_count)s","--parse-metadata", "upload_date:%(upload_date)s", "--parse-metadata", "description:%(description)s","--parse-metadata", "duration:%(duration)s", "--windows-filenames"]
    video_info = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    # video_info = subprocess.run(cmd, capture_output=True, text = True)
    # return str(video_info),str(playlist_info)
    return video_info,playlist_info


def get_available_quality(url):
    cmd = ['yt-dlp', url, "--list-formats", "--no-download"]
    output = subprocess.run(cmd, capture_output=True, text = True)
    pattern = r'\b(1080p|720p|480p|360p|240p|144p)\b'
    matches = re.findall(pattern, output.stdout.strip())
    return set(matches)


def getThumbnail(url, thumbnail_filepath):
    cmdThumbnail = ['yt-dlp', url, "--write-thumbnail", "--no-download","-P",thumbnail_filepath,"--windows-filenames"]
    subprocess.run(cmdThumbnail, capture_output=True, text = True)
    # print(output)




# def download_live_stream(url):
#     cmd = ['yt-dlp',"--live-from-start","--cookies", "youtube.com_cookies.txt", url]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
    # subprocess.run(cmd, text = True)




# def download_playlist_selection(playlist_url:str, selection:str):
#     cmd = ['yt-dlp',"-I", selection , playlist_url, "--yes-playlist", "-P", "playlist\\", "-P", "temp:temp\\","-f","bv*[height=720]+ba", "--merge-output-format", "mkv", "--windows-filenames"]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
#     # subprocess.run(cmd, text = True)

# def download_playlist_audio_selection(playlist_url:str, selection:str):
#     cmd = ['yt-dlp', "-I", selection, playlist_url, "--yes-playlist", "--extract-audio", "--audio-format", "mp3"]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
#     # subprocess.run(cmd, capture_output=True, text = True)

# def download_playlist(playlist_url):
#     cmd = ['yt-dlp', playlist_url, "--yes-playlist", "-P", "playlist\\", "-P", "temp:temp\\","-f","bv*[height=720]+ba", "--merge-output-format", "mkv", "--windows-filenames"]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
#     # subprocess.run(cmd, text = True)

# def download_playlist_audio(playlist_url):
#     cmd = ['yt-dlp', playlist_url, "--yes-playlist", "--extract-audio", "--audio-format", "mp3"]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
#     # subprocess.run(cmd, capture_output=True, text = True)




# def download_audio(url):
#     cmd = ['yt-dlp', url, "--extract-audio", "--audio-format", "mp3"]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
#     # subprocess.run(cmd, capture_output=True, text = True)


# def download_video(url):
#     cmd = ['yt-dlp', url,"-f", f"bv*[height=720]+ba","--merge-output-format", "mp4", "-P", "downloads\\", "-P", "temp:temp\\","--windows-filenames","-N", "4"]
#     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
#     return process
#     # subprocess.run(cmd, text = True, check=True)








if __name__ == "__main__":
    PLAYLIST_URL = "https://youtube.com/playlist?list=PLbpi6ZahtOH7c6nDA9YG3QcyRGbZ4xDFn&si=TClA3jkK99Ce2DRl"
    THUMBNAIL_FILEPATH = "thumbnail\\"
    URL = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
    AGE_RESTRICTED_VIDEO = "https://youtu.be/voQBX6yn2XY?si=e_4DHuE3jUDv5whc"

    youtubeLink = input("Enter the youtube link: ")
    print("download in progress...")
    # t1 = threading.Thread(target=download_video, args=(URL,))
    # t1.start()
    # t1.join()
    print("download completed!")


    






