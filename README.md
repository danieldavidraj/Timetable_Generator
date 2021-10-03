# Timetable Generator
### Demo: [Timetable Generator](https://timetable-allocator.herokuapp.com/)

A timetable generator application which can be used to generate timetables for schools, colleges for each class for 5 days in a week by providing respective csv files.

## Features :
* Generates timetables for each class in the csv file.
* Teachers can see their personal timetables.
* Teachers wont be allotted the same slot on the same day.
* Optimizes the process to finish within limited slots using <b>Graph Coloring.</b>

## Algorithm :
* <b>Graph Coloring</b> Algorithm to avoid conflicts like teachers being assigned courses at the same time and day.

## Tools :
* Django
* Python
* HTML
* CSS
* JavaScript
* jQuery

## Documentation :
### 1) Takes two csv files:
##### Classes and their courses
<img src="images/csv1.png">

##### Teachers and courses handled by them
<img src="images/csv2.png">

### 2) Creates a Bipartite graph:
<img src="images/bipartite.png" height="auto" width="500px">

### 3) Creates a Line Graph from the Bipartite graph and graph colors it such that no two adjacent vertices are of the same color:
<img src="images/line.png" height="auto" width="500px">

### 4) Graph Coloring Solution Table with all teachers allotted to slots without conflicts:
<img src="images/solution.png">

### 5) Segregates for each class based on their courses:
<img src="images/solution1.png">

### 6) Teachers can also view their personal timetables:
<img src="images/solution2.png">
