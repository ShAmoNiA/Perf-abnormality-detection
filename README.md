## Project: Flamegraph similarity analysis

 

The objective is to compare a flame graph that is derived from either pure function tracing such as with uftrace/ftrace or callstack attached to LTTng sched_switch events or system calls. This comparison can be useful to identify various application/system behavior patterns as well as anomalous or malign behavior.

The callstacks should be compared using several relevant metrics such as edit distance and other alignment methods. The objective is to experiment with a number of similarity metrics and several clustering algorithms. Another obvious comparison is the conventional delta flamechart.One more reason to compare stacks is to look at software evolution over multiple releases and commits.

 

An example open source application will be chosen as a use case. Alternatively the linux kernel can be targeted, for example the network stack can be traced to identify anomalous arriving packets or behavior. This may be more relevant in a network node such as a firewall or router than a simple host, however. A few example applications can be the OpenVSwitch, nginx, apache browser, etc.

 

Skillset: Tracecompass, LTTng, uftrace, ftrace, scikit-learn, python.
