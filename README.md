Airports
========

A JSON collection of 28k+ entries with basic information about nearly every airport and landing strip in the world. ICAO codes used as keys. Each entry contains IATA code, airport name, city, two-letter ISO country code, ISO country short name, elevation above sea level in feet, coordinates in decimal degrees and time zone.

```json
"KOSH": {
    "icao": "KOSH",
    "iata": "OSH",
    "name": "Wittman Regional Airport",
    "city": "Oshkosh",
    "state": "Wisconsin",
    "country": "US",
    "elevation": 808,
    "lat": 43.9844017029,
    "lon": -88.5569992065,
    "tz": "America\/Chicago",
    "country_short_name":"United States of America"
},
```

Time zones initially sourced from [TimeZoneDB](https://timezonedb.com) and updated using [TimeAPI](https://www.timeapi.io/).
Country short names sourced from [Wikipedia ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1).
