
from classes.roads import Roads
from classes.stops import TubeStops, BusStops
from classes.hult import Hult

def create_infratructrure(screen, settings):
    """Create infrastructure"""
    # Roads
    roads = Roads(screen)

    #Hult
    hult = Hult(screen)

    # Tube stops
    tubestop_stpauls = TubeStops(screen,
                                 x=settings.tubestop_stpauls_x,
                                 y=settings.tubestop_stpauls_y,
                                 text="St. Paul's")
    tubestop_holborn = TubeStops(screen,
                                 x=settings.tubestop_holborn_x,
                                 y=settings.tubestop_holborn_y,
                                 text="Holborn")
    tubestop_tottenhamcourtroad = TubeStops(screen,
                                            x=settings.tubestop_tottenhamcourtroad_x,
                                            y=settings.tubestop_tottenhamcourtroad_y,
                                            text="Tottenham Court Road")
    tubestop_russlesquare = TubeStops(screen,
                                      x=settings.tubestop_russlesquare_x,
                                      y=settings.tubestop_russlesquare_y,
                                      text="Rusell Square")
    tubestop_coventgarden = TubeStops(screen,
                                      x=settings.tubestop_coventgarden_x,
                                      y=settings.tubestop_coventgarden_y,
                                      text="Covent Garden")
    # Bus stops
    busstop_x = BusStops(screen,
                         x=settings.busstop_x_x,
                         y=settings.busstop_x_y,
                         text="Stop X")
    busstop_other1 = BusStops(screen,
                              x=settings.busstop_other1_x,
                              y=settings.busstop_other1_y,
                              text="Stop other 1")
    busstop_other2 = BusStops(screen,
                              x=settings.busstop_other2_x,
                              y=settings.busstop_other2_y,
                              text="Stop other 2")

    busstop_y = BusStops(screen,
                         x=settings.busstop_y_x,
                         y=settings.busstop_y_y,
                         text="Stop Y")
    busstop_other3 = BusStops(screen,
                              x=settings.busstop_other3_x,
                              y=settings.busstop_other3_y,
                              text="Stop other 3")
    busstop_other4 = BusStops(screen,
                              x=settings.busstop_other4_x,
                              y=settings.busstop_other4_y,
                              text="Stop other 4")

    # build
    roads.draw_roads()
    hult.blitme()
    tubestop_stpauls.blitme()
    tubestop_holborn.blitme()
    tubestop_tottenhamcourtroad.blitme()
    tubestop_russlesquare.blitme()
    tubestop_coventgarden.blitme()
    busstop_x.blitme()
    busstop_other1.blitme()
    busstop_other2.blitme()
    busstop_y.blitme()
    busstop_other3.blitme()
    busstop_other4.blitme()







