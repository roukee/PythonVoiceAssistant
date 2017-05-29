import logging
import pkgutil


class Brain(object):

    def __init__(self, mic, profile):
        """
        Instantiates a new Brain object, which cross-references user
        input with a list of modules. Note that the order of brain.modules
        matters, as the Brain will cease execution on the first module
        that accepts a given input.
        Arguments:
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
        """

        self.mic = mic
        self.profile = profile
        self.modules = self.get_modules()
        self._logger = logging.getLogger(__name__)

    @classmethod
    def get_modules(cls):
        """
        Dynamically loads all the modules in the modules folder and sorts
        them by the PRIORITY key. If no PRIORITY is defined for a given
        module, a priority of 0 is assumed.
        """

        locations = ["modules"]
        modules = []
        for finder, name, ispkg in pkgutil.walk_packages(locations):
            try:
                loader = finder.find_module(name)
                mod = loader.load_module(name)
            except:
                print("Skipped module due to an error.")
            else:
                if hasattr(mod, 'WORDS'):
                    print("Found module with words: " + mod.WORDS)
                    modules.append(mod)
                else:
                    print("Skipped module because it misses " +
                                   "the WORDS constant.")
        modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY')
                     else 0, reverse=True)
	return modules	
    
    @classmethod
    def query(text, modules, texts, transcript):
        """
        Passes user input to the appropriate module, testing it against
        each candidate module's isValid function.
        Arguments:
        text -- user input, typically speech, to be parsed by a module
        """
	for module in modules:
                if module.isValid(texts):
                    	result = module.handle(texts, transcript)			
		    	return result

		
