/**
 * @param {string} s
 * @return {boolean}
 */

/**
use a stack -> do not implement fully in JS, just assume that this arr acts like one
    utilize the following methods:
    peek -> view top value
    pop -> remove + return top
    push -> add value to top


create set of opening
create set of closing

loop over the string
    if the current character is in closing, put the current char on the top of the stack
    if the current char is in closing
        if the top of the stack is the not the opening character, return false

return true 
*/

const opening = new Set(["{", "(", "["]);
const closing = new Set(["}", ")", "]"]);
const complete = new Set(["()", "{}", "[]"]);


function isValid (s) {
    let stack = [] // (

    for (let char of s) {
        if (opening.has(char)) {
            stack.unshift(char)
            continue;
        }
        if (closing.has(char)) {
            const val = stack.shift(); // (
            if (!complete.has(val + char)){
                console.log(val + char)
                return false;
            }
            
        }
    }
    if (stack.length > 0) return false
    return true
    
};