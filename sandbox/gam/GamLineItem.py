from googleads import ad_manager

from sandbox.gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamLineItem:
    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('LineItemService')

    def get_all_line_items(self):
        statement = ad_manager.StatementBuilder()

        result = []
        while True:
            response = self.__service.getLineItemsByStatement(statement.ToStatement())
            if 'results' in response and len(response['results']):
                result += response['results']
                statement.offset += statement.limit
            else:
                break

        return result
