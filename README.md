python-patterns
===============

Tập hợp của design patterns và idioms trong Python được môt tả sử dụng jupyter notebook.

Tham khảo từ branch forked và từ các trang web:
- [https://www.tutorialspoint.com/python_design_patterns](https://www.tutorialspoint.com/python_design_patterns)
- [https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm](https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm)
- [https://sourcemaking.com/design_patterns](https://sourcemaking.com/design_patterns)
- [Design Pattern for dummies](https://tedu.com.vn/design-pattern/chuong-1-tong-quan-cac-mau-design-pattern-45.html)

**Chý ý**: Trước khi đi sâu vào các pattern, hãy tìm hiểu **design pattern** là gì [tại đây](documents/design_partterns.md) và tìm hiểu **4 tính chất của hướng đối tượng** [tại đây](documents/oop.ipynb)

Current Patterns
----------------

__Creational Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](creational/abstract_factory.ipynb) | use a generic function with specific factories |
| [singleton](creational/singleton.ipynb) | cách để tạo một đối tượng toàn cục duy nhất cho cả hệ thống |
| [builder](creational/builder.ipynb) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory_method](creational/factory-pattern.ipynb) | sử dụng một function/method để tạo đối tượng |
| [lazy_evaluation](creational/lazy_evaluation.ipynb) | lazily-evaluated property pattern in Python |
| [pool](creational/pool.ipynb) | preinstantiate and maintain a group of instances of the same type |
| [prototype](creational/prototype.ipynb) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

__Structural Patterns__:

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

__Behavioral Patterns__:

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

__Design for Testability Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [setter_injection](patterns/dft/setter_injection.ipynb) | the client provides the depended-on object to the SUT via the setter injection (implementation variant of dependency injection) |

__Fundamental Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [delegation_pattern](patterns/fundamental/delegation_pattern.ipynb) | an object handles a request by delegating to a second object (the delegate) |

__Others__:

| Pattern | Description |
|:-------:| ----------- |
| [blackboard](patterns/other/blackboard.ipynb) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](patterns/other/graph_search.ipynb) | graphing algorithms - non gang of four pattern |
| [hsm](patterns/other/hsm/hsm.ipynb) | hierarchical state machine - non gang of four pattern |


Videos
------
[Design Patterns in Python by Peter Ullrich](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Sebastian Buczyński - Why you don't need design patterns in Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[You Don't Need That!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Pluggable Libs Through Design Patterns](https://www.youtube.com/watch?v=PfgEU3W0kyU)


Contributing
------------
When an implementation is added or modified, please review the following guidelines:

##### Output
All files with example patterns have `### OUTPUT ###` section at the bottom 
(migration to OUTPUT = """...""" is in progress).

Run `append_output.sh` (e.g. `./append_output.sh borg.ipynb`) to generate/update it.

##### Docstrings
Add module level description in form of a docstring with links to corresponding references or other useful information.

Add "Examples in Python ecosystem" section if you know some. It shows how patterns could be applied to real-world problems.

[facade.ipynb](patterns/structural/facade.ipynb) has a good example of detailed description,
but sometimes the shorter one as in [template.ipynb](patterns/behavioral/template.ipynb) would suffice.

In some cases class-level docstring with doctest would also help (see [adapter.ipynb](patterns/structural/adapter.ipynb))
but readable OUTPUT section is much better.


##### Python2/3 compatibility
Try to keep it (discussion is held in [issue #208](https://github.com/faif/python-patterns/issues/208))
- use new style classes (inherit from `object`)
- use `from __future__ import print_function`

##### Update README
When everything else is done - update corresponding part of README.


##### Travis CI
Please run `flake8` and `pytest` commands locally to be sure your changes will pass CI .
