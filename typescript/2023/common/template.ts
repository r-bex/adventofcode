import { getExampleInput, getChallengeInput } from '../common/file'
import { compareAnswers, getDayFromFilename } from '../common/utils'

const currentDay = getDayFromFilename(__filename)

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const part1 = (lines: string[]): number => {
  // implement part 1 here
  return 0
}

// put the example solution here
const exampleInputPt1: string[] = getExampleInput(currentDay, 1)
const EXAMPLE_SOLUTION_PT1: number = -1 // PUT EXAMPLE ANSWER HERE
console.log(`EXAMPLE PT 1`)
console.log(compareAnswers(EXAMPLE_SOLUTION_PT1, part1(exampleInputPt1)))

// read the puzzle input and run part 1
const input: string[] = getChallengeInput(currentDay)
console.log('PART 1')
console.log(part1(input))
console.log()

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const part2 = (lines: string[]): number => {
  // implement part 2 here
  return 0
}

// read the example input for part 2 and check answer
const exampleInputPt2: string[] = getExampleInput(currentDay, 2)
const EXAMPLE_SOLUTION_PT2: number = -1 // PUT EXAMPLE ANSWER HERE
console.log(`EXAMPLE PT 2`)
console.log(compareAnswers(EXAMPLE_SOLUTION_PT2, part2(exampleInputPt2)))

// run part2
console.log('PART 2')
console.log(part2(input))
