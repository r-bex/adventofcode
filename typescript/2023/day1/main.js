"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const file_1 = require("../common/file");
const utils_1 = require("../common/utils");
const NumberMap = {
    one: '1',
    two: '2',
    three: '3',
    four: '4',
    five: '5',
    six: '6',
    seven: '7',
    eight: '8',
    nine: '9',
};
// the union of the keys above and the digit matcher
const DigitRegex = new RegExp([...Object.keys(NumberMap), '\\d'].join('|'), 'g');
const combineFirstLastStringDigits = (inputLine, regex) => {
    if (inputLine.match(regex)) {
        // overlapping matches e.g. fiveeight will not be extracted
        // separately using matchall, have to either match one by one
        // and reset match index, or use lookaheads...
        const matches = [];
        let found = null;
        while ((found = regex.exec(inputLine))) {
            matches.push(found[0]);
            regex.lastIndex = found.index + 1;
        }
        const digits = matches.map((dm) => (dm in NumberMap ? NumberMap[dm] : dm));
        return parseInt(`${digits[0]}${digits[digits.length - 1]}`);
    }
    return 0;
};
const part1 = (lines) => {
    const results = lines.map((line) => combineFirstLastStringDigits(line, /\d/g));
    return results.reduce((a, b) => a + b);
};
const part2 = (lines) => {
    const results = lines.map((line) => combineFirstLastStringDigits(line, DigitRegex));
    return results.reduce((a, b) => a + b);
};
// read the example input
const exampleInput = (0, file_1.getExampleInput)(1, 1);
console.log(`EXAMPLE`);
console.log((0, utils_1.compareAnswers)(142, part1(exampleInput)));
// //read the puzzle input
const input = (0, file_1.getChallengeInput)(1);
console.log('PART 1');
console.log(part1(input));
console.log();
// read the example input for part 2
const exampleInput2 = (0, file_1.getExampleInput)(1, 2);
console.log(`EXAMPLE2`);
console.log((0, utils_1.compareAnswers)(281, part2(exampleInput2)));
// do part2
console.log('PART 2');
console.log(part2(input));
