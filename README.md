#Expense Tracker
Description
This is a simple expense tracker application that allows users to add, update, delete, and view expenses. Data is stored in a JSON file, preserving the information between sessions.

#Features
Add Expense: Add new expenses with a description and amount.
Update Expense: Update an existing expense by ID.
Delete Expense: Remove an expense by ID.
View All Expenses: List all expenses with details.
Total Expenses: View the total amount of all expenses.
Monthly Expenses: View the total expenses for a specific month.

#Data Structure
Expenses are saved in expense_traker.json with the following fields:

id: Unique identifier.
date: Date and time of the expense.
description: Description of the expense.
amount: Amount spent.

#Example Output
json
[
    {
        "id": 1,
        "date": "2024-12-01 12:30",
        "description": "Lunch",
        "amount": 15.50
    }
]

#Explanation
generate_id(): Generates a unique ID for each new expense.
add(): Adds a new expense.
update(): Updates an expense by ID.
delete(): Deletes an expense by ID.
total_expense(): Displays total expenses.
expenses_per_month(): Displays expenses for a specific month.

https://roadmap.sh/projects/expense-tracker
