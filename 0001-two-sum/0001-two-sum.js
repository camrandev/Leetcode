/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/**
approach: we want to solve this in o(n) time complexity, so only one total loop.

we need to loop over the input array. for each value in the input array, we need to 
know what number plus the current number equals the target

as we loop, we compute what the complement is. If the complement exists in the map,
we return an array with the index of complement and the index of the number itself

if the complement does not exist, we store the current number + index as a key value pair in our map. the number is the key, the index is the value

declare pojo to use as a map, to store key value pairs

loop over the nums

for each num, find the complement (target - num)
check if the complement exists in the map
if it does, return the values stored at keys equal to the value and the complement in an array

if it does not, set a key value pair in the map, with the key being the current number, and the value being the index


 */

nums = [2,7,11,15]

const twoSum = function(nums, target) {
    let map = {} // {2:1, }
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i] //7
        let complement = target - num //2

        if (complement in map) {
            return [i, map[complement]]
        }
        map[num] = i
    }
  
    
};