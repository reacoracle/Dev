# 找出两个时间区间的重叠区间

from collections import namedtuple

from datetime import datetime, time, date  # noqa

TimeInterval = namedtuple('TimeInterval', ['StartTime', 'EndTime'])

# time_interval_1 = TimeInterval(StartTime=time(
#     12, 45, 00), EndTime=time(14, 00, 00))
# time_interval_2 = TimeInterval(
#     StartTime=time(10, 30, 00), EndTime=time(12, 30, 00))

time_interval_1 = TimeInterval(
    StartTime=datetime(2022, 9, 9, 11, 45, 00),
    EndTime=datetime(2022, 9, 9, 14, 00, 00)
)
time_interval_2 = TimeInterval(
    StartTime=datetime(2022, 9, 9, 10, 30, 00),
    EndTime=datetime(2022, 9, 9, 12, 30, 00)
)
latest_start = max(time_interval_1.StartTime,
                   time_interval_2.StartTime)
earliest_end = min(time_interval_1.EndTime, time_interval_2.EndTime)

print(f'Overlapping time intervals: {latest_start}~{earliest_end}')
print(f'Overlapping time intervals: {earliest_end - latest_start}')

# 计算两个时间区间的总时间
i1 = [datetime(2022, 9, 9, 11, 45, 00), datetime(2022, 9, 9, 14, 00, 00)]
i2 = [datetime(2022, 9, 9, 10, 30, 00), datetime(2022, 9, 9, 12, 30, 00)]


def interval(i1, i2):
    minstart, minend = [min(*e) for e in zip(i1, i2)]
    maxstart, maxend = [max(*e) for e in zip(i1, i2)]
    print(minstart, minend)
    print(maxstart, maxend)

    if minend < maxstart:  # no overlap
        return minend - minstart + maxend - maxstart
    else:  # overlap
        return maxend - minstart


time_interval = interval(i1, i2)
print(time_interval)

# 区间等分
from decimal import Decimal

counter = 0
step = Decimal((119 - 21) / 6)
starts = 21
while counter < 6:
    lower_bound = starts + counter * step
    if counter < 5:
        upper_bound = lower_bound + step
    else:
        upper_bound = 119

    counter += 1
    print('lower_bound: ', lower_bound, 'upper_bound: ', upper_bound)

# 翻转列表(或者使用内置reversed方法)
list_1 = [date(2017, 3, 22), date(2017, 3, 24), date(2018, 3, 24), date(2019, 3, 24), date(2020, 3, 24),
          date(2021, 3, 24)]
list_1.reverse()

# 计算时间差(s)
start_time = '2019-07-28 12:30:43.456'
end_time = '2019-07-28 12:30:44.134'


def get_second(start_time_, end_time_):
    start_time = datetime.strptime(start_time_, "%Y-%m-%d %H:%M:%S.%f")
    end_time = datetime.strptime(end_time_, "%Y-%m-%d %H:%M:%S.%f")
    return (end_time - start_time).total_seconds()


print(get_second(start_time, end_time))
