# 100 Prisoners (and a Light Bulb) Problem

##  Pair Programming - Rebecca and Laura

## The Problem:

There are 100 prisoners are in solitary cells, unable to see, speak or communicate in any way with each other. There’s a central living room with one light bulb, the bulb is initially off.
No prisoner can see the light bulb from his own cell. Everyday, the warden picks a prisoner at random, and that prisoner goes to the central living room. While there, the prisoner can toggle the
bulb if he wishes. Also, the prisoner has the option of asserting the claim that all 100 prisoners have been to the living room. If this assertion is false (that is, some prisoners still haven’t
been to the living room), all 100 prisoners will be shot for their stupidity. However, if it is indeed true, all prisoners are set free. Thus, the assertion should only be made if the prisoner is
100% certain of its validity. Before the random picking begins, the prisoners are allowed to get together to discuss a plan.  What plan should they agree on, so that eventually,
someone will make a correct assertion?

## The Code Problem

Before we look at writing a programme to simulate a possible solution to the problem, you may like to think about how they can do it (no googling!). If you think you have a solution to the problem,
write a simulation for it (to check your chosen strategy works).

## Solution:

The plan the prisoners have:
- One prisoner is picked as the leader. Until he first enters the room nobody touches the light.
- When the leader enters the room for the first time, he turns on the light off, or keeps it off, and counts 1.
- When each prisoner enters the room for the first time, they turn the light on if it is off, or leave it alone if the light is on.
- Each new time the leader enters the room, he turns the light off if it is on and counts + 1.
- Each prisoner will therefore only turn on the light once.
- The leader is the only one allowed to turn it off. He therefore will know how many times it has been turned on - which is the number of unique prisoners who have entered the room.
- When the leader counts 100, every prisoner has been in the room.
