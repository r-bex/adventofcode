export const compareAnswers = (expected: number, actual: number): string => {
    const outcome = expected === actual ? "SUCCESS" : "OOPS"
    return `Expected ${expected}, you got ${actual} -> ${outcome}\n`
}

