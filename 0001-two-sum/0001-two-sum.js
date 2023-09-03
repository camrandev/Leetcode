/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //set p1 to 0
    let p1 = 0
    //set p2 to 1
    let p2 = 1
    while (p1 < nums.length - 1) {
        if (nums[p1] + nums[p2] === target) return [p1, p2];
        p2++
        if (p2 === nums.length) {
            p1++
            p2 = p1 + 1
        }
    }

};