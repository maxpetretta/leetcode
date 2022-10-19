from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.trips, self.averages = {}, defaultdict(lambda: TripAverage(0, 0))
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = TripDetails(stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        trip = self.trips.pop(id)
        total = t - trip.time
        self.averages[(trip.station, stationName)].total += total
        self.averages[(trip.station, stationName)].count += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        average = self.averages.get((startStation, endStation))
        return (average.total / average.count)

    
class TripDetails:
    def __init__(self, station, time):
        self.station = station
        self.time = time

        
class TripAverage:
    def __init__(self, total, count):
        self.total = total
        self.count = count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
