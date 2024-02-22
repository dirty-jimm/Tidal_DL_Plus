# Tidal_DL_Plus
Script to automatically download albums added to Tidal collection via Tidal-DL. Removes album from collection post download.

A few prerequisites:
- A linux server.
- A Tidal Subscription.

1. Install Tidal-DL, https://github.com/yaronzz/Tidal-Media-Downloader.
This is the program that does the actual downloading. Play around with it and get it to a state where you are able to successfully download albums to the location of your choice. I like to use a folder that both Plex and Lidarr can see, but is distinct from my "processed" music folder.

3. Download and run the pyhton script in this repo.
You'll need to change the 'X_USER_X' on line 49 to the user with tidal-dl installed. The first time you run it, it will generate a Tidal Url to visit to generate some API credentials. These creds will save in a text file so you shouldn't need to do this again.

5. Add an album to your favourites (if using the Plexamp this is called "Add to collection", run the script again and it should download that album.

6. Schedule the script as you like. I cron job it to run every minute. Part of the script ensures only one instance runs at a time.


Recommended tidal-dl settings:
<img width="690" alt="image" src="https://github.com/dirty-jimm/Tidal_DL_Plus/assets/41983227/820dc294-9883-4834-8c4f-ddc9a7cfd419">

