import ctypes
from ctypes.wintypes import *
from ctypes import Structure, Union

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
SIZE_T = ctypes.c_size_t

if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_ulonglong):
    DWORD_PTR = ctypes.c_ulonglong
elif ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_ulong):
    DWORD_PTR = ctypes.c_ulong


class OsVersionInfoEx(Structure):
    """
    https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-osversioninfoexa
    :cvar dwOSVersionInfoSize: The size of this data structure
    :cvar dwMajorVersion: The major version number of the operating system
    :cvar dwMinorVersion: The minor version number of the operating system
    :cvar dwBuildNumber: The build number of the operating system
    :cvar dwPlatformId: The operating system platform
    :cvar szCSDVersion: indicates the latest Service Pack installed on the system
    :cvar wServicePackMajor: The major version number of the latest Service Pack installed on the system
    :cvar wServicePackMinor: The minor version number of the latest Service Pack installed on the system
    :cvar wSuiteMask: A bit mask that identifies the product suites available on the system
    :cvar wProductType: Any additional information about the system
    :cvar wReserved: Reserved for future use

    """
    dwOSVersionInfoSize = ...
    dwMajorVersion = ...
    dwMinorVersion = ...
    dwBuildNumber = ...
    dwPlatformId = ...
    szCSDVersion = ...
    wServicePackMajor = ...
    wServicePackMinor = ...
    wSuiteMask = ...
    wProductType = ...
    wReserved = ...

    _fields_ = (
        ('dwOSVersionInfoSize', DWORD),
        ('dwMajorVersion', DWORD),
        ('dwMinorVersion', DWORD),
        ('dwBuildNumber', DWORD),
        ('dwPlatformId', DWORD),
        ('szCSDVersion', WCHAR * 128),
        ('wServicePackMajor', WORD),
        ('wServicePackMinor', WORD),
        ('wSuiteMask', WORD),
        ('wProductType', BYTE),
        ('wReserved', BYTE)
    )

    def __init__(self, *args, **kwargs):
        super(OsVersionInfoEx, self).__init__(*args, **kwargs)
        self.dwOSVersionInfoSize = ctypes.sizeof(self)
        kernel32.GetVersionExW(ctypes.byref(self))


class SystemInfo(Structure):
    """
    https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/ns-sysinfoapi-system_info
    wProcessorArchitecture =
    """
    wProcessorArchitecture = ...
    wReserved = ...
    dwOemId = ...
    dwPageSize = ...
    lpMinimumApplicationAddress = ...
    lpMaximumApplicationAddress = ...
    dwActiveProcessorMask = ...
    dwNumberOfProcessors = ...
    dwProcessorType = ...
    dwAllocationGranularity = ...
    wProcessorLevel = ...
    wProcessorRevision = ...

    class _U(Union):
        class _S(Structure):
            _fields_ = (('wProcessorArchitecture', WORD),
                        ('wReserved', WORD))

        _fields_ = (('dwOemId', DWORD),
                    ('_s', _S))
        _anonymous_ = ('_s',)

    _fields_ = (('_u', _U),
                ('dwPageSize', DWORD),
                ('lpMinimumApplicationAddress', LPVOID),
                ('lpMaximumApplicationAddress', LPVOID),
                ('dwActiveProcessorMask',   DWORD_PTR),
                ('dwNumberOfProcessors',    DWORD),
                ('dwProcessorType',         DWORD),
                ('dwAllocationGranularity', DWORD),
                ('wProcessorLevel',    WORD),
                ('wProcessorRevision', WORD))
    _anonymous_ = ('_u',)

    def __init__(self, *args, **kwargs):
        super(SystemInfo, self).__init__(*args, **kwargs)
        self.dwPageSize = ctypes.sizeof(self)
        kernel32.GetSystemInfo(ctypes.byref(self))


class System:
    @staticmethod
    def bsod() -> None:
        """
        Make bsod with ntdll RaiseHardError
        :return: None
        """
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

    @staticmethod
    def get_windows_version() -> OsVersionInfoEx:
        """
        Use kernel32 to fetch windows information
        :return: OsVersionInfoEx (ctypes structure)
        """
        return OsVersionInfoEx()

    @staticmethod
    def get_system_info() -> SystemInfo:
        """
        Use kernel32 to fetch System info
        :return: SystemInfo (ctypes structure)
        """
        return SystemInfo()