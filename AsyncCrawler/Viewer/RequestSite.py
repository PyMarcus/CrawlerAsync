from Controller.RequestSiteController import RequestSiteController
from ParserRequest import ParserRequest
import asyncio


class RequestSite:
    __site = "https://www.bibliaon.com/salmo_do_dia/"

    @property
    def site(self):
        return str(RequestSite.__site)

    @classmethod
    def requisicao(cls):
        el = asyncio.get_event_loop()
        resposta = el.run_until_complete(RequestSiteController.req(RequestSite.__site))
        return ParserRequest.capture(resposta)


if __name__ == '__main__':
    RequestSite.requisicao()
