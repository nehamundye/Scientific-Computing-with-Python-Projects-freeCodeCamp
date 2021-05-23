class Category:
  def __init__(self, category):
   self.category = category
   self.ledger = []
  
  def deposit(self, amount, description=''):
    result = {"amount": amount, "description": description}
    return self.ledger.append(result)

  def withdraw(self, amount, description=''):
    result = {"amount": amount*-1, "description": description}
    if self.check_funds(amount):
      self.ledger.append(result)
      return True
    return False
  
  def get_balance(self):
    all_amount = []
    total_budget = 0
    for d in self.ledger:
      all_amount.append(d['amount']) 
      total_budget = sum(all_amount)
    return total_budget
  
  def transfer(self, amount, othercategory):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {othercategory.category}")
      othercategory.deposit(amount, f"Transfer from {self.category}")
      return True
    return False


  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True
  
  def __str__(self):
    half_star = (30 - len(self.category))/2
    if len("*"* int(half_star)  + self.category + "*"* int(half_star)) != 30:
      s = ("*"* int(half_star)  + self.category + "*"* (int(half_star)+1))+ '\n'
    else:
      s = ("*"* int(half_star)  + self.category + "*"* int(half_star))+ '\n'
    
    for i in range(len(self.ledger)):
      s = s + ((self.ledger[i]['description'])[:23] + (str("{:.2f}".format(self.ledger[i]['amount'])))[:7].rjust(30-(len((self.ledger[i]['description'])[:23] )), " ") + '\n')
    return s + f'Total: {self.get_balance()}'
    




def create_spend_chart(categories):
  temp_spend = 0
  spend_list = []

  for category in categories:
    temp_spend = 0   
    for d in category.ledger:
      if d['amount'] < 0:
        temp_spend = temp_spend + abs(d['amount'])
    spend_list.append(temp_spend)

  total_spend = sum(spend_list)

  percentage_total_spend = [(spend/total_spend)*100 for spend in spend_list]

  for i in range(0, len(percentage_total_spend)):
    if percentage_total_spend[i] % 10 != 0:
        percentage_total_spend[i] = percentage_total_spend[i] - (percentage_total_spend[i] % 10)

  chart = "Percentage spent by category\n"
  for percent in range(100, -10, -10):
      chart = chart  + str(percent).rjust(3)+'| '
      for spend in percentage_total_spend:
          if percent > spend:
              chart = chart + '   '
          else:
              chart = chart + 'o  '  
      chart = chart + '\n'  

  chart = chart + "    "  

  for i in range(len(percentage_total_spend)):
      chart = chart +  "---" 
  chart = chart +  "-" + '\n'


  len_of_categories = []
  name_of_categories = []
  for category in categories:
    len_of_categories.append(len(category.category))
  for category in categories:
    name_of_categories.append(category.category)


  chart_categories = '   '
  for i in range(0, max(len_of_categories)):
    for name in name_of_categories:
        if len(name) > i:
            chart_categories = chart_categories + '  ' + name[i]
        else:
            chart_categories = chart_categories + '   ' 
    chart_categories = chart_categories + '  ' + '\n'
    chart = chart + chart_categories
    chart_categories = '   '
  return chart[0:-1]