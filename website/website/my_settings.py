import subprocess
DEBUG = False
if subprocess.getstatusoutput("echo $USER")[1] == 'odland':
    DEBUG = True

STATIC_URL = '/static/'
ROOT_URLCONF = 'website.urls'