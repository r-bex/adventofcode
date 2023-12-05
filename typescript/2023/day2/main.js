"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const file_1 = require("../common/file");
const utils_1 = require("../common/utils");
const _ = require("lodash");
const currentDay = (0, utils_1.getDayFromFilename)(__filename);
const MAXIMUMS = {
    red: 12,
    green: 13,
    blue: 14,
};
const gameParser = (line) => {
    try {
        const [head, tail] = line.split(': ');
        const drawsRaw = tail.split('; ');
        const gameIndex = parseInt(head.split(' ')[1]);
        const draws = drawsRaw.map((draw) => {
            const counts = {};
            draw.split(', ').forEach((numBalls) => {
                const [number, colour] = numBalls.split(' ');
                counts[colour] = parseInt(number);
            });
            return counts;
        });
        return {
            index: gameIndex,
            draws: draws,
        };
    }
    catch {
        console.warn(`Couldn't parse game from line ${line}`);
        return null;
    }
};
const part1 = (lines) => {
    const games = lines.map((line) => gameParser(line)).filter((game) => game);
    const validGames = games.filter(({ draws }) => {
        const coloursValid = ['red', 'green', 'blue'].map((colour) => draws.every((drawCounts) => colour in drawCounts ? drawCounts[colour] <= MAXIMUMS[colour] : true));
        return coloursValid.every((bool) => bool);
    });
    return _.sum(validGames.map((game) => game.index));
};
// put the example solution here
const exampleInputPt1 = (0, file_1.getExampleInput)(currentDay, 1);
const EXAMPLE_SOLUTION_PT1 = 8;
console.log(`EXAMPLE PT 1`);
console.log((0, utils_1.compareAnswers)(EXAMPLE_SOLUTION_PT1, part1(exampleInputPt1)));
// read the puzzle input and run part 1
const input = (0, file_1.getChallengeInput)(currentDay);
console.log('PART 1');
console.log(part1(input));
console.log();
const part2 = (lines) => {
    const games = lines.map((line) => gameParser(line)).filter((game) => game);
    const powers = games.map((game) => {
        return ['red', 'green', 'blue']
            .map((colour) => _.max(game.draws.map((drawCounts) => drawCounts[colour])))
            .reduce((a, b) => a * b);
    });
    return _.sum(powers);
};
// read the example input for part 2 and check answer
const exampleInputPt2 = (0, file_1.getExampleInput)(currentDay, 2);
const EXAMPLE_SOLUTION_PT2 = 2286;
console.log(`EXAMPLE PT 2`);
console.log((0, utils_1.compareAnswers)(EXAMPLE_SOLUTION_PT2, part2(exampleInputPt2)));
// run part2
console.log('PART 2');
console.log(part2(input));
