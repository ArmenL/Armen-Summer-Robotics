# Phase 3 - Engineering Notebook

Notes: For wiring diagrams, please refer to wiring-diagram.md

## Thoughts

### My earlest code thoughts:
    I think it should be drive(ML_Power(ex: 1, 2, 3, -1, -2, -3), MR_Power). in total, all the files need to create a dashboard to send signals and then use those signals to power the pololu robot and there needs to be an estop button and a rule: signal timeout = estop. when I was younger, I played with the dash and dot robots from www.makewonder.com, and I liked their dashboard for mobile - a simulated joystick to control the robot. if you drag the joystick a little up, it would go slowly forward, if you drag it a lot up, it would make the robot go really fast. and you can drag it to the sides or even the corners without constraint such as it can only go up and down or left and right, but not to the corners. and I want the full range of motion. I would like to pair the key "e" for the estop because e stands for emergency. I think a good json format would be {"ML_Power"=-2, "MR_Power"=2, "estop"=0 or 1} or {"joystick_x"=-1024, "joystick_y"=209, "estop"=0 or 1} In addition, we need something to translate the joystick coordinates and I was wondering, should that be in app.py, or in index.html?

