from Controller.ParserRequestController import ParserRequestController


class ParserRequest:
    @classmethod
    def capture(cls, resposta):
        result = ParserRequestController.parser(resposta)
        for i, l in enumerate(result):
            if i % 2 == 0:
                print(l + "\n")
            else:
                print(l)
