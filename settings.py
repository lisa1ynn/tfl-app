class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Vehicle settings
        self.vehicle_speed = 0.8

        # Tube Station settings
        self.tubestop_stpauls_x = 690
        self.tubestop_stpauls_y = 830
        self.tubestop_holborn_x = 380
        self.tubestop_holborn_y = 560
        self.tubestop_tottenhamcourtroad_x = 40
        self.tubestop_tottenhamcourtroad_y = 540
        self.tubestop_russlesquare_x = 340
        self.tubestop_russlesquare_y = 20
        self.tubestop_coventgarden_x = 340
        self.tubestop_coventgarden_y = 850

        # Bus Station settings
        # North/South bus route
        self.busstop_x_n_x = 980
        self.busstop_x_n_y = 50
        self.busstop_x_x = 980
        self.busstop_x_y = 200
        self.busstop_x_s_x = 980
        self.busstop_x_s_y = 600
        # East/West bus route
        self.busstop_y_w_x = 500
        self.busstop_y_w_y = 360
        self.busstop_y_x = 800
        self.busstop_y_y = 360
        self.busstop_y_e_x = 1200
        self.busstop_y_e_y = 360

        # Bus times
        #self.bus1_station1_time = 12.00
        #self.bus1_station2_time = 12.03

        # Tube times
        #self.tube1_station2_time = datetime(2023, 12, 5, 12, 0)  # Replace with your start time
        #self.tube1_station1_time = datetime(2023, 12, 5, 12, 3)  # Replace with your end time

        # vehicle start and stop position
        # self.startstop1_x = self.station1_x - 50
        # self.startstop1_y = self.station1_y

        # self.startstop2_x = self.station2_x + 50
        # self.startstop2_y = self.station2_y
