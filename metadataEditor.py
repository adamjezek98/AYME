import requests
import json


class MetadataEditor():
    def __init__(self, key_path="token.json"):
        with open(key_path) as json_file:
            self.token = json.load(json_file)
        # self.api_key = json.loads(open(key_path))
        self.access_token = None  # self.api_key["access_token"]
        self.BASIC_HEADER = None
        self.BASE_PATH = "https://www.googleapis.com/youtube/v3/"
        self.get_auth_token()

    def get_auth_token(self):
        url = "https://www.googleapis.com/oauth2/v4/token"

        payload = {'client_id': self.token["client_id"],
                   'client_secret': self.token["client_secret"],
                   'refresh_token': self.token["refresh_token"],
                   'grant_type': 'refresh_token'}
        files = [

        ]
        response = requests.request("POST", url, data=payload, files=files)
        json_data = json.loads(response.text)
        self.access_token = json_data["access_token"]
        self.BASIC_HEADER = {'Authorization': f'Bearer {self.access_token}'}

    def upload_thumbnail(self, video_id, file_path):
        files = {'upload_file': open(file_path, 'rb')}
        params = {"videoId": video_id}
        r = requests.post("https://www.googleapis.com/upload/youtube/v3/thumbnails/set", files=files, params=params,
                          headers=self.BASIC_HEADER)
        return r.status_code == 200, r.status_code, r.text

    def edit_metadata(self, video_id, title=None, description=None, tags=None, categoryId=None, fetchData=True):
        data = {"id": video_id}
        snip = {}
        part = set()
        if fetchData:
            vid_data = self.get_video_info(video_id)
            print(vid_data)
            snip["title"] = vid_data["snippet"]["title"]
            snip["description"] = vid_data["snippet"]["description"]
            snip["categoryId"] = vid_data["snippet"]["categoryId"]
            snip["tags"] = vid_data["snippet"]["tags"]
        if title is not None:
            snip["title"] = title
            part.add("snippet")
        if description is not None:
            snip["description"] = description
            part.add("snippet")
        if tags is not None:
            snip["tags"] = tags
            part.add("snippet")
        if categoryId is not None:
            snip["categoryId"] = categoryId
            part.add("snippet")

        data["snippet"] = snip
        headers = self.BASIC_HEADER
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'
        params = {"part": ",".join(part)}
        r = requests.put(self.BASE_PATH + "videos", data=json.dumps(data), headers=headers, params=params)
        return r.status_code == 200, r.status_code, r.text

    def get_video_info(self, videoId):

        headers = self.BASIC_HEADER
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'

        params = {
            "part": "snippet",
            "id": videoId
        }

        response = requests.request("GET", self.BASE_PATH + "videos", headers=headers, params=params)
        if response.status_code != 200:
            return False, response.status_code, {}
        else:
            json_data = response.json()
            return json_data['items'][0]
