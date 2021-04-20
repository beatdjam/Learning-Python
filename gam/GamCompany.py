from googleads import AdManagerClient, ad_manager
from googleads.errors import GoogleAdsServerFault


class GamCompany:
    def __init__(self, client: AdManagerClient):
        self.__service = client.GetService('CompanyService')

    def get_all_companies(self):
        # 何も指定せず会社をすべて取得する
        statement = ad_manager.StatementBuilder()

        # 広告主・自社広告主を取得する場合のStatement
        # statement = ad_manager.StatementBuilder()\
        #     .Where('type IN (\'ADVERTISER\' , \'HOUSE_ADVERTISER\')')

        while True:
            response = self.__service.getCompaniesByStatement(statement.ToStatement())
            if 'results' in response and len(response['results']):
                for company in response['results']:
                    print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
                          (company['id'], company['name'], company['type']))
                statement.offset += statement.limit
            else:
                break

        print('\nNumber of results found: %s' % response['totalResultSetSize'])

    def create_advertiser(self, company_name: str):
        try:
            companies = self.__service.createCompanies([{'name': company_name, 'type': 'ADVERTISER'}])
            for company in companies:
                print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
                      (company['id'], company['name'], company['type']))
        except GoogleAdsServerFault as e:
            # TODO すでに存在していた場合のエラー処理
            print(e)
            print('already exists.')