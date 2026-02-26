import csv
from math import ceil
from colorama import Fore, Style

# Directory
def create_empty_stats():
    return {
        "totals": {"videos": 0, "subscribers": 0, "impressions": 0, "threshold": 0, "likes": 0, "dislikes": 0, "views": 0},
        "time_vars": {"upload_time": 0, "hour": 0, "time_groups":
                    {"time_group0_2": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group2_4": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group4_6": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group6_8": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group8_10": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0}, 
                        "time_group10_12": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group12_14": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group14_16": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group16_18": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group18_20": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group20_22": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "time_group22_24": {"counter": 0, "views": 0, "likes": 0, "subscribers": 0, "avg_views": 0, "avg_likes": 0, "avg_subscribers": 0},
                        "best_time_group_views": {"name": "something", "views": 0, "subscribers": 0},
                        "best_time_group_likes": {"name": "something", "likes": 0, "subscribers": 0}}},
        "averages": {"likes": 0, "dislikes": 0, "subscribers": 0, "views": 0, "impressions": 0},
        "most": {"likes": 0, "subscribers": 0, "views": 0, "impressions": 0, "dislikes": 0,
                "videos": {"liked": "something", "viewed": "something", "subscribed": "something", "disliked": "something", "impressive": "something"}},
        "least": {"likes": float('inf'), "subscribers": float('inf'), "views": float('inf'), "impressions": float('inf'), "dislikes": float('inf'),
                "videos": {"liked": "something", "viewed": "something", "subscribed": "something", "disliked": "something", "impressive": "something"}}
    }

full_stats = create_empty_stats()
shorts_stats = create_empty_stats()
tiktok_stats = create_empty_stats()


# YouTube Videos Analyzer

print(f"{Fore.RED}Youtube Full-Length-Video Statistics:\n")

csv_path = r"C:\Users\patky\Documents\VS_code\video_analyzer\data\full_videos_data.csv"
with open(csv_path, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        stats = full_stats
    # variables

        likes_temp1 = 0
        likes_temp2 = float('inf')
        likes_temp3 = 0
        likes_temp4 = float('inf')
        views_temp1 = 0
        views_temp2 = float('inf')
        views_temp3 = 0 
        views_temp4 = float('inf')
        impressions_temp1 = 0
        impression_temp2 = float('inf')
        best_subscriptions1 = 0
        best_subscriptions2 = 0
        best_likes2 = 0
        best_views2 = 0
        # shortcuts

        time_groups = stats["time_vars"]["time_groups"]
        best_views = stats["time_vars"]["time_groups"]["best_time_group_views"]["views"]
        best_likes = stats["time_vars"]["time_groups"]["best_time_group_likes"]["likes"]
        best_viewed = stats["time_vars"]["time_groups"]["best_time_group_views"]["name"]
        best_liked = stats["time_vars"]["time_groups"]["best_time_group_likes"]["name"]
        
        title = row['Title'].strip()

        if title:
            
            likes_temp = row['Likes'].strip()
            dislikes_temp = row['Dislikes'].strip()
            impressions_temp = row['Impressions'].strip()
            views_temp = row['Views'].strip()
            subscribers_temp = row['Subscribers']
            stats["time_vars"]["upload_time"] = row['Upload_Time'].strip()
            stats["time_vars"]["hour"] = int(stats["time_vars"]["upload_time"].split(":")[0])
            subscribers = int(subscribers_temp) if subscribers_temp else 0
            likes = int(likes_temp) if likes_temp else 0
            dislikes = int(dislikes_temp) if dislikes_temp else 0
            views = int(views_temp) if views_temp else 0
            impressions = int(impressions_temp) if impressions_temp else 0

            # total data accumulation
            stats["totals"]["videos"] += 1
            stats["totals"]["likes"] += int(likes)
            stats["totals"]["views"] += int(views)
            stats["totals"]["subscribers"] += int(subscribers)
            stats["totals"]["impressions"] += int(impressions)
            stats["totals"]["dislikes"] += int(dislikes)

    # most/least data accumulation

            if likes > stats["most"]["likes"]:
                stats["most"]["likes"] = likes
                stats["most"]["videos"]["liked"] = title
                views_temp1 = views
            elif likes == stats["most"]["likes"]:
                if views > views_temp1:
                    stats["most"]["videos"]["liked"] = title
                    views_temp1 = views

            if likes < stats["least"]["likes"]:
                stats["least"]["likes"] = likes
                stats["least"]["videos"]["liked"] = title
                views_temp2 = views
            elif likes == stats["least"]["likes"]:
                if views < views_temp2:
                    stats["least"]["videos"]["liked"] = title
                    views_temp2 = views

            if dislikes > stats["most"]["dislikes"]:
                stats["most"]["dislikes"] = dislikes
                stats["most"]["videos"]["disliked"] = title
                likes_temp1 = likes
            elif dislikes == stats["most"]["dislikes"]:
                if likes_temp1 > likes:
                    stats["most"]["videos"]["disliked"] = title
                    likes_temp1 = likes

            if dislikes < stats["least"]["dislikes"]:
                stats["least"]["dislikes"] = dislikes
                stats["least"]["videos"]["disliked"] = title
                likes_temp2 = likes
            elif dislikes == stats["least"]["dislikes"]:
                if likes_temp2 < likes:
                    stats["least"]["videos"]["disliked"] = title
                    likes_temp2 = likes                       

            if views > stats["most"]["views"]:
                stats["most"]["views"] = views
                stats["most"]["videos"]["viewed"] = title
                likes_temp3 = likes
            elif views == stats["most"]["views"]:
                if likes_temp3 < likes:
                    stats["most"]["videos"]["viewed"] = title
                    likes_temp3 = likes

            if views < stats["least"]["views"]:
                stats["least"]["views"] = views
                stats["least"]["videos"]["viewed"] = title
                likes_temp4 = likes
            elif views == stats["least"]["views"]:
                if likes_temp4 > likes:
                    stats["least"]["videos"]["viewed"] = title
                    likes_temp4 = likes

            if subscribers > stats["most"]["subscribers"]:
                stats["most"]["subscribers"] = subscribers
                stats["most"]["videos"]["subscribed"] = title
                impressions_temp1 = impressions
            elif subscribers == stats["most"]["subscribers"]:
                    if impressions_temp1 < impressions:
                        stats["most"]["videos"]["subscribed"] = title
                        impressions_temp1 = impressions    

            if subscribers < stats["least"]["subscribers"]:
                stats["least"]["subscribers"] = subscribers
                stats["least"]["videos"]["subscribed"] = title
                impressions_temp2 = impressions
            elif subscribers == stats["least"]["subscribers"]:
                    if impressions_temp2 > impressions:
                        stats["least"]["videos"]["subscribed"] = title
                        impressions_temp2 = impressions

            if impressions > stats["most"]["impressions"]:
                stats["most"]["impressions"] = impressions
                stats["most"]["videos"]["impressive"] = title
                views_temp3 = views
            elif impressions == stats["most"]["impressions"]:
                if views_temp3 < views:
                    stats["most"]["videos"]["impressive"] = title
                    views_temp3 = views

            if impressions < stats["least"]["impressions"]:
                stats["least"]["impressions"] = impressions
                stats["least"]["videos"]["impressive"] = title
                views_temp4 = views
            elif impressions == stats["least"]["impressions"]:
                if views_temp4 > views:
                        stats["least"]["videos"]["impressive"] = title
                        views_temp4 = views

        # average stats accumulation

            if stats["totals"]["videos"]:
                stats["averages"]["likes"] = stats["totals"]["likes"] / \
                    stats["totals"]["videos"]
                stats["averages"]["views"] = stats["totals"]["views"] / \
                    stats["totals"]["videos"]
                stats["averages"]["subscribers"] = stats["totals"]["subscribers"] / \
                    stats["totals"]["videos"]
                stats["averages"]["dislikes"] = stats["totals"]["dislikes"] / \
                    stats["totals"]["videos"]
                stats["averages"]["impressions"] = stats["totals"]["impressions"] / \
                    stats["totals"]["videos"]
        
            # time groups data accumulation

            time_group_list = [time_groups[f"time_group{i}_{i+2}"] for i in range (0, 24, 2)]
            group = time_group_list[stats["time_vars"]["hour"] // 2]
            group["counter"] += 1
            group["views"] += views
            group["likes"] += likes
            group["subscribers"] += subscribers

    # time groups data sorting

    stats["totals"]["threshold"] = 10 * stats["totals"]["videos"] / 100

    for name, bucket in time_groups.items():
        if name == "best_time_group_views" or name == "best_time_group_likes" or stats["totals"]["threshold"] > bucket["counter"]:
            continue

        bucket["avg_likes"] = bucket["likes"] / bucket["counter"]
        bucket["avg_views"] = bucket["views"] / bucket["counter"]
        bucket["avg_subscribers"] = bucket["subscribers"] / bucket["counter"]

        if bucket["avg_likes"] > best_likes:
            best_liked2 = best_liked
            best_likes2 = best_likes
            best_liked = name
            best_likes = bucket["avg_likes"]
            best_subscriptions3 = best_subscriptions1
            best_subscriptions1 = bucket["avg_subscribers"]
        elif bucket ["avg_likes"] <best_likes and bucket["avg_likes"] >= best_likes2:
            best_likes2 = bucket["avg_likes"]
            best_liked2 = name
            best_subscriptions3 = bucket["avg_subscribers"]

            
        if bucket["avg_views"] > best_views:
            best_viewed2 = best_viewed
            best_views2 = best_views
            best_viewed = name
            best_views = bucket["avg_views"]
            best_subscriptions4 = best_subscriptions2
            best_subscriptions2 = bucket["avg_subscribers"]
        elif bucket["avg_views"] < best_views and bucket["avg_views"] >= best_views2:
            best_views2 = bucket["avg_views"]
            best_viewed2 = name
            best_subscriptions4 = bucket["avg_subscribers"]

        # Filtering the best upload time

    print(f"""
          Total YouTube Videos: {stats["totals"]["videos"]}
          Total YouTube Likes: {stats["totals"]["likes"]}
          Total YouTube Dislikes: {stats["totals"]["dislikes"]}
          Total YouTube Views: {stats["totals"]["views"]}
          Total YouTube Subscribers: {stats["totals"]["subscribers"]} 
          Total YouTube Impressions: {stats["totals"]["impressions"]}
          Average Likes per YouTube Video: {ceil(stats["averages"]["likes"])}
          Average Dislikes per YouTube Video: {ceil(stats["averages"]["dislikes"])}
          Average Views per YouTube Video: {ceil(stats["averages"]["views"])}
          Average Impressions per YouTube Video: {ceil(stats["averages"]["impressions"])}
          Average Subscribers per YouTube Video: {ceil(stats["averages"]["subscribers"])}
          Most Views in a YouTube Video: {stats["most"]["views"]}
          Most Viewed YouTube Video: {stats["most"]["videos"]["viewed"]}
          Most Likes in a YouTube Video: {stats["most"]["likes"]}
          Most Liked YouTube Video: {stats["most"]["videos"]["liked"]}
          Most Dislikes in a YouTube Video: {stats["most"]["dislikes"]}
          Most Disliked YouTube Video: {stats["most"]["videos"]["disliked"]}
          Most Impressions in a YouTube Video: {stats["most"]["impressions"]}
          Most Impressive YouTube Video: {stats["most"]["videos"]["impressive"]}
          Most Subscribers gained in a YouTube Video: {stats["most"]["subscribers"]}
          Most Subscribed YouTube Video: {stats["most"]["videos"]["subscribed"]}
          Least Views in a YouTube Video: {stats["least"]["views"]}
          Least Viewed YouTube Video: {stats["least"]["videos"]["viewed"]}
          Least Likes in a YouTube Video: {stats["least"]["likes"]}
          Least Liked YouTube Video: {stats["least"]["videos"]["liked"]}
          Least Dislikes in a YouTube Video: {stats["least"]["dislikes"]}
          Least Disliked YouTube Video: {stats["least"]["videos"]["disliked"]}
          Least Impressions in a YouTube Video: {stats["least"]["impressions"]}
          Least Impressive YouTube Video: {stats["least"]["videos"]["impressive"]}
          Least Subscribers gained in a YouTube Video: {stats["least"]["subscribers"]}
          Least Subscribed YouTube Video: {stats["least"]["videos"]["subscribed"]}
          Best Time to Post a YouTube Video based on Views: {best_viewed} with average views: {ceil(best_views)} and {ceil(best_subscriptions1)} average subscriptions
          Second Best Time to Post a YouTube Video based on Views: {best_viewed2} with average views: {ceil(best_views2)} and {ceil(best_subscriptions3)} average subscriptions
          Best Time to Post a YouTube Video for Likes: {best_liked} with average likes: {ceil(best_likes)} and {ceil(best_subscriptions2)} average subscriptions
          Second Best Time to Post a YouTube Video Based on Likes: {best_liked2} with {ceil(best_likes2)} and {ceil(best_subscriptions4)} average subscriptions
          """, Style.RESET_ALL)

# YouTube Shorts Analyzer

print(f"{Fore.LIGHTRED_EX}YouTube Shorts Statistics:\n")

csv_path = r"C:\Users\patky\Documents\VS_code\video_analyzer\data\shorts_data.csv"
with open(csv_path, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        stats = shorts_stats
        title = row['Title'].strip()

        if title:
            
            likes_temp = row['Likes'].strip()
            dislikes_temp = row['Dislikes'].strip()
            impressions_temp = row['Impressions'].strip()
            views_temp = row['Views'].strip()
            subscribers_temp = row['Subscribers']
            stats["time_vars"]["upload_time"] = row['Upload_Time'].strip()
            stats["time_vars"]["hour"] = int(stats["time_vars"]["upload_time"].split(":")[0])
            subscribers = int(subscribers_temp) if subscribers_temp else 0
            likes = int(likes_temp) if likes_temp else 0
            dislikes = int(dislikes_temp) if dislikes_temp else 0
            views = int(views_temp) if views_temp else 0
            impressions = int(impressions_temp) if impressions_temp else 0

            # total data accumulation
            stats["totals"]["videos"] += 1
            stats["totals"]["likes"] += int(likes)
            stats["totals"]["views"] += int(views)
            stats["totals"]["subscribers"] += int(subscribers)
            stats["totals"]["impressions"] += int(impressions)
            stats["totals"]["dislikes"] += int(dislikes)

    # most/least data accumulation

            if likes > stats["most"]["likes"]:
                stats["most"]["likes"] = likes
                stats["most"]["videos"]["liked"] = title
                views_temp1 = views
            elif likes == stats["most"]["likes"]:
                if views > views_temp1:
                    stats["most"]["videos"]["liked"] = title
                    views_temp1 = views

            if likes < stats["least"]["likes"]:
                stats["least"]["likes"] = likes
                stats["least"]["videos"]["liked"] = title
                views_temp2 = views
            elif likes == stats["least"]["likes"]:
                if views < views_temp2:
                    stats["least"]["videos"]["liked"] = title
                    views_temp2 = views

            if dislikes > stats["most"]["dislikes"]:
                stats["most"]["dislikes"] = dislikes
                stats["most"]["videos"]["disliked"] = title
                likes_temp1 = likes
            elif dislikes == stats["most"]["dislikes"]:
                if likes_temp1 > likes:
                    stats["most"]["videos"]["disliked"] = title
                    likes_temp1 = likes

            if dislikes < stats["least"]["dislikes"]:
                stats["least"]["dislikes"] = dislikes
                stats["least"]["videos"]["disliked"] = title
                likes_temp2 = likes
            elif dislikes == stats["least"]["dislikes"]:
                if likes_temp2 < likes:
                    stats["least"]["videos"]["disliked"] = title
                    likes_temp2 = likes                       

            if views > stats["most"]["views"]:
                stats["most"]["views"] = views
                stats["most"]["videos"]["viewed"] = title
                likes_temp3 = likes
            elif views == stats["most"]["views"]:
                if likes_temp3 < likes:
                    stats["most"]["videos"]["viewed"] = title
                    likes_temp3 = likes

            if views < stats["least"]["views"]:
                stats["least"]["views"] = views
                stats["least"]["videos"]["viewed"] = title
                likes_temp4 = likes
            elif views == stats["least"]["views"]:
                if likes_temp4 > likes:
                    stats["least"]["videos"]["viewed"] = title
                    likes_temp4 = likes

            if subscribers > stats["most"]["subscribers"]:
                stats["most"]["subscribers"] = subscribers
                stats["most"]["videos"]["subscribed"] = title
                impressions_temp1 = impressions
            elif subscribers == stats["most"]["subscribers"]:
                    if impressions_temp1 < impressions:
                        stats["most"]["videos"]["subscribed"] = title
                        impressions_temp1 = impressions    

            if subscribers < stats["least"]["subscribers"]:
                stats["least"]["subscribers"] = subscribers
                stats["least"]["videos"]["subscribed"] = title
                impressions_temp2 = impressions
            elif subscribers == stats["least"]["subscribers"]:
                    if impressions_temp2 > impressions:
                        stats["least"]["videos"]["subscribed"] = title
                        impressions_temp2 = impressions

            if impressions > stats["most"]["impressions"]:
                stats["most"]["impressions"] = impressions
                stats["most"]["videos"]["impressive"] = title
                views_temp3 = views
            elif impressions == stats["most"]["impressions"]:
                if views_temp3 < views:
                    stats["most"]["videos"]["impressive"] = title
                    views_temp3 = views

            if impressions < stats["least"]["impressions"]:
                stats["least"]["impressions"] = impressions
                stats["least"]["videos"]["impressive"] = title
                views_temp4 = views
            elif impressions == stats["least"]["impressions"]:
                if views_temp4 > views:
                        stats["least"]["videos"]["impressive"] = title
                        views_temp4 = views

        # average stats accumulation

            if stats["totals"]["videos"]:
                stats["averages"]["likes"] = stats["totals"]["likes"] / \
                    stats["totals"]["videos"]
                stats["averages"]["views"] = stats["totals"]["views"] / \
                    stats["totals"]["videos"]
                stats["averages"]["subscribers"] = stats["totals"]["subscribers"] / \
                    stats["totals"]["videos"]
                stats["averages"]["dislikes"] = stats["totals"]["dislikes"] / \
                    stats["totals"]["videos"]
                stats["averages"]["impressions"] = stats["totals"]["impressions"] / \
                    stats["totals"]["videos"]
        
            # time groups data accumulation

            time_group_list = [time_groups[f"time_group{i}_{i+2}"] for i in range (0, 24, 2)]
            group = time_group_list[stats["time_vars"]["hour"] // 2]
            group["counter"] += 1
            group["views"] += views
            group["likes"] += likes
            group["subscribers"] += subscribers

    # time groups data sorting

    stats["totals"]["threshold"] = 10 * stats["totals"]["videos"] / 100

    for name, bucket in time_groups.items():
        if name == "best_time_group_views" or name == "best_time_group_likes" or stats["totals"]["threshold"] > bucket["counter"]:
            continue

        bucket["avg_likes"] = bucket["likes"] / bucket["counter"]
        bucket["avg_views"] = bucket["views"] / bucket["counter"]
        bucket["avg_subscribers"] = bucket["subscribers"] / bucket["counter"]

        if bucket["avg_likes"] > best_likes:
            best_liked2 = best_liked
            best_likes2 = best_likes
            best_liked = name
            best_likes = bucket["avg_likes"]
            best_subscriptions3 = best_subscriptions1
            best_subscriptions1 = bucket["avg_subscribers"]
        elif bucket ["avg_likes"] <best_likes and bucket["avg_likes"] >= best_likes2:
            best_likes2 = bucket["avg_likes"]
            best_liked2 = name
            best_subscriptions3 = bucket["avg_subscribers"]

            
        if bucket["avg_views"] > best_views:
            best_viewed2 = best_viewed
            best_views2 = best_views
            best_viewed = name
            best_views = bucket["avg_views"]
            best_subscriptions4 = best_subscriptions2
            best_subscriptions2 = bucket["avg_subscribers"]
        elif bucket["avg_views"] < best_views and bucket["avg_views"] >= best_views2:
            best_views2 = bucket["avg_views"]
            best_viewed2 = name
            best_subscriptions4 = bucket["avg_subscribers"]

        # Filtering the best upload time

    print(f"""
          Total Shorts: {stats["totals"]["videos"]}
          Total Short Likes: {stats["totals"]["likes"]}
          Total Short Dislikes: {stats["totals"]["dislikes"]}
          Total Short Views: {stats["totals"]["views"]}
          Total Short Subscribers: {stats["totals"]["subscribers"]} 
          Total Short Impressions: {stats["totals"]["impressions"]}
          Average Likes per Short: {ceil(stats["averages"]["likes"])}
          Average Dislikes per Short: {ceil(stats["averages"]["dislikes"])}
          Average Views per Short: {ceil(stats["averages"]["views"])}
          Average Impressions per Short: {ceil(stats["averages"]["impressions"])}
          Average Subscribers per Short: {ceil(stats["averages"]["subscribers"])}
          Most Views in a Short: {stats["most"]["views"]}
          Most Viewed Short: {stats["most"]["videos"]["viewed"]}
          Most Likes in a Short: {stats["most"]["likes"]}
          Most Liked Short: {stats["most"]["videos"]["liked"]}
          Most Dislikes in a Short: {stats["most"]["dislikes"]}
          Most Disliked Short: {stats["most"]["videos"]["disliked"]}
          Most Impressions in a Short: {stats["most"]["impressions"]}
          Most Impressive Short: {stats["most"]["videos"]["impressive"]}
          Most Subscribers gained in a Short: {stats["most"]["subscribers"]}
          Most Subscribed Short: {stats["most"]["videos"]["subscribed"]}
          Least Views in a Short: {stats["least"]["views"]}
          Least Viewed Short: {stats["least"]["videos"]["viewed"]}
          Least Likes in a Short: {stats["least"]["likes"]}
          Least Liked Short: {stats["least"]["videos"]["liked"]}
          Least Dislikes in a Short: {stats["least"]["dislikes"]}
          Least Disliked Short: {stats["least"]["videos"]["disliked"]}
          Least Impressions in a Short: {stats["least"]["impressions"]}
          Least Impressive Short: {stats["least"]["videos"]["impressive"]}
          Least Subscribers gained in a Short: {stats["least"]["subscribers"]}
          Least Subscribed Short: {stats["least"]["videos"]["subscribed"]}
          Best Time to Post a Short based on Views: {best_viewed} with average views: {ceil(best_views)} and {ceil(best_subscriptions1)} average subscriptions
          Second Best Time to Post a Short based on Views: {best_viewed2} with average views: {ceil(best_views2)} and {ceil(best_subscriptions3)} average subscriptions
          Best Time to Post a Short for Likes: {best_liked} with average likes: {ceil(best_likes)} and {ceil(best_subscriptions2)} average subscriptions
          Second Best Time to Post a Short Based on Likes: {best_liked2} with {ceil(best_likes2)} and {ceil(best_subscriptions4)} average subscriptions
          """, Style.RESET_ALL)


# TikTok Analyzer

print(f"{Fore.LIGHTMAGENTA_EX}TikTok Videos Statistics:\n")

csv_path = r"C:\Users\patky\Documents\VS_code\video_analyzer\data\tiktok_data.csv"
with open(csv_path, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        stats = tiktok_stats
        title = row['Title'].strip()

        if title:
            
            likes_temp = row['Likes'].strip()
            views_temp = row['Views'].strip()
            stats["time_vars"]["upload_time"] = row['Upload_Time'].strip()
            stats["time_vars"]["hour"] = int(stats["time_vars"]["upload_time"].split(":")[0])
            likes = int(likes_temp) if likes_temp else 0
            views = int(views_temp) if views_temp else 0

            # total data accumulation
            stats["totals"]["videos"] += 1
            stats["totals"]["likes"] += int(likes)
            stats["totals"]["views"] += int(views)

    # most/least data accumulation

            if likes > stats["most"]["likes"]:
                stats["most"]["likes"] = likes
                stats["most"]["videos"]["liked"] = title
                views_temp1 = views
            elif likes == stats["most"]["likes"]:
                if views > views_temp1:
                    stats["most"]["videos"]["liked"] = title
                    views_temp1 = views

            if likes < stats["least"]["likes"]:
                stats["least"]["likes"] = likes
                stats["least"]["videos"]["liked"] = title
                views_temp2 = views
            elif likes == stats["least"]["likes"]:
                if views < views_temp2:
                    stats["least"]["videos"]["liked"] = title
                    views_temp2 = views                 

            if views > stats["most"]["views"]:
                stats["most"]["views"] = views
                stats["most"]["videos"]["viewed"] = title
                likes_temp3 = likes
            elif views == stats["most"]["views"]:
                if likes_temp3 < likes:
                    stats["most"]["videos"]["viewed"] = title
                    likes_temp3 = likes

            if views < stats["least"]["views"]:
                stats["least"]["views"] = views
                stats["least"]["videos"]["viewed"] = title
                likes_temp4 = likes
            elif views == stats["least"]["views"]:
                if likes_temp4 > likes:
                    stats["least"]["videos"]["viewed"] = title
                    likes_temp4 = likes

        # average stats accumulation

            if stats["totals"]["videos"]:
                stats["averages"]["likes"] = stats["totals"]["likes"] / \
                    stats["totals"]["videos"]
                stats["averages"]["views"] = stats["totals"]["views"] / \
                    stats["totals"]["videos"]
        
            # time groups data accumulation

            time_group_list = [time_groups[f"time_group{i}_{i+2}"] for i in range (0, 24, 2)]
            group = time_group_list[stats["time_vars"]["hour"] // 2]
            group["counter"] += 1
            group["views"] += views
            group["likes"] += likes

    # time groups data sorting

    stats["totals"]["threshold"] = 10 * stats["totals"]["videos"] / 100

    for name, bucket in time_groups.items():
        if name == "best_time_group_views" or name == "best_time_group_likes" or stats["totals"]["threshold"] > bucket["counter"]:
            continue

        bucket["avg_likes"] = bucket["likes"] / bucket["counter"]
        bucket["avg_views"] = bucket["views"] / bucket["counter"]

        if bucket["avg_likes"] > best_likes:
            best_liked2 = best_liked
            best_likes2 = best_likes
            best_liked = name
            best_likes = bucket["avg_likes"]
        elif bucket ["avg_likes"] <best_likes and bucket["avg_likes"] >= best_likes2:
            best_likes2 = bucket["avg_likes"]
            best_liked2 = name

            
        if bucket["avg_views"] > best_views:
            best_viewed2 = best_viewed
            best_views2 = best_views
            best_viewed = name
            best_views = bucket["avg_views"]
        elif bucket["avg_views"] < best_views and bucket["avg_views"] >= best_views2:
            best_views2 = bucket["avg_views"]
            best_viewed2 = name

        # Filtering the best upload time

    print(f"""
          Total Videos: {stats["totals"]["videos"]}
          Total Likes: {stats["totals"]["likes"]}
          Total Views: {stats["totals"]["views"]}
          Average Likes per Video: {ceil(stats["averages"]["likes"])}
          Average Views per Video: {ceil(stats["averages"]["views"])}
          Most Views in a Video: {stats["most"]["views"]}
          Most Viewed Video: {stats["most"]["videos"]["viewed"]}
          Most Likes in a Video: {stats["most"]["likes"]}
          Least Views in a Video: {stats["least"]["views"]}
          Least Viewed Video: {stats["least"]["videos"]["viewed"]}
          Least Likes in a Video: {stats["least"]["likes"]}
          Least Liked Video: {stats["least"]["videos"]["liked"]}
          Best Time to Post a Video based on Views: {best_viewed} with average views: {ceil(best_views)}
          Second Best Time to Post a Video based on Views: {best_viewed2} with average views: {ceil(best_views2)}
          Best Time to Post a Video for Likes: {best_liked} with average likes: {ceil(best_likes)}
          Second Best Time to Post a Video Based on Likes: {best_liked2} with average likes: {ceil(best_likes2)}
          """, Style.RESET_ALL)
