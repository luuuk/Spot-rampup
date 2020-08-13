import json
import requests

from playsound import playsound
from exceptions import ResponseException
from secret import spotify_token, username
import webbrowser
import os


class Player:
    def __init__(self):
        show_id = self.searchShow()
        self.sampleEpisodes(show_id)

    def searchShow(self):
        pod_name = input(
            "What is the name of your podcast? ")
        print("Searching for " + pod_name + "\n")

        query = "https://api.spotify.com/v1/search?q=name:{}&type=show".format(
            pod_name.replace(' ', '%20')
        )

        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        if response.status_code != 200:
            webbrowser.open(
                "https://developer.spotify.com/console/get-show-episodes/")
            raise ResponseException(response.status_code)

        response_json = response.json()
        shows = response_json["shows"]["items"]

        print(str(len(response_json["shows"]["items"])) + " shows found\n")
        for show in shows:
            print("Name: " + show["name"] + " / " +
                  show["description"].strip() + "\n")
            if (input("Is this the show you were looking for (Y/N)? ").lower() == "y"):
                return show["id"]

        print(":(")
        quit()

    def sampleEpisodes(self, show_id):
        query = "https://api.spotify.com/v1/shows/{}/episodes".format(
            show_id
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        episodes = response_json["items"]

        print("Now sampling " + str(len(episodes)) +
              " episodes")

        print("Once audio begins playing, you can use ")

        path = "/Users/{}/Downloads/temp.mp3".format(username)
        for show in episodes:
            print("\n" + show["description"].strip() + "\n")

            # Download audio
            r = requests.get(show["audio_preview_url"])

            with open(path, 'wb') as f:
                f.write(r.content)

            # Play audio
            while (1):
                playsound(path)

                if input("Press S to exit and listen on Spotify ").upper() == "S":
                    liked_show = show["external_urls"]["spotify"]
                    print("Internal break")
                    break

            if liked_show:
                print("WTF")
                break

        # Delete audio
        os.remove(path)
        if liked_show:
            webbrowser.open(liked_show)
            print("We're glad we could help you find a show you like!\n")


if __name__ == '__main__':
    cp = Player()
