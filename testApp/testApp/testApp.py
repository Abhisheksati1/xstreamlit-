import nextpy as rx
import openai

openai.api_key = "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"

class State(rx.State):
    """The app state."""
    user_input = ""
    assistant_response = ""
    processing = False

    def set_user_input(self, value):
        self.user_input = value

    def get_response(self):
        if not self.user_input:
            return rx.window_alert("Please ask a question.")

        self.processing = True
        yield
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.user_input,
            max_tokens=100,
        )
        self.assistant_response = response["choices"][0]["text"]
        self.processing = False

def index():
    return rx.center(
        rx.box(
            rx.heading("ChatGPT"),
            rx.input(
                placeholder="Ask a question...",
                on_change=State.set_user_input,
                width="100%",
            ),
            rx.framer_motion.motion_div(
                class_name = "w-28 h-28 bg-blue-200 rounded-full",
                whileHover = {"scale": 1.2},
                whileTap = {"scale": 0.8},
            ),
            rx.button(
                "Get Answer",
                on_click=State.get_response,
                is_loading=State.processing,
                width="100%",
            ),
            rx.text(State.assistant_response, color="blue"),
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index, title="ChatGPT App")
app.compile()