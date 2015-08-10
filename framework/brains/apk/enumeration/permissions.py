from framework.brains.apk.enumeration.api.mappings import APIPermissionMappings
from datetime import datetime
from blessings import Terminal
t = Terminal()


class Permissions(object):

    def __init__(self, apk, apks):

        super(Permissions, self).__init__()
        self.apk = apk
        self.apks = apks

    def run_list_permissions(self):

        """
        List the permissions within the target APK
        """

        permissions = self.apk.get_permissions()

        for permission in permissions:
            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow("Permission: ") +
                  permission)

    def run_map_permissions(self):

        """
        Map permissions within the target APK to API calls
        """

        mappings = APIPermissionMappings(self.apk, self.apks)
        mappings.run_find_mapping()
