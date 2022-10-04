"""
Movie class
Maintains a list of movie titles and release years
"""

class Movie:
    
    # class constants
    DEFAULT_NAME = "" 
    DEFAULT_YEAR = 2022
    _movieList = []
    
    # initialization
    def __init__(self, name, year):
        self.setName(name)
        self.setYear(year)
    
    def __str__(self):
        return f'{self.name} ({self.year})'
    
    # mutators
    def setName(self, the_name):
        # set movie name
        if Movie.strOK(self, the_name):
            self.name = the_name
        else:
            self.name = Movie.DEFAULT_NAME
    
    def setYear(self, the_year):
        # set movie year
        if Movie.yearOK(self, the_year):
            self.year = the_year
        else:
            self.year = Movie.DEFAULT_YEAR
    
    def add(the_movie):
        Movie._movieList.append(the_movie)
        print(f'{the_movie.getName()} was added.\n')
    
    def delete(num):
        removed = Movie._movieList.pop(num-1)
        print(f'{removed.getName()} was deleted.\n')
        
    # accessors
    def getName(self):
        return self.name
    
    def getYear(self):
        return self.year
    
    def getList():
        # display a numbered list of all recorded movie titles and years
        count = 1
        for item in Movie._movieList:
            print(f'{count}. {item}')
            count +=1
        print('')
            
        
    # helpers
    def getStr(self):
        # returns a string of the movie title and year
        return str(self)
    
    def strOK(self, the_str):
        # checks if an input string is less than 50 characters
        MAX_LEN = 50
        if len(the_str) <= MAX_LEN:
            return True
        else:
            return False
    
    def yearOK(self, the_year):
        # checks if an input year is valid, between years 1000 and 2023
        MIN_YEAR = 1000
        MAX_YEAR = 2023
        if MIN_YEAR < the_year < MAX_YEAR:
            return True
        else:
            return False
    
        
        
    