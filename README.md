# Splitwise Clone Project

## Table of Contents
- [Introduction](#introduction)
- [Step 1: Creating User and Group Models](#step-1-creating-user-and-group-models)
- [Step 2: Basic GUI](#step-2-basic-gui)
- [Step 3: Graph Visualization](#step-3-graph-visualization)
- [Step 4: Database Setup](#step-4-database-setup)
- [Final Integration](#final-integration)
- [Bug Fixes](#bug-fixes)
- [Project_Features](#project-features)

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
## Project Features

### Groups
- Add new groups with **customized default splits** (equal, percentage, custom split).  
- View all the groups you are in, along with **total expenses**.  
- Add new expenses for each group, with features including:  
  - Multi-currency support  
  - Selective contributors for an expense  
  - Customized splits  
  - Expense **date** and **category** selection  
- View the **debts graph**, showing who owes whom (before simplification).  
- **Simplify** the debts graph and visualize it.  
- View **group expenses categorized** by type.  
- **Import groups from an Excel file**.  

### Friends
- View all friends with whom you have exchanged money and the **total expenses** for each.  
- Add new friends with **customized default splits** (equal, percentage, custom split).  
- Add new expenses for each friend (with the same options as **group expenses**).  
- View **categorized expenses** for each friend.  
- **Simplified debts** are displayed on the **Debts Page**.  

### Currency Conversion
- Convert **any currency** to another with ease.  

### Reports
- View your expenses in multiple categories:  
  - **Total expenses**  
  - **Group expenses**  
  - **Friend expenses**  
  - **Current month's expenses**  
- View **total amount owed and due**.  
- **Visualize reports** with the option to:  
  - Set a **time duration**  
  - Filter by **group, friends, or category**  

### Profile
- View **your account information**.  
- Edit your **name** or **balance**.  
- Add **recurring expenses** (set specific dates for automatic payments).  

### Debts Page
- **View and pay** your simplified debts.  
- Payment methods:  
  - **Cash Payments:** The debt is marked as paid instantly.  
  - **Online Payments:**  
    - If the creditor has an account in our app, they must **verify** your payment before it is finalized.  
    - If the creditor **does not** have an account, the payment is **automatically approved** (we cannot request verification from external users).  
- Manage and pay **recurring expenses** as well.  

### Search Page
- **Search for any expense** by:  
  - **Label**  
  - **User (payer)**  
  - **Date**  

### Notification Bar
- View **payment notifications** when someone pays their debt to you.  
- **Verify or deny payments**:  
  - If verified, the amount is **added to your balance**.  


💡 **Run the program and explore more features yourself!** 🎉  



---

Feel free to contribute, report issues, or suggest improvements! 🚀
