import warnings

c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

# Run without authentication
c.NotebookApp.token = ''
# Allow requests from the proxy
c.NotebookApp.allow_origin = '*'

# c.NotebookApp.nbserver_extensions = {
#     'jupyter_localize_extension': True,
# }

c.NotebookApp.trust_xheaders = True
# c.NotebookApp.terminals_enabled = True

# hide warnings by default
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

