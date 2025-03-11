import shutil
from pathlib import Path

# from Crypto.PublicKey import RSA
#
# from src.Utilities.cryptorsautil import CryptoRsaUtil
from src.Utilities.enums import CenterPageType

''' Added by Jacky(ID: jawang) on Sept.5th, 2023'''
from src.Data.data import Data
from src.Data.data_fr import DataFR
from src.Data.data_zh import DataZH
import os
import logging
from src.Utilities.vars import global_locale


class Helper:

    @staticmethod
    def get_data_locale():
        if global_locale == "zh-CN":
            return DataZH()
        elif global_locale == "en-US":
            return Data()
        elif global_locale == "fr-FR":
            return DataFR()

    data_locale = get_data_locale()

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on September 12th, 2024
    public_folder_path = [data_locale.SAS_CONTENT, "Public"]
    # END Added by Jacky(ID: jawang) on September 12th, 2024 >>>

    # ADDED
    # BEGIN <<< Added by Jacky(ID: jawang) on Tuesday 11th, 2025
    # Path to save files on SAS Server, i.e. {SAS Server/Home/tmp}
    # Revert after the fix of SASSTUDIO-43504 : Duplicate 'SAS Server' nodes in central content selector
    tmp_folder_path = [data_locale.SAS_SERVER, "SAS Server", "Home", "tmp"]
    # tmp_folder_path = [data_locale.SAS_CONTENT, "Public"]

    # END Added by Jacky(ID: jawang) on Tuesday 11th, 2025 >>>

    @staticmethod
    def call_SDSTest():
        os.chdir("c:\\studio-next-playwright-automation\\src\\Helper")
        os.system("SDSTest.bat")

    @staticmethod
    def call_SDSTest_Steps():
        os.chdir("c:\\studio-next-playwright-automation\\src\\Helper")
        os.system("SDSTest_Steps.bat")

    @staticmethod
    def create_dir(folder_name):
        current_dir = os.getcwd()
        if not os.path.exists(current_dir + "/" + folder_name):
            os.makedirs(current_dir + "/" + folder_name)

    @staticmethod
    def create_logger():
        return logging.getLogger(__name__)

    logger = create_logger()

    ''' Modified by Jacky(ID: jawang) on Sept.5th, 2023 '''

    @staticmethod
    def create_folder(path, replace):
        print("Create folder")
        if os.path.exists(path):
            if replace:
                shutil.rmtree(path)
                # original version
                # os.makedirs(path, exist_ok=True)

                # revised version
                path_to_create = Path(path)
                path_to_create.mkdir(exist_ok=True)
                print(f"Path created and overwritten: {path}")
            else:
                print("Creation aborted. Path already exist.")
        else:
            os.makedirs(path, exist_ok=True)
            print(f"Path created: {path}")

    ''' Modified by Jacky(ID: jawang) on Sept.5th, 2023 '''

    @staticmethod
    def delete_folder(path):
        if os.path.exists(path):
            print("Prepare to delete " + path)
            # original version: WORKS FINE
            shutil.rmtree(path)
            print("Successfully deleted: " + path)
        else:
            print(path + "does not exist!")

        # Revised version: DID NOT WORK
        # in pathlib, to remove this directory.  The directory must be empty.
        '''
        path_to_delete = Path(path)
        if path_to_delete.exists():
            path_to_delete.rmdir()  # Cannot remove this path if it is NOT EMPTY.
            print("Deleted: " + path)
        else:
            print(path + "does not exist!")
        '''

    ''' Modified by Jacky(ID: jawang) on Sept 4th, 2023 '''

    @staticmethod
    def get_testfile_abbreviation():
        return (os.environ.get('PYTEST_CURRENT_TEST').split("/")[-1].split("::")[0].split(".py")[0].split("_")[1]
                + "_" +
                os.environ.get('PYTEST_CURRENT_TEST').split("/")[-1].split("::")[0].split(".py")[0].split("_")[2])

    @staticmethod
    def get_testmethod_number():
        return os.environ.get('PYTEST_CURRENT_TEST').split("/")[-1].split("::")[-1].split("_")[1]

    @staticmethod
    def get_storage_path(output_path, testfile_abbreviation, testmethod_number):
        return output_path + "\\" + testfile_abbreviation + "_" + testmethod_number + "\\"

    ''' Modified by Jacky(ID: jawang) on Sept 4th, 2023 '''

    """Added by Alice on 10/08/2023 start"""

    @staticmethod
    def if_contain_quotation(query_str: str):
        if query_str.find("\"") == -1 and query_str.find("'") == -1:
            return False
        return True

    @staticmethod
    def escape_quotation_for_xpath(query_str: str):
        if query_str.find("\"") == -1 and query_str.find("'") == -1:
            return query_str
        query_str = query_str.replace("\"", "[\"]")
        query_str = query_str.replace("'", "',\"'\",'")
        query_str = query_str.replace("[\"]", "','\"','")
        query_str = "concat('" + query_str + "')"
        Helper.logger.debug(query_str)
        return query_str

    """Added by Alice on 10/08/2023 end"""

    # @staticmethod
    # def get_password():
    #     x = RSA.generate(2048)
    #     private_key = str(x.export_key(), encoding="utf-8")  # 私钥
    #     public_key = str(x.publickey().export_key(), encoding="utf-8")  # 公钥
    #     rsa = CryptoRsaUtil(rsa_publicKey=public_key, rsa_privateKey=private_key)
    #     data = "The power to know!"
    #     data_encrypt = rsa.encrypt(data)
    #     data_decrypt = rsa.decrypt(data_encrypt)
    #     return data_decrypt
