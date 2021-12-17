# Vending Machine Python Challenge

## Day 3 - Rebecca and Tracy

A vending machine is a machine that dispenses items such as snacks and beverages to customers automatically, after the customer inserts currency or credit into the machine.
The first modern vending machines were developed in England in the early 19th century and dispensed postcards.

In this exercise you will build the brains of a vending machine. It will accept money, make change, maintain inventory, and dispense products. All the things that you might expect a vending machine to accomplish.
The point of this kata to to provide a slightly larger than trivial exercise that can be used to practice TDD. A significant portion of the effort will be in determining what tests should be written and, more importantly, what should be written next.

## Features

The core features of our vending machine, which you should look to implement in order to complete this challenge are as follows:

## 1: Accept Coins

As a vendor I want a vending machine that will accept coins so that I can collect money from the customer. NB. This is an American vending machine, so the currency being used will reflect this.
The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid one (pennies). When a valid coin is inserted the amount of the coin will be added to the current
amount and the display will be updated. When there are no coins inserted, the machine displays INSERT COIN. Rejected coins are placed in the coin return.

## 2: Select Product

As a vendor I want customers to select products so that I can give them an incentive to put money in the machine. There are three products: cola for $1.00, crisps for $0.50, and chocolate for $0.65.
When the respective button is pressed and enough money has been inserted, the product is dispensed and the machine displays THANK YOU. If the display is checked again, it will display INSERT COINS
and the current amount will be set to $0.00. If there is not enough money inserted then the machine displays PRICE and the price of the item and subsequent checks of the display will
display either INSERT COINS or the current amount as appropriate.

## 3: Make Change

As a vendor I want customers to receive correct change so that they will use the vending machine again. When a product is selected that costs less than the amount of money in the machine,
then the remaining amount is placed in the coin return.

## 4: Return Coins

As a customer I want to have my money returned so that I can change my mind about buying stuff from the vending machine. When the return coins is selected, the money the customer has placed
in the machine is returned and the display shows INSERT COIN.

## 5: Sold Out

As a customer I want to be told when the item I have selected is not available so that I can select another item. When the item selected by the customer is out of stock,
the machine displays SOLD OUT. If the display is checked again, it will display the amount of money remaining in the machine or INSERT COIN if there is no money in the machine.

## 6: Exact Change Only

As a customer I want to be told when exact change is required So that I can determine if I can buy something with the money I have before inserting it.
When the machine is not able to make change with the money in the machine for any of the items that it sells, it will display EXACT CHANGE ONLY instead of INSERT COINS.

## Refactor

It's annoying that this vending machine only accepts American currency. Let's convert the currency to GBP. Then let's add some more items to the vending machine.

## 8: Convert currency to GBP

As a customer I want to be able to use British currency so that I may buy an item. You will need to refactor your code and your tests to remove any references to American currency.
The newly converted vending machine accepts coins of 5p, 10p, 20p, 50p, £1 and £2. It does not accept 1p or 2p coins, nor does it accept notes.

The vending machine will accept valid coins (5p, 10p, 20p, 50p, £1, £2) and reject invalid ones (2p, 1p, £5, £10, £20).

When a valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated. When there are no coins inserted, the machine displays INSERT COIN.
Rejected coins are placed in the coin return.

You should convert the value of these items to GBP. Don't concern yourself with conversion rates, the following values will suffice for the items:
- cola: £1:00
- crisps: 50p
- chocolate: 50p
