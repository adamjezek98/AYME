from airtable import Airtable
from metadataEditor import MetadataEditor
from urllib.request import urlretrieve
import airtable_keys as ak

airtable = Airtable(api_key=ak.api_key, base_key=ak.base_key, table_name=ak.table_name)
lines = airtable.get_all()

ME = MetadataEditor()

for line in lines:
    fields = line["fields"]


    if "YTVideoID" not in fields.keys():
        continue
    videoId = fields["YTVideoID"]
    if "Uploaded" not in fields.keys():
        print()
        continue
    if not fields["Uploaded"]:
        print("uploaded")
        continue

    if "Metadata nahrana" in fields.keys() and fields["Metadata nahrana"]:
        continue

    print("Processing", fields.keys())
    if "Fotka" in fields:
        file_name = "tmp/" + fields["Fotka"][0]["filename"].replace(" ", "_")
        url = fields["Fotka"][0]["url"]
        urlretrieve(url, file_name)
        print("Photo upload", file_name, ME.upload_thumbnail(videoId, file_path=file_name))

    YTname = fields["YTname"]
    YTtext = fields["YTtext"]
    YTtagy = fields["YTtagy"].split(", ")

    isok, statuscode, response = ME.edit_metadata(video_id=videoId, title=YTname, description=YTtext, tags=YTtagy, categoryId=28, fetchData=False)
    if isok:
        airtable.update(line["id"], {"Metadata nahrana": True})

