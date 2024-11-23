miniSleep(): randomSleep(200,400);
bigSleep(): sleep(500);
save(): Ctrl + V;
copy(): Ctrl + C;

Main {
    Z + Ctrl : Tab;
    X + Ctrl : Tab + Shift;
    B + Ctrl : Tab, miniSleep(), copy(), Tab;
    A + Ctrl : Tab, Tab, save(), bigSleep(), Tab;
};