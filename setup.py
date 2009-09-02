from setuptools import setup

packages_path = os.path.abspath(os.path.dirname(__file__))

datafiles = []
doc_files = []
icon_files = []

prefix = sys.prefix + '/'

for arg in sys.argv:
	if arg.startswith('--prefix='):
		prefix = arg[9:]
		prefix = os.path.expandvars(prefix)

ipath_docs = '%sshare/doc/qtumblr/' % prefix
ipath_images = '%sshare/pixmaps/qtumblr/' % prefix
ipath_dashboard = ipath_images+'dashboard/'

path_images = packages_path + '/images/'

images = ['audio.png','chat.png','link.png','photo.png','quote.png','text.png','video.png']
for img in images:
	image_files.append(path_images + img)

docs = ['AUTHORS','INSTALL','LICENSE','README','THANKS','PKG-INFO']
for doc in docs:
	doc_files.append(packages_path + '/' + doc)

icons = ['qtumblr.png','qtumblr.xpm']
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

datafiles.append(('share/pixmaps/', icon_files))
datafiles.append((ipath_docs, doc_files))
datafiles.append(('share/applications',[packages_path+'/qtumblr.desktop']))
datafiles.append((ipath_dashboard, image_files))

setup(
    name = 'Qtumblr',
    version = '0.1',
    description = 'Qt Tumblr Client based on Opentumblr',
    author = 'Alejandro Villanueva',
    author_email = 'admin at ialex.org',
    url = 'http://ialex.org',
    license = 'MIT',
    scripts = ['qtumblr-client.py'],
    packages = find_packages(),
    package_dir = {'qtumblr' : qtumblr}, 
    data_files = datafiles,
    install_requires = ['poster','simplejson']
     )
