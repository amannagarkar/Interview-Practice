from src.OOAD.Parking.Car import Car


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ParkingLot = dict()
        self.EmptyLot = ['P' + str(k) for k in range(capacity)]
        self.parking_cost = 2

    def display_lot(self):
        for i in self.ParkingLot:
            print(i)

    def empty_spots(self):
        print(self.EmptyLot)

    def allocate_parking(self, vehicle_id, vehicle_name, entry_time):
        if len(self.EmptyLot) > 0:
            spot = self.EmptyLot.pop(0)
            vehicle = Car(vehicle_id, vehicle_name, entry_time, spot)
            self.ParkingLot[vehicle.vehicle_id] = vehicle
            return f"Vehicle {vehicle_id} assigned to Spot {spot}"
        else:
            return "Parking Lot Full"

    def vehicle_exit(self, vehicle_id, exit_time):
        if vehicle_id in self.ParkingLot:
            vehicle = self.ParkingLot[vehicle_id]
            amount = self.payment_calculate(vehicle.vehicle_id,exit_time)
            self.EmptyLot.append(vehicle.parking_spot)
            self.ParkingLot.pop(vehicle_id)
            return f"Vehicle {vehicle_id} left from Spot {vehicle.parking_spot}. Payment owed {amount} USD"
        else:
            return "Vehicle not in Spot"

    def payment_calculate(self, vehicle_id, exit_time):
        if vehicle_id in self.ParkingLot:
            vehicle = self.ParkingLot[vehicle_id]
            return (vehicle.parked_hour_total(exit_time) * self.parking_cost) / 100
