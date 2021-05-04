import webbrowser
import os
import sys

from pkg_resources import working_set
from pkg_resources import Requirement

pkg_name = 'eomwgtsite'

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/env/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

site_path = working_set.find(Requirement.parse(pkg_name)).location + "/" + '\\WGT_Website\\'

command = 'python3 ' + site_path + '/manage.py runserver'
os.system(command)

#url = 'http://localhost:8000/'

#webbrowser.open(url)
