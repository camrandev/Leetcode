/**
 * @param {string} s
 * @return {boolean}
 */

 /**
 input: any valid string, contains spaces, punctionation
 output: boolean, indicating if stripped string is a palindrome
 edge cases: will receive valid input, but need to strip the string
    input of 1

 set a guard for a single character string
    test if the character is alphabetical, if so return true

 strip the string
    set a variable to an empty string
    loop over the input string
    if the current character is alpha -> concat it to the new string


 perform the check
    set p1 to the start, set p2 to the end
    if they are equal, increment p1, decrement p2, repeat the check
    do this until p1 is is head of p2


  */

/** check if a single is*/  
var isAlpha = function(char) {
    char = char.toLowerCase()
    return (char >= "a" && char <= "z" && char) ? true : false
}

var isDigit = function(char) {
    char = char.toLowerCase()
    return (char >= "0" && char <= "9" && char) ? true : false
}

var stripString = function(s) {
    let out = ""
    for (const char of s) {
        if (isAlpha(char) || isDigit(char)) {
            out += char.toLowerCase()
        }
    }
    return out
}

var isPalindrome = function(s) {
    if (s.length === 1) return true;

    s = stripString(s);

    let p1 = 0;
    let p2 = s.length - 1;

    while (p1 <= p2) {
        if (s[p1] !== s[p2] ) {
            return false
        }
        p1++
        p2--
    }

    return true
    
};