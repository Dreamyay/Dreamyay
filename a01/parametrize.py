import pytest
class Test():
    # @pytest.mark.parametrize("name",["张","李"])
    # def test01(self,name):
    #     print("name",name)
    @pytest.mark.parametrize("name,age",[("康",18),("黄",26),("王",20)])
    def test01(self,name,age):
        print("name：",name,"age：",age)

