# PodSampler

Search for your favorite podcast and scan through it's episodes, 30 seconds at a time. Get sentiment analysis and a keyword summary before committing to listen.

## Technologies

- [Spotify Web API]
- [Google Cloud NLP APIs]

## LocalSetup

1. Install Dependencies  
   `pip3 install -r requirements.txt`

2. Populate secret.py with spotify auth token and local username

   - Your auth token can be found at https://developer.spotify.com/console/get-show-episodes/ by clicking "Get Token"
   - Your local username can be found by running `pwd` from any terminal and copying the directory name after "/Users/"

3. Configure a Google Cloud project and download the appropriate authentication tokens

   - There are a lot of details I'm omitting here, this is a complex process (as far as I know)

4. Run  
   `python3 player.py`

## Troubleshooting

- Spotify Oauth tokens expire quickly. Watch for KeyErrors - they likely are the result of an expired token. Follow step 2 to generate a fresh one
- There is a good bit of Google Cloud authentication necessary to get this running