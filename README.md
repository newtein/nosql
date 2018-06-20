# Empirical Investigation of Trends in NoSQL-based Big-data Solutions in the Last Decade
## Research Abstract
The usage and popularity of NoSQL databases have sharply risen over the past decade due to their ability to handle a huge amount of data by employing scalable architecture, schema-less structure, high availability and better performance than traditional relational database systems (RDBMS). Currently, there exist more than 225 NoSQL databases. In this paper, we aim to study variation in yearly trends of 20 NoSQL databases from the perspective of programmers of widely-used community-based Q&A website Stack Overflow. To reveal the interest of the programmers we have investigated questions-asked and presented an unbiased Normal Interest Score by employing three parameters, first, the number of questions asked, second, mean views on a question and third, the mean score on a question. MongoDB, Cassandra, Redis, and Neo4j emerged as most popular databases in their respective families while Normal Interest Score of all four of them is decreasing 2015 onwards. For the first time in a decade, the number of questions asked related to Cassandra decreased in the year 2017. Additionally, we have also discussed how real-world events like publications, open-sourcing, mention in controversial bills, version-release, acquiring ventures etc affect the interest corresponding to NoSQL databases over Stack Overflow.

## Methodology

<img src="https://raw.githubusercontent.com/newtein/nosql/master/image/method.JPG"/>

## Column NoSQL Family

<img src="https://raw.githubusercontent.com/newtein/nosql/master/image/c1.JPG"/>
## Key-Value NoSQL Family
<img src="https://raw.githubusercontent.com/newtein/nosql/master/image/k1.JPG"/>
## Document NoSQL Family
<img src="https://raw.githubusercontent.com/newtein/nosql/master/image/d1.JPG"/>
## Graph NoSQL Family
<img src="https://raw.githubusercontent.com/newtein/nosql/master/image/g1.JPG"/>

## Interfamily Comparison 
<img src="https://raw.githubusercontent.com/newtein/nosql/master/image/comp.png">

## Conclusion

Normal Interest Score depicts that decade started with a boom in interest around NoSQL-based solutions but 2015 onwards interest seems to gradually decrease.
We have witnessed that events like acquisitions or transfers (by HP Vertica-2011, by CNCF/Linux Foundation RethinkDB-2016-17), publication of research paper (Vertica-2012), mention in US DoD Authorization Bill (Accumulo-2012), open-sourcing (Aerospike-2012, RethinkDB-2012) and version-release (BaseX-2011) ostensibly contributes to gather interests of programmers corresponding to databases on Stack Overflow.
Interest corresponding to old NoSQL solutions like DBM and BerkeleyDB is stagnant over the decade while MemcacheDB stopped development of stable-releases since 2008 but it still accumulates interests of programmers over Stack Overflow considering, this may be attributed to the fact that in terms of elapsed time, MemcacheDB provides the best write performance.
A common attribute is observed in most of the analysis that means views on NoSQL related questions are decreasing with the time that could be explained with an increase in a number of questions corresponding to a constant audience of programmers.  
Cassandra, MongoDB, Redis, and Neo4j are most popular databases of their respective families. Additionally, an interesting point to outline is that Normal Interest Score of these four databases is decreasing from the year 2015. There can be multiple underlying reasons for the cause, for example, the evolution of NewSQL, Spark or HDFS-based solutions. Therefore, we aim to extend our work to a comprehensive decade-long empirical analysis of complete data storage solutions. 
