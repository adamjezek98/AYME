
Requirements
===
```
pip install google-auth-oauthlib
pip install google-api-python-client  
pip install google-auth-httplib2
```

Access token
===
Create project at console.developer.google.com. Make consent screen, save it, but don't send it for google verification. 
Then go to credentials, create OAuth cliend ID, download it as json, and then let this json be processed with oauth_autorize_token.py
Run the script, you will get an URL, visit it in browser (you will get warning about unauthorized app, doesn't matter), choose account, and you will get key.
Paste that to the console, and token json will be printed. Save that to token.json, which is used by metedaaEditor class. 


