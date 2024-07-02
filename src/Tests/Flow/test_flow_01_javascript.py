from src.Helper.playwright_helper import PlaywrightHelper
from src.Helper.helper import Helper
import time
from playwright.sync_api import Playwright, sync_playwright, Page

from src.Utilities.vars import global_username, global_password


def run(pw: Playwright) -> None:
    data_locale = Helper.data_locale
    pw_objects = PlaywrightHelper.init_create_page(pw)
    page: Page = pw_objects[0]
    context = pw_objects[1]
    browser = pw_objects[2]
    page.goto("https://daily.pgc.unx.sas.com/SASStudioNext/")
    page.wait_for_timeout(1000)
    page.get_by_placeholder(data_locale.USER_ID).click()
    page.get_by_placeholder(data_locale.USER_ID).fill(global_username)
    page.get_by_placeholder(data_locale.PASSWORD).click()
    page.get_by_placeholder(data_locale.PASSWORD).fill(Helper.get_password())
    page.wait_for_timeout(1000)
    page.get_by_role("button", name=data_locale.SIGN_IN).click()
    time.sleep(5)


    page.get_by_test_id("appHeaderToolbar-new-button").click()
    page.get_by_test_id("appHeaderToolbar-flow").locator("div").nth(1).click()

    page.get_by_test_id("flowtoolbar-addStepMenuButton-button").click()
    page.get_by_test_id("flowtoolbar-GENERIC_TABLE_TRANSFORMATION-text").click()

    time.sleep(2)

    position = page.evaluate(
        "function a(){ return document.getElementsByClassName('sas_styles-Diagram_diagram-component')["
        "0].robot.diagram.model.nodeDataArray.filter(n=> n.name == ['表'])[0].location}")
    position_list = position.split()
    # page.pause()
    page.evaluate("currentFlow = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot")
    page.evaluate("currentFlow.mousePressAction (" + position_list[0] + "," + position_list[1] + ")")
    time.sleep(2)
    position = page.evaluate(
        "function b(){ return document.getElementsByClassName('sas_styles-Diagram_diagram-component')["
        "0].robot.diagram.model.nodeDataArray.filter(n=> n.name == ['表'])[0].location}")
    position_list = position.split()
    page.evaluate("currentFlow = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot")
    page.evaluate("currentFlow.mouseDown (" + position_list[0] + "," + position_list[1] + ",0,{button:2})")
    time.sleep(1)
    page.evaluate("currentFlow.mouseUp (" + position_list[0] + "," + position_list[1] + ",100,{button:2})")
    time.sleep(3)
    page.get_by_text("添加查询").click()
    time.sleep(3)

    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
