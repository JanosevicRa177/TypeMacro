writeName(trimLetters :boolean): D,U, {if(trimLetters):[S];else:[Š]}, A, N;
loopName(loopTimes: number) : loop(loopTimes, [writeName(true)]);
myMinLoop(loopCounter: number,loopCounter2: number): {if(loopCounter < loopCounter2):[loopName(5)];};

Main {
    Z + Ctrl : Tab;
    X + Ctrl : Tab + Shift;
    C + Ctrl : loop(4, [Tab]), Ctrl + A, loop(2, [Tab]);
    V + Ctrl : loop(4, [Tab]), Ctrl + B, loop(2, [Tab]);
    D + Ctrl : loopName(24);
    T + Ctrl : myMinLoop(7,6);
};