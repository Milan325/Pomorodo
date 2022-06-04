# Pomorodo 
This program is a study tool based on [Pomorodo technique](https://en.wikipedia.org/wiki/Pomodoro_Technique).

## Run
GUI has two buttons: "POČNI"(start) and "PONOVI" (reset). When start button is pressed, first of 5 cycles is initiated. One cycle consists of 25 minutes work timer and 5 minutes break timer. After completing one cycle, check mark is written on the screen. Instead of the fifth short break, long 30 minutes long break is initiated. One full session lasts for two and a half hours.

## Modules and functions
Modules used in this program are `math` and `tkinter` module. Tkinter module builds GUI of the program and runs as the program engine. 
Canvas object is used to display tomato.png image and countdown text. 
Countdown is done using `Screen.after()` method of `tkinter` module instead of `time` module. 
### `start_timer()`
This function takes global variables: `repetitions`, `LABEL`, `check` label object and `CHECK` constant for check mark string. It updates `LABEL` and `check` Label objects according to the number of repetitions.

### `reset_timer()`
This function resets cavnas text to "00:00" and variable `repetitions` to 0.

### `count_down(count)`
This function takes argument as int input that represents number of minutes to count, and, using `math.floor()` displays minutes left until the end of a cycle. `//` operand is not used, because it returns float. 
```python
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
```
This statement checks if the timer should continue ticking or a new cycle should be initiated.

## Program engine
Program engine runs between calling of `Tk()` object and `Tk.mainloop()` method. Program's logic is defined in functions that are called by pressing the buttons.

## Running the program
This game is intended to be run by Python IDE or other Python interpeter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
