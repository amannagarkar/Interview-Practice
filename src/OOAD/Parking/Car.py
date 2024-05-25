class Car:
    def __init__(self, vehicle_id, vehicle_name, vehicle_entry_time, spot):
        self.vehicle_id = vehicle_id
        self.vehicle_name = vehicle_name
        self.entry_time = vehicle_entry_time
        self.parking_spot = spot

    def parked_hour_total(self, vehicle_exit_time):
        parked_hour = vehicle_exit_time - self.entry_time
        return parked_hour
