Main {
    Z + Ctrl : Tab ;
    X + Ctrl : Tab + Shift;
    C + Ctrl : loop(4, [Tab]), Ctrl + A, loop(2, [Tab]);
    V + Ctrl : loop(4, [Tab]), Ctrl + A, loop(2, [Tab]);
    A + Ctrl : randomSleep(200,400), loop(2, [shift + Q, Shift + W, Shift + E]);
};