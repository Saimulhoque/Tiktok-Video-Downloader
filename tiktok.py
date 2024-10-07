import yt_dlp
import os


def download_tiktok_video(video_url, save_path='tiktok_videos'):
    # Ensure the save directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'format': 'best',
    }

    try:
        # Create a yt-dlp object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"Video successfully downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading video: {str(e)}")


# Example usage
video_url = "https://www.tiktok.com/@tuhin.k.1/video/7221809911766715650?q=funny&t=1728295082091"
download_tiktok_video(video_url)
