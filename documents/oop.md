- [4 tính chất của lập trình hướng đối tượng](#4-tính-chất-của-lập-trình-hướng-đối-tượng)
  - [**Tính đóng gói (encapsulation)** và che giấu thông tin (information hiding)](#tính-đóng-gói-encapsulation-và-che-giấu-thông-tin-information-hiding)
  - [**Tính kế thừa (inheritance)**](#tính-kế-thừa-inheritance)
  - [**Tính đa hình (polymorphism)**](#tính-đa-hình-polymorphism)
  - [**Tính trừu tượng (abstraction)**](#tính-trừu-tượng-abstraction)
- [Ví dụ minh họa](#ví-dụ-minh-họa)
- [Tham khảo](#tham-khảo)

# 4 tính chất của lập trình hướng đối tượng

## **Tính đóng gói (encapsulation)** và che giấu thông tin (information hiding)

- Tức là trạng thái của đối tượng được bảo vệ không cho các truy cập từ code bên ngoài như thay đổi trong thái hay nhìn trực tiếp. Việc cho phép môi trường bên ngoài tác động lên các dữ liệu nội tại của một đối tượng theo cách nào là hoàn toàn tùy thuộc vào người viết mã. Đây là tính chất đảm bảo sự toàn vẹn, bảo mật của đối tượng
- Trong Java, tính đóng gói được thể hiện thông qua phạm vi truy cập (access modifier). Ngoài ra, các lớp liên quan đến nhau có thể được gom chung lại thành package.
  
## **Tính kế thừa (inheritance)**

Tính kế thừa là khả năng cho phép ta xây dựng một lớp mới dựa trên các định nghĩa của một lớp đã có. Lớp đã có gọi là lớp Cha, lớp mới phát sinh gọi là lớp Con và đương nhiên kế thừa tất cả các thành phần của lớp Cha, có thể chia sẻ hay mở rộng các đặc tính sẵn có mà không phải tiến hành định nghĩa lại.

## **Tính đa hình (polymorphism)**

- Khi một tác vụ được thực hiện theo nhiều cách khác nhau được gọi là **tính đa hình**.
- Đối với tính chất này, nó được thể hiện rõ nhất qua việc gọi phương thức của đối tượng. Các phương thức hoàn toàn có thể giống nhau, nhưng việc xử lý luồng có thể khác nhau. Nói cách khác: Tính đa hình cung cấp khả năng cho phép người lập trình gọi trước một phương thức của đối tượng, tuy chưa xác định đối tượng có phương thức muốn gọi hay không. Đến khi thực hiện (**run-time**), chương trình mới xác định được đối tượng và gọi phương thức tương ứng của đối tượng đó. Kết nối trễ giúp chương trình được uyển chuyển hơn, chỉ yêu cầu đối tượng cung cấp đúng phương thức cần thiết là đủ.
- Trong Java, chúng ta sử dụng nạp chồng phương thức (method overloading) và ghi đè phương thức (method overriding) để có tính đa hình.
  
    - **Nạp chồng (Overloading)**: Đây là khả năng cho phép một lớp có nhiều thuộc tính, phương thức cùng tên nhưng với các tham số khác nhau về loại cũng như về số lượng. Khi được gọi, dựa vào tham số truyền vào, phương thức tương ứng sẽ được thực hiện.
    - **Ghi đè (Overriding)**: là hai phương thức cùng tên, cùng tham số, cùng kiểu trả về nhưng thằng con viết lại và dùng theo cách của nó, và xuất hiện ở lớp cha và tiếp tục xuất hiện ở lớp con. Khi dùng override, lúc thực thi, nếu lớp Con không có phương thức riêng, phương thức của lớp Cha sẽ được gọi, ngược lại nếu có, phương thức của lớp Con được gọi.
  
## **Tính trừu tượng (abstraction)**

- Tính trừu tượng là một tiến trình ẩn các chi tiết trình triển khai và chỉ hiển thị tính năng tới người dùng. Tính trừu tượng cho phép bạn loại bỏ tính chất phức tạp của đối tượng bằng cách chỉ đưa ra các thuộc tính và phương thức cần thiết của đối tượng trong lập trình.
- Tính trừu tượng giúp bạn tập trung vào những cốt lõi cần thiết của đối tượng thay vì quan tâm đến cách nó thực hiện.
- Trong Java, chúng là sử dụng abstract class và abstract interface để có tính trừu tượng.


# Ví dụ minh họa

Ví dụ dưới tôi làm với ngôn ngữ Python

- [animal.py](opp_example/animal.py): Tạo abstract class *Animal* có phương thức *say_hello*, abstract class này thể hiện **tính trừu tượng**, có nghĩa ta định ra rằng dù là con vật gì đi nữa thì nó cũng có phương thức *say_hello*.
- [cat.py](opp_example/cat.py), [dog.py](opp_example/dog.py): Tạo 2 lớp *Cat* và *Dog* kế thừa từ *Animal*. Khi khởi tạo chúng sẽ có tên. Chúng **override** lại phương thức say_*hello* để chào hỏi theo cách riêng của chúng. Điều này thể hiện **tính đóng gói** (đóng gói biến tên và phương thức *say_hello* với nhau) và **tính thừa kế ** (*Cat* và *Dog* mang đặc điểm chung là có *say_hello* từ *Animal*).
- [zoo.py](opp_example/zoo.py), [opp_demo.py](opp_example/oop_demo.py): Tạo lớp *Zoo* để quản lí nhiều *Animal*, có (1) phương thức *add*, *remove* để thêm, bớt các *Animal* (các đối tượng của các lớp thừa kế từ *Animal*), (2) phương thức *show_list_animal* để gọi *say_hello* của tất cả đối tượng nó quản lí. Điều này thể hiện **tính đa hình**, Zoo gọi chỉ gọi một phương thức **say_hello**, nhưng tùy con vật mà lời chào hỏi sẽ khác nhau.

Chạy test:

```shell
$python oop_demo.py
Hi, I am Tom
Hello, My name is Milu
```

# Tham khảo

[https://gpcoder.com/2232-4-tinh-chat-cua-lap-trinh-huong-doi-tuong-trong-java/](https://gpcoder.com/2232-4-tinh-chat-cua-lap-trinh-huong-doi-tuong-trong-java/)
