
## Video Data Analyzer

## Description
A Python tool, which the user can analyze their videos' data with a CSV file.

## Features Youtube/Short Videos
- Allows the user to use their own CSV files.
- Counts total Views, Likes, Subscriptions, Impressions, Dislikes and total Video Count in each category.
- Calculates the average of likes, views, subscriptions, impressions, dislikes of up to 100 videos.
- Searches for the highest and lowest values of the above data, as well as to which video they belong to.
- Finds the best and the least performing video based on the above data.
- Seperates above data on time groups of 2 hours, calculates each time groups' average likes, views and subscriptions and
  based on the averages of likes and views, it pinpoints the two best time groups to post a video based on likes and
  the two best time groups to post a video based on views.
- Displays separately Full-Length YouTube Videos Data and YouTube Short Videos Data with different colors for each group.

## Features TikTok Videos
- Allows the user to use their own CSV files.
- Counts total Views, Likes and Video Count.
- Calculates the average of likes and views.
- Searches for the highest and lowest values of the above data, as well as to which video they belong to.
- Finds the best and the least performing video based on the above data.
- Seperates above data on time groups of 2 hours, calculates each time groups' average likes and views and based on that,
  it pinpoints the two best time groups to post a video based on likes and the two best time groups to post a video based on views.
- Displays seperately from the Youtube analytics its data and in a different color.

## How to run
1. Place your CSV Folders in the Data Folder. In this version, only either Youtube CSV files with rows of likes, dislikes, impressions, views, dislikes, subscriptions and upload time or
   TikTok CSV files with likes, views and upload time are compatible.
3. Run main.py
4. Input the exact path of your file, as well as the name of the data and the .csv in the end.
5. To exit, simply input 'Exit' when the file path is asked or when you're asked, if you
   want to continue, simply type 'no'.

## Requirements
1. Windows 8 or later

2. Python 3.13.7 or later

