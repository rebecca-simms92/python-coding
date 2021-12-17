# The Virtual Pet (Tamagotchi) Challenge

# Day 2 - Rebecca and Elena

A Tamagotchi is a small, handheld digital pet that you can feed, play with, put to bed and clean up after. Look after it well by feeding it the right kinds of foods,
showering it with attention and cleaning up after it when required, and your Tamagotchi will grow up to be a smart, well-respected member of society.
Ignore its needs and its mood will sour until it eventually dies.

## Implementing 'Basic Needs'

To aid the quick release of this project, we require you to deliver the absolute minimum that could reasonably be called a Tamagotchi pet as soon as possible.
Then we're going to add all of the good stuff- different foods and games to play, all purchasable with our own very special currency, the Kablammo.
Our stories for our 'quick release' Tamagotchi will include:
- Tamagotchi has basic stats
- Feeding the Tamagotchi
- Playing with the Tamagotchi
- Putting the Tamagotchi to bed
- Making the Tamagotchi poop
- Tamagotchi's needs change over time
- Tamagotchi can be hungry
- Tamagotchi can be dead

Like we said before, first things first is to get all of the basic needs finished so we have some semblance of a basic Tamagotchi pet. We're talking about things like hungriness,
fullness, tiredness, happiness and of course, the actions required to mitigate these needs. We're not really sure of the implementation though. We were thinking of needs on a scale of 1-100,
with different activities having different effects on them, but we'll go with whatever you think is best.


## 1: Tamagotchi Has Basic Stats

As a Tamagotchi owner, I want my Tamagotchi to have basic stats. So that I know its current state

**GIVEN** I have a Tamagotchi
**WHEN** I inspect its stats
**THEN** it has a default Hunger stat of 50
**AND** it has a default Fullness stat of 50

## 2: Feeding the Tamagotchi

As a Tamagotchi owner I want to feed my Tamagotchi. So that I can satiate its hunger

**GIVEN** I have a Tamagotchi
**WHEN** I feed it
**THEN** its hunger is decreased by 10
**AND** its fullness is increased by 10

## 3: Playing with Tamagotchi

As a Tamagotchi owner I want to play with my Tamagotchi. So that I can make it happier

**GIVEN** I have a Tamagotchi
**WHEN** I play with it
**THEN** it's happiness is increased by 10
**AND** it's tiredness is increased by 10

## 4: Putting Tamagotchi to Bed

As a Tamagotchi owner I want to put my Tamagotchi to bed. So that I can refill it's energy

**GIVEN** I have a Tamagotchi
**WHEN** I put it to bed
**THEN** it's tiredness is decreased by 10

## 5: Making Tamagotchi Poop

As a Tamagotchi owner I want to make my Tamagotchi poop. So that it is more comfortable

**GIVEN** I have a Tamagotchi
**WHEN** I make it poop
**THEN** it's fullness is decreased by 10

## 6: Changing Tamagotchi Needs Over Time

As a Tamagotchi owner I want my Tamagotchi's needs to change over time. So that I have to look after it carefully

**GIVEN** I have a Tamagotchi
**WHEN** time passes
**THEN** it's tiredness is increased
**AND** it's hungriness is increased
**AND** it's happiness is decreased

## 7: Tamagotchi can be Hangry

As a Tamagotchi owner I want to know when my Tamagotchi is hangry. So that I may give it a sandwich

**GIVEN** I have a Tamagotchi
**WHEN** its hunger is above 70
**THEN** its mood will be sad

## 8: Tamagotchi can be Dead

As a Tamagotchi owner I want to know when my Tamagotchi is dead. So that I may hide the body...

**GIVEN** I have a Tamagotchi
**WHEN** its hunger is 100
**THEN** it will be dead
