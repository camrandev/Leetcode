/**
 * @param {number[]} nums
 * @return {boolean}
 */

/**

freq table problem

create a freq table

iterate over nums
for each num in nums

if the num is already in nums, return false, otherwise map[nums] = true

if the above completes, return true

*/

var containsDuplicate = function(nums) {
    let map = {}

    for (const num of nums) {
        if (num in map) return true
        map[num] = true
    }
    
    return false
};