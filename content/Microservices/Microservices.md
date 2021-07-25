# Microservices #

## Resources ##

- [What I Wish I Knew About Microservices](https://www.youtube.com/watch?v=kb-m2fasdDY)

## What I Wish I Knew Notes ##

- Costs of Microservices
  - You are using a distributed system (complex)
  - Everything is an RPC
  - Everything is a tradeoff
  - You end up building around problems rather than solving them
  - You trade complexity for politics
  - You keep your biases (I like this language / tool / framework)
- RPC
  - HTTP / REST Gets complicated quickly
    - Why are you using HTTP symantics?
  - JSON needs a schema (lacks types)
  - RPCs are slower than PCs
  - **Servers are not browsers**
- Many Repositories
- Operational Issues
- Monitoring
  - Require a standarized dashboard for services from the start and build them in for free (created on initial service creation)
  - Want to be able to perform traces
- Performance
  - Doesn't matter until it does
  - **'Good' not required but 'known' is**
- Fanout
  - Need distributed tracing
- Failure Testing
  - You don't opt in, like it or not we failure test your service