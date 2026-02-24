import csv
from math import ceil

# Directory

stats = {
    "totals": {"videos": 0, "youtube_videos": 0, "tiktok_videos": 0, "impressions": 0, "threshold": 0},
    "time_vars": {"upload_time": 0, "hour": 0, "time_groups": {"time_group0_4": {"counter": 0, "views": 0, "likes": 0, "avg_views": 0, "avg_likes": 0}, "time_group4_8": {"counter": 0, "views": 0, "likes": 0, "avg_views": 0, "avg_likes": 0},
                                                               "time_group8_12": {"counter": 0, "views": 0, "likes": 0, "avg_views": 0, "avg_likes": 0}, "time_group12_16": {"counter": 0, "views": 0, "likes": 0, "avg_views": 0, "avg_likes": 0},
                                                               "time_group16_20": {"counter": 0, "views": 0, "likes": 0, "avg_views": 0, "avg_likes": 0}, "time_group20_24": {"counter": 0, "views": 0, "likes": 0, "avg_views": 0, "avg_likes": 0},
                                                               "best_time_group_views": {"name": "something", "views": 0},
                                                               "best_time_group_likes": {"name": "something", "likes": 0}}},
    "likes": {"total": 0, "youtube": 0, "tiktok": 0, "dislikes": 0},
    "views": {"total": 0, "youtube": 0, "tiktok": 0},
    "averages": {"likes": {"total": 0, "dislikes": 0, "youtube": 0, "tiktok": 0},
                 "views": {"total": 0, "youtube": 0, "tiktok": 0}, "impressions": 0},
    "most": {"likes": {"all": 0, "youtube": 0, "tiktok": 0},
             "views": {"all": 0, "youtube": 0, "tiktok": 0},
             "videos": {"liked": {"all": "something", "youtube": "something", "tiktok": "something"},
                        "viewed": {"all": "something", "youtube": "something", "tiktok": "something"}}},
    "least": {"likes": {"all": float('inf'), "youtube": float('inf'), "tiktok": float('inf')},
              "views": {"all": float('inf'), "youtube": float('inf'), "tiktok": float('inf')},
              "videos": {"liked": {"all": "something", "youtube": "something", "tiktok": "something"},
                         "viewed": {"all": "something", "youtube": "something", "tiktok": "something"}}}
}

# shortcuts

time_groups = stats["time_vars"]["time_groups"]
tg_short1 = stats["time_vars"]["time_groups"]["time_group0_4"]
tg_short2 = stats["time_vars"]["time_groups"]["time_group4_8"]
tg_short3 = stats["time_vars"]["time_groups"]["time_group8_12"]
tg_short4 = stats["time_vars"]["time_groups"]["time_group12_16"]
tg_short5 = stats["time_vars"]["time_groups"]["time_group16_20"]
tg_short6 = stats["time_vars"]["time_groups"]["time_group20_24"]
best_views = stats["time_vars"]["time_groups"]["best_time_group_views"]["views"]
best_likes = stats["time_vars"]["time_groups"]["best_time_group_likes"]["likes"]
best_viewed = stats["time_vars"]["time_groups"]["best_time_group_views"]["name"]
best_liked = stats["time_vars"]["time_groups"]["best_time_group_likes"]["name"]

csv_path = "C:/Users/patky/Documents/Programming/Python/Hello/Shorts_Analyzer/data/shorts_data.csv"

with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:

        title = row['Title'].strip()

        if title:
            stats["totals"]["videos"] += 1
        likes_temp = row['Likes'].strip()
        dislikes_temp = row['Dislikes'].strip()
        impressions_temp = row['Impressions'].strip()
        views_temp = row['Views'].strip()
        platform = row['Platform'].strip().lower()
        stats["time_vars"]["upload_time"] = row['Upload_Time'].strip()
        stats["time_vars"]["hour"] = int(
            stats["time_vars"]["upload_time"].split(":")[0])
        stats["likes"]["total"] += int(likes_temp) if likes_temp else 0
        stats["views"]["total"] += int(views_temp) if views_temp else 0
        likes = int(likes_temp) if likes_temp else 0
        dislikes_1 = int(dislikes_temp) if dislikes_temp else 0
        views = int(views_temp) if views_temp else 0
        impressions_1 = int(impressions_temp) if impressions_temp else 0

# most/least data accumulation

        if likes > stats["most"]["likes"]["all"]:
            stats["most"]["likes"]["all"] = likes
            stats["most"]["videos"]["liked"]["all"] = title
        if likes < stats["least"]["likes"]["all"]:
            stats["least"]["likes"]["all"] = likes
            stats["least"]["videos"]["liked"]["all"] = title

        if views > stats["most"]["views"]["all"]:
            stats["most"]["views"]["all"] = views
            stats["most"]["videos"]["viewed"]["all"] = title
        if views < stats["least"]["views"]["all"]:
            stats["least"]["views"]["all"] = views
            stats["least"]["videos"]["viewed"]["all"] = title

        if platform == "youtube":
            stats["totals"]["youtube_videos"] += 1
            stats["likes"]["youtube"] += likes
            stats["views"]["youtube"] += views
            stats["totals"]["impressions"] += impressions_1
            stats["likes"]["dislikes"] += dislikes_1
            if likes > stats["most"]["likes"]["youtube"]:
                stats["most"]["likes"]["youtube"] = likes
                stats["most"]["videos"]["liked"]["youtube"] = title
            if likes < stats["least"]["likes"]["youtube"]:
                stats["least"]["likes"]["youtube"] = likes
                stats["least"]["videos"]["liked"]["youtube"] = title
            if views > stats["most"]["views"]["youtube"]:
                stats["most"]["views"]["youtube"] = views
                stats["most"]["videos"]["viewed"]["youtube"] = title
            if views < stats["least"]["views"]["youtube"]:
                stats["least"]["views"]["youtube"] = views
                stats["least"]["videos"]["viewed"]["youtube"] = title
        else:
            stats["totals"]["tiktok_videos"] += 1
            stats["likes"]["tiktok"] += likes
            stats["views"]["tiktok"] += views
            if likes > stats["most"]["likes"]["tiktok"]:
                stats["most"]["likes"]["tiktok"] = likes
                stats["most"]["videos"]["liked"]["tiktok"] = title
            if likes < stats["least"]["likes"]["tiktok"]:
                stats["least"]["likes"]["tiktok"] = likes
                stats["least"]["videos"]["liked"]["tiktok"] = title
            if views > stats["most"]["views"]["tiktok"]:
                stats["most"]["views"]["tiktok"] = views
                stats["most"]["videos"]["viewed"]["tiktok"] = title
            if views < stats["least"]["views"]["tiktok"]:
                stats["least"]["views"]["tiktok"] = views
                stats["least"]["videos"]["viewed"]["tiktok"] = title

    # average stats accumulation

        if stats["totals"]["videos"]:
            stats["averages"]["likes"]["total"] = stats["likes"]["total"] / \
                stats["totals"]["videos"]
            stats["averages"]["views"]["total"] = stats["views"]["total"] / \
                stats["totals"]["videos"]
        if stats["totals"]["youtube_videos"]:
            stats["averages"]["likes"]["dislikes"] = stats["likes"]["dislikes"] / \
                stats["totals"]["youtube_videos"]
            stats["averages"]["impressions"] = stats["totals"]["impressions"] / \
                stats["totals"]["youtube_videos"]
            stats["averages"]["likes"]["youtube"] = stats["likes"]["youtube"] / \
                stats["totals"]["youtube_videos"]
            stats["averages"]["views"]["youtube"] = stats["views"]["youtube"] / \
                stats["totals"]["youtube_videos"]
        if stats["totals"]["tiktok_videos"]:
            stats["averages"]["likes"]["tiktok"] = stats["likes"]["tiktok"] / \
                stats["totals"]["tiktok_videos"]
            stats["averages"]["views"]["tiktok"] = stats["views"]["tiktok"] / \
                stats["totals"]["tiktok_videos"]

        # time groups data accumulation

        if stats["time_vars"]["hour"] >= 0 and stats["time_vars"]["hour"] < 4:
            stats["time_vars"]["time_groups"]["time_group0_4"]["counter"] += 1
            stats["time_vars"]["time_groups"]["time_group0_4"]["views"] += views
            stats["time_vars"]["time_groups"]["time_group0_4"]["likes"] += likes
        elif stats["time_vars"]["hour"] >= 4 and stats["time_vars"]["hour"] < 8:
            stats["time_vars"]["time_groups"]["time_group4_8"]["counter"] += 1
            stats["time_vars"]["time_groups"]["time_group4_8"]["views"] += views
            stats["time_vars"]["time_groups"]["time_group4_8"]["likes"] += likes
        elif stats["time_vars"]["hour"] >= 8 and stats["time_vars"]["hour"] < 12:
            stats["time_vars"]["time_groups"]["time_group8_12"]["counter"] += 1
            stats["time_vars"]["time_groups"]["time_group8_12"]["views"] += views
            stats["time_vars"]["time_groups"]["time_group8_12"]["likes"] += likes
        elif stats["time_vars"]["hour"] >= 12 and stats["time_vars"]["hour"] < 16:
            stats["time_vars"]["time_groups"]["time_group12_16"]["counter"] += 1
            stats["time_vars"]["time_groups"]["time_group12_16"]["views"] += views
            stats["time_vars"]["time_groups"]["time_group12_16"]["likes"] += likes
        elif stats["time_vars"]["hour"] >= 16 and stats["time_vars"]["hour"] < 20:
            stats["time_vars"]["time_groups"]["time_group16_20"]["counter"] += 1
            stats["time_vars"]["time_groups"]["time_group16_20"]["views"] += views
            stats["time_vars"]["time_groups"]["time_group16_20"]["likes"] += likes
        elif stats["time_vars"]["hour"] >= 20 and stats["time_vars"]["hour"] < 25:
            stats["time_vars"]["time_groups"]["time_group20_24"]["counter"] += 1
            stats["time_vars"]["time_groups"]["time_group20_24"]["views"] += views
            stats["time_vars"]["time_groups"]["time_group20_24"]["likes"] += likes

    # time groups data sorting

    stats["totals"]["threshold"] = 10 * stats["totals"]["videos"] / 100

    for name, bucket in time_groups.items():
        if name == "best_time_group_views" or name == "best_time_group_likes" or stats["totals"]["threshold"] > bucket["counter"]:
            continue

        bucket["avg_likes"] = bucket["likes"]/bucket["counter"]
        bucket["avg_views"] = bucket["views"]/bucket["counter"]

        if bucket["avg_likes"] > best_likes:
            best_liked = name
            best_likes = bucket["avg_likes"]
        if bucket["avg_views"] > best_views:
            best_viewed = name
            best_views = bucket["avg_views"]

        # Filtering the best upload time

    print(f"""
          Total Videos: {stats["totals"]["videos"]}
          Youtube Videos: {stats["totals"]["youtube_videos"]}
          TikTok Videos: {stats["totals"]["tiktok_videos"]}
          Total Likes: {stats["likes"]["total"]}
          Total Dislikes: {stats["likes"]["dislikes"]}
          YouTube Likes: {stats["likes"]["youtube"]}
          TikTok Likes: {stats["likes"]["tiktok"]}
          TikTok Views: {stats["views"]["tiktok"]}
          Total Views: {stats["views"]["total"]}
          Youtube Views: {stats["views"]["youtube"]}
          Average Likes: {ceil(stats["averages"]["likes"]["total"])}
          Average Dislikes: {ceil(stats["averages"]["likes"]["dislikes"])}
          Average YouTube Likes: {ceil(stats["averages"]["likes"]["youtube"])}
          Average TikTok Likes: {ceil(stats["averages"]["likes"]["tiktok"])}
          Average Views: {ceil(stats["averages"]["views"]["total"])}
          Average Youtube Views: {ceil(stats["averages"]["views"]["youtube"])}
          Average TikTok Views: {ceil(stats["averages"]["views"]["tiktok"])}
          Average Impressions: {ceil(stats["averages"]["impressions"])}
          Most Views: {stats["most"]["views"]["all"]}
          Most Viewed Video: {stats["most"]["videos"]["viewed"]["all"]}
          Most Views in YouTube: {stats["most"]["views"]["youtube"]}
          Most Viewed YouTube Video: {stats["most"]["videos"]["viewed"]["youtube"]}
          Least Views in Youtube: {stats["least"]["views"]["youtube"]}
          Least Viewed Video in YouTube: {stats["least"]["videos"]["viewed"]["youtube"]}
          Most Views in TikTok: {stats["most"]["views"]["tiktok"]}
          Most Viewed Video in TikTok: {stats["most"]["videos"]["viewed"]["tiktok"]}
          Least Views in TikTok: {stats["least"]["views"]["tiktok"]}
          Least Viewed Video in TikTok: {stats["least"]["videos"]["viewed"]["tiktok"]}
          Most Likes: {stats["most"]["likes"]["all"]}
          Most Liked Video: {stats["most"]["videos"]["liked"]["all"]}
          Most likes in YouTube: {stats["most"]["likes"]["youtube"]}
          Most Liked Video in YouTube: {stats["most"]["videos"]["liked"]["youtube"]}
          Least Likes in Youtube: {stats["least"]["likes"]["youtube"]}
          Least Liked Video in Youtube: {stats["least"]["videos"]["liked"]["all"]}
          Most Likes in TikTok: {stats["most"]["likes"]["tiktok"]}
          Most Liked Video in TikTok: {stats["most"]["videos"]["liked"]["tiktok"]}
          Least Likes in TikTok: {stats["least"]["likes"]["tiktok"]}
          Least Liked Video in TikTok: {stats["least"]["videos"]["liked"]["tiktok"]}
          Best Time to Post a Video for Views: {best_viewed} with average views: {ceil(best_views)}
          Best Time to Post a Video for Likes: {best_liked} with average likes: {ceil(best_likes)}
          """)
