import click
import requests
import sys

from PIL import Image
try:
    from StringIO import StringIO
except: # when using python3.x
    from io import BytesIO, StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('src', nargs=-1)
#@click.argument('dst', nargs=1)
def main(src):
    	"""Get postter hero lol list"""
	name=""	
	for fn in src:
        	name+='%s' % (fn)+" "
	#name+='%s'%(dst)
	url='https://lol.garena.in.th/champions/detail/{}'.format(name.replace(" ",""))
	html=requests.get(url)
	beau=BeautifulSoup(html.content,'html.parser')
	poster="https://lol.garena.in.th"+beau.find_all('div',{'class':'default-1-3'})[0].img['src']	
	print poster
	req=requests.get(poster)
	img=Image.open(StringIO(req.content))
	img.show()
