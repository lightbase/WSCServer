from pyramid.view import view_config
from pyramid.response import FileResponse
from wscserver.scripts.createzip import zipcoleta
import os

@view_config(route_name='download')
def download(request):
    filepath = zipcoleta()
    # filesize = str(os.path.getsize(filepath))
    response = FileResponse(filepath,request=request,
    						content_type='application/zip')
    return response