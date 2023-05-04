from selene import be, have, command
from selene.support.shared import browser

from demoqa_tests import helpers, resource, data


class RegistrationPage:
    def __init__(self):
        self.dropdown_menu = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open('/automation-practice-form')
        helpers.remove('#fixedban')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type('Ivan')
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{int(month) - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def modal_should_have_registered_user_info(self, *args):
        browser.all(' td:nth-of-type(2)').should(have.exact_texts(args))

    def select_subjects(self, value):
        for subject in value:
            browser.element('#subjectsInput').should(be.blank).type(subject).press_tab()
        return self

    def select_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.get_path(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def select_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        self.dropdown_menu.element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        self.dropdown_menu.element_by(have.exact_text(value)).click()
        return self

    def submit_data(self):
        browser.element('#submit').execute_script('element.click()')

    def should_have_title(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))

    def close_modal(self):
        browser.element('#closeLargeModal').should(be.clickable)
