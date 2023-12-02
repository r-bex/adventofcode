## Usage

To create a blank folder for a new day, run `DAY=x npm run new` and you will get a new `dayX` folder containing empty .txt files for you to copy and paste the puzzle input into, and a template main.ts to start from. X should be 1, 2, 3 etc...

To run your solution, run `DAY=X npm run challenge`. This will compile ts -> js and run the js of the solution to that day's challenge.

Both of these are currently hardcoded to 2023.

## TODO

* stick compiled js files somewhere out of sight
* automatically download puzzle input?