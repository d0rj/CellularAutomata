# ⬛⬜ Cellular automata

## Description

A simple application for studying cellular automata, in particular "The game of life". Currently, only it is supported.

The field is an unfolding of the torus.

## Environment

* numpy
* tkinter

## Example of work

<p float="left">
<img src="https://github.com/d0rj/CellularAutomata/blob/master/screenshots/on_start.PNG?raw=true" width=300>

<img src="https://github.com/d0rj/CellularAutomata/blob/master/screenshots/planner_gun.PNG?raw=true" width=300>
</p>

## How to use

No *.exe* files, only hardcore:

```bash
python main.py
```

### Control

* Step - calculate one iteration of the machine;
* Clear - clear the field;
* Random - fill in the field randomly;
* Simulate - calculate the state of the machine before the stop signal;
* *Click on the field* - on/off a cell.
* Log - on/off logging. Logs are saved to the 'default' folder (name editing is not supported yet) and are signed with their serial number relative to the beginning of the recording.

## Roadmap

* Quick change of the rules for the transition of the machine;
* Prettier interface 😆;
* Adding many known configurations;
* One-dimensional mode;
* More convenient work with logs.
