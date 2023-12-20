class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Vehicle settings
        self.vehicle_speed = 2

        # Tube Station settings
        self.tubestop_chancerylane_x = 690
        self.tubestop_chancerylane_y = 850
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
        self.busstop_x_s_y = 850
        # East/West bus route
        self.busstop_y_w_x = 500
        self.busstop_y_w_y = 360
        self.busstop_y_x = 800
        self.busstop_y_y = 360
        self.busstop_y_e_x = 1300
        self.busstop_y_e_y = 360

        self.bus_groups_dict = {
            'bus17_north': {
                'lineID': "17",
                'first_station_id': "490008165C",
                'third_station_id': "490007598S",
                'direction': "inbound",
                'first_station_x': self.busstop_x_s_x - 40,
                'first_station_y': self.busstop_x_s_y,
                'second_station_x': self.busstop_x_x - 40,
                'second_station_y': self.busstop_x_y,
                'third_station_x': self.busstop_x_n_x - 40,
                'third_station_y': self.busstop_x_n_y,
                'direction_x': 0,
                'direction_y': -1,
                'rotation_angle': 90,

            },
            'bus17_south': {
                'lineID': "17",
                'first_station_id': "490007598S",
                'third_station_id': "490008165C",
                'direction': "outbound",
                'first_station_x': self.busstop_x_n_x,
                'first_station_y': self.busstop_x_n_y,
                'second_station_x': self.busstop_x_x,
                'second_station_y': self.busstop_x_y,
                'third_station_x': self.busstop_x_s_x,
                'third_station_y': self.busstop_x_s_y,
                'direction_x': 0,
                'direction_y': 1,
                'rotation_angle': 270
            },
            'bus46_north': {
                'lineID': "46",
                'first_station_id': "490008165C",
                'third_station_id': "490007598S",
                'direction': "inbound",
                'first_station_x': self.busstop_x_s_x - 40,
                'first_station_y': self.busstop_x_s_y,
                'second_station_x': self.busstop_x_x - 40,
                'second_station_y': self.busstop_x_y,
                'third_station_x': self.busstop_x_n_x - 40,
                'third_station_y': self.busstop_x_n_y,
                'direction_x': 0,
                'direction_y': -1,
                'rotation_angle': 90
            },
            'bus46_south': {
                'lineID': "46",
                'first_station_id': "490007598S",
                'third_station_id': "490008165C",
                'direction': "outbound",
                'first_station_x': self.busstop_x_n_x,
                'first_station_y': self.busstop_x_n_y,
                'second_station_x': self.busstop_x_x,
                'second_station_y': self.busstop_x_y,
                'third_station_x': self.busstop_x_s_x,
                'third_station_y': self.busstop_x_s_y,
                'direction_x': 0,
                'direction_y': 1,
                'rotation_angle': 270
            },
            'bus19_east': {
                'lineID': "19",
                'first_station_id': "490007834F",
                'third_station_id': "490011679W",
                'direction': "inbound",
                'first_station_x': self.busstop_y_w_x,
                'first_station_y': self.busstop_y_w_y - 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y - 20,
                'third_station_x': self.busstop_y_e_x,
                'third_station_y': self.busstop_y_e_y - 20,
                'direction_x': 1,
                'direction_y': 0,
                'rotation_angle': 0
            },
            'bus19_west': {
                'lineID': "19",
                'first_station_id': "490011679W",
                'third_station_id': "490007834F",
                'direction': "outbound",
                'first_station_x': self.busstop_y_e_x,
                'first_station_y': self.busstop_y_e_y + 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y + 20,
                'third_station_x': self.busstop_y_w_x,
                'third_station_y': self.busstop_y_w_y + 20,
                'direction_x': -1,
                'direction_y': 0,
                'rotation_angle': 180
            }
            ,
            'bus38_east': {
                'lineID': "38",
                'first_station_id': "490007834F",
                'third_station_id': "490011679W",
                'direction': "inbound",
                'first_station_x': self.busstop_y_w_x,
                'first_station_y': self.busstop_y_w_y - 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y - 20,
                'third_station_x': self.busstop_y_e_x,
                'third_station_y': self.busstop_y_e_y - 20,
                'direction_x': 1,
                'direction_y': 0,
                'rotation_angle': 0
            },
            'bus38_west': {
                'lineID': "38",
                'first_station_id': "490011679W",
                'third_station_id': "490007834F",
                'direction': "outbound",
                'first_station_x': self.busstop_y_e_x,
                'first_station_y': self.busstop_y_e_y + 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y + 20,
                'third_station_x': self.busstop_y_w_x,
                'third_station_y': self.busstop_y_w_y + 20,
                'direction_x': -1,
                'direction_y': 0,
                'rotation_angle': 180
            },
            'bus55_east': {
                'lineID': "55",
                'first_station_id': "490007834F",
                'third_station_id': "490011679W",
                'direction': "inbound",
                'first_station_x': self.busstop_y_w_x,
                'first_station_y': self.busstop_y_w_y - 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y - 20,
                'third_station_x': self.busstop_y_e_x,
                'third_station_y': self.busstop_y_e_y - 20,
                'direction_x': 1,
                'direction_y': 0,
                'rotation_angle': 0
            },
            'bus55_west': {
                'lineID': "55",
                'first_station_id': "490011679W",
                'third_station_id': "490007834F",
                'direction': "outbound",
                'first_station_x': self.busstop_y_e_x,
                'first_station_y': self.busstop_y_e_y + 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y + 20,
                'third_station_x': self.busstop_y_w_x,
                'third_station_y': self.busstop_y_w_y + 20,
                'direction_x': -1,
                'direction_y': 0,
                'rotation_angle': 180
            },
            'bus243_east': {
                'lineID': "243",
                'first_station_id': "490007834F",
                'third_station_id': "490011679W",
                'direction': "inbound",
                'first_station_x': self.busstop_y_w_x,
                'first_station_y': self.busstop_y_w_y - 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y - 20,
                'third_station_x': self.busstop_y_e_x,
                'third_station_y': self.busstop_y_e_y - 20,
                'direction_x': 1,
                'direction_y': 0,
                'rotation_angle': 0
            },
            'bus243_west': {
                'lineID': "243",
                'first_station_id': "490011679W",
                'third_station_id': "490007834F",
                'direction': "outbound",
                'first_station_x': self.busstop_y_e_x,
                'first_station_y': self.busstop_y_e_y + 20,
                'second_station_x': self.busstop_y_x,
                'second_station_y': self.busstop_y_y + 20,
                'third_station_x': self.busstop_y_w_x,
                'third_station_y': self.busstop_y_w_y + 20,
                'direction_x': -1,
                'direction_y': 0,
                'rotation_angle': 180
            }
        }

        self.tube_groups_dict = {
            'piccadilly_north': {
                'lineID': "piccadilly",
                'first_station_id': "940GZZLUCGN",
                'third_station_id': "940GZZLURSQ",
                'first_station_name': "Covent Garden",
                'second_station_name': "Holborn",
                'third_station_name': "Russel Square",
                'direction': "outbound",
                'first_station_x': self.tubestop_coventgarden_x,
                'first_station_y': self.tubestop_coventgarden_y,
                'second_station_x': self.tubestop_holborn_x,
                'second_station_y': self.tubestop_holborn_y,
                'third_station_x': self.tubestop_russlesquare_x,
                'third_station_y': self.tubestop_russlesquare_y,
                'direction_x': 0,
                'direction_y': -1,
                'rotation_angle': 90
            },
            'piccadilly_south': {
                'lineID': "piccadilly",
                'first_station_id': "940GZZLURSQ",
                'third_station_id': "940GZZLUCGN",
                'direction': "inbound",
                'first_station_name': "Covent Garden",
                'second_station_name': "Holborn",
                'third_station_name': "Russel Square",
                'first_station_x': self.tubestop_russlesquare_x + 40,
                'first_station_y': self.tubestop_russlesquare_y,
                'second_station_x': self.tubestop_holborn_x + 40,
                'second_station_y': self.tubestop_holborn_y,
                'third_station_x': self.tubestop_coventgarden_x + 40,
                'third_station_y': self.tubestop_coventgarden_y,
                'direction_x': 0,
                'direction_y': 1,
                'rotation_angle': 270
            },
            'central_east': {
                'lineID': "central",
                'first_station_id': "940GZZLUTCR",
                'third_station_id': "940GZZLUCHL",
                'direction': "outbound",
                'first_station_name': "Tottenham Court Road",
                'second_station_name': "Holborn",
                'third_station_name': "Chancery Lane",
                'first_station_x': self.tubestop_tottenhamcourtroad_x,
                'first_station_y': self.tubestop_tottenhamcourtroad_y,
                'second_station_x': self.tubestop_holborn_x,
                'second_station_y': self.tubestop_holborn_y,
                'third_station_x': self.tubestop_chancerylane_x,
                'third_station_y': self.tubestop_chancerylane_y,
                'direction_x': 1,
                'direction_y': 0,
                'rotation_angle': 0
            },
            'central_west': {
                'lineID': "central",
                'first_station_id': "940GZZLUCHL",
                'third_station_id': "940GZZLUTCR",
                'direction': "inbound",
                'first_station_name': "Chancery Lane",
                'second_station_name': "Holborn",
                'third_station_name': "Tottenham Court Road",
                'first_station_x': self.tubestop_chancerylane_x,
                'first_station_y': self.tubestop_chancerylane_y + 50,
                'second_station_x': self.tubestop_holborn_x,
                'second_station_y': self.tubestop_holborn_y + 50,
                'third_station_x': self.tubestop_tottenhamcourtroad_x,
                'third_station_y': self.tubestop_tottenhamcourtroad_y + 50,
                'direction_x': -1,
                'direction_y': -1,
                'rotation_angle': 135
            }
        }



