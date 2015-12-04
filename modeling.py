import random

class Person:

    population = []
    graveyard = []

    def __init__ (self):
        self.infected = False
        self.population.append(self)

    def die (self):
        self.population.remove(self)
        self.graveyard.append(self)

    def tick (self):
        # Do whatever you do to simulate a unit of life. Perhaps
        # interact with some subset of the population?
        if len(self.population) > 5:
            friends = random.sample(self.population,5)
            spouses = random.sample(self.population,1)
        else:
            friends = self.population[:] # Everyone!
        # Do something with your friends here...
            

        
class DataWriter:
    '''A simple class to write data to a file.'''

    
    def __init__ (self, filename):
        self.f = file(filename,'w')
        self.output_header()

    def output_text (self, txt):
        self.f.write(txt+'\n') # Add newline

    def output_list (self, data_list):
        txt = ''
        for itm in data_list:
            txt += str(itm)+','
        self.output_text(txt)

    def output_header (self):
        self.output_text('Live,Dead')

    def output_data (self):
        # Output data for our population...
        # You'll want to do something more so you can track the number
        # of infected people, immune people, etc.
        self.output_list([len(Person.population),len(Person.graveyard)])

    def finish (self):
        self.f.close()
    

def create_people (self):
        for i in range(5000):
            Person()
        

def run_simulation (population, ticks, filename='data.csv'):
    print 'really running'
    dataWriter = DataWriter(filename) 
    create_people(population)
    for t in range(ticks):
        dataWriter.output_data()
        for p in Person.population:
            p.tick() # Tick tick tick
    dataWriter.finish()

# Run simulation for population & ticks...
run_simulation(5000,365)
create_people()

