class Flight:
    def __init__(self, flight_id, flight_name, land_time, depart_time):
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.seats = [0] * 40
        self.flight_time = (land_time, depart_time)

