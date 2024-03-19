from src.Helper.page_helper import *


def test_01_document_recovery_dialog_recover_all(page, init):
    PageHelper.document_recovery_dialog_recover_all(page, Helper.data_locale.RECOVERY_APPLY_CLOSE)


def test_02_document_recovery_dialog_delete_all(page, init):
    PageHelper.document_recovery_dialog_delete_all(page, Helper.data_locale.RECOVERY_APPLY_CLOSE)


def test_03_document_recovery_dialog_recover_files(page, init):
    PageHelper.document_recovery_dialog_recover_files(page, Helper.data_locale.RECOVERY_APPLY, file_names=["file0", "file1"])


def test_04_document_recovery_dialog_delete_files(page, init):
    PageHelper.document_recovery_dialog_delete_files(page, Helper.data_locale.RECOVERY_APPLY, file_indexes=[0, 1, 13])
