AVC YouTube Metadata Editor
===
The important part is `MetadataEditor` class, which can upload a thumbnail to YT video, or edit it's metadata. Samples can be seen im `editorTester.py`. Also, some other scripts for access token generation are incuded (see Access token section). 

As this was designed to process batches of videos based on input from Airtable, some sample usage (without any documentation, yet) is in `service.py`.

Requirements
===
```
pip install google-auth-oauthlib
pip install google-api-python-client  
pip install google-auth-httplib2
```

Access token
===
Create project at `console.developer.google.com`. Make consent screen, save it, but don't send it for google verification. 
Then go to credentials, create OAuth cliend ID, download it as json (`client?secret.json`), and then let this json be processed with `oauth_autorize_token.py`
Run the script, you will get an URL, visit it in browser (you will get warning about unauthorized app, doesn't matter), choose account, and you will get key.
Paste that to the console, and token json will be printed. Save that to `token.json`, which is used by `MetedataEditor` class. On init, the class uses that refresh token to generate access tokens. Access tokens are valid for 60 minutes. You are expected to process all requests withint that period. Automatic refresh of tokens is not implemented yet. If your script will run for a longer time, you should call `get_auth_token` sometimes.
`

