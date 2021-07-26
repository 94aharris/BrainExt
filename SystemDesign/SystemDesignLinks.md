# System Design Links #

## General ##

- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Ops School Cirriculum](https://www.opsschool.org/)
- [Design System Checklist](https://www.designsystemchecklist.com/)
- [Numbers and Calculations Everyone Should Know](http://www.cs.cornell.edu/projects/ladis2009/talks/dean-keynote-ladis2009.pdf) 

## DevOps ##

- [Atlassian DevOps Framework](https://www.atlassian.com/devops/frameworks)
- [DevOps Patterns and Anti-Patterns](http://web.devopstopologies.com/)
- [12 DevOps Anti-Patterns](https://www.devopsgroup.com/blog/twelve-devops-anti-patterns/)
- [Hacking Culture (building DevOps Culture)](https://www.slideshare.net/jesserobbins/cloud-expo-jesserobbinsopscode20130129b)
- [IT Revolution](https://itrevolution.com/)
- [What is DevOps? (Agile Admins)](https://theagileadmin.com/what-is-devops/)
- [Implement SRE in your organization in one year](https://medium.com/site-reliability-engineering-leadership/how-to-implement-sre-in-your-organization-f103b30b1747) 
- [Cross Functional DevOps Teams](https://caylent.com/devops-handbook-part-2-defining-devops-teams)
- [Generate System Documentation Using Python](https://github.com/mingrammer/diagrams)
- [We Don't Use Kubernetes](https://ably.com/blog/no-we-dont-use-kubernetes)
  
## Microsoft ##

- [Best Practices in Cloud Applications](https://docs.microsoft.com/en-us/azure/architecture/best-practices/index-best-practices)
- [Application Architecture Design](https://docs.microsoft.com/en-us/azure/architecture/guide/)

## CloudFlare ##

- [How Cloudflare Workers Work](https://developers.cloudflare.com/workers/learning/how-workers-works)

## Distributed Systems ##

- [Distributed Systems Lecture](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB)
- [Distributed Computing for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)
- [CAP - You Can't Sacrifice Partition Tolerance](https://codahale.com/you-cant-sacrifice-partition-tolerance/)
- [PACELC Theorem (extended CAP)](https://en.wikipedia.org/wiki/PACELC_theorem)
- [Parrallel Processing in Distributed Systems](https://heather.miller.am/teaching/cs212/slides/week19-scaled.pdf)
- [Intro to Big Data Processing](http://www.eli.sdsu.edu/courses/spring20/cs696/notes/D02BigDataIntro.pdf)

## Microservices ##

- [Microservices Criticisms and Concerns](https://en.wikipedia.org/wiki/Microservices#Criticism_and_concerns)
- [Raspberry-pi-dramble](https://github.com/geerlingguy/raspberry-pi-dramble)
- [Uber Engineering Microservices Architecture](https://eng.uber.com/microservice-architecture/)

## Examples ##

- [Reddit System Design Following WSB Incident p1](https://www.reddit.com/r/RedditEng/comments/o4yb4z/rwallstreetbets_incident_anthology_more_data_more/)
- [Reddit System Design Following WSB Incident p2](https://www.reddit.com/r/RedditEng/comments/o4ygp0/rwallstreetbets_incident_anthology_what_worked/)
- [Caching at Reddit](https://redditblog.com/2017/01/17/caching-at-reddit/)
  - Heavy use of memcached
    - **Key Value Store**
    - **Slab allocation** - certain sized chunks of memory
  - Workload Based Pools
    - scale pools independently based on utilization
    - make reasonable failure predictions
  - Issues
    - consistency issues / race conditions
    - No TTLs on warmup routes causing stale data
    - **Specify a TTL when warming up if your app relies on it**
