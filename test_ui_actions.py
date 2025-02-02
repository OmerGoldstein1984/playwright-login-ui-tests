from time import sleep

from playwright.sync_api import expect
def test_uiActions(browser):
    showOrHide=browser.get_by_placeholder('Hide/Show Example')
    expect(showOrHide).to_be_visible()
    showOrHide.fill('AbCD')
    browser.get_by_role('button' , name="Hide").click()
    expect(showOrHide).to_be_hidden()

    #alerts
    browser.on('dialog',lambda dialog:dialog.accept())
    browser.get_by_role('button',name='Confirm').click()

    #iframe
    iframe= browser.frame_locator('#courses-iframe')
    #iframe.get_by_role('link',name='All Access plan').click()

    #mousehover
    browser.locator(".mouse-hover+").hover()
    browser.get_by_role('link',name='Top').click()
    sleep(3)
