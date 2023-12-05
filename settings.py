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

        # Station settings
        self.station1_x = 300
        self.station1_y = 500

        self.station2_x = 1000
        self.station2_y = 500

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
