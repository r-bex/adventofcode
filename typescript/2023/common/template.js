"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const file_1 = require("../common/file");
const utils_1 = require("../common/utils");
const currentDay = (0, utils_1.getDayFromFilename)(__filename);
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const part1 = (lines) => {
    // implement part 1 here
    return 0;
};
// put the example solution here
const exampleInputPt1 = (0, file_1.getExampleInput)(currentDay, 1);
const EXAMPLE_SOLUTION_PT1 = -1; // PUT EXAMPLE ANSWER HERE
console.log(`EXAMPLE PT 1`);
console.log((0, utils_1.compareAnswers)(EXAMPLE_SOLUTION_PT1, part1(exampleInputPt1)));
// read the puzzle input and run part 1
const input = (0, file_1.getChallengeInput)(currentDay);
console.log('PART 1');
console.log(part1(input));
console.log();
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const part2 = (lines) => {
    // implement part 2 here
    return 0;
};
// read the example input for part 2 and check answer
const exampleInputPt2 = (0, file_1.getExampleInput)(currentDay, 2);
const EXAMPLE_SOLUTION_PT2 = -1; // PUT EXAMPLE ANSWER HERE
console.log(`EXAMPLE PT 2`);
console.log((0, utils_1.compareAnswers)(EXAMPLE_SOLUTION_PT2, part2(exampleInputPt2)));
// run part2
console.log('PART 2');
console.log(part2(input));
