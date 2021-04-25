# 認証ファイルのpathを取得
from gam.GamCompany import GamCompany
from gam.GamLineItem import GamLineItem
from gam.GamNetwork import GamNetwork
from gam.GamOrder import GamOrder
from gam.GamUser import GamUser


def main():
    networks = GamNetwork().get_all_networks()
    for network in networks:
        print('Network with network code "%s" and display name "%s" was found.'
              % (network['networkCode'], network['displayName']))

    user = GamUser().get_current_user()
    print('User with ID %d, name "%s", email "%s", and role "%s" '
          'is the current user.' % (user.id, user.name, user.email, user.roleName))

    company_service = GamCompany()
    companies = company_service.get_all_companies()
    for company in companies:
        print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
              (company['id'], company['name'], company['type']))
    print('\nNumber of results found: %s' % len(companies))

    created_companies = company_service.create_advertiser('Advertiser by API')
    if created_companies is not None:
        for company in created_companies:
            print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
                  (company['id'], company['name'], company['type']))

    order_service = GamOrder()
    orders = order_service.get_all_orders()
    for order in orders:
        print('Order with ID "%d" and name "%s" was found.\n' % (order['id'],
                                                                 order['name']))
    line_item = GamLineItem()
    line_items = line_item.get_all_line_items()
    for line_item in line_items:
        # Print out some information for each line item.
        print(line_item)
        print('Line item with ID "%d" and name "%s" was found.\n' %
              (line_item['id'], line_item['name']))

    print('\nNumber of results found: %s' % len(line_items))


if __name__ == '__main__':
    main()
