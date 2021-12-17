# The Birthday Paradox

## Pair Programming - Rebecca and Laura

## The Problem:

In probability theory, the birthday problem, or birthday paradox, pertains to the probability that in a set of randomly chosen people some pair of them will have the same birthday.
In a group of at least 23 randomly chosen people, there is more than 50% probability that some pair of them will have the same birthday. Such a result is counterintuitive to many people.
For 57 or more people, the probability is more than 99%, and it reaches 100% when, ignoring leap-years, the number of people reaches 366 (by the **pigeonhole principle**).
The mathematics behind this problem led to a well-known cryptographic attack called the birthday attack.

## The Code Problem

Nobody believes you (even when you refer them to the Wikipedia article), so you'll just have to write some code to emulate the problem and display the probabilities.

## Solution

With 23 people we have 253 pairs:

```python
23 * 22 / 2 = 253
```

The chance of 2 people having different birthdays is:

```python
1 - 1/365 = 364/365 = .997260
```

making 253 comparisons and having them all be different is

```python
(364/365) ** 253 = 0.4995
```

The chance we find a match is

```python
1 – 49.95% = 50.05%
```
