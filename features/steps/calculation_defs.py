from behave import given, then, when

@given ("I navigate to homepage")
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/')

@given ("a valid name is used")
def low(context):
    context.browser.find_element_by_name('name').send_keys('John')

@given ("systolic is {Systolic}")
def low(context,Systolic):
    context.browser.find_element_by_name('systolic_level').send_keys(Systolic)


@given ("diastolic is {Diastolic}")
def low(context, Diastolic):
    context.browser.find_element_by_name('diastolic_level').send_keys(Diastolic)


@when ("I click on Calculate Blood Pressure")
def low(context):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='Calculate Blood Pressure']").click()


@then ("Bloodpressure should be {Result}")
def low(context, Result):
    assert context.browser.current_url == 'http://127.0.0.1:5000/'
    text = context.browser.find_element_by_xpath("//*[@id='Result']/p").text
    assert text == Result


