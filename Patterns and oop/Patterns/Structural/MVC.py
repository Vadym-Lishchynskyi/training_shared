"""
MVC = Model-View-Controller
One of the design principles related to software engineering is the separation of concerns (SoC) principle. The
idea behind the SoC principle is to split an application into distinct sections, where each section addresses a
separate concern. Examples of such concerns are the layers used in a layered design (data access layer,
business logic layer, presentation layer, and so forth). Using the SoC principle simplifies the development and
maintenance of software applications.

The MVC pattern is nothing more than the SoC principle applied to OOP. The name of the pattern comes from the three
main components used to split a software application: the model, the view, and the controller. MVC is considered an
architectural pattern rather than a design pattern.

The difference between an architectural and a design pattern is that the former has a broader scope than the latter.

Useful All common frameworks use MVC or a slightly different version of it.!!!!


Model:
    The model is the core component. It represents knowledge. It contains and manages the (business) logic, data,
state, and rules of an application.

View:
    The view is a visual representation of the model. Examples of views are a computer GUI, the text output of a
computer terminal, a smartphone's application GUI, a PDF document, a pie chart, a bar chart, and so forth. The view
only displays the data; it doesn't handle it.

Controller:
    The controller is the link/glue between the model and view. All communication between the model and the
view happens through a controller.


Pros:
- the ability to use more than one view (even at the same time, if that's what we want) without modifying the model.
- easy find the mistake (decomposition)

To achieve decoupling between the model and its representation, every view typically needs its own controller. If the
model communicated directly with a specific view, we wouldn't be able to use multiple views.


Real use cases in frameworks Python:
- The Web2py Framework (j.mp/webtopy) is a lightweight Python Framework that embraces the MVC pattern.
- Django is also an MVC Framework, although it uses different naming conventions.
- Flask also provide such ability (I used it personally on the last project)

"""

quotes = (
  'A man is not complete until he is married. Then he is finished.',
  'As I said before, I never repeat myself.',
  'Behind a successful man is an exhausted woman.',
  'Black holes really suck...',
  'Facts are stubborn things.'
)


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
