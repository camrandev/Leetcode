#we will know a number is happy if we are able to get it to equal one, before we repeat a number that has been reached

#create helper function to handle the actual digit processing

#set fast and slow "pointers"
#init the slow pointer to the number
#init the fast pointer to the result of calling helper on the number

#process the number until one of the following conditions is met
    #fast number is equal to one
    #fast number is equal to slow
    #if EITHER of the above is true, stop processing

    #check if fast equal slow, and return the boolean


class Solution:
    def isHappy(self, n: int) -> bool:

        def _sum_digits(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                number = number // 10
                total_sum += digit ** 2
            return total_sum
        
        slow = n
        fast = _sum_digits(n)

        while fast != 1 and fast != slow:
            fast = _sum_digits(_sum_digits(fast))
            slow = _sum_digits(slow)
        
        return fast == 1


        