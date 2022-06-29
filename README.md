# LecturesLesroosters-DeRoosterRegering
The compilation of schedules can be hard. A schedule contains information on courses, activitities, students, rooms and timeslots. This repository contains code that compiles a weekschedule for a subject list on the FNWI, part of the University of Amsterdam. It must conform to constraints: all activities should have a roomslot (room at a certain time), a roomslot can be used for a single activity and students may not have three gap hours in their personal weekschedule. The goal is to limit the number of maluspoints (MP), which are used to score the schedule. Maluspoints can be received on various occasions:
- 1 MP when a student has two simultaneous activities.
- 1 MP when a students has a gap hour.
- 3 MP when a student has two gap hours.
- 1 MP when the number of participants of an activity exceeds the capacity of a room.
- 5 MP when the eveningslot (17-19h) is used by room C1.110.

## Let's get started
### Requirements
This code was written in Python 3.8. requirements.txt contains all packages that are needed to run the code. These packages can be installed using:
```
pip install -r requirements.txt
```

## Usage
The code can be used by running:
```
python3 main.py [algorithm] [number]
```

[algorithm] can be replaced by:
- **random**: Construct a schedule with random placement of activities and students.
- **greedy_topdown**: Construct a schedule that sorts all the groups of activities from largest group of participating students to smallest and also sorts all roomslots based on their capacity from largest to smallest. This algorithm then matches the two starting from the top going downwards.
- **greedy_bottomup**: Construct a schedule that sorts all the groups of activities from smallest group of participating students to largest and also sorts all roomslots based on their capacity from smallest to largest. This algorithm then matches the two starting from the bottom going up.
 - **random_hillclimber**: This algorithm uses the random algorithm as baseline, and applies a hillclimber on it. The hillclimber swaps roomslots around looking for an alternative schedule until the swaps stop resulting in a decrease in malus points.
 - **greedy_topdown_hillclimber**: This algorithm uses the greedy topdown algorithm as baseline, and applies a hillclimber on it. The hillclimber swaps roomslots around looking for an alternative schedule until the swaps stop resulting in a decrease in malus points.
 - **greedy_bottomup_hillclimber**: This algorithm uses the greety bottomup algorithm as baseline, and applies a hillclimber on it. The hillclimber swaps roomslots around looking for an alternative schedule until the swaps stop resulting in a decrease in malus points.

 [number] can be replaced by a number, which indicates the number of repetitions of the algorithm.

## Structure
The most important files are:
- **/code**: contains all code
    - **/algorithms**: contains all code used for the algorithms
    - **/classes**: contains all classes that are used in this case
- **/data**: contains datafiles necessary for compiling a schedule
- **/images**: contains visualization of the resuls

## Representation
### Overview of classes
![](images/UML.jpeg)

*Overview of the classes that are used for this case.*

### Timeslot clarification
| Time | Monday | Tuesday | Wednesday | Thursday | Friday |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 9 - 11 | 0 | 5 | 10 | 15 | 20 |
| 11 - 13 | 1 | 6 | 11 | 16 | 21 |
| 13 - 15 | 2 | 7 | 12 | 17 | 22 |
| 15 - 17 | 3 | 8 | 13 | 18 | 23 |
| 17 - 19 | 4 | 9 | 14 | 19 | 24 |

*The timeslots in the table refer to the timeslots in the output. For example, timeslot 3 is a timeslot 15-17h on monday.*

### Output
![](images/Output.jpg)

*An example of output that will be printed when code is run. Columns from left to right: Timeslot, RoomID, Course name, Type, Number of participants and Room capacity. Timeslots indicate a certain day and time (0-24). A clarification of this number can be found under Timeslot clarification. The timeslots 17-19h can only be used by room C1.110. RoomID displays the assigned room. Course name contains the name of the assigned course. Type indicates the type of activity. Number of participants shows the number of participants for the assigned activity. Room capacity displays the capacity for the room.*

## Authors
- Victor Storm van 's Gravesande, 13141406
- Luuk van Vliet, 12251925
- Sharon Visser, 12228451