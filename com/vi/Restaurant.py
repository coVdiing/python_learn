# coding:UTF-8
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print "餐厅名为:{},主营美食是:{}".format(self.restaurant_name,self.cuisine_type)

    def open_restaurant(self):
        print "{} 餐厅营业中...".format(self.restaurant_name)

restaurant1 = Restaurant('一盏灯','湘菜')
restaurant2 = Restaurant('费大厨','辣椒炒肉')
restaurant3 = Restaurant('海底捞','火锅')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()