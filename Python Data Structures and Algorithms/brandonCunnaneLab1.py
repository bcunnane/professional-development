

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
        if Movie.strOK(self, the_name):
            self.name = the_name
        else:
            self.name = Movie.DEFAULT_NAME
    
    def setYear(self, the_year):
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
        count = 1
        for item in Movie._movieList:
            print(f'{count}. {item}')
            count +=1
        print('')
            
        
    # helpers
    def getStr(self):
        return str(self)
    
    def strOK(self, the_str):
        MAX_LEN = 50
        if len(the_str) <= MAX_LEN:
            return True
        else:
            return False
    
    def yearOK(self, the_year):
        MIN_YEAR = 1000
        MAX_YEAR = 2023
        if MIN_YEAR < the_year < MAX_YEAR:
            return True
        else:
            return False
    
        
        
    