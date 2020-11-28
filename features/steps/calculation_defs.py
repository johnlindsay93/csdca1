from behave import given, then, when

@given ("I navigate to homepage")
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/')

@given ("a valid name is used")
def low(context):
    context.browser.find_element_by_name('name').send_keys('John')

@given ("systolic is less than 90")
def low(context):
    context.browser.find_element_by_name('systolic_level').send_keys('89')


@given ("diastolic is less than 60")
def low(context):
    context.browser.find_element_by_name('diastolic_level').send_keys('55')


@when ("I click on Calculate Blood Pressure")
def low(context):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='Calculate Blood Pressure']").click()


@then ("Bloodpressure should be Low")
def low(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/'
