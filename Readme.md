# ⬛⬜ Cellular automata

[![CodeFactor](https://www.codefactor.io/repository/github/d0rj/cellularautomata/badge)](https://www.codefactor.io/repository/github/d0rj/cellularautomata)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/617d2ea267ba46d2ac6201398c5cbe06)](https://www.codacy.com/gh/d0rj/CellularAutomata/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=d0rj/CellularAutomata&amp;utm_campaign=Badge_Grade)
[![DeepSource](https://deepsource.io/gh/d0rj/CellularAutomata.svg/?label=active+issues&show_trend=true&token=C_6GALLxta4c7iTqg5bl8y8p)](https://deepsource.io/gh/d0rj/CellularAutomata/?ref=repository-badge)

## Description

A simple application for studying cellular automata, in particular "The game of life". Currently, only it is supported.

The field is an unfolding of the torus.

## Environment

- numpy
- tkinter

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

- Step - calculate one iteration of the machine;
- Clear - clear the field;
- Random - fill in the field randomly;
- Simulate - calculate the state of the machine before the stop signal;
- *Click on the field* - on/off a cell.
- Log - on/off logging. Logs are saved to the 'default' folder (name editing is not supported yet) and are signed withtheir serial number relative to the beginning of the recording.
- Configure - change birth/survive rules for automata to entered.

## Serialization

The map configuration is saved according to the following template:

```python
x y # width and height of map in cells
0 213 4 0 ... 0 0 # Each line of the field is encoded with a binary number, these numbers are written sequentially into one line. There should be y numbers in total
```

Examples of serialized maps you can see [there](https://github.com/d0rj/CellularAutomata/tree/master/map_configs).

## Roadmap

- [x] Quick change of the rules for the transition of the machine;
- [ ] Prettier interface 😆;
- [x] Adding many known configurations;
- [ ] One-dimensional mode;
- [ ] More convenient work with logs.
