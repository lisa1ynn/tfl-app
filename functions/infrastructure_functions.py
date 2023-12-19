
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

    # North/South Bus line (Bus 17, 46)
    # Coley Street (HD, HC)
    busstop_x_n = BusStops(screen,
                           x=settings.busstop_x_n_x,
                           y=settings.busstop_x_n_y,
                           text="Coley Street (HD & HC)")
    # Gray's Inn Road (B) & Clerkenwell Road/Rosebery (CD)
    busstop_x = BusStops(screen,
                         x=settings.busstop_x_x,
                         y=settings.busstop_x_y,
                         text="Gray's Inn Road (B) & Clerkenwell Road (CD)")
    # Holborn Circus/Fetter Lane (H) & High Holborn/Chancery Lane Station (C)
    busstop_x_s = BusStops(screen,
                              x=settings.busstop_x_s_x,
                              y=settings.busstop_x_s_y,
                              text="Holborn Circus (H) & High Holborn (C)")

    # East/West Bus line (Bus 19, 38, 55, 243)
    # Red Lion Street (G and A)
    busstop_y_w = BusStops(screen,
                              x=settings.busstop_y_w_x,
                              y=settings.busstop_y_w_y,
                              text="Red Lion Street (G & A)")
    # Gray's Inn Road (CA and CP)
    busstop_y = BusStops(screen,
                         x=settings.busstop_y_x,
                         y=settings.busstop_y_y,
                         text="Gray's Inn Road (CA & CP)")
    # Rosebery Avenue (CE and CU and CW) & Clerkenwell Road (CN)
    busstop_y_e = BusStops(screen,
                              x=settings.busstop_y_e_x,
                              y=settings.busstop_y_e_y,
                              text="Rosebery Avenue (CE, CU, CW) & Clerkenwell Road (CN)")

    # build
    roads.draw_roads()
    hult.blitme()
    tubestop_stpauls.blitme()
    tubestop_holborn.blitme()
    tubestop_tottenhamcourtroad.blitme()
    tubestop_russlesquare.blitme()
    tubestop_coventgarden.blitme()
    busstop_x_n.blitme()
    busstop_x.blitme()
    busstop_x_s.blitme()
    busstop_y_w.blitme()
    busstop_y.blitme()
    busstop_y_e.blitme()







