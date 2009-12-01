#!/usr/bin/python
from distutils.core import setup
import os, sys

packages_path = os.path.abspath(os.path.dirname(__file__))

datafiles = []
doc_files = []
icon_files = []
image_files = []

prefix = sys.prefix + '/'
qtumblr = packages_path + '/opentumblrqt'
print qtumblr 

for arg in sys.argv:
	if arg.startswith('--prefix='):
		prefix = arg[9:]
		prefix = os.path.expandvars(prefix)

ipath_docs = '%sshare/doc/opentumblr-qt/' % prefix
ipath_images = '%sshare/pixmaps/opentumblr-qt/' % prefix
ipath_icons = '%sshare/pixmaps/' % prefix
ipath_desktop_file = '%sshare/applications/' % prefix
ipath_dashboard = ipath_images+'dashboard/'

path_images = packages_path + '/images/'

images = ['audio.png','chat.png','link.png','photo.png','quote.png','text.png','video.png',
		  'bold.png','italic.png','strike.png','more.png','link_editor.png','image.png','preview.png',
		  'close.png','opentumblr_icon.jpg']
for img in images:
	image_files.append(path_images + img)

docs = ['AUTHORS','INSTALL','LICENSE','README','THANKS']
for doc in docs:
	doc_files.append(packages_path + '/' + doc)

icons = ['opentumblr-qt.png','opentumblr-qt.xpm']
for icon in icons:
	icon_files.append(path_images + icon)

if not os.path.isdir(ipath_docs):
	if not os.path.isdir(prefix + 'share'):
		os.mkdir(prefix + 'share')
		os.mkdir(prefix + 'share/doc')
	os.mkdir(ipath_docs)

if not os.path.isdir(ipath_images):
	if not os.path.isdir(prefix + 'share/pixmaps'):
		os.mkdir(prefix + 'share/pixmaps')
	os.mkdir(ipath_images)
	os.mkdir(ipath_dashboard)

datafiles.append((ipath_icons, icon_files))
datafiles.append((ipath_docs, doc_files))
datafiles.append((ipath_desktop_file,[packages_path + '/opentumblr-qt.desktop']))
datafiles.append((ipath_dashboard, image_files))

setup(
    name = 'opentumblr-qt',
    version = '0.2',
    description = 'Qt Tumblr Client based on Opentumblr',
    author = 'Alejandro Villanueva',
    author_email = 'admin at ialex.org',
    url = 'http://ialex.org',
    license = 'MIT',
    scripts = ['opentumblrqt/opentumblr-qt-client.py'],
    packages = ['opentumblrqt','opentumblrqt.gui'],
    #package_dir = {'qtumblr' : tumblr,}, 
    data_files = datafiles,
    #include_package_data = True,
    #install_requires = ['poster','simplejson']
     )
#print datafiles
#print packages_path
