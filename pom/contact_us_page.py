class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email):
        self.page.fill("[placeholder=\"Enter your name\"]", name)
        self.page.fill("[placeholder=\"Enter your address\"]", address)
        self.page.fill("[placeholder=\"Enter your email\"]", email)
        self.page.fill("[placeholder=\"Enter your phone number\"]", "132-324-5456")
        self.page.fill("[placeholder=\"Type the subject\"]", "test subject")
        self.page.fill("textarea", "test msg blah")

        self.page.press('[aria-label="Enter your search term"]', "Enter")
