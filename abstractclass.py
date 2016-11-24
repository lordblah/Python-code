from abc import ABCMeta, abstractmethod
#baseclass below
class BaseClass(object):
    __metaclass__ =  ABCMeta
    #setting up the metaclass to be abract base clasee

    @abstractmethod #decorator,#way of altering functions or classes without having to inherit or subclass
    def printHam(self):
        pass

class InClass(BaseClass): #This is the inheritance class
    def printHam(self):
        print "ham"

#@abstrackmethod = decorator


    #why use abract classes, prevents base class from being instantiated
    #force funtions with EXCET name to be defined
