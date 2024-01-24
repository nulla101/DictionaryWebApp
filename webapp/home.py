import justpy as jp
from webapp import layout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-blue-200 h-screen text-center")
        jp.Div(a=div, text="Welcome to the homepage!",
               classes="text-4xl m-2 pt-16 pb-8 text-center text-bold font-serif")
        jp.Div(a=div, text="Welcome to the Instant Dictionary, your gateway to a world of knowledge at your fingertips."
                           " This revolutionary web app allows you to instantly access the definition of any English "
                           "word, right as you type it. No more tediously flipping through pages or searching through "
                           "online dictionaries. With our intuitive interface, you can effortlessly expand your "
                           "vocabulary and enhance your understanding of language.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        return wp


