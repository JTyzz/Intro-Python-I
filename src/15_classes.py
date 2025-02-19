# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

  def __str__(self):
    return f"name: {self.name}   lat: {self.lat}   lon: {self.lon}"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"name: {self.name} lat: {self.lat} lon: {self.lon} size: {self.size} difficulty: {self.difficulty}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print("The location is %s, located at latitude %s and longitude %s" % (waypoint.name, waypoint.lat, waypoint.lon))

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print("The geocache is at %s, with a difficulty of %s. Located at lat: %s and lon: %s" % (geocache.name, geocache.difficulty, geocache.lat, geocache.lon))
