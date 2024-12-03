/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * Two sum problem 
 */
var twoSum = function(nums, target) {
    // nums - array of integers
    // target - integer 
    // return - indices of 2 numbers such that they add up to the target 

    var length = nums.length; // get total length 

    // Iterate through each element
    for (let i = 0; i < length; i++) {
        var k = nums[i]; // Current number
        
        // Check pairs with the next elements
        for (let j = i + 1; j < length; j++) {
            var l = nums[j]; // Next number
            
            // Check if they sum to the target
            if (k + l === target) {
                return [i, j]; // Return indices if found
            }
        }
    }

    // If no solution is found, return an empty array
    return [];
};

// Example usage:
const nums = [2, 7, 11, 15];
const target = 9;
const result = twoSum(nums, target);
console.log(result); // Output: [0, 1]