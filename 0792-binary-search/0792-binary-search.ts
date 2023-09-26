//pointers to track the first and last item of the array
//want to search until we have 0 or 1 items left

//while the left pointer is less than or equal to the right pointer, run the following:
    //calculate the midpoint, rounding down
    //if the target value is greater than the midpoint
        //move the left pointer to the mid + 1
    //if the target is less than the midpoint
        //move the right pointer to mid - 1
    //if equal, return the midpoint

    //return negative 1 if the above completes without an early return

function search(nums: number[], target: number): number {
    let l: number = 0;
    let r: number = nums.length - 1

    while (l <= r) {
        let m:number = Math.floor((l + r) / 2 )

        if (target > nums[m]) {
            l = m + 1
        } else if (target < nums[m]) {
            r = m - 1
        } else {
            return m
        }
    }
    
    return -1

};