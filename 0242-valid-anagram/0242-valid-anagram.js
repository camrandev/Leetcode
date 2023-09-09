/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

/**
input: two strings, S and T
output: boolean, true if valid anagram, false otherwise

no edgecases here
use a gaurd, check if length is not equal -> return false

create frequency tables of both s and t

for each key: value pair in s, check if that key value pair is the
same in t
if not, return false

if the above operation is able to complete witbout a return, return true
*/

function makeFreqTable(str) {
    let out = {}

    for (const char of str) {
        out[char] = (out[char] || 0) + 1;
    }

    return out
}

const isAnagram = function(s, t) {
    if (s.length != t.length) return false
    
    const sMap = makeFreqTable(s)
    const tMap = makeFreqTable(t)

    for (const key in sMap) {
        if (sMap[key] != tMap[key]) return false
    }

    return true

    
};