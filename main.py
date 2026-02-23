import csv
from math import ceil

# variables
total_videos = 0
youtube_videos = 0
tiktok_videos = 0
total_likes = 0
dislikes = 0
youtube_likes = 0
tiktok_likes = 0
total_views = 0
youtube_views = 0
tiktok_views = 0
impressions = 0
avg_likes = 0
avg_dislikes = 0
avg_youtube_likes = 0
avg_tiktok_likes = 0
avg_views = 0
avg_youtube_views = 0
avg_tiktok_views = 0
avg_impressions = 0
most_likes = 0
least_likes = float('inf')
most_likes_youtube = 0
least_likes_youtube = float('inf')
most_likes_tiktok = 0
least_likes_tiktok = float('inf')
most_views = 0
least_views = float('inf')
most_views_youtube = 0
least_views_youtube = float('inf')
most_views_tiktok = 0
least_views_tiktok = float('inf')
most_liked_video = "something"
least_liked_video = "something"
most_liked_youtube_video = "something"
least_liked_youtube_video = "something"
most_liked_tiktok_video = "something"
least_liked_tiktok_video = "something"
most_viewed_video = "something"
least_viewed_video = "something"
most_viewed_youtube_video = "something"
least_viewed_youtube_video = "something"
most_viewed_tiktok_video = "something"
least_viewed_tiktok_video = "something"


csv_path = "C:/Users/patky/Documents/Programming/Python/Hello/Shorts_Analyzer/data/shorts_data.csv"

with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:

        title = row['Title'].strip()

        if title:
            total_videos += 1
        likes_temp = row['Likes'].strip()
        dislikes_temp = row['Dislikes'].strip()
        impressions_temp = row['Impressions'].strip()
        views_temp = row['Views'].strip()
        platform = row['Platform'].strip().lower()
        total_likes += int(likes_temp) if likes_temp else 0
        total_views += int(views_temp) if views_temp else 0
        likes = int(likes_temp) if likes_temp else 0
        dislikes_1 = int(dislikes_temp) if dislikes_temp else 0
        views = int(views_temp) if views_temp else 0
        impressions_1 = int(impressions_temp) if impressions_temp else 0

        if likes > most_likes:
            most_likes = likes
            most_liked_video = title
        if likes < least_likes:
            least_likes = likes
            least_liked_video = title

        if views > most_views:
            most_views = views
            most_viewed_video = title
        if views < least_views:
            least_views = views
            least_viewed_video = title

        if platform == "youtube":
            youtube_videos += 1
            youtube_likes += likes
            youtube_views += views
            impressions += impressions_1
            dislikes += dislikes_1
            if likes > most_likes_youtube:
                most_likes_youtube = likes
                most_liked_youtube_video = title
            if likes < least_likes_youtube:
                least_likes_youtube = likes
                least_liked_youtube_video = title
            if views > most_views_youtube:
                most_views_youtube = views
                most_viewed_youtube_video = title
            if views < least_views_youtube:
                least_views_youtube = views
                least_viewed_youtube_video = title
        else:
            tiktok_videos += 1
            tiktok_likes += likes
            tiktok_views += views
            if likes > most_likes_tiktok:
                most_likes_tiktok = likes
                most_liked_tiktok_video = title
            if likes < least_likes_tiktok:
                least_likes_tiktok = likes
                least_liked_tiktok_video = title
            if views > most_views_tiktok:
                most_views_tiktok = views
                most_viewed_tiktok_video = title
            if views < least_views_tiktok:
                least_views_tiktok = views
                least_viewed_tiktok_video = title
    if total_videos:
        avg_likes = total_likes/total_videos
        avg_views = total_views/total_videos
    if youtube_videos:
        avg_dislikes = dislikes/youtube_videos
        avg_impressions = impressions/youtube_videos
        avg_youtube_likes = youtube_likes/youtube_videos
        avg_youtube_views = youtube_views/youtube_videos
    if tiktok_videos:
        avg_tiktok_likes = tiktok_likes/tiktok_videos
        avg_tiktok_views = tiktok_views/tiktok_videos

    print(f"""
          Total Videos: {total_videos}
          Youtube Videos: {youtube_videos}
          TikTok Videos: {tiktok_videos}
          Total Likes: {total_likes}
          Total Dislikes: {dislikes}
          YouTube Likes: {youtube_likes}
          TikTok Likes: {tiktok_likes}
          TikTok Views: {tiktok_views}
          Total Views: {total_views}
          Youtube Views: {youtube_views}
          Average Likes: {ceil(avg_likes)}
          Average Dislikes: {ceil(avg_dislikes)}
          Average YouTube Likes: {ceil(avg_youtube_likes)}
          Average TikTok Likes: {ceil(avg_tiktok_likes)}
          Average Views: {ceil(avg_views)}
          Average Youtube Views: {ceil(avg_youtube_views)}
          Average TikTok Views: {ceil(avg_tiktok_views)}
          Average Impressions: {ceil(avg_impressions)}
          Most Views: {most_views}
          Most Viewed Video: {most_viewed_video}
          Most Views in YouTube: {most_views_youtube}
          Most Viewed YouTube Video: {most_viewed_youtube_video}
          Least Views in Youtube: {least_views_youtube}
          Least Viewed Video in YouTube: {least_viewed_youtube_video}
          Most Views in TikTok: {most_views_tiktok}
          Most Viewed Video in TikTok: {most_viewed_tiktok_video}
          Least Views in TikTok: {least_views_tiktok}
          Least Viewed Video in TikTok: {least_viewed_tiktok_video}
          Most Likes: {most_likes}
          Most Liked Video: {most_liked_video}
          Most likes in YouTube: {most_likes_youtube}
          Most Liked Video in YouTube: {most_liked_youtube_video}
          Least Likes in Youtube: {least_likes_youtube}
          Least Liked Video in Youtube: {least_liked_youtube_video}
          Most Likes in TikTok: {most_likes_tiktok}
          Most Liked Video in TikTok: {most_liked_tiktok_video}
          Least Likes in TikTok: {least_likes_tiktok}
          Least Liked Video in TikTok: {least_liked_tiktok_video}
          """)
