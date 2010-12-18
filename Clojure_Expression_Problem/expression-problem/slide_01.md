!SLIDE
#The Expression Problem#

!SLIDE center
#The Expression Problem#
![pic1](1.png)

!SLIDE center
#The Expression Problem#
![pic2](2.png)

!SLIDE center
#The Expression Problem#
![pic3](3.png)

!SLIDE center
#The Expression Problem#
![pic3](3.png)
###A should be able to work with B's abstractions, and vice versa,###
###**without modification of the original code**###

!SLIDE bullets incremental
#A can't inherit from B#

* A is newer than B
* A is hard to change
* We don't control A

!SLIDE
#Some approaches to the Expression Problem#

!SLIDE center
#1. Wrappers#
![wrappers1](wrappers1.png)

!SLIDE center
#1. Wrappers#
![wrappers2](wrappers2.png)

!SLIDE bullets incremental
#Wrappers add complexity#

* Ruin identity
* Ruin equality
* Causes non-local defects
* Don't compose

!SLIDE center
#2. Monkey Patching#
![monkey1](monkey1.png)

!SLIDE center
#2. Monkey Patching#
![monkey2](monkey2.png)

!SLIDE bullets incremental
#Monkey patching adds complexity#

* Preserves identity (barely)
* Ruins namespacing
* Causes non-local defects
* Not allowed in many languages

!SLIDE
#Clojure's Solutions#

!SLIDE bullets incremental
#Generic functions#

* Dispatch to an arbitrary function of the first argument
* Polymorphism lives in the functions
* Preserves namespacing

!SLIDE
#Example#

!SLIDE bullets incremental
#Drawbacks of multimethods#
* Performance

!SLIDE bullets incremental
#Protocols#

* The best of all the worlds

!SLIDE center
#Protocols#
![protocols](protocols.png)

!SLIDE
#Example#
