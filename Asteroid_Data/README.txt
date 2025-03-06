Here are general notes about this folder and what it does

asteroid_fetcher.py connects to JPL/NASA's Small-Body Database Lookup API.
It requests asteroids in batches of 100 and logs the data of any asteroid between 25m and 250m.
It collects all of the known data into a CSV file that is also contained in this folder.
The data logged about each asteroid of interest is as follows:

    id	                        A unique identifier assigned to the asteroid by NASA’s Near-Earth Object (NEO) database.
------------------------------------------------------------------------------------------------------------------------
    name	                    The official or provisional name of the asteroid.
------------------------------------------------------------------------------------------------------------------------
    diameter (meters)	        The estimated maximum diameter of the asteroid, based on observations and brightness.
------------------------------------------------------------------------------------------------------------------------
    absolute_magnitude	        A measure of the asteroid's brightness if it were placed 1 AU (astronomical unit)
                                from both the Sun and Earth. A lower value means a brighter object.
------------------------------------------------------------------------------------------------------------------------
    is_potentially_hazardous	A boolean (True or False) indicating if the asteroid's orbit brings it close enough to 
                                Earth to be classified as potentially hazardous.
------------------------------------------------------------------------------------------------------------------------
    orbiting_body	            The celestial body around which the asteroid orbits, typically the Sun but sometimes 
                                another planet or moon.
------------------------------------------------------------------------------------------------------------------------
    last_observation_date	    The most recent date on which the asteroid was observed and recorded in orbital 
                                calculations.
------------------------------------------------------------------------------------------------------------------------
    eccentricity	            A measure of how elliptical (oval-shaped) the asteroid’s orbit is. A value of 0 means a 
                                perfect circle, while values closer to 1 indicate a more elongated orbit.
------------------------------------------------------------------------------------------------------------------------
    inclination (degrees)	    The tilt of the asteroid’s orbit relative to Earth’s orbital plane (the ecliptic). A 
                                higher inclination means the asteroid orbits at a steeper angle compared to Earth's orbit.
------------------------------------------------------------------------------------------------------------------------
    mean_motion (°/day)	        The rate at which the asteroid moves along its orbit, measured in degrees per day.
------------------------------------------------------------------------------------------------------------------------
    semi_major_axis (AU)	    The longest radius of the asteroid's elliptical orbit, representing the average distance 
                                between the asteroid and the Sun over one full orbit. Measured in Astronomical Units (AU),
                                where 1 AU = Earth's average distance from the Sun (~149.6 million km).
------------------------------------------------------------------------------------------------------------------------


The current data in the CSV was from a 144,000 asteroid query that collected 16,014 target asteroids (25m-250m)
Only 144 queries were requested before a connection time out occured. Thanks BDTU Linde Alle Wi-fi :)

