# Staff Management System (OOP Implementation in Python)

## Project Overview

This project is a console-based Staff Management System built to demonstrate advanced Object-Oriented Programming (OOP) concepts in Python.

It models a real-world organizational hierarchy using structured class design, inheritance, encapsulation, polymorphism, and operator overloading. The system allows dynamic creation and management of different staff roles through a menu-driven interface.

---

## Objective

The project focuses on applying core and advanced OOP principles, including:

* Class and object modeling
* Encapsulation using private attributes
* Getter and setter methods
* Inheritance and subclassing
* Method overriding and polymorphism
* Operator overloading
* Special methods implementation
* Dynamic object storage using dictionaries

---

## System Architecture

### Base Class: Staff

Represents a general staff member with attributes such as:

* Name
* Age
* Staff ID
* Pay

Key implementations:

* Private attributes for ID and pay
* Controlled access via getters and setters
* Custom string representation (`__str__`)
* Overloaded comparison operators for salary comparison
* Destructor method (`__del__`)

---

### Derived Classes

**Supervisor**

* Extends the Staff class
* Adds division-level information
* Overrides display behavior

**Engineer**

* Extends the Staff class
* Adds skill specialization
* Customizes output formatting

---

## Core Functionalities

### Add Staff Members

* Create Staff, Supervisor, or Engineer objects
* Store objects dynamically using unique IDs

### Display Staff Details

* Retrieve and display staff information by ID

### Salary Comparison

* Compare salaries between two staff members
* Uses overloaded operators (`__lt__`, `__gt__`, `__eq__`)

### Inheritance Validation

* Demonstrates subclass relationships

### Exit System

* Controlled application termination

---

## Technical Implementation

* Encapsulation with private attributes
* Inheritance and method overriding
* Polymorphism
* Operator overloading
* Special methods (`__str__`, `__del__`)
* Dictionary-based object management
* Menu-driven console architecture

---

## Engineering Highlights

* Clean and extendable class hierarchy
* Logical separation of responsibilities
* Reusable object-oriented structure
* Practical modeling of organizational roles
* Abstraction of comparison logic

---

## Potential Enhancements

* Add structured input validation
* Implement file or database persistence
* Introduce role-based access control
* Modularize into multiple Python files
* Build GUI or web interface
* Add reporting and analytics features

---

## Author

Rajvi Trivedi
Data Analyst | Business Analyst

---

