class TextDocument:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

class TextView:
    def show_text(self, text):
        print("Text in the document:")
        print(text)

class TextController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_text(self, new_text):
        self.model.set_text(new_text)

    def display_text(self):
        text = self.model.get_text()
        self.view.show_text(text)


if __name__ == "__main__":
    model = TextDocument()
    view = TextView()
    controller = TextController(model, view)

    while True:
        user_input = input("Enter new text (or 'q' to quit): ")
        if user_input == 'q':
            break
        controller.update_text(user_input)
        controller.display_text()