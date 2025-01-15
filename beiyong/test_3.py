import pytest


class TestLogin:

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    @pytest.mark.parametrize("name", ["zhangsan", "lisi"])
    def test_c(self, name):
         print(name)

    @pytest.mark.parametrize(("username", "password"), [("zhangsan", "111111"), ("lisi", "222222")])
    def test_d(self,username, password):
        print(username + "---" + password)
        assert username != password
        print("test_d")

    @pytest.mark.parametrize("params",[{"username": "zhangsan", "password": "111"}, {"username": "lisi", "password": "222"}])
    def test_e(self, params):
        print(params)