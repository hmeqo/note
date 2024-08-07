# time.h

## 属性

| 函数 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| time | 返回时间从1970年到现在的秒数 | (time_t *) | timet_t |
| localtime | 返回本地时间的tm结构体 | (time_t *) | struct tm * |

| typedef | 描述 | 原型 |
| --- | --- | --- |
| time_t |  |  |

| struct | 描述 |
| --- | --- |
| [tm](#tm) | 包含时间信息的结构体 |

### tm

| 结构体成员 | 描述 | 类型 |
| --- | --- | --- |
| tm_sec | seconds after the minute - [0, 60] including leap second | int |
| tm_min | minutes after the hour - [0, 59] | int |
| tm_hour | hours since midnight - [0, 23] | int |
| tm_mday | day of the month - [1, 31] | int |
| tm_mon | months since January - [0, 11] | int |
| tm_year | years since 1900 | int |
| tm_wday | days since Sunday - [0, 6] | int |
| tm_yday | days since January 1 - [0, 365] | int |
| tm_isdst | daylight savings time flag | int |
