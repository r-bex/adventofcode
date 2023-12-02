import { getExampleInput, getChallengeInput } from "../common/file"
import { compareAnswers } from "../common/utils"

const NumberMap: Record<string, string> = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

// the union of the keys above and the digit matcher
const DigitRegex: RegExp = new RegExp([...Object.keys(NumberMap), "\\d"].join("|"), "g")

const combineFirstLastStringDigits = (inputLine: string, regex: RegExp): number => {
    if (inputLine.match(regex)) {
        // overlapping matches e.g. fiveeight will not be extracted
        // separately using matchall, have to either match one by one
        // and reset match index, or use lookaheads...
        var matches = [], found;
        while (found = regex.exec(inputLine)) {
            matches.push(found[0]);
            regex.lastIndex = found.index + 1;
        }
        const digits = matches.map((dm => dm in NumberMap ? NumberMap[dm] : dm))
        return parseInt(`${digits[0]}${digits[digits.length - 1]}`)
    }
    return 0
}

const part1 = (lines: string[]): number => {
    const results = lines.map((line) => combineFirstLastStringDigits(line, /\d/g))
    return results.reduce((a, b) => a + b)
}

const part2 = (lines: string[]): number => {
    const results = lines.map((line) => combineFirstLastStringDigits(line, DigitRegex))
    return results.reduce((a, b) => a + b)
}

// read the example input
const exampleInput = getExampleInput(1, 1)
console.log(`EXAMPLE`)
console.log(compareAnswers(142, part1(exampleInput)))

// //read the puzzle input
const input = getChallengeInput(1)
console.log("PART 1")
console.log(part1(input))
console.log()

// read the example input for part 2
const exampleInput2 = getExampleInput(1, 2)
console.log(`EXAMPLE2`)
console.log(compareAnswers(281, part2(exampleInput2)))

// do part2
console.log("PART 2")
console.log(part2(input))