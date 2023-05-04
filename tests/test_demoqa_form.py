from demoqa_tests.pages.registration_page import RegistrationPage


def test_form_filling(browser_actions):
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Ivan')
        .fill_last_name('Petrov')
        .fill_email('ivanpetrov@mail.ru')
        .select_gender('Male')
        .fill_mobile('8999999999')
        .fill_date_of_birth('19', '11', '1989')
        .select_subjects(['Maths', 'Hindi'])
        .select_hobby('Reading')
        .upload_picture('Capibara.jpg')
        .fill_address('Pushkina Street, Kolotushkina house')
        .select_state('Uttar Pradesh')
        .select_city('Merrut')
        .submit_data()
    )
    registration_page.should_have_title('Thanks for submitting the form')
    registration_page.modal_should_have_registered_user_info('Ivan Petrov', 'ivanpetrov@mail.ru', 'Male', '8999999999',
                                                       '19 November,1989', 'Maths, Hindi', 'Reading', 'Capibara.jpg',
                                                       'Pushkina Street, Kolotushkina house',
                                                       'Uttar Pradesh Merrut')
    registration_page.close_modal()
