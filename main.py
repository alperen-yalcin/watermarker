from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
os.environ["IMAGEMAGICK_BINARY"] = "/opt/homebrew/bin/magick"  


video = VideoFileClip("./video/watermarked.mp4")

watermark = TextClip("@watermark", fontsize=40, color="white", font="Arial-Bold")
watermark = watermark.set_duration(video.duration)  
watermark = watermark.set_pos(("right","bottom"))   
watermark = watermark.set_opacity(0.6)             

final = CompositeVideoClip([video, watermark])

final.write_videofile("video_watermarked.mp4", codec="libx264", audio_codec="aac")
