
def checking_team_length(team_list):
    if len(team_list)!=16:
        print('Please enter exactly 16 teams')
    else:
        print('Thanks!')



def make_list_of_teams(to_break, to_append):
    '''Teams given by user is broken up from a string to a list
    Parameters:
    to_break = string
    to_append = empty list'''
    
    temp_list = to_break.split(', ')
    for team in temp_list:
        to_append.append(team)
    return to_append    
        
        
def make_dict_of_all(team_list, dictionary):
    '''makes dictionary of teams where the key is their seed in the tournament and the value is the team name
    parameter:
    team_list = list of teams in order of seed'''
    
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    for rank in keys:
        temp_index = rank-1
        dictionary[rank] = team_list[temp_index]


        
        
def single_elim_rd1(team_dict, bracket_name, match_keys = [1, 8, 5, 4, 6, 3, 7, 2]):
    '''prints round 1 matches based on initial tournament seed
    Parameters: 
    team_dict = dictionary made with make_dict_of_all
    bracket_name = string of tournament name
    match_keys = list, ensures teams are matched up against proper teams
    
    Output:
    strings with teams in each match'''
    
    round_label = bracket_name + ' Round 1' 
    print(round_label.center(20, ' '))
    
    for key in match_keys:
        home_team = team_dict[key]
        away_key = 17 - key
        away_team = team_dict[away_key]
        str_away_key = str(away_key)
        str_home_key = str(key)
        
        print(str_home_key + ':' + team_dict[key] + ' vs ' + str_away_key + ':' + team_dict[away_key])
        
        

def make_dict_winners(prev_round, cur_round, cur_round_dict):
    '''Given user input of the winning teams, makes dictionary with just the winners, preserving their initial seeding in the tournament
    Parameters: 
    prev_round = dictionary of teams that participated in the previous round
    cur_round = list of teams who have advanced
    cur_round_dict = empty dictionary appended in this function with winning teams. key is tournament seed and value is team name'''
    
    for index in prev_round:
        team = prev_round.get(index)
        if team in cur_round:
            cur_round_dict.update({index: team})
            
            
            
def single_elim_rd2(team_dict, to_fill):
    '''fills the dictionary round2_matches which is used in print_matches to create match ups for round 2 (Quarterfinals)
    Parameters: 
    team_dict = dictionary of teams participating in round 2'''
    
    loop_list = [(1, 16), (8, 9), (5, 12), (4, 13), (6, 11), (3, 14), (7, 10), (2, 15)]
    i = 1
    for position in loop_list:
        for index in position:
            if index in team_dict:
                if len(to_fill[i]) == 0:
                    to_fill[i].append({index: team_dict[index]})
                elif len(to_fill[i]) == 1:
                    to_fill[i].append({index: team_dict[index]})
                    i += 1
             

            
def print_matches (unformatted, round_num, bracket_name):
    '''prints matches for all rounds except round 1
    Parameters:
    unformatted = dictionary with team match ups
    round_num = string defining which section of the tournament it is printing
    bracket_name = sting of tournament name
    
    Output:
    string formatted to show matches and participant teams' seeding'''
    
    print(bracket_name + ' ' + round_num)
    for match_num in unformatted:
        list_print = []
        for team_index in unformatted[match_num]:
            list_print.append(team_index)
        print(str(list_print[0]).replace('{', '').replace('}', '').replace("'", '') + '  vs  ' + str(list_print[1]).replace('{', '').replace('}', '').replace("'", ""))

        
        
def single_elim_rd3(team_dict, to_fill):
    '''fills the dictionary round3_matches which is used in print_matches to create match ups for round 3 (semifinals)
    Parameters: 
    team_dict = dictionary of teams participating in round 3'''
    
    loop_list = [(1, 16, 8, 9), (5, 12, 4, 13), (6, 11, 3, 14), (7, 10, 2, 15)]
    i = 1
    for position in loop_list:
        for index in position:
            if index in team_dict:
                if len(to_fill[i]) == 0:
                    to_fill[i].append({index: team_dict[index]})
                elif len(to_fill[i]) == 1:
                    to_fill[i].append({index: team_dict[index]})
                    i += 1
                    
                    
                    
def single_elim_rd4(team_dict, to_fill):
    '''fills the dictionary round4_matches which is used in print_matches to create match ups for round 4 (semifinals)
    Parameters: 
    team_dict = dictionary of teams participating in round 4'''
    
    loop_list = [(1, 16, 8, 9, 5, 12, 4, 13), (6, 11, 3, 14, 7, 10, 2, 15)]
    i = 1
    for position in loop_list:
        for index in position:
            if index in team_dict:
                if len(to_fill[i]) == 0:
                    to_fill[i].append({index: team_dict[index]})
                elif len(to_fill[i]) == 1:
                    to_fill[i].append({index: team_dict[index]})
                    i += 1