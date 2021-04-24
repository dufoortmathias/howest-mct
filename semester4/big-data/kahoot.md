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