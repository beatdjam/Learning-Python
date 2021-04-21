from googleads import AdManagerClient, ad_manager


class GamLineItem:
    def __init__(self, client: AdManagerClient):
        self.__service = client.GetService('LineItemService')

    def get_all_line_items(self):
        statement = ad_manager.StatementBuilder()

        while True:
            response = self.__service.getLineItemsByStatement(statement.ToStatement())
            if 'results' in response and len(response['results']):
                for line_item in response['results']:
                    # Print out some information for each line item.
                    print(line_item)
                    print('Line item with ID "%d" and name "%s" was found.\n' %
                          (line_item['id'], line_item['name']))
                statement.offset += statement.limit
            else:
                break

        print('\nNumber of results found: %s' % response['totalResultSetSize'])