# Splitwise Clone Project

## Table of Contents
- [Introduction](#introduction)
- [Step 1: Creating User and Group Models](#step-1-creating-user-and-group-models)
- [Step 2: Basic GUI](#step-2-basic-gui)
- [Step 3: Graph Visualization](#step-3-graph-visualization)
- [Step 4: Database Setup](#step-4-database-setup)
- [Final Integration](#final-integration)
- [Bug Fixes](#bug-fixes)
- [Project_Features](#project_features)

## Introduction
This project is a simplified clone of **Splitwise**, designed to help users manage group expenses efficiently. It allows users to create groups, add expenses, track balances, and visualize financial data.  

## Step 1: Creating User and Group Models
- The `User` class (found in `users.py`) stores a user's **name, email, and balance**. It includes methods to retrieve and update the balance.  
- The `Group` class (found in `groups.py`) manages a group's **name, members, and expenses**.  

## Step 2: Basic GUI
- We implemented a **basic graphical user interface (GUI)** in this step.  
- The interface will be improved and refined in later stages.  

## Step 3: Graph Visualization
- We created a **graphical representation** of group expenses using **Matplotlib**.  
- This feature helps users visualize financial distributions and understand spending patterns.  

## Step 4: Database Setup
- An **SQLite database** was set up to manage users, groups, expenses, and debts.  
- This database ensures **data persistence**, enables **historical analysis**, and improves **efficiency** in handling relationships and transactions.  

## Final Integration
- The **frontend and backend** were successfully integrated to provide a smooth user experience.  
- This was the **most time-consuming step** in the project!  

## Bug Fixes
- Some small bugs were identified and fixed.  
- The corrected version is available in the **"Correction"** branch.  

---
## Project Features:

### Groups:
- - Add new groups with customized default splits (equal, percentage, split)
  - See all of the groups you are in, and the total expenses
  - Add new expenses for each group (expenses can be in other currencies, all or some be contributed in the expense, use customized splits, enter the date and category of your expense)
  -  See the debts graph; who owes whom?(Before simplification)
  -  Simplify the debts grph and visualised it.
  -  See the group expenses classified by their category!
  -  Add new groups from excel file!
    
### Friends:
- - See all of the friends you have excahnged money with and total expenses for each.
  - Add new friends with customized default splits (equal, percentage, split)
  - Add new expenses for each friend ( with all options same as group expenses!)
  - See all expenses with each friend classified by their category!
  - Debts will be simplified and showed in debts page.

### Currency Conversion
- Convert any currency to any other you wish!

### Reports:
- - 


---

Feel free to contribute, report issues, or suggest improvements!
