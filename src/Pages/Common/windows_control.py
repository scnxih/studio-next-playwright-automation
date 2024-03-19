import time

"""These two methods have problems mow, need further debug"""
def dismiss_dialog(dialog):
    print("this is dialog type:" + dialog.type)
    time.sleep(1)
    dialog.dismiss()
def accept_dialog(dialog):
    print("this is ialog type:" + dialog.type)
    time.sleep(1)
    dialog.accept()