# PodSampler

Search for your favorite podcast and scan through it's episodes, 30 seconds at a time

## Technologies

- [Spotify Web API]
- [Requests Library v 2.22.0]=

## LocalSetup

1. Install Dependencies  
   `pip3 install -r requirements.txt`

2. Collect You Spotify User ID and Oauth Token From Spotfiy and add it to secrets.py file

   - To Collect your User ID, Log into Spotify then go here: [Account Overview] and its your **Username**
     ![alt text](images/userid.png)
   - To Collect your Oauth Token, Visit this url here: [Get Oauth] and click the **Get Token** button
     ![alt text](images/spotify_token.png)

3. Run  
   `python3 player.py`

## Troubleshooting

- Spotify Oauth token expires very quickly, If you come across a `KeyError` this could
  be caused by an expired token. So just refer back to step 3 in local setup, and generate a new
  token
