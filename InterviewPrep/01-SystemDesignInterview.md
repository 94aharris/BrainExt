# System Design #

## Resource ## 

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

## Interview Question Steps ##

1. Outline Use Cases, Constraints and Assumptions

   * who are the users?
   * how will they use?
   * how many users?
   * what will the system do
   * what are the inputs and outputs
   * how much data
   * how many requests per second
   * read to write ratio

2. High level design

   * Sketch and Justify

3. Design core components

4. Scale the design

   * Identify bottlenecks
   * do you need scalability w/ load balancing, scaling, caching, database sharding, etc

5. Show back of the envelope calculations

## Back of the Envelope Calculations ##

**Numbers Everyone Should Know**

* L1 cache reference 0.5 ns
* Branch mispredict 5 ns
* L2 cache reference 7 ns
* Mutex lock/unlock 100 ns
* Main memory reference 100 ns
* Compress 1K bytes with Zippy 10,000 ns
* Send 2K bytes over 1 Gbps network 20,000 ns
* Read 1 MB sequentially from memory 250,000 ns
* Round trip within same datacenter 500,000 ns
* Disk seek 10,000,000 ns
* Read 1 MB sequentially from network 10,000,000 ns
* Read 1 MB sequentially from disk 30,000,000 ns
* Send packet CA->Netherlands->CA 150,000,000 ns 

Keys about the numbers
* Memory is fast and disks are slow
* Even just cheap compression can save a lot of bandwidth
* Writes are 50 times more expensive than reads
* Architect for scaling writes
* Optimize for low contention
* Optimize wide. Make writes as parallel as you can


## Scalability for Dummies ##

### Clones ###

* Every server contains the same codebase and does not store user related data
* Sessions need to be stored in a centralized data store
  * external database
  * external persistent cache

### Database ###

* After app grows and starts to get slower you can
  * (not great) Stick with same sql (e.g. MySQL) let is grow and start trying things like master-slave and upgrading RAM and sharding / denomalizing
  * (better) denormalize from the start, no more joins in any database query. Use mysql like NoSQL or switch right away to nosql

### Caches ###

[Caches](https://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache)

### Async ###

[Asynchronism](https://www.lecloud.net/post/9699762917/scalability-for-dummies-part-4-asynchronism)