'''
Reloading a module:
------------------
module reload once, even you declared multiple import of the modules...

how to get the latest changes of the module, if the module changed in between.

you can use reload() in the imp module...
'''

import moduleone
from imp import reload

reload(moduleone)