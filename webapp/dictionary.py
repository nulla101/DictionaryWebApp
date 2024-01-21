import justpy as jp


class Dictionary:
    path = "/dictionary"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-blue-200 h-screen text-center")
        jp.Div(a=div, text="Instant English Dictionary",
               classes="text-4xl m-2 pt-8 pb-1 text-center text-bold font-serif")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        jp.Input(a=div, placeholder="Type in a word here...",
                 classes="m-2 text-center text-italic font-serif bg-blue-300 rounded w-64 "
                         "focus:outline-none focus:bg-white py-2 px-4")

        jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40 rounded")

        return wp