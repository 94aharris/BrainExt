
# Links #

## SRE Teams ##
- [How to get Started / Organize your SRE Team](https://cloud.google.com/blog/products/devops-sre/how-sre-teams-are-organized-and-how-to-get-started)
- [Start and Asses your SRE Journey](https://cloud.google.com/blog/products/devops-sre/how-to-start-and-assess-your-sre-journey)
- [Building Blocks for SRE](https://medium.com/@skirsch/building-blocks-for-site-reliability-engineering-503c451d1fca)
- [Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [On-Call](https://sre.google/workbook/implementing-slos/)
- [SRE Team Lifecycles](https://sre.google/workbook/team-lifecycles/)
- [SRE Reaching Beyond Walls](https://sre.google/workbook/reaching-beyond/)
- [SRE Documentation](https://queue.acm.org/detail.cfm?id=3283589)
- [Organizing an SRE Team](https://cloud.google.com/blog/products/devops-sre/how-sre-teams-are-organized-and-how-to-get-started)
- [SRE Team Lifecycle](https://sre.google/workbook/team-lifecycles/)
- [Amazon Principles](https://www.amazon.jobs/en/principles)
- [12 -Factor App](https://12factor.net/)
- [Overview of SRE Best Practices](https://www.slideshare.net/agarwalashutosh/overview-of-site-reliability-engineering-sre-best-practices)
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- [Dropbox SRE Career Ladder](https://dropbox.github.io/dbx-career-framework/ic1_reliability_engineer.html)

## Tools ##

- [List of Awsome SRE Tools](https://github.com/SquadcastHub/awesome-sre-tools)

## Random ##

- [Cascading Failures(Video)](https://www.infoq.com/presentations/cascading-failure-risk)
  - Cascading failures are at risk of requiring intervention during problem spike
    - Take down entire service
    - don't self heal
    - no warning
  - Any system that is designed to failure is at risk of cascading failure
  - Example: AWS DynamoDB outage in 2015
  - **CLD (Causal Loop Diagram)**
    - **system dynamics modeling** to identify potential cascading failures
    - All +'s can cause cascade
  - Recovery
    - Can't just scale out (get overstated)
    - Reduce load until you can get sufficient capacity in place
    - Disabling health checks temporarily help
  - Avoid Cascading Failures
    - Avoid accepting unbounded numbers of incoming requests
    - Avoid dangerous client retry behavior (when you have control)
    - Avoid crashing on bad input (poison pill)
    - Avoid proximity-based failover without imposing maximum capacities (potential over-provisioning)
    - Avoid work prompted by failure
    - Avoid long startup times (makes autoscaling difficult)

- [Need for systems observability (blog)](https://blog.last9.io/need-for-systems-observability/)
  - Everyday questions in war room
    - What other services are impacted?
    - What is going wrong?
    - Is this happening somewhere else?
    - Did we deploy something?
    - Is the <external API> impacting us?
    - It’s Kafka. Right?
    - What’s the reason for this increased error rate?
    - Did we get a page?
    - Something is wrong. We had a massive spike of alerts
  - How to Answer
    - Ingest all sorts of **observability pillars**
      - logs
      - metrics
      - traces
    - Use dashboards and cross-hairs to detect correlations
    - Build correlations and reliably inform the stakeholders on contextual information

![Typical Monitoring Landscape](/Images/typical_monitoring_landscape.jpg)

- [Troubleshooting a journey into the unknown (blog)](https://medium.com/booking-com-infrastructure/troubleshooting-a-journey-into-the-unknown-e31b524fa86)
- [How SREs Prepared for Black Friday](https://medium.com/back-market-engineering/how-back-market-sres-prepared-for-black-friday-5f017f343408)
  