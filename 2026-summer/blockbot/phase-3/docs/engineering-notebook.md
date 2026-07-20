# Phase 3 - Engineering Notebook

Notes: For wiring diagrams, please refer to wiring-diagram.md

## Thoughts

### My earlest code thoughts:
    I think it should be drive(ML_Power(ex: 1, 2, 3, -1, -2, -3), MR_Power). in total, all the files need to create a dashboard to send signals and then use those signals to power the pololu robot and there needs to be an estop button and a rule: signal timeout = estop. when I was younger, I played with the dash and dot robots from www.makewonder.com, and I liked their dashboard for mobile - a simulated joystick to control the robot. if you drag the joystick a little up, it would go slowly forward, if you drag it a lot up, it would make the robot go really fast. and you can drag it to the sides or even the corners without constraint such as it can only go up and down or left and right, but not to the corners. and I want the full range of motion. I would like to pair the key "e" for the estop because e stands for emergency. I think a good json format would be {"ML_Power"=-2, "MR_Power"=2, "estop"=0 or 1} or {"joystick_x"=-1024, "joystick_y"=209, "estop"=0 or 1} In addition, we need something to translate the joystick coordinates and I was wondering, should that be in app.py, or in index.html?

## Date
7/12/2026 (my birthday!)

## What I built
A web dashboard that includes a joystick that makes a robot move in real time, a header, an updating connection status indicator, 
motor status indicator, and a working emergency stop button with keyboard shortcuts for everything.

## How it works
This project works by having the web dashboard send json to app.py, which then forwards it to main.py, which uses motor.py's functions
 to do things based on the json string. then main.py sends json back to app.py, which again, forwards them to the web dashboard.

## Problems I hit and how I fixed them
### Problem 1:
**Expected:** Ground Wire to Solder on Passively
**What happened:** The wire shorted ground and battery 2's positive terminal and created a small flame and a very startled me.
**Cause:** I did not twist the multi core wire so it would be more stiff. And the batteries were in while I was soldering
**Fix:** twisting it and taking the batteries out
**Lesson:** don't leave the batteries in while soldering.

---

### Problem 2:
**Expected:** All Elements on the Dashboard to Update in Unison
**What happened:** only the joystick updated.
**Cause:** the dashboard's attention was on the joystick, not the drive status.
**Fix:** making the dashboard pay attention to everything.
**Lesson:** force the dashboard to pay attention everywhere.

---

### Problem 3:
**Expected:** Parked to Mean Parked and Drive to Mean Drive
**What happened:** I think you know it did not work already because otherwise this would not be a problem
**Cause:** there was a code error
**Fix:** make the motor status update only when I wanted it to
**Lesson:** don't let things change when it does not help you - be a dictator of your code.

---

## Most memorable moment
The robot finnaly moving on my table and clicking capslock and saying a couple of letters in capslock - its first act of rebellion! I was so proud.

## One thing that confused me at first but makes sense now
joystick math

## One thing I'm still fuzzy on
What happened in phase 3. (I am writing this a full week later of overnight summer camp.)

## Lessons learned
take out batteries before soldering, make dashboard pay attention everywhere, only change things when I want to.

## What's next
Phase 4 — sensors!