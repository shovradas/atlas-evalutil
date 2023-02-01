from enum import Enum


class MemoryUnit(Enum):
    BYTE = "B"
    KILOBYTE = "KB"
    MEGABYTE = "MB"
    GIGABYTE = "GB"
    TERABYTE = "TB"


class TimeUnit(Enum):
    SECOND = "s"
    MINUTE = "m"
    HOUR = "h"


def memory_factor(unit: MemoryUnit):
    return {
        MemoryUnit.BYTE: 1,
        MemoryUnit.KILOBYTE: 1024,
        MemoryUnit.MEGABYTE: 1_048_576,         # 1024**2
        MemoryUnit.GIGABYTE: 1_073_741_824,     # 1024**3
        MemoryUnit.TERABYTE: 1_099_511_627_776  # 1024**4
    }[unit]


def time_factor(unit: TimeUnit):
    return {
        TimeUnit.SECOND: 1,
        TimeUnit.MINUTE: 60,
        TimeUnit.HOUR: 3600                     # 60**2
    }[unit]