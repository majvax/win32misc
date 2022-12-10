from .system import OsVersionInfoEx


# wProductType flags
VER_NT_WORKSTATION = 0x0000001
VER_NT_DOMAIN_CONTROLLER = 0x0000002
VER_NT_SERVER = 0x0000003

# wSuiteMask flags
VER_SUITE_SMALLBUSINESS = (0x00000001, "small business")                          # 1
VER_SUITE_ENTERPRISE = (0x00000002, "enterprise")                                 # 2
VER_SUITE_BACKOFFICE = (0x00000004, "BackOffice")                                 # 4
VER_SUITE_TERMINAL = (0x00000010, "terminal")                                     # 16
VER_SUITE_SMALLBUSINESS_RESTRICTED = (0x00000020, "small business restricted")    # 32
VER_SUITE_EMBEDDEDNT = (0x00000040, "embedded nt")                                # 64
VER_SUITE_DATACENTER = (0x00000080, "datacenter")                                 # 128
VER_SUITE_SINGLEUSERTS = (0x00000100, "single use rts")                           # 256
VER_SUITE_PERSONAL = (0x00000200, "personal")                                     # 512
VER_SUITE_BLADE = (0x00000400, "blade")                                           # 1024
VER_SUITE_STORAGE_SERVER = (0x00002000, "storage server")                         # 8192
VER_SUITE_COMPUTE_SERVER = (0x00004000, "compute server")                         # 16384
VER_SUITE_WH_SERVER = (0x00008000, "home server")                                 # 32768
VER_SUITE_MULTIUSERTS = (0x00020000, "multi use rts")                             # 131072
VER_ALL = [
    VER_SUITE_SMALLBUSINESS,
    VER_SUITE_ENTERPRISE,
    VER_SUITE_BACKOFFICE,
    VER_SUITE_TERMINAL,
    VER_SUITE_SMALLBUSINESS_RESTRICTED,
    VER_SUITE_EMBEDDEDNT,
    VER_SUITE_DATACENTER,
    VER_SUITE_SINGLEUSERTS,
    VER_SUITE_PERSONAL,
    VER_SUITE_BLADE,
    VER_SUITE_STORAGE_SERVER,
    VER_SUITE_COMPUTE_SERVER,
    VER_SUITE_WH_SERVER,
    VER_SUITE_MULTIUSERTS
]


class Parser:
    @staticmethod
    def parse_os_version_info(obj: OsVersionInfoEx) -> dict[any]:
        if obj.dwMajorVersion == 10 and obj.dwMinorVersion == 0:
            if obj.wProductType == VER_NT_WORKSTATION:
                version = "Windows 10"
            else:
                version = "Windows Server 2016"
        elif obj.dwMajorVersion == 6 and obj.dwMinorVersion == 3:
            if obj.wProductType == VER_NT_WORKSTATION:
                version = "Windows 8.1"
            else:
                version = "Windows Server 2012 R2"
        elif obj.dwMajorVersion == 6 and obj.dwMinorVersion == 2:
            if obj.wProductType == VER_NT_WORKSTATION:
                version = "Windows 8"
            else:
                version = "Windows Server 2012"
        elif obj.dwMajorVersion == 6 and obj.dwMinorVersion == 1:
            if obj.wProductType == VER_NT_WORKSTATION:
                version = "Windows 7"
            else:
                version = "Windows Server 2008 R2"
        elif obj.dwMajorVersion == 6 and obj.dwMinorVersion == 0:
            if obj.wProductType == VER_NT_WORKSTATION:
                version = "Windows Vista"
            else:
                version = "Windows Server 2008"
        else:
            version = "unknown"

        flags = []
        for i in VER_ALL:
            if obj.wSuiteMask & i[0] == i[0]:
                flags.append(i[1])

        return {
            "version": version,
            "flags": flags
        }