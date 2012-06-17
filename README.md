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
    *** Itinerary #1 (2012-06-17 16:00:00 => 2012-06-17 16:50:00)
     - Type: Trajet arrivée au plus tôt
     - Duration: 0:50:00
     - Zones: [1, 5]

    *** Itinerary #2 (2012-06-17 15:58:00 => 2012-06-17 17:09:00)
     - Type: Trajet le moins de correspondances
     - Duration: 1:11:00
     - Zones: [1, 5]

    Which one (1-2) ? 1
    ********************************************************************************
    *** Itinerary Trajet arrivée au plus tôt
    1. At 16:00, from NATION, Paris
    Take RER A - TERI, direction GARE DE POISSY
    Stop at CHATELET LES HALLES, Paris

    2. At CHATELET LES HALLES, Paris (16:05)
    Walk to RER B - EKLI (CHATELET LES HALLES, Paris) for 0:02:00
    Wait for 0:04:00

    3. At CHATELET LES HALLES, Paris (16:11)
    Take RER B - EKLI, direction CDG Terminal 2 / TGV
    Stop at AEROPORT CDG 1, Tremblay-en-France

    4. Here you go: AEROPORT CDG 1, Tremblay-en-France

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

