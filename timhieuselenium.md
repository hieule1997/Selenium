## Getting Started
### 1. Đoạn mã đơn giản
Nếu bạn đã cài đặt Selenium Python bindings, bạn có thể bắt đầu sử dụng nó như sau
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```
Script trên có thể lưu trong file (eg:- python_org_search.py) sau đó có thể run như sau:
```
python python_org_search.py
```
Python bạn đang chạy nên có selenium module cài đặt.
### 2. Giải thích đoạn mã

Selenium.webdriver module cung cấp tất cả Webdriver implementations. Hiện nay hỗ trợ Webdriver implementations là Firefox, Chrome, IE và Remote
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```
Firefox webDriver được tạo thì sử dụng câu lệnh:

```
driver = webdriver.Firefox()
```
Chorme webDriver được tạo thì sử dụng câu lệnh
```
driver = webdriver.Chorme("path/to/chorme")
```
Phương thức Driver.get sẽ điều hướng tới một page được cung cấp bởi URL.WebDriver sẽ đợi cho đến khi trang được tải xong. Trước khi trả lại điều khiển test hoặc script.
```
driver.get("http://www.python.org")
```
Dòng lệnh tiếp theo là một assertion để xác nhận rằng trong tiêu đề có từ 'Python'
```
assert "Python" in driver.title
```
WebDriver cung cấp một số cách để tìm elements sử dụng một trong các cách tìm đó là: find_element_by_* methods.

Tiếp theo là input text element có thể được đặt bằng tên thuộc tính của nó sử dụng find_element_by_name method  
```
elem = driver.find_element_by_name("q")
```
Trường hợp gửi một keys, các phím đặc biệt có thể gửi sử dụng bởi lớp keys được import từ selenium.webdriver.common.keys.
```
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```
Sau khi thực hiện một action nào đó trên page bạn nên lấy kết quả trả ra bằng cậu lệnh lấy message như dưới đấy:
```
assert "No results found." not in driver.page_source
```
Cuối cùng là phương thức close window như sau:
```
driver.close()
```
### 3. Sử dụng Selenium viết Unitest
Các gói selenium không cung cấp một công cụ testing/framework. Bạn có thể viết test cases sử dụng unit test module của Python. Một lựa chọn khác cho tool/frameworke là `py.test` và `nose`

Trong chương này, chúng ta sử dụng unit test như framework là một lựa chọn. Dưới đây là một ví dụ sửa đổi trong đó sử dụng module unnit test. Đây là một thử nghiệm cho chức năng tìm kiếm của python.org  

```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```
Và kết qủa sau khi chạy thành công thể hiện như ở dưới:

```
python test_python_org_search.py
.
----------------------------------------------------------------------
Ran 1 test in 15.566s

OK
```