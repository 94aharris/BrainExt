# Cassandra #

## Key Terminology ##

*keyspace*

Namespace for a set of tables. similar to a 'database' in relational sql.

## Important Cassandra Commands ##

- Create a new simple keyspace (db) with no replication
  
```CQL
CREATE KEYSPACE cycling
    WITH REPLICATION = {
        'class' : 'SimpleStrategy',
        'replication_factor':1
    }
```

- Query existing replication factors

```CQL
SELECT * FROM system_schema.keyspaces;
```

- Get status of nodes
```bash
nodetool status
```

## Cassandra Docker ##

- Pull cassandra image, name the docker instance 'some-cassandra', open a pseudo TTY interface (-it) and connect using cqlsh (Cassandra Query Lnaguage Shell)
  
```bash
docker run -it --network some-network --rm cassandra cqlsh some-cassandra
```

## Resources ##

- [Cassandra Counters: Nice in Theory Hazardous in Practice](https://ably.com/blog/cassandra-counter-columns-nice-in-theory-hazardous-in-practice)
- [Apache Cassandra Fundamentals (Katacoda)](https://www.katacoda.com/datastax/courses/cassandra-intro)
- [Cassandra architecture](https://docs.datastax.com/en/archived/cassandra/3.0/cassandra/architecture/archIntro.html)
- [Cassandra Docker Image](https://hub.docker.com/_/cassandra)