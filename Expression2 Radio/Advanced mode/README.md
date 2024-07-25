# Radio Expression2
## Advanced mode

### USE ONLY IF YOURE CONFORTABLE WITH PYTHON AND API

The advanced mode is to download spotify playlist and put them into a dropbox
To download the spotify playlist we'll be using the Spotdl librairie 
Then with the "dropbox-mp3-scrapper" file you'll be able to extract the dropbox sharelink and put it into a file 

## Spotdl download 

To download the Spotdl librairie you'll need to have python installed 
if you don't have python installed i invite you to download it 

once you arrived in the download menu i invite you to check this option : 

![image](https://github.com/user-attachments/assets/986d8318-6d97-4f26-84d4-e6fc05e66a24)

once this done you'll just need to do the classic python install (if you don't know how to install it i invite you to watch a youtube tuto)

next you have to open the windows terminal and type ```pip install spotdl```
when the download is complete type ```spotdl --download-ffmpeg```

And it should be good

## Spotdl usage 

you just have to type ```spotdl <SPOTIFY PLAYLIST LINK<```

and you're playlist should be downloading 

## Playlist to dropbox 

just put the new downloaded playlist to dropbox...

## Dropbox sharlink excrator

### Step 1: Access Dropbox Developer Console:
Visit the [Dropbox Developer Console](https://www.dropbox.com/developers) webpage and use your Dropbox account credentials to log in. (There’s no way to access it from your main Dropbox account.) 

### Step 2: Create a new app
In the Developer Console, click on the "Create app" button.
![image](https://github.com/user-attachments/assets/e6dc781e-3dc6-4a8d-83c1-1842708931cd)

Creating a new app in Dropbox

### Step 3: Configure your app settings
Provide a unique name for your app, and select the appropriate access level (e.g., Full Dropbox, App folder). Configure other settings as needed for your specific use case.
![image](https://github.com/user-attachments/assets/489cd029-3112-4420-ac2f-64501f39a811)

Configuring your app settings

‍### Step 4 : Edit the app permissions 

you'll need to check the following options : 

![image](https://github.com/user-attachments/assets/02f195ea-87b0-4890-983f-643b78823645)

### Step 5: Generate your access token (i.e. your API key)
Once your app is created, you’ll land on the settings tab. Scroll down to the "OAuth 2" section, where you'll find the option to generate an access token. This access token serves as your API key.
![image](https://github.com/user-attachments/assets/c95d31b4-c04d-4251-acf7-68c78c234551)


### Step 6: Copy and store your API key
After generating the access token, copy it and securely store it in your application's configuration. 


### Step 7: Install the dropbox librairie
Open the terminal and type : ```pip install dropbox```


### Step 8: Edit the the "dropbox-mp3-scrapper" file 
Put your api key here : 

![image](https://github.com/user-attachments/assets/6c574b62-4ae9-47c2-953e-60d8f36d2e90)


### Step 9: Run the script 
Run the script and it should start making the file (the process might be a bit long so be patient)



## Puting the new created file to the e2file folder

First rename the file to "playlist_<WHATEVER YOU WANT<" then put it in the e2file folder (Steam\steamapps\common\GarrysMod\garrysmod\data\e2files)

to load the playlist you'll have to type ```/load <WHAT YOU PUT IN WHATEVER YOU WANT<```

And everything should work !
(if not good luck)

if the dropbox link is too long for the gmod chat you can use the ranme script that will only keep the music name and remove the author name 
