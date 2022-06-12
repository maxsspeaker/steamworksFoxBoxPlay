simple steam workshop downloader using steamcmd.

## USAGE

Download the release, extract and download SteamCmd and specify the path to it in the ini file. Run "steamworksFoxBoxPlay.exe". Enter the app ID of the game (see below) 
in the first field and to the second field one workshop ID or URL, then press "Download".

The file will be downloaded to the `mods` folder.

if you didn't find the mod file then the mod will be here:
`steamcmd/steamapps/workshop/content/<appID>/<workshop ID>`

Right now, only single items are supported (no batch downloading of collections yet).

### App ID

To find out the app ID of a game, go to its store page and look at the URL. The number after `/app/` is the app ID (eg. `https://store.steampowered.com/app/281990/Stellaris/` means the app ID of stellaris is 281990).

### WARNING

SteamworksFoxBoxPlay 
does not have steamCmd in it, in order for the program to work, download SteamCmd and specify the path to it in the ini file!

you can download here: https://developer.valvesoftware.com/wiki/SteamCMD

## Screenshots

![pythonw_OyamD1kZ73](https://user-images.githubusercontent.com/56259377/173238086-dfdef71c-f313-490d-bb28-9f64296ae9a4.png)

## Reminder

You can also move this exe file in the place with the config to the game folder, thereby automating the installation of mods!
