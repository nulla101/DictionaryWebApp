import justpy as jp
import definition
from webapp import layout


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-blue-200 h-screen text-center")
        jp.Div(a=div, text="Instant English Dictionary",
               classes="text-4xl m-2 pt-8 pb-1 text-center text-bold font-serif")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        input_box = jp.Input(a=div, placeholder="Type in a word here...",
                             classes="m-2 text-center text-italic font-serif bg-blue-300 rounded w-64 "
                                     "focus:outline-none focus:bg-white py-2 px-4")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-base border-8 h-40 rounded font-serif")

        jp.Button(a=div, text="Get Definition",
                  classes="m-2 py-2 px-4 bg-blue-500 rounded font-serif",
                  click=cls.get_definition, outputdiv=output_div, inputbox=input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.inputbox.value).get()
        widget.outputdiv.text = " ".join(defined)
