import justpy as jp
from webapp import layout


class About:
    path = "/about"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-blue-200 text-center")
        jp.Div(a=div, text="Welcome to the about page!", classes="text-4xl m-2 pt-8 pb-8 text-center text-italic "
                                                                 "font-serif text-bold")
        jp.Div(a=div, text="Welcome to the Instant Dictionary, your gateway to a world of knowledge at your fingertips."
                           " This revolutionary web app allows you to instantly access the definition of any English "
                           "word, right as you type it. No more tediously flipping through pages or searching through "
                           "online dictionaries. With our intuitive interface, you can effortlessly expand your "
                           "vocabulary and enhance your understanding of language.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        jp.Div(a=div, text="Features That Make Us Stand Out", classes="text-2xl m-2 text-center text-bold")
        jp.Div(a=div, text="Real-time Definition: Our lightning-fast search engine delivers definitions instantly, "
                           "as you type. No more waiting for results – get the information you need when you need it.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")
        jp.Div(a=div, text="Comprehensive Coverage: Our vast database encompasses a wide range of English words, from "
                           "common terms to obscure vocabulary. Whether you're writing an essay, engaging in a "
                           "conversation, or simply curious about a word's meaning, we've got you covered.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")
        jp.Div(a=div, text="User-Friendly Interface: Our clean and intuitive design makes it easy to navigate the "
                           "dictionary and find the information you need. With a simple search bar and clear "
                           "definitions, you can explore the world of words with ease.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        jp.Div(a=div, text="Elevate Your Language Skills", classes="text-2xl m-2 text-center text-bold")
        jp.Div(a=div, text="The Instant Dictionary is an invaluable tool for anyone who wants to improve their "
                           "English language skills. Whether you're a student, a writer, or simply someone who enjoys "
                           "learning new things, our app can help you expand your vocabulary, enhance your writing, "
                           "and communicate more effectively.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        jp.Div(a=div, text="Embrace the Power of Words", classes="text-2xl m-2 text-center text-bold")
        jp.Div(a=div, text="With the Instant Dictionary as your companion, you'll never be at a loss for words again. "
                           "Explore the vast world of language, discover new meanings, and unlock the power of words "
                           "to enhance your life.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        jp.Div(a=div, text="Get Started Now!", classes="text-2xl m-2 text-center text-bold")
        jp.Div(a=div, text="Visit our website and experience the instant gratification of our dictionary. "
                           "Start typing and watch as the definitions flow before your eyes. Elevate your language "
                           "skills and unlock a world of knowledge with the Instant Dictionary.",
               classes="text-lg m-2 pb-5 text-center text-italic font-serif")

        return wp




