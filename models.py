class Seller():
  def __init__(self, seller_cpf, seller_name, seller_salary):
    self.seller_cpf = seller_cpf
    self.seller_name = seller_name
    self.seller_salary = seller_salary


class Client():
  def __init__(self, client_cnpj, client_name, client_business_area):
    self.client_cnpj = client_cnpj
    self.client_name = client_name
    self.client_business_area = client_business_area


class Sells():
  ITEM_ID = 0
  ITEM_QUANTITY = 1
  ITEM_PRICE = 2
  def __init__(self, sell_id, item_list, seller_name):
    self.sell_id = sell_id
    self.item_list = item_list[1:-1].split(',')
    self.seller_name = seller_name

  def calculate_sell_value(self):
    aux_float = 0
    for item in self.item_list:
      item_attrs_list = item.split('-')
      aux_float += float(item_attrs_list[self.ITEM_QUANTITY])*float(item_attrs_list[self.ITEM_PRICE])
    return aux_float
