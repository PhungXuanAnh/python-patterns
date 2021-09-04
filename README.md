
Collection design patterns and idioms in Python described by Jupyter Notebook.
---

- [1. what is design pattern ?](#1-what-is-design-pattern-)
- [2. 4 characteristics of OOP (object oriented programming)](#2-4-characteristics-of-oop-object-oriented-programming)
- [3. Current Patterns](#3-current-patterns)
  - [3.1. Creational Patterns](#31-creational-patterns)
  - [3.2. License Structural Patterns](#32-license-structural-patterns)
  - [3.3. Behavioral Patterns](#33-behavioral-patterns)
  - [3.4. Design for Testability Patterns](#34-design-for-testability-patterns)
  - [3.5. Fundamental Patterns](#35-fundamental-patterns)
  - [3.6. Others](#36-others)
  - [3.7. Videos](#37-videos)
- [4. References](#4-references)

# 1. what is design pattern ?

[what is design pattern ?](https://phungxuananh.github.io/programing/design-pattern-definition/) 

# 2. 4 characteristics of OOP (object oriented programming)

[4 characteristics of OOP](documents/oop.ipynb)

# 3. Current Patterns

## 3.1. Creational Patterns

| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](creational/abstract_factory.ipynb) |  |
| [singleton](creational/singleton.ipynb) | cách để tạo một đối tượng toàn cục duy nhất cho cả hệ thống |
| [builder](creational/builder.ipynb) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory_method](creational/factory-pattern.ipynb) | sử dụng một function/method để tạo đối tượng |
| [lazy_evaluation](creational/lazy_evaluation.ipynb) | lazily-evaluated property pattern in Python |
| [pool](creational/pool.ipynb) | preinstantiate and maintain a group of instances of the same type |
| [prototype](creational/prototype.ipynb) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

## 3.2. License Structural Patterns

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](patterns/structural/3-tier.ipynb) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](patterns/structural/adapter.ipynb) | adapt one interface to another using a white-list |
| [bridge](patterns/structural/bridge.ipynb) | a client-provider middleman to soften interface changes |
| [composite](patterns/structural/composite.ipynb) | lets clients treat individual objects and compositions uniformly |
| [decorator](patterns/structural/decorator.ipynb) | wrap functionality with other functionality in order to affect outputs |
| [facade](patterns/structural/facade.ipynb) | use one class as an API to a number of others |
| [flyweight](patterns/structural/flyweight.ipynb) | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](patterns/structural/front_controller.ipynb) | single handler requests coming to the application |
| [mvc](patterns/structural/mvc.ipynb) | model<->view<->controller (non-strict relationships) |
| [proxy](patterns/structural/proxy.ipynb) | an object funnels operations to something else |

## 3.3. Behavioral Patterns

| Pattern | Description |
|:-------:| ----------- |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility.ipynb) | apply a chain of successive handlers to try and process the data |
| [catalog](patterns/behavioral/catalog.ipynb) | general methods will call different specialized methods based on construction parameter |
| [chaining_method](patterns/behavioral/chaining_method.ipynb) | continue callback next object method |
| [command](patterns/behavioral/command.ipynb) | bundle a command and arguments to call later |
| [iterator](patterns/behavioral/iterator.ipynb) | traverse a container and access the container's elements |
| [mediator](patterns/behavioral/mediator.ipynb) | an object that knows how to connect other objects and act as a proxy |
| [memento](patterns/behavioral/memento.ipynb) | generate an opaque token that can be used to go back to a previous state |
| [observer](patterns/behavioral/observer.ipynb) | provide a callback for notification of events/changes to data |
| [publish_subscribe](patterns/behavioral/publish_subscribe.ipynb) | a source syndicates events/data to 0+ registered listeners |
| [registry](patterns/behavioral/registry.ipynb) | keep track of all subclasses of a given class |
| [specification](patterns/behavioral/specification.ipynb) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](patterns/behavioral/state.ipynb) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](patterns/behavioral/strategy.ipynb) | selectable operations over the same data |
| [template](patterns/behavioral/template.ipynb) | an object imposes a structure but takes pluggable components |
| [visitor](patterns/behavioral/visitor.ipynb) | invoke a callback for all items of a collection |

## 3.4. Design for Testability Patterns

| Pattern | Description |
|:-------:| ----------- |
| [setter_injection](patterns/dft/setter_injection.ipynb) | the client provides the depended-on object to the SUT via the setter injection (implementation variant of dependency injection) |

## 3.5. Fundamental Patterns 

| Pattern | Description |
|:-------:| ----------- |
| [delegation_pattern](patterns/fundamental/delegation_pattern.ipynb) | an object handles a request by delegating to a second object (the delegate) |

## 3.6. Others

| Pattern | Description |
|:-------:| ----------- |
| [blackboard](patterns/other/blackboard.ipynb) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](patterns/other/graph_search.ipynb) | graphing algorithms - non gang of four pattern |
| [hsm](patterns/other/hsm/hsm.ipynb) | hierarchical state machine - non gang of four pattern |


## 3.7. Videos

[Design Patterns in Python by Peter Ullrich](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Sebastian Buczyński - Why you don't need design patterns in Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[You Don't Need That!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Pluggable Libs Through Design Patterns](https://www.youtube.com/watch?v=PfgEU3W0kyU)

# 4. References

- [https://www.tutorialspoint.com/python_design_patterns](https://www.tutorialspoint.com/python_design_patterns)
- [https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm](https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm)
- [https://sourcemaking.com/design_patterns](https://sourcemaking.com/design_patterns)
- [Design Pattern for dummies](https://tedu.com.vn/design-pattern/chuong-1-tong-quan-cac-mau-design-pattern-45.html)
-  branch `forked`