keypressDelay = 100;

typeOpera(): o,p,e,r,a,enter;
typeYoutube(): y,o,u,enter;
typeRickRoll(): r,i,c,k,space,r,o,l,l,enter;

Main {
    onColor(#145032, 1720, 720, 1000): typeOpera(),sleep(200), typeYoutube(),sleep(2500), loop(4,[Tab]), typeRickRoll(),sleep(1000), loop(23, [Tab]), enter;
    Alt + Shift: loop(3, [Alt + Tab, sleep(500)]);
};