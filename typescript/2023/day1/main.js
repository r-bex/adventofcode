"use strict";
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
var file_1 = require("../common/file");
var utils_1 = require("../common/utils");
var NumberMap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
};
// the union of the keys above and the digit matcher
var DigitRegex = new RegExp(__spreadArray(__spreadArray([], __read(Object.keys(NumberMap)), false), ["\\d"], false).join("|"), "g");
var combineFirstLastStringDigits = function (inputLine, regex) {
    if (inputLine.match(regex)) {
        // overlapping matches e.g. fiveeight will not be extracted
        // separately using matchall, have to either match one by one
        // and reset match index, or use lookaheads...
        var matches = [], found;
        while (found = regex.exec(inputLine)) {
            matches.push(found[0]);
            regex.lastIndex = found.index + 1;
        }
        var digits = matches.map((function (dm) { return dm in NumberMap ? NumberMap[dm] : dm; }));
        return parseInt("".concat(digits[0]).concat(digits[digits.length - 1]));
    }
    return 0;
};
var part1 = function (lines) {
    var results = lines.map(function (line) { return combineFirstLastStringDigits(line, /\d/g); });
    return results.reduce(function (a, b) { return a + b; });
};
var part2 = function (lines) {
    var results = lines.map(function (line) { return combineFirstLastStringDigits(line, DigitRegex); });
    return results.reduce(function (a, b) { return a + b; });
};
// read the example input
var exampleInput = (0, file_1.getExampleInput)(1, 1);
console.log("EXAMPLE");
console.log((0, utils_1.compareAnswers)(142, part1(exampleInput)));
// //read the puzzle input
var input = (0, file_1.getChallengeInput)(1);
console.log("PART 1");
console.log(part1(input));
console.log();
// read the example input for part 2
var exampleInput2 = (0, file_1.getExampleInput)(1, 2);
console.log("EXAMPLE2");
console.log((0, utils_1.compareAnswers)(281, part2(exampleInput2)));
// do part2
console.log("PART 2");
console.log(part2(input));
