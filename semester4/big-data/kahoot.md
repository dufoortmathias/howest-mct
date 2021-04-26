# Kahoot 1

*  Een message queue systeem...
    * Buffert data in DRAM, maar spilt over naar disk
* True or false: een message in een message queue kan maar door 1 consumer verwerkt worden
    * False
* Wat is een eigenschap van een database die message queue niet heeft?
    * Random search
* Wat is gelijkaardig tussen een LSM database en een message broker?
    * data wordt append-only weggeschreven
* Welke message technologie heeft de laagste latency?
    * UDP multicast
* Een applicatie trackt ieder punt van een route. Welke message queue zal je gebruiken?
    * Log based message queue
* Kafka is een...
    * distributed event log
* True or false: Azure service bus is een distributed log message queue
    * False
* True or false: AWS Kinesis is een distributed log message queue
    * True

# Kahoot 2

*  Hardware caching can cause the database to be... 
    * Not durable at all times
* True or false: The best storage for a transactional database is block storage:
    * True
* Isolation in databases is all about:
    * Concurrency performance and keeping data constistency
* Stronger isolation results in ...
    * Lower DB performance
* Atomicity in database ACID context means:
    * the complete transaction gets done or is rolled back
* Atomicity in the context of multi-threaded code makes sure that
    * Intermediate results of a thread are not visible
* What is true about consistency & an ACID compliant transactional database?
    * It is mostly up to the application
* Tuples in Python are more or less the same as relational Tuples
    * False
* The relation in a relational table is most similar to ...
    * a Python dictionairy 
* The commit Rollback is able to
    * prevent corrupt data

# Leho Tests

*  Welke data store technologie gebruikt Log Structured Merge Tree met Sorted String tables (LSM- SST) architectuur  
   *  ElasticSearch/Lucene
   *  MySQL MyRocks
*  Wat is correct omtrent  SQL en non-relationele databases?
   *  SQL wordt ook gebruikt door non-relationele databases: het is een declaratieve taal
*  Juiste database / data store.
   *  Je wil een platform waarop ieder bedrijf zo snel mogelijk met al zijn top referentie klanten wordt getoond (en enkel dat)  
      *  document store
   *  Een app met de mogelijkheid om regematig een backup te maken van een belangrijke financiële database
      *  Relationele database met snapshot isolation          
   *  Snel opvragen hoeveel items een bepaalde klant al heeft gekocht. Je zoekt enkel op één klant
      *  Key Value
   *  Grote hoeveelheden sensor data wegschrijven
      *  timeseries data
   *  Een persoon kunnen linken aan zijn opleidingen en die opleidingen kunnen linken aan de juiste instelling (univ, Hogeschool)
      *  Relationele database met read commited isolation
*  Wat is een correcte manier om een WAL (log) te omschrijven
   *  Een log die alle inkomende updates etc. sequentieel wegschrijft
   *  Een log waar je op kan terugvallen als een update onderbroken wordt    
*  In de documentatie van ElasticSearch lees je: "Lucene is the name of the search engine that powers Elasticsearch." "The Lucene index is divided into smaller files called segments. A segment is a small Lucene index. Lucene searches in all segments sequentially." Wat betekent dat?
   *  Dat ElasticSearch/Lucene steeds zoekt in het meest recente segment en dan de vorige segmenten doorzoekt.
*  relational database tuples lijken zeer goed op what we in Python: 
   *  dictionaries noemen
*  Waarom wordt een database "relationeel" genoemd
   *  omdat tabellen een combinatie van keys en foreign keys bevatten
*  De "Repeatable read" instelling als "isolation level" is meestal zeer gelijkaardig als
   *   Snapshot
*  Het feit dat Compaction Planning in InfluxDB noodzakelijk is is het gevolg van      
   *  Segmenten moeten regelmatig gemerged/gecombineerd worden
*  Een voorbeeld van een key-value met hash index data store is:
   *   Riak Bitcask
*  Wat is correct omtrent  SQL en non-relationele databases?
   *  Wat is correct omtrent  SQL en non-relationele databases?


*  Wanneer gebruik je Linux tools zoals "Sort", "Grep" en "tail", wanneer gebruik je een framework zoals Spark? 
   *   Spark indien je over meerdere nodes wil processen
*  Waarom heb je bij een data pipeline meestal "bulk storage" nodig zoals een HDFS cluster of Amazon S3? Wat is het verschil met een normale schijf?
   *   Werkt met grote blokken met replica over meerdere nodes
*  De analyse van een time series streaming processor wordt gemaakt op: Minuut 1 tot 3, Minuut 2 tot 4, Minuut 3 tot 5 Dit is ... analytics
   *   Hopping Window 
*  Wat is de bedoeling van Batch Processing? 
   *  Data van bestaande datasets en databases  omvormen tot een nieuwe dataset die bruikbaar is voor data analyse
   *  Het opkuisen en omvormen van grote logs en andere ongestructureerde data tot iets dat je kan gebruiken voor bvb. machine learning  
*  Voor welke use cases is een message Broker zoals Kafka zeer geschikt? 
   *  Events in de juiste volgorde verwerken
   *  stream herinlezen zodat je een gecrashte consumer terug kan up tot date krijgen
   *  mogelijkheid om messages te bufferen zodat de kans klein is dat events gedropt worden
*  Wat is een Spark RDD? 
   *  Een dataset die nooit veranderd wordt maar wel opgesplitst in partities
*  Zie onze video over de use case van Be-mobile (Sizing Servers onderzoeker), Wat was de belangrijkste reden dat zij kozen om Kafka te gebruiken en geen andere msg broker?
   *  dat events altijd in volgorde gehouden worden
*  Welke beweringen zijn waar omtrent message brokers? 
   *  Data/event producers krijgen sneller de bevesting dat de data verwerkt is dan bij direct messaging
   *  Een stream processor mag even crashen zonder dat daarom de stream stopt
   *  Het is eenvoudiger om te schalen zowel langs consumer als langs producer zijde
*  Welke bewering is correct omtrent Stream Processing? 
   *  bij stream processing gebeurt de verwerking continue
   *  stream processing is goed om trend analyse uit te voeren
*  Voor welke use cases is een message Broker zoals RabbitMQ en Azure Service Bus geschikt? 
   *  lage latency verwerking
   *  mogelijkheid om messages te bufferen zodat de kans klein is dat events gedropt worden 
*  In Kafka is de relatie tussen "Topic" en partition als volgt: 
   *   Eén topic kan verdeeld worden over één of meerdere partities 


*  Welke beweringen zijn correct omtrent Parquet & JSON? 
   *  Beide zijn encoding formaten die toelaten dat verschillende software componenten data kunnen uitwisselen 
   *  Parquet is veel efficient dan JSON als je een paar kolomen uit je dataset wil halen om te verwerken     
*  Waarom heb je bij een data pipeline meestal "bulk storage" nodig zoals een HDFS cluster of Amazon S3? Wat is het verschil met een normale schijf?
   *  Werkt met grote blokken met replica over meerdere nodes  
*  De relatie tussen een Stream processor/Consumer en een partitie is als volgt
   *  Meerdere partities kunnen gelezen worden door één consumer 
*  Match de use case met de juiste technologie.
   *  Het verwerken van een maandenlange log tot een bruikbare CSV voor machine learning
      *  Apache Spark
   *  Het doorsturen van zowel sensor data als GPS data naar verschillende applicaties 
      *  Apache Kafka
   *  Het doorzoeken van grote hoeveelheden documents met JSON text data
      *  Elasticsearch
   *  Het opslaan van zowel sensor data en GPS data 
      *  Influxdb
*  Snapshot isolation heb je nodig als:  
   *  Over de tijd heen consistent data wil wegschrijven in een database waar naar geschreven wordt  
      
