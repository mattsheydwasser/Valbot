from valo_api import endpoints

def main():
    
    dets = endpoints.get_account_details_by_name_v1('Silas', '69LOL')
    print(dets.account_level, dets.card.small)
    
main()