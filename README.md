# Parikstra

`parikstra` is a Python module to calculate journey with the Parisian transport system, and read some other interesting data.

It uses official API of Parisian transport websites, but is still an unofficial API client.

It is at the moment in developpement. Use at your own risk.

By the way, `parikstra` = Paris + [Djikstra](http://en.wikipedia.org/wiki/Dijkstra's_algorithm)

## Usage

Install `parikstra`, either cloning this repository

    git clone git://github.com/Gawen/parikstra.git

or using `pip` (or other)

    pip install parikstra

Import the `parikstra` module
    
    import parikstra

Get your departure point

    departure = parikstra.Point("nation")

Get your arrival point
    
    arrival = parikstra.Point("dammartin juilly saint mard")

Ask to calculate the itineraries

    itineraries = departure.to(arrival)

Print the itineraries' type

    for i, itinerary in enumerate(itineraries):
        print "#%d. %s (duration %s)" % (i, itinerary.type, itinerary.duration, )

Let's say you take the first one

    itinerary = itineraries[0]

Request the itinerary's steps ...

Iterate the different steps of the journey

    for i, step in enumerate(itinerary):
        print "#%d. %s => %s @ %s" % (i + 1, step.name, step.direction, step.time, )

Here you go.

### CLI

You can use `parikstra` as a CLI client.

    Usage: parikstra.py [options]

    Options:
      -h, --help            show this help message and exit
      -d DEPARTURE, --departure=DEPARTURE
                            Departure
      -a ARRIVAL, --arrival=ARRIVAL
                            Arrival
      -v, --verbose         Verbosify

Example:

    $ python parikstra.py --departure "nation" --arrival "aeroport charles de gaule"
    *** Itinerary #1 (2012-06-15 17:30:00 => 2012-06-15 18:11:00)
     - Type: Trajet arriv?e au plus t?t
     - Duration: 0:41:00
     - Zones: [1, 5]

    *** Itinerary #2 (2012-06-15 17:33:00 => 2012-06-15 18:58:00)
     - Type: Trajet le moins de correspondances
     - Duration: 1:25:00
     - Zones: [1, 5]

    Which one (1-2) ? 1
    ********************************************************************************
    Itinerary Trajet arriv?e au plus t?t
    *** Steps
    1. Departure: NATION, Paris => GARE DE CERGY LE HAUT @ 17:30
     - Line: RER A - UXOL

    2. CHATELET LES HALLES, Paris => CHATELET LES HALLES, Paris @ 17:35
     - Walk duration: 0:02:00
     - Wait duration: 0:04:00

    3. CHATELET LES HALLES, Paris => CDG Terminal 2 / TGV @ 17:41
     - Line: RER B - EMOI

    4. Arrival: AEROPORT CDG 1, Tremblay-en-France => AEROPORT CDG 1, Tremblay-en-France @ 18:11

## Work in progress

A lot has to be done.

- First, a lot of FIXes. I've already see some bugs during steps parsing
- Second, a lot of FIXes. Again ...
- Add some other interesting meta-data
- And your imagination / needs

## License

The code is under MIT license. Please note the data are not, and are the property of the website vianavigo.com !

## Copyright reminder

Please remember that these data are the property of vianavigo.com !

