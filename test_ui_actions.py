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

