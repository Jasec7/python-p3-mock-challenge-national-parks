class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise Exception("National Park already assigned")
        if not isinstance(value, str):
            raise Exception("National Park must be a string")
        if len(value.strip()) < 3:
            raise Exception("Names must be equal or greater than 3")
        self._name = value

        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        matches = []
        for trip in self.trips():
            vi = trip.visitor
            if vi not in matches:
                matches.append(vi)
        return matches
    
    def total_visits(self):
        all_visits = self.trips()
        return  len(all_visits)
    
    def best_visitor(self):
        count = 0
        person = None 
        visits = {}
        for trip in self.trips():
            visitor = trip.visitor
            if visitor in visits:
                visits[visitor] = visits[visitor] + 1
            else:
                visits[visitor] = 1
        
            
        for visitor, num_trips in visits.items():
                if num_trips > count:
                    person = visitor
                    count = num_trips
        return person
    
    @classmethod
    def  most_visited(cls):
        popular_park = None
        count = 0

        for p in cls.all:
            visits = p.total_visits()
            if visits > count:
                count = visits
                popular_park = p
        return popular_park

            

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise Exception("Not a visitor")
        else: 
            self._visitor = value

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise Exception("Not a park")
        else:
            self._national_park = value

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise Exception("Not a date")
        if len(value.strip()) < 7:
            raise Exception("Start date must be greater than 7 characters")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise Exception("Not a date")
        if len(value.strip()) < 7:
            raise Exception("End date must be greater than 7 characters")
        self._end_date = value





class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise Exception("Names must be between 1 and 15 characters, inclusive")
        self._name = value
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        matches = []
        for trip in self.trips():
            p = trip.national_park
            if p not in matches:
                matches.append(p)
        return matches

    
    def total_visits_at_park(self, park):
        count = 0

        for trips in self.trips():
            if trips.national_park == park:
                count += 1
        return count
