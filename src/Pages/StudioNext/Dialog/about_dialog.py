from src.Pages.Common.dialog import Dialog


class AboutDialog(Dialog):
    """

    """

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on May.6th, 2024
    @property
    def release_number(self):
        """
        Release in About dialog, which is constantly changing.
        """
        return self.locate_xpath('//input[@id="release_sas_RC-about-field-0"]/../../div')

    @property
    def site_name(self):
        """
        Site name in About dialog, which is constantly changing.
        """
        return self.locate_xpath('//input[@id="site-name_sas_RC-about-field-0"]/../../div')

    @property
    def site_number(self):
        """
        Site number in About dialog, which is constantly changing.
        """
        return self.locate_xpath('//input[@id="site-number_sas_RC-about-field-0"]/../../div')

    # END Added by Jacky(ID: jawang) on May.6th, 2024 >>>

    # MODIFIED
    # <<< Modified by Jacky(ID: jawang) on May.6th, 2024
    # Comment out and use the new implementation instead.
    # pass
    # Modified by Jacky(ID: jawang) on May.6th, 2024 >>>
