from valo_api import endpoints

def main():
    
    dets = endpoints.get_match_history_by_name_v3('na', 'Silas', '69LOL', game_mode='Competitive')
    
    # get map, game_length (do ((3.6 * (10^6)) * 60) to get minutes),
    # game_start_patched = date of game, rounds played
    
    one = dets[0].players.blue[0]
   
    print(one)
        
    
main()