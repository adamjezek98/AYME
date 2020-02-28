from metadataEditor import MetadataEditor

ME = MetadataEditor()
print(ME.access_token)
#print(ME.upload_thumbnail(video_id="ZrUOOUKWEQY", file_path="C:\\Users\\jezek\\Downloads\\20191102_215528.jpg"))

#print(ME.get_video_info("ZrUOOUKWEQY"))



#print(ME.edit_metadata(video_id="ZrUOOUKWEQY", title="New editet title", description="And here goes description",
#                      tags=["and", "some", "tags"], categoryId=22))
print(ME.edit_metadata(video_id="ZrUOOUKWEQY", title="🐝 zigbee2mqtt.io (Adam Hořčica)", fetchData=True))