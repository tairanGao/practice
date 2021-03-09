class Solution:

    def is_valid_date(self, year, month, day):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day_count_for_month[2] = 29
        return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]

    def palindromeDates(self, year):
        starting = year // 100 * 100
        count = 0
        days = []
        for i in range(100):
            year = starting + i
            # check 8 digit
            curr_date_8 = str(year)[::-1]+ str(year)
            month = int(curr_date_8[:2])
            day = int(curr_date_8[2:4])
            if self.is_valid_date(year, month, day):
                count += 1
                days.append(curr_date_8)

            # check 7 digit
            curr_date_7 = str(year)[1:][::-1] + str(year)
            month = int(curr_date_7[:2])
            day = int(curr_date_7[2:3])
            if self.is_valid_date(year, month, day):
                count += 1
                days.append(curr_date_7)
                continue

            month = int(curr_date_7[:1])
            day = int(curr_date_7[1:3])
            if self.is_valid_date(year, month, day):
                count += 1
                days.append(curr_date_7)

        print(days)
        return count


sol = Solution()
print(sol.palindromeDates(1909))


