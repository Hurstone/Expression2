# Radio Expression2
## Advanced mode

### USE ONLY IF YOURE COMFORTABLE WORKING WITH PYTHON AND API

The advanced mode is made to download spotify playlist(s) and put them into a dropbox
To download the spotify playlist we will be using the Spotdl library 
Then with the "dropbox-mp3-scrapper" file you will be able to extract the dropbox sharelink and put it into a file

## Spotdl download 

To download the Spotdl library you will need to have python installed 
if you do not have python installed you should download the python installer before continuing the setup. 

once you run the installer, make sure this option is checked and then you can proceed to start the installation.

![image](https://github.com/user-attachments/assets/986d8318-6d97-4f26-84d4-e6fc05e66a24)

once the installer has finished the installation,

you have to open the command-line and type ```pip install spotdl```
and then running ```spotdl --download-ffmpeg``` should finish installation of Spotdl

## Spotdl usage 

using the command ```spotdl <SPOTIFY PLAYLIST LINK>``` you can download the specified playlist

## Playlist to dropbox 

simply upload the files downloaded by executing the Spotdl command to your dropbox

## Dropbox sharelink extractor

### Step 1: Access Dropbox Developer Console:
Visit the [Dropbox Developer Console](https://www.dropbox.com/developers) webpage and log in with your dropbox credentials. (a Dropbox account is required for this) 

### Step 2: Create a new app
In the Developer Console, click on the "Create app" button.
![image](https://github.com/user-attachments/assets/e6dc781e-3dc6-4a8d-83c1-1842708931cd)

Creating a new app in Dropbox

### Step 3: Configure your app settings
Provide a unique name for your app and select the appropriate access level (e.g., Full Dropbox, App folder). Configure other settings as needed for your specific use case.
![image](https://github.com/user-attachments/assets/489cd029-3112-4420-ac2f-64501f39a811)

Configuring your app settings

‍### Step 4 : Edit the app permissions 

you will need to check the following options : 

![image](https://github.com/user-attachments/assets/02f195ea-87b0-4890-983f-643b78823645)

### Step 5: Generate your access token (i.e. your API key)
Once your app is created, you will be redirected to the settings tab. Scroll down to the "OAuth 2" section, where you will find the option to generate an access token. This access token serves as your API key.
![image](https://github.com/user-attachments/assets/c95d31b4-c04d-4251-acf7-68c78c234551)


### Step 6: Copy and store your API key
After generating the access token, copy it and securely store it in your application's configuration. 


### Step 7: Install the dropbox library
Open the command-line and type : ```pip install dropbox```


### Step 8: Edit the the "dropbox-mp3-scrapper" file 
Put your api key here : 

![image](https://github.com/user-attachments/assets/6c574b62-4ae9-47c2-953e-60d8f36d2e90)


### Step 9: Run the script 
Run the script and it should start making the file (the process might be a bit long so be patient)



## Puting the new created file to the e2files folder

First rename the file to "playlist_<PLAYLIST NAME>" then put it in the e2files folder (Steam\steamapps\common\GarrysMod\garrysmod\data\e2files)

to load the playlist you will have to type ```/load <PLAYLIST NAME>```

And everything should be operational.

