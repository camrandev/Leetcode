/**
 * @param {string} s
 * @return {number}
 */


const numerals = {
I:             1,
IV: 4,
V:             5,
IX:9,
X:             10,
XL: 40,
L:             50,
XC: 90,
C:             100,
CD:400,
D:             500,
CM: 900,
M:             1000,
}
/**
save the roman numeral values in an object for a reference
initialize a sum variable to 0

loop over the input string

for each character, access the appropriate roman numeral value
handle the cases of i, x, and c
    if current + next in reference
    add reference value to total
    increment the counter

*/

var romanToInt = function(s) {
    let sum = 0;

    for(let i = 0; i < s.length; i++) {
        let combination = s[i]+s[i+1]
        if (numerals[combination]) {
            sum += numerals[combination]
            i++
            continue
        }
        sum += numerals[s[i]]
    }
    return sum

    
};