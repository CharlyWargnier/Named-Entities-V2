from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder
vendor.add('lib')

############

# URL -> https://stackoverflow.com/questions/45232015/testing-my-gae-application-with-virtualenv-in-python
#import os
#from google.appengine.ext import vendor
#vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
