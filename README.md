# A Simple Pokedex

A Simple Pokedex Web Application. Just type in the name of the Pokemon you're searching for, and the Pokedex can tell you all about it.

## Design
- Framework: Django
- Data is retrieved from PokeAPI whenever user enters a pokemon name or number in the search bar.
    - All flavor text is pulled from the first available English flavor text from PokeAPI.
    - All game indices are pulled from the first available game index from PokeAPI

- Postgres database and Pokemon model were set up but were not used due to use being out of scope.... for now.

## Related References
- [Corey Shafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)  Python Django Tutorial Series
- https://www.twilio.com/blog/2014/11/build-your-own-pokedex-with-django-mms-and-pokeapi.html