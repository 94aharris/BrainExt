# System Design #

> Remember Everything is a Tradeoff

## Contents ##
- Resources
- Interview Question Steps
- Back of the Envelope Calculations
- Scalability for Dummies
- High Level Tradeoffs to Remember
- Non-Abstract Large System Design
- Important Tools to Know

## **Resources** ## 

- [ ] [System Design Primer](https://github.com/donnemartin/system-design-primer#study-guide)
- [ ] [Google Pro Back of Envelope Calculations](http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelope-calculations-to-choo.html)
- [ ] [Palantir - How to rock a systems design interview](https://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/)
- [ ] [Numbers every programmer should know](https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know)
- [ ] [Powers of two table](https://github.com/donnemartin/system-design-primer#powers-of-two-table)
- [ ] [What Happens When...](https://github.com/alex/what-happens-when)
- [ ] [SRE Cheat Sheets](https://github.com/michael-kehoe/awesome-sre-cheatsheets/blob/master/README.md)
- [ ] [Distributed Systems Primer by Loyola](https://ds.cs.luc.edu/index.html)
- [ ] [SRE Flash Cards](https://danrl.com/sre-flash-cards/SRE%20Flash%20Cards.pdf)
- [ ] [How to get into SRE](https://blog.alicegoldfuss.com/how-to-get-into-sre/)
- [ ] [My Path to Site Reliablity Management](https://danrl.com/srm/#qualified)
- [ ] [Google Book - Non Abstract Large System Design](https://sre.google/workbook/non-abstract-design/)
- [ ] [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [ ] [You're Doing it Wrong (server performance rethought)](https://queue.acm.org/detail.cfm?id=1814327)
- [ ] [Scaling Instagram Infrastructure (video)](https://www.youtube.com/watch?v=hnpzNAPiC0E)

## **Interview Question Steps** ##

1. Outline Use Cases, Constraints and Assumptions [5-mins]

- who are the users?
- how will they use?
- how many users?
- what will the system do
- what are the inputs and outputs
- how much data
- how many requests per second
- read to write ratio
- Usage Patterns

2. Estimations [5-mins]

- Throughput (QPS for read and write queries)
- Latency expected from the system (for read and write queries)
- Read / Write Ratio
- Traffic Estimates
  - Write (QPS, Volume of data)
  - Read (QPS, Volume of data)
- Storage Estimates
- Memory estimates
  - if using a cache, what is the kind of data we want to store in cache
  - How much RAM and how many machines do we need
  - Amount of data you want to store in disk / ssd
  
3. Design Goals [5-mins]

- Latency and Throughput requirments
- Consistency vs Availability 
  - Weak / Strong / eventual -> Consistency 
  - Failover / Replication -> Availability

4. High level design [5-10 mins]

- APIs for Read / Write scenarios for crucial components
  - Public APIs
  - Private APIs
- Database Schema
- Basic Algorithm
- High level design for Read/Write Scenario


5. Deep Dive [15 - 20 mins]
   
- Scaling the algorithm
- Scaling individual components
  - Availabiity, Consistency and Scale story for each component
  - Consistency and availabilty patterns
- Think about following and how they would fit
  - DNS
  - CDN [Push Pull]
  - Load Balancers [Active-Passive, Active-Active, Layer 4, Layer 7]
  - Reverse Proxy
  - Application Layer Scaling [Microservices, Service Discovery
  - DB [RDBMS, NoSql]
    - RDBMS
      - Master-Slave, Master-Master, Federation, Sharding, Denormalization, SQL Tuning
    - NoSql
      - Key-Value, Wide-Column, Graph, Document
      - Fast Lookups
        - RAM [Bounded Size] -> Redis, Memcached
        - AP [Unbounded Size] -> Cassandra, RIAK, Voldemort
        - CP [Unbounded Size] -> HBase, MongoDB, Couchbase, DynamoDB
  - Caches
    - Client Caching, CDN caching, Webserver caching, Database caching, Application caching, Cache @ Query level, Cache @Object LLevel
    - Eviction policies
      - Cache aside
      - Write Through
      - Write Behind
      - Refresh ahead
  - Asychronism
    - Message Queues
    - Task Queues
    - Backpressure
  - Communication
    - TCP
    - UDP
    - REST
    - RPC

6. Justify [5-minutes]

- Throughput of each layer
- Latency cacuse between each layer
- Overall latency justification

Bonus: Show back of the envelope calculations

## **Back of the Envelope Calculations** ##

**Numbers Everyone Should Know**

- L1 cache reference 0.5 ns
- Branch mispredict 5 ns
- L2 cache reference 7 ns
- Mutex lock/unlock 100 ns
- Main memory reference 100 ns
- Compress 1K bytes with Zippy 10,000 ns
- Send 2K bytes over 1 Gbps network 20,000 ns
- Read 1 MB sequentially from memory 250,000 ns
- Round trip within same datacenter 500,000 ns
- Disk seek 10,000,000 ns
- Read 1 MB sequentially from network 10,000,000 ns
- Read 1 MB sequentially from disk 30,000,000 ns
- Send packet CA->Netherlands->CA 150,000,000 ns 

Keys about the numbers
- Memory is fast and disks are slow
- Even just cheap compression can save a lot of bandwidth
- Writes are 50 times more expensive than reads
- Architect for scaling writes
- Optimize for low contention
- Optimize wide. Make writes as parallel as you can


## **Scalability for Dummies** ##

### 1. Clones ###

#### Overview ####

- Every server contains the same codebase and does not store user related data
- Sessions need to be stored in a centralized data store
  - external database
  - external persistent cache

### 2. Database ###

#### Database ####

- After app grows and starts to get slower you can
  - (not great) Stick with same sql (e.g. MySQL) let is grow and start trying things like master-slave and upgrading RAM and sharding / denomalizing
  - (better) denormalize from the start, no more joins in any database query. Use mysql like NoSQL or switch right away to nosql

### 3. Caches ###

- Caches like Memcached and Redis
- Key value store as a buffering layer between application and storage 
  - App should try to read from here first

#### Cache Patterns ####

1. Cached Database Queries

- Most common used caching pattern
- Hash of query is key, value is returned value
- First check is in cache
- Hard to delete a cached result when you cache a complex query, when one piece of data changes you have to delete all cached queries who may contain cell

2. Cached Objects

- Newer and recommended
- See your data as an object
- Let your class assemble a dataset from your database and store instance of the class in the cache
- Once a data object is assembled, store it directly in the cache (data array or better yet the object)
- Rid the object when something changes
- Worker processes can assemble the object and application never directly touches the database
- Good Objects to cach
  - User Sessions
  - Fully rendered blog articles
  - Activity streams
  - User <-> friend relationships

#### Cache Types ####

- **Redis**
  - allows for persistence and built in data structures
  - with cleverness can use to completely remove a database
- **Memcached**
  - better if just need a cache
  - easy to setup and easy to scale

### Async ###

Asynchronism allows work to be done bit by bit rather than waiting for the whole completed product to be dropped at once

#### Async Paradigms ####

1. Turn dynamic content into static content

- Pages are pre-rendered and stored as static HTML
- Static pages can be stored to CDN to handle scale very well

2. Special requests can not be pre-rendered
   1.  user hits page and a request is sent to a job queue for work. User is shown loading signal. 
   2.  The frontend constantly checks for completed job and pulls content when ready

#### Async Tips ####

- Look at RabbitMQ
- Look at Redis List
- Look at ActiveMQ
- Basic idea is to have a queue of tasks or jobs that a worker can process
- If you do something time-consuming try to do it asynchronously

## **High Level Tradeoffs to Remember** ##

### Performance vs Scalability ###

### Latency vs Throughput ###

### Availability vs Consistency ###

## **Non-Abstract Large System Design** ##