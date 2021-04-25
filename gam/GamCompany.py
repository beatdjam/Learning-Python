from googleads import ad_manager
from googleads.errors import GoogleAdsServerFault

from gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamCompany:
    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('CompanyService')

    def get_all_companies(self):
        # 何も指定せず会社をすべて取得する
        statement = ad_manager.StatementBuilder()

        # 広告主・自社広告主を取得する場合のStatement
        # statement = ad_manager.StatementBuilder()\
        #     .Where('type IN (\'ADVERTISER\' , \'HOUSE_ADVERTISER\')')

        result = []
        while True:
            response = self.__service.getCompaniesByStatement(statement.ToStatement())
            if 'results' in response and len(response['results']):
                result += response['results']
                statement.offset += statement.limit
            else:
                break

        return result

    def create_advertiser(self, company_name: str):
        try:
            return self.__service.createCompanies(
                [{'name': company_name, 'type': 'ADVERTISER'}])
        except GoogleAdsServerFault as e:
            # TODO すでに存在していた場合のエラー処理
            print(e)
            print('already exists.')
