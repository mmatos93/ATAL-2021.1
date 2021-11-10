import os
import requests

video_url = input("Enter URL: ")
video_id = video_url.split('/')[-1]
final_file_name = video_url.split('/')[-2]


def get_video(video_url):
    num = 1
    files = ''
    while num:
        piece_number = str(num).zfill(5)
        url = 'https://d13z5uuzt1wkbz.cloudfront.net/' + video_id + '/HIDDEN4500-' + piece_number + '.ts'
        req = requests.get(url)
        file_size = (len(req.content) / 1024) /1024

        if req.status_code == 200:
            file_name = url.split('/')[-1]
            download_sc(url)
            num = num + 1
            files += file_name + ' '
            print(f'Download file: {file_name} {file_size:.2f}Mb')
        else:
            print(f'Downloaded {num-1} files.')
            os.system("cat " + files + " > " + final_file_name +".ts")
            os.system("rm " + files)
            print("Temporary files deleted...")
            print(f"Video file {final_file_name} created.")
            break

def download_sc(download_url):
    file_name = download_url.split('/')[-1]

    with requests.get(download_url) as req:
        with open(file_name, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return file_name

get_video(video_url)
