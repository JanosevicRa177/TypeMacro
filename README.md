# TypeMacro
Software and master thesis that will follow development and research of macro writting DSL development using TextX

## Project theme
Project will implement DSL from domain of writting macros for keyboards on computers. Idea is to create a complex Macro DSL which will enable automation of the wide range of user tasks. Developer can write any type of macro for specific domain and doman expert can use that group of macros to enhance productivity. 

Also idea is to enable and research multi point macro control. Which means we can add macros to one computer and we will have admin computer which can control one or more connected computers.
On the smallest scale DSL will enable user to create wide variety of specific keyboard macros. On the large scale, it will enable user to create multiple macro profiles on multiple computers for single user - multiple computer interaction.

Because user can write macros in any way possible it is possible for user to make his computer unusable, for that use case there is safe Command that is stopping the executing of all commands: Alt+F8. This command cannot be used in macros.

## DSL specification

### Main program
Main program will consists of all the Macros that will be active on computer, it will support combination of key presses which will then translate to other key presses, in more complex scenarios macros can support more complex features as loop, sleep, randomSleep. Also there will be functions and function calls.

Every part of the macro sequence is single command which should be registered as single input(Similar as pressing ctrl and V at the same time).

There cannot be macro calls with same key presses.

Also user can specify delay between single keypress combination, default is 50ms, and he can specify color offset with will be calculated between all rgb colors, default is 10 which means red component +-10, green component +-10, blue component +-10

```
keypressDelay = 60;
colorOffset = 15;
Main {
    Z + Ctrl : Tab ;
    X + Ctrl : Tab + Shift;
    C + Ctrl : Tab, Ctrl + C, Tab;
    V + Ctrl : Tab, Tab, Ctrl + V, Tab, Tab;
};
```

### Sleep
For sleep to work we will add it as command and it will support passing milliseconds that will pause execution of the macro, after timer rans out, macro continues executing as intended.

```
Main {
    Z + Ctrl : Tab;
    X + Ctrl : Tab + Shift;
    C + Ctrl : Tab, sleep(250), Ctrl + C, Tab;
    V + Ctrl : Tab, Tab, Ctrl + V, sleep(1000), Tab;
};
```

### randomSleep
Random sleep is a little bit different than regular sleep, with this we pass minimum and maximum value we want command to sleep, program will the pick a random number that it will sleep from the desired spectrum

```
Main {
    Z + Ctrl : Tab;
    X + Ctrl : Tab + Shift;
    C + Ctrl : Tab, randomSleep(200,400), Ctrl + C, Tab;
    V + Ctrl : Tab, Tab, Ctrl + V, sleep(500), Tab;
};
```

### macro loop
Loop function in commands will enable user to loop trough commands or sequence of commands. Also what was not mentioned it is possible to add right and left mouse click as commands.

```
Main {
    Z + Ctrl : Tab ;
    X + Ctrl : Tab + Shift;
    C + Ctrl : loop(4, [Tab]), Ctrl + C, loop(2, [Tab]);
    V + Ctrl : loop(4, [Tab]), Ctrl + V, loop(2, [Tab]);
    A + Ctrl : loop(2, [leftClick]), randomSleep(200,400), loop(2, [shift + Q, Shift + W, Shift + E]);
};
```

### macro function
Functions similar to programming are sequence of commands that can be used instead of rewritting big parts of macros.

```
miniSleep(): randomSleep(200,400);
bigSleep(): sleep(500);
save(): Ctrl + V;
copy(): Ctrl + C;

Main {
    Z + Ctrl : Tab;
    X + Ctrl : Tab + Shift;
    C + Ctrl : Tab, miniSleep(), copy(), Tab;
    V + Ctrl : Tab, Tab, save(), bigSleep(), Tab;
};
```

Every part of the macro sequence is single command which should be registered as single input(Similar as pressing ctrl and V at the same time).

```
  Main {
      Z + ctrl : Tab ;
      X + ctrl : Tab + shift;
      C + ctrl : Tab, Ctrl + C, Tab;
      V + ctrl : Tab, Tab, Ctrl + V, Tab, Tab;
  };
```

### if statements
Classic if statement, if passed parameter or value is true in if, it will execute if part sequence, one of the examples whos strong use of if and loop statements. Currently it supports just if and else, no else if cases. If no else case is passed, nothing will be executed.


if example:
```
writeName(trimLetters :boolean): D,U, {if(trimLetters):[S];else:[Š]}, A, N;
loopName(loopTimes: number) : loop(loopTimes, [writeName(true)]);
myMinLoop(loopCounter: number): {if(loopCounter < 5):[loopName(5)];};

Main {
    Z + Ctrl : Tab;
    X + Ctrl : Tab + Shift;
    C + Ctrl : loop(4, [Tab]), Ctrl + C, loop(2, [Tab]);
    V + Ctrl : loop(4, [Tab]), Ctrl + V, loop(2, [Tab]);
    D + Ctrl : loopName(24);
    T + Ctrl : myMinLoop(3);
};
```

### auto macros
For example, we want to execute macro when color of single pixel on the screen is changed, we specify color we want  to execute code, with or without offset and macro fill execute just when pixel takes that color.
```
heal(): 1;

Main {
    Z + ctrl : Tab;
    X + ctrl : Tab + shift;
    onColor(#FF0000,  1720, 720) : heal();
};
```
