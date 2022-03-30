from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

start_time =100
end_time = 160
ffmpeg_extract_subclip("match_1_.mp4", start_time, end_time, targetname="test_one_minute.avi")