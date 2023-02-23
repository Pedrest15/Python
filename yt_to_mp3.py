from pytube import YouTube
import os
from pathlib import Path

def youtube_to_mp3 (url: str, outdir: str) -> None:
    # url input from user
    yt = YouTube(url)

    # extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='160kbps').last()

    # download the file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    
    # check if it was successful
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
    else:
        print(f'ERROR: {yt.title} could not be downloaded!')


if __name__ == "__main__":
    music_dir: str = "Output_Directory"

    with open("List_of_Musics.txt", "r") as musics_names:
        for music in musics_names:
            youtube_to_mp3(music, music_dir)
