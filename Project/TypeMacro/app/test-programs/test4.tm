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