# Distributed Computing #
## Fallacies of distributed computing ##
* The network is reliable
* Latency is zero
* Bandwidth is infinite
* The network is secure
* Topology doesn't change
* There is one administrator
* Transport cost is zero
* The network is homogeneous

## CAP Theorem ##
*It is impossible for a distributed data store to simultaneously provide more than 2 of the following*
* Consistency
  * Every Read receives the most recent write or error
* Availability 
  * Every request receives a (non-error) response, without the guarantee that it contains the most recent write
* Partition Tolerance
  * The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes

## Resources ##
* [Distributed Systems Lecture](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB)
* [System Design Primer](https://github.com/donnemartin/system-design-primer)