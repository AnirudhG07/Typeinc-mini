# Typeinc-mini ![Static Badge](https://img.shields.io/badge/version-1.0.0-red) ![Static Badge](https://img.shields.io/badge/Typing_Test-CHECK_IT-blue)

Typeinc-mini, is a miniature version of Typeinc. Same features but less UI (you don't get the Typeinc-keyboard :<). This is made for those who do not have a big enough screen and see the message - <br>
`...If still the issue persists, too bad.`<br>

I certainly don't want people to not feel left-out due to their smaller screen.
_Please note:_ If your screen is still smaller in full screen mode than required, just buy a NEW-ONE bruh!!! 
<br>

<p align="center">
  <img src="https://media2.giphy.com/media/ule4vhcY1xEKQ/200w.gif?cid=6c09b952li35zp64s3iz0l9u482nurwqbtz49iv8hod95ox0&ep=v1_gifs_search&rid=200w.gif&ct=g" alt="Funny GIF">
</p>

# Previews/Screenshots

TO BE ADDED

# Features

Tyepinc provide some a next level typing test experience sitting on your terminal.

## 1. UI ![Static Badge](https://img.shields.io/badge/WATCH_ME-cyan)

This terminal software provides a user-friendly UI with easy interactions, unless the user purposefully messes with things.<br>
The UI is smaller than Typeinc, but has enough features to be able to play and test your skills! 
### What you have lesser here than Typeinc Original-
1. Keyboard UI
2. Display of top 5 scores, instead of top 10

## 2. Difficulty levels ![Static Badge](https://img.shields.io/badge/SO_HARD-red)

Typeinc has the widest range of difficulty level. You can actually put any number between -infinity to +infinity (keeping in mind computer limitations). Although they are categorized so any difficulty level more than 1000 will be based on LUCK, you may get an easy level 1000 + typing test, or really nasty cause it's absolutely random.<br>
Give your best shot with the difficulty levels and have fun typing!<br>

Here is a detailed summary of the Difficulty level division.

```markdown
- Level <= 0 : Super Easy (Regular) (SE)
- 0 < Level <= 2 : Easy (E)
- 2 < Level <= 4 : Normal (N)
- 4 < Level <= 6 : Hard (H)
- 6 < Level <= 9 : Super Hard (SH)
- 9 < Level <= 10 : Insane (I)
- 10 < Level < 20 : Super Insane (SI)
- 20 <= Level < 50: BRUH (X)
- 50 <= Level < 100: SUPER BRUHH (X2)
- 100 <= Level < 500: DAMNN BRUHHH!! (XX)
- 500 <= Level < 1000: U ROCK BRUHHH! (XX2)
- 1000 <= Level: GOD BRUH!!! (SXX)
```

All the difficulties levels are set by me, including the names. This test is a total 'BRUHHH'!<br>
For example-
<br>
<img width="940" alt="higher_diff_txt-img" src="https://github.com/AnirudhG07/Typeinc-mini/assets/146579014/72be858b-554a-44ce-830f-f12931233850">

This is an example of 50 word test-text at difficulty level = 20. (It may differ for you).

**Note:** If you want to have the regular typing test, please enter without mentioning any difficulty level since Default Difficulty is set to 0.

## 3. Grading and Typeinc score ![Static Badge](https://img.shields.io/badge/I_PASSED!-green)

The grading system differs for each difficulty level chosen and so is your score. The higher the difficulty level,
more the score you will obtain.<br>
Refer this tool to your friends, family and colleagues and compete with them!<br>

Please refer to <a href="https://github.com/AnirudhG07/Typeinc-mini/blob/main/docs/standards_grading.md"> Typeinc standards & grades </a> for more information regarding the grading and typeinc score.

## 4. Highscore Display Typeinc-mini ![Static Badge](https://img.shields.io/badge/RANKS!-yellow)

Save your result with your name for each test you take. You can also see the top 5 for each respective difficulty level by running the command - (Note: difficulty level is code for each difficulty level, like 'E', 'X2', etc.)

```bash
typeinc-mini -r <difficulty-level>
```

The topper is the one with higher `Typeinc Score`.<br>

Only 100 scores are saved in database which are ordered in desceding order w.r.t Typeinc score. Any score which is lesser than least of them, will not be saved. Try to beat that score to be able to save it, but this will push out the one who went to position 101, which will be deleted.

# How to Install

This is a cross-platform tool so it can be downloaded in your MacOS, Linux, Windows, etc.<br>
Follow the below guidelines to download the software

## ~> PIP Installation

1. You can install this package from PyPi by running the following command0

```bash
pip install typeinc-mini
```

If it gives any permission error, you can run using `sudo`(for Unix).

```bash
sudo pip install typeinc-mini
```

2. Now you are good to go! Play by simply running typeinc-mini by-

```bash
typeinc-mini # to play
typeinc-mini -h # to see help message
```

## ~> Homebrew Installation

This tool can also be installed using Homebrew(for MacOS only). You can install it by tapping my homebrew-tap repo and installing the tool.

```bash
brew tap AnirudhG07/AnirudhG07
brew install typeinc-mini
```

You can now run the tool by running `typeinc-mini -h` in your terminal. If you are facing issues, try running-

```bash
brew install AnirudhG07/AnirudhG07/Typeinc-mini # After tapping the repo
```

Make sure you have Homebrew installed in your MacOS and it is updated which can be done by running `brew update`.

## ~> Manual Installation

To install this tool manually, you can `git clone` this repository in your directory and run it, with the below command guidelines-

1. Clone the repository in your directory

```bash
cd /path/to/your/directory/
git clone https://github.com/AnirudhG07/Typeinc
```

2. Run `setup.py` to set the tool

```bash
python setup.py install #use python3 if required
# OR if it throws an error
pip install .
```

Now you should be able to run the tool using `typeinc-mini` in your terminal. Feel free to raise an issue if you face with any errors.

# Dependencies

This tool doesn't require a lot of dependencies but you need some basic requirements like

- python version >= 3.9
- curses library of python (Note: It will be automatically installed if you use the Pip Installation process)
- For Windows, windows-curses and setuptools are needed.

If you have any doubts/facing any issue, feel free to raise an issue.

# Documentation

Check out the <a href ="https://github.com/AnirudhG07/Typeinc-mini/tree/main/docs"> docs </a> in the repository for information regarding how to use, grading system, general queries, etc. Check out the help message in your terminal to check out the usage too ny running `typeinc-mini -h`.

# Contribution

It would be great to have contributions from anyone. To make Typeinc-mini more loved among everyone and make it better, feel free to raise an issue, discuss and make a PR.

### Contribution Guidelines

1. If you would like to raise any grading system based issues, please have a valid point using some mathematical figures to support your statements.
   Statements like `This is unfair`, `I don't like it`, etc. will not be attended to.
2. If you feel like adding a feature or fixing bug, please put up an issue before adding a PR.
   <br>
   You can always post your highest score and grade with wpm, accuracy and difficulty level chosen. I would love to make a global top list and add you there, if you are worthy!

## Note regarding Grading system ![Static Badge](https://img.shields.io/badge/Grading_Acknowldgement-purple)

- All the grading, difficulty level, typeinc score is devised by AnirudhG07(me). It has not been taken from anywhere
  and all the numbers set has been made from a fair system and intuition.
- I honestly would give more score to a person trying higher difficulty level cause they won't achieve a good wpm, unlike regular level where even 140-150 is possible.
- In no way I am also trying to equate the best possible (wpm, accuracy) of Regular Difficulty level to least possible (wpm, accuracy) of the most Difficult level.
  <br>
  Thanks!
