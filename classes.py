# Filename: classes.py
# Author: Jesmine Mok 6c11
# Description: Support classes for music library


'''Super Class Resource '''
class Resource:

    '''Constructor; Its first line will always call a self; to denote private data self.__XXXXX'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    '''Resource number accessor'''
    def getResourceNo(self):
        return self.__ResourceNo

    ''' Title accessor'''
    def getTitle(self):
        return self.__Title

    '''Date Acquired accessor'''
    def getDateAcquired(self):
        return self.__DateAcquired

    '''Resource type accessor'''
    def getResourceType(self):
        return self.__ResourceType

    '''Title modifier'''
    def setTitle(self, newTitle):
        self.__Title = newTitle

    '''Date acquired modifier'''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    '''ResourceType modifier'''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    '' 'Display helper function'''
    def display(self):
        return "{0:5s}{1:32s}{2:6s}{3}".format(self.getResourceNo(), self.getTitle(), self.getDateAcquired(), self.getResourceType())
    

''' Sub Class Resource'''
class MusicCd(Resource):

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks

    '''Artist accesoor'''
    def getArtist(self):
        return self.__Artist

    ''' Number of Tracks accessor'''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    '''Artist modifier'''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    '''Number of tracks modifier'''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    '''Display help modifier'''
    def display(self):
        return "{0}{1}{2}".format(super().display(), self.getArtist(), self.getNoOfTracks())
    

''' Sub Class Resource'''
class FilmDvd(Resource):

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime

    ''' Director accessor'''
    def getDirector(self):
        return self.__Director

    '''RunningTime accessor'''
    def getRunningTime(self):
        return self.__RunningTime

    '''Director modifier'''
    def setDirector(self, newDirector):
        self.__Director = newDirector

    '''RunningTime modifier'''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    ''' Display help modifier'''
    def display(self):
        return "{0}{1}{2}".format(super().display(), self.getDirector(), self.getRunningTime())





### main
##r1 = Resource("00001", "Good Day", "110115", "C")
##print(r1.getResourceNo())
##r1.setTitle("TGIF")
##print(r1.getTitle())
##print(r1.display())
##
### another way to do
##r2 = Resource("00002", "", "", "")
##r2.setTitle("BT")
##r2.setDateAcquired("101010")
##r2.setResourceType("C")
##
##print(r2.display())
##
##cd1 = MusicCd("00003", "Beatles Vol.1", "090909", "C", "Beatles", 10)
##print(cd1.getResourceNo()) # inheritance
##print(cd1.getArtist())
##print(cd1.display()) # overriding
##
##dvd1 = FilmDvd("00004", "Kungfu Panda", "090810", "D", "Bamboo Association", 135)
##print(dvd1.display())
##
##resource_list = []
##
##resource_list.append(cd1)
##resource_list.append(dvd1)
##print(resource_list)
##
##for item in resource_list:
##    print(item.display()) # polymorphism
##
