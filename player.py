import json

import requests

from exceptions import ResponseException
from secret import spotify_token, spotify_user_id


class Player:
    def __init__(self):
        show_id = self.searchShow()
        self.sampleEpisodes(show_id)

    def searchShow(self):
        """Search For Podcast"""
        # TODO localization info
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
        """Get show episodes"""
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

        for show in episodes:
            print(show["description"] + "\n")


if __name__ == '__main__':
    cp = Player()
