---
title: Dependency Inversion
date: 2023-09-18
tags: []
aliases: []
feed: hide
---

> High level modules should not depend on low level modules. Instead both should depend on abstractions (modules) and these abstractions should not depend on details

Rather than instantiating `new` instances of a class- refactor the class to implement an interface, then only use Interfaces in the main code / the higher level interface.

To handle instantiation you can refactor to use a single class that instantiates all the dependent classes as interfaces- so that all your dependencies are in one place:
```c#

interface Iperson;

class person implents Iperson;

public static class Factory{
	public static Iperson createPerson(){
		return new Person()
	}
}

public class main(){
	Iperson thisPerson = Factory.createPerson()
//do code with thisPerson
}
```
This removes all dependencies through out code and can allow for changing out the details of any class without worrying about breaking other parts of the code.

This can be solved with dependency injection as well

--- 
[Stackify, Dependency Inversion](https://stackify.com/dependency-inversion-principle/), accessed: 9/18/2023
#### Related:
[[Programming]]