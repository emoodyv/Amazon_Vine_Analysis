import pandas as pd

vine_table = pd.read_csv("vine_table.csv", names=['review_id', 'star_rating', 'helpful_votes', 'total_votes',
                                                  'vine', 'verified_purchase'])

vine_table = vine_table[vine_table['total_votes'] > 20]

vine_table = vine_table[vine_table['helpful_votes'] / vine_table['total_votes'] > .5]

vined = vine_table[vine_table['vine'] == 'Y']

nonvined =  vine_table[vine_table['vine'] == 'N']

vined_total = len(vined['review_id'])
vined_total_five = len(vined[vined['star_rating'] == 5])
vined_per_five = vined_total_five / vined_total * 100

nonvined_total = len(nonvined['review_id'])
nonvined_total_five = len(nonvined[nonvined['star_rating'] == 5])
nonvined_per_five = nonvined_total_five / nonvined_total * 100

print(f'The vine reviews had {vined_total_five} five star reviews out of {vined_total} total reviews. Therefore '
      f'{vined_per_five}% of the vine reviews where five stars')
print(f'The non-vine reviews had {nonvined_total_five} five star reviews out of {nonvined_total} total reviews. Therefore '
      f'{nonvined_per_five}% of the non-vine reviews where five stars')
