import os
import json
from datetime import datetime
from dataclasses import dataclass


filename = "expense_traker.json"
        
def write_to_json(file, x):
    with open(file, 'w') as f:
        json.dump(x, f, default=str, indent=4)


def read_from_json(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

@dataclass
class ExpenseConfiguration:
    id: int
    date: datetime
    description: str
    amount: int

class ExpenseTraker:

    def generate_id(self) -> int:
        expense_list = read_from_json(filename)
        if expense_list:
            id = max(expense['id'] for expense in expense_list) + 1
            return id
        return 1 
    
    def add(self, description: str, amount: float):
        if amount < 0:
            print("Amount cannot be negative")
            return 
        
        expense_list = read_from_json(filename)
        date_now = datetime.now()
        expense = ExpenseConfiguration(
            id=self.generate_id(),
            date=date_now.strftime("%Y-%m-%d %H:%M"),
            description=description,
            amount=amount
        )
        expense_list.append(expense.__dict__) 
        write_to_json(filename, expense_list)

      
    def update(self, id: int, description: str = None, amount: int = None):
        if amount is not None and  amount < 0:
            print("Amount cannot be negative")
            return 
        date_time = datetime.now()
        expense_list = read_from_json(filename)
        for expense in expense_list:
            if expense['id'] == id:
                if description:
                    expense['description'] = description
                if amount:
                    expense['amount'] = amount
                expense['Update_date'] = date_time.strftime("%Y-%m-%d %H:%M")
        write_to_json(filename, expense_list)
        
    def delete(self, id: int):
        expense_list = read_from_json(filename)
        expense_list = [expense for expense in expense_list if expense['id'] != id]
        write_to_json(filename, expense_list)
    
    def total_expense(self):
        expense_list = read_from_json(filename)
        expense_sum = sum(expense['amount'] for expense in expense_list)
        print("Total expences: ", expense_sum)
        
    def view_all_expenses(self):
        expenses_list = read_from_json(filename)
        if not expenses_list:
            print("No expenses recorded yet.")
            return
        
        print(f"{'ID':<5}{'Date':<12}{'Description':<30}{'Amount':<10}")
        print("-" * 60)
        for expense in expenses_list:
            date_only = expense['date'][:10]
            print(f"{expense['id']:<5}{date_only:<12}{expense['description']:<30}{expense['amount']:<10.2f}")
            
    def expenses_per_month(self, month: int):
        expense_list = read_from_json(filename)
        expenses = [
            expense for expense in expense_list
            if datetime.strptime(expense['date'], "%Y-%m-%d %H:%M").month == month
        ]
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total expenses for month {month}: {total}")
        return total
            

t = ExpenseTraker()
