- [1. Design Patterns là gì?](#1-design-patterns-là-gì)
- [2. Tại sao phải sử dụng Design Patterns?](#2-tại-sao-phải-sử-dụng-design-patterns)
- [3. Phân loại Design Patterns](#3-phân-loại-design-patterns)
- [4. Để học Design Patterns cần có gì?](#4-Để-học-design-patterns-cần-có-gì)


# 1. Design Patterns là gì?
Design patterns là một kỹ thuật trong lập trình hướng đối tượng, là các giải pháp đã được tối ưu hóa và tạo thành các mẫu thiết kế chuẩn nhằm tái sử dụng cho các vấn đề lập trình mà chúng ta gặp phải hàng ngày..

Các vấn đề mà bạn gặp phải có thể bạn sẽ tự nghĩ ra cách giải quyết nhưng có thể nó chưa phải là tối ưu. Design Pattern giúp bạn giải quyết vấn đề một cách tối ưu nhất, cung cấp cho bạn các giải pháp trong lập trình OOP.

Nó không phải là ngôn ngữ cụ thể nào cả. Design patterns có thể thực hiện được ở phần lớn các ngôn ngữ lập trình. Ta thường gặp nó nhất trong lập trình OOP.

# 2. Tại sao phải sử dụng Design Patterns?
Design Patterns là tập hơn những giải pháp đã được tối ưu hóa, đã được kiểm chứng để giải quyết các vấn đề trong software engineering. Vậy khi bạn gặp bất kỳ khó khăn gì, design patterns là kim chỉ nam giúp bạn giải quyết vấn đề thay vì tự tìm kiếm giải pháp cho một vấn đề đã được chứng minh.

- Cung cấp giải pháp ở dạng tổng quát, giúp tăng tốc độ phát triển phần mềm bằng cách đưa ra các mô hình test, mô hình phát triển đã qua kiểm nghiệm.
- Giúp bạn tái sử dụng mã lệnh, giúp cho dự án của chúng ta dễ bảo trì, nâng cấp và mở rộng
- Dùng lại các design pattern giúp tránh được các vấn đề tiềm ẩn có thể gây ra những lỗi lớn, dễ dàng nâng cấp, bảo trì về sau.
- Giúp code của chúng ta sẽ dễ đọc hơn, giúp cho các lập trình viên khác có thể hiểu code 1 cách nhanh chóng (có thể hiểu là tính communicate). Mọi thành viên trong team có thể dễ dàng trao đổi với nhau để cùng xây dựng dự án mà k mất quá nhiều thời gian.
- Design pattern sẽ giúp chúng ta giảm được thời gian và công sức suy nghĩ ra các cách giải quyết cho những vấn đề đã có lời giải.

# 3. Phân loại Design Patterns

Có 3 nhóm chính sau:

**Creational Pattern** (nhóm khởi tạo): iúp bạn trong việc khởi tạo đối tượng, như bạn biết để khởi tạo bạn phải sử dụng từ khóa new, nhóm Creational Pattern sẽ sử dụng một số thủ thuật để khởi tạo đối tượng mà bạn sẽ không nhìn thấy từ khóa này. Nhóm này gồm 9 mẫu design là:

    Abstract Factory
    Builder
    Factory Method
    Multiton
    Pool
    Prototype
    Simple Factory
    Singleton
    Static Factory

**Structural Pattern** (nhóm cấu trúc): giúp chúng ta thiết lập, định nghĩa quan hệ giữa các đối tượng. Nhóm này gồm có 11 mẫu design là:

    Adapter/ Wrapper
    Bridge
    Composite
    Data Mapper
    Decorator
    Dependency Injection
    Facade
    Fluent Interface
    Flyweight
    Registry
    Proxy

**Behavioral Pattern** (nhóm ứng xử) : tập trung thực hiện các hành vi của đối tượng. Gồm 12 mẫu design là:

    Chain Of Responsibilities
    Command
    Iterator
    Mediator
    Memento
    Null Object
    Observer
    Specification
    State
    Strategy
    Template Method
    Visitor

**Ngoài ra thì trong thời gian gần đây đã xuất hiện thêm 4 mẫu design nữa đó là:**

    1.4.1 Delegation.
    Service Locator.
    Repository.
    Entity-Attribute-Value (EAV).

# 4. Để học Design Patterns cần có gì?
 
Bốn đặc tính của OOP: Thừa kế, Đa hình, Trừu tượng, Bao đóng.
Khái niệm interface và abstract. Cái này cực kỳ quan trọng, để hiểu và áp dụng 2 khái niệm này có thể sẽ mất một thời gian, nhưng khi bạn nắm chắc nó bạn sẽ thấy nó thực sự cần thiết.
Bỏ tư duy theo lối cấu trúc, nâng tư duy hoàn toàn OOP.