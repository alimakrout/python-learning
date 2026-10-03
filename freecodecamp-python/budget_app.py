class Category():
    def __init__(self,name):
        self.name = name 
        self.ledger = []
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({
            "amount" : -amount,
            "description" : description}) 
            return True
        else : 
            return False

    def get_balance(self):
        solde = 0
        for item in self.ledger:
            solde = solde + item["amount"]
        return solde 
        

    
    def transfer(self,amount,other_category):
        if self.withdraw(amount, description=f"Transfer to {other_category.name}"):
            other_category.deposit(amount, description=f"Transfer from {self.name}")
            return True   
        else: 
            return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else: 
            return True

    def __str__(self):
        output = self.name.center(30,"*") + "\n"
        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            output += f"{desc:<23}{amount:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output
def create_spend_chart(categories):
    spent_amounts = []
    for c in categories:
        spent = 0
        for item in c.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(spent)
        
    total_spent = sum(spent_amounts)
    
    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        percentages = [(spent / total_spent * 100) // 10 * 10 for spent in spent_amounts]

    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
      
        chart += f"{i:>3}| "
        for pct in percentages:
            if pct >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.name) for c in categories)
    
    for i in range(max_len):
        chart += "     "
        for c in categories:
            if i < len(c.name):
                chart += c.name[i] + "  "
            else:
                chart += "   "
        
        if i < max_len - 1:
            chart += "\n"

    return chart
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)