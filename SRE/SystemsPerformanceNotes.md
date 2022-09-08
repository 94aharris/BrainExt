# Systems Performance Notes

Notes during reading 'Systems Performance: Enterprise and the Cloud' Second Edition by Brendan Gregg

# Chapter 1 - Introduction

- Understand your Data Path, if you don't have a diagram **Draw One**
- Canary Testing, Blue/Green Deploy, Capacity Planning are are after the fact
- Understand Resource Analysis vs Workload Analysis
- Understand 'Latency' and use to predict potential speedup
- Observability comes first
  - Counters
  - Metrics
  - Profiling
  - Tracing (CPU Flame graphs **super useful**)
- Expirimentation comes second
  - Macro Benchmarks (end to end)
  - Micro Benchmarks (specific component e.g. Network bandwidth test)
- Two Hands: Observability and Expirimentation **Use them Both**