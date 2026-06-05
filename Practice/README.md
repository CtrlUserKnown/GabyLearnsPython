# Practice Runner

This is a self-checking practice system. You write your code directly in the
Mod files, run the checker, and it tells you what passed and what didn't.


## Folder Structure

Make sure your folder looks like this before you start:

     GabyLearnsPython/
    ├── pylings
    └── Practice/
        ├── Mod1.py
        ├── Mod2.py
        ├── Mod3.py
        ├── Mod4.py
        ├── Mod5.py
        ├── Mod6.py
        ├── Mod7.py
        └── Mod8.py

`pylings` needs to be one level above the Practice folder. If the structure is off,
the runner won't find your files.


## Commands

Run these from anywhere (after setup):

| Command | What it does |
|---|---|
| `pylings list` | List all exercises with ✔ Done / ✘ Not Done status |
| `pylings next` | Run the first incomplete exercise |
| `pylings 3` | Run a specific exercise (replace 3 with any number 1-8) |
| `pylings watch` | Watch the next incomplete exercise — tests re-run on every save |
| `pylings watch 3` | Watch a specific exercise |

## How It Works (Rustlings-style)

1. Each Mod file starts with **`# I AM NOT DONE`** — this means the exercise is still waiting to be completed.

2. Open any Mod file (e.g. `Practice/Mod1.py`), read the comments, and replace the `None` placeholders with your code.

3. Run the checker whenever you want:

        pylings next

   or

        pylings 1

4. The output shows you what passed and what didn't:

        ✔  cityName is a non-empty string
        ✘  temperature is 98.6
           hint: temperature = 98.6

    At the bottom you'll see a progress bar:

        ████████████░░░░░░░░░░░░░░░░░░  8/13 passed

5. **When all checks pass**, the runner will tell you to remove `# I AM NOT DONE` from the file. Do that to mark the exercise as complete.

6. Use `pylings watch` for the full Rustlings experience — it watches your file and re-runs tests automatically every time you save.

## Tips

- Run `pylings list` anytime to see your overall progress.
- You don't have to finish all problems before running the checker. Run it as often as you want.
- If your file has a syntax error, the runner will print the error and stop. Fix it first.
- Variable names must match exactly what the problem asks for — the checker looks for specific names.
- Some checks are flexible (e.g. `testScore` can be any number — the checker grades it based on what you pick).

## Module Topics

    Module 1 — Variables, Math, and Functions
    Module 2 — Data Types and Functions
    Module 3 — Operators and Conditionals
    Module 4 — Scopes
    Module 5 — Loops
    Module 6 — Error Handling
    Module 7 — Classes and Inheritance
    Module 8 — Common Methods
