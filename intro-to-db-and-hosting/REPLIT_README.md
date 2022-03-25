# TUHSD Hackathon 2022
_Intro to DB REPL.it_


## Terminology

| Term     | Spreadsheet Equivalent |
|----------|------------------------|
| Database | File                   |
| Table    | Sheet / Tab            |
| Schema   | Headers / Format       |
| Entry    | Row                    |


## Basic Queries

__Hello World__

```sql
SELECT "Hello World";
```

__Select everything from a table__

```sql
SELECT * FROM pokemon;
```

__Some examples of filtering:__

```sql
---
--- Get all pokemon of a certain generation
---
SELECT * 
  FROM pokemon
  WHERE Generation = 3;

---
--- You can also limit the columns returned
---
SELECT Name, Type_1, Type_2
  FROM pokemon
  WHERE Legendary = "True";

---
--- You can also get more complex with your filtering
--- maybe you want to run a pure fire team using only pokemon from gen 4?
---
SELECT *
  FROM pokemon
  WHERE
    Generation = 4
    AND Type_1 = "Fire"
    AND Type_2 IS NULL;

---
--- Well, that's not going to work very well.... 
--- Let's include pokemon from the previous generations as well.
---
SELECT *
  FROM pokemon
  WHERE
    Generation < 5
    AND Type_1 = "Fire"
    AND Type_2 IS NULL:
  
---
--- That's better, if we want more options though, lets include 
--- pokemon with Fire as one of their two types (not just pure fire)
---
SELECT *
  FROM pokemon
  WHERE
    Generation < 5
    AND "Fire" IN (Type_1, Type_2);

---
--- If you want to see how many results you're getting
---
SELECT COUNT(*)
  FROM pokemon
  WHERE
    Generation < 5
    AND "Fire" IN (Type_1, Type_2);
```

__You can also sort the results__

```sql
---
--- You're tired of fire teams ... I wonder what sort of dragons there are?
--- Let's sort by generation descending, so we can see the newest pokemon first!
---
SELECT *
  FROM pokemon
  WHERE "Dragon" IN (Type_1, Type_2)
  ORDER BY Generation DESC;

---
--- That's pretty good, but maybe lets also sort by If they are legendary?
---
SELECT *
  FROM pokemon
  WHERE "Dragon" IN (Type_1, Type_2)
  ORDER BY Legendary, Generation DESC;
```

__Grouping is an option as well__

```sql
---
--- What if you want to know how many Legendary pokemon each generation has?
---
SELECT Generation, COUNT(*)
  FROM pokemon
  WHERE Legendary = "True"
  GROUP BY Generation;

---
--- You can also alias columns to make the output more legible
---
SELECT Generation, COUNT(*) AS "Legendaries"
  FROM pokemon
  WHERE Legendary = "True"
  GROUP BY Generation;
```

## Creating a Table


__This is how our existing Pokemon table was created__

```sql
---
--- Create a table for pokemon
---
CREATE TABLE pokemon(
  Number      INTEGER  NOT NULL PRIMARY KEY,
  Name       VARCHAR(25) NOT NULL,
  Type_1     VARCHAR(8) NOT NULL,
  Type_2     VARCHAR(8),
  Total      INTEGER  NOT NULL,
  HP         INTEGER  NOT NULL,
  Attack     INTEGER  NOT NULL,
  Defense    INTEGER  NOT NULL,
  Sp_Atk     INTEGER  NOT NULL,
  Sp_Def     INTEGER  NOT NULL,
  Speed      INTEGER  NOT NULL,
  Generation INTEGER  NOT NULL,
  Legendary  VARCHAR(5) NOT NULL
);
```

__Let's create a table for pokemon trainers__

```sql
---
--- Create a table for Trainers
--- Trainers can carry up to 6 pokemon in a team
---
CREATE TABLE trainers(
  Id             INTEGER NOT NULL PRIMARY KEY,
  Name           VARCHAR(50) NOT NULL,
  Pokemon_1      INTEGER,
  Pokemon_2      INTEGER,
  Pokemon_3      INTEGER,
  Pokemon_4      INTEGER,
  Pokemon_5      INTEGER,
  Pokemon_6      INTEGER,
  FOREIGN KEY(Pokemon_1) REFERENCES pokemon(Number),
  FOREIGN KEY(Pokemon_2) REFERENCES pokemon(Number),
  FOREIGN KEY(Pokemon_3) REFERENCES pokemon(Number),
  FOREIGN KEY(Pokemon_4) REFERENCES pokemon(Number),
  FOREIGN KEY(Pokemon_5) REFERENCES pokemon(Number),
  FOREIGN KEY(Pokemon_6) REFERENCES pokemon(Number)
);
```

## Creating Rows/Entries in a Table

```sql

---
--- Let's create the trio of trainers from gen1
---
INSERT INTO trainers (Name, Pokemon_1, Pokemon_2, Pokemon_3, Pokemon_4, Pokemon_5, Pokemon_6)
VALUES
  ("Ash Ketchum", 25, 12, 17, 1, 6, 7),
  ("Misty", 120, 121, NULL, NULL, NULL, NULL),
  ("Brock", 73, 95, NULL, NULL, NULL, NULL);

---
--- We can check our work with this query
---
SELECT * FROM trainers;
```

## Updating an Entry/Row

```sql
---
--- It's not obvious, but we made a mistake above.
--- We gave Brock a Tentacruel rather than a Geodude.
--- We can fix that by updating him
---
UPDATE trainers
  SET Pokemon_1 = 74
  WHERE Name = "Brock";

```

## Joining Tables

```sql
---
--- Now this works, but it would be nice to see something more meaningful than the ID# of the pokemon
--- We can do this in a single query, by performing a JOIN.
--- 
--- Let's get each trainer's first pokemon
---
SELECT t.Name, p.Name, p.Type_1, p.Type_2
  FROM trainers AS t
  LEFT OUTER JOIN pokemon AS p
    ON p.Number = t.Pokemon_1;
```

## Challenges

- Update the pokemon table to include a pokedex description.
- Create a new table to track individual pokemon, their level, and attributes.
- Improve the trainer query above to use the table for individual pokemon.
- Improve the trainer query to get all pokemon for a given trainer.

## Additional Topics to Research

There are many many more database topics that we won't have time to cover today. Here are some topics you may want to research:

- Types of Joins
- Migrations
- Seeding
- ACID
- First, Second, and Third normal forms
- Stored Procedures
- Query Optimization
- Indexing
- Object Relational Mapping

