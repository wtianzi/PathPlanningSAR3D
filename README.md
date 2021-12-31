# PathPlanningSAR3D
The web user interface for path planning recommendation in search and rescue missions. Build for study 3.

# 12/29/2021
Steps to do:
1. Divide into grids (considered finished)
  - Build the 3D view of web user interface (Try to add a 2D small map)
  - Divide the area based on the previous algorithm
  - Load heatmap models
2. Send an UAV to a cell for coverage search
  - Build a simple path planning model based on 3 base height and ground info (wood density)
  - Display planned path
3. Show search results
  - Prepare the content of result
  - Display the result of find, subject/clue/nothing, and related uncertainty.
  - The returned images has related area and resolution.
  - Prepare three pairs of images (9 in total) for demo.
  - Display the result images
4. Give recommendation based on the results
  - Build an algorithm of cell/path recommendation considering previous results (first recommend next cell or redo search on lower height; Second, plan the base height for the new search)
  - Display the demo images of a certain height to help the user make wise decisions
5. Make the decision for the next step: height, based on image resolution, speed
  - Build user interface to setup user interaction for the next step, for example: next cell, height,
  - Link to the step 1
  - Organize the experiment flow: 2 task loop
# Notes
  - The z in 3D is the height above water level
# 12/22/2021
First draft:
based on version 1 of study 1 and 2,
1) how high should an UAV fly to covearge search an area by one path
2) how much distance should an UAV fly at the minimum height, like 10 meters, to cover the area
3) regular camera

0:47:36+
## Design of the task: path planning recommendation.
Task description:
1) find the lost person in the area, alternatively clues in the area
2)
3) option: fly lower to get more clear images in order to distinguish the animal/clues from noise
4) machine detect relevance of clues/human


Choice: path, next sub area, height
Measure: performance (time,distance,accuracy), transparency, trust,

## Code
create a django project: SARVACSE, create an application:pathplanning, create database:pptrustdb, create tables: demographics, performance, actionlog, questionnaire1,questionnaire2

## Calculation
calculate boundary of the area, height of UAV [min,max], distance of one search [min,max]

## steps
Create python virtual envionment: https://docs.python-guide.org/dev/virtualenvs/
