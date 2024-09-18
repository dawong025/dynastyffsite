select * from weekly_rostered wr
join player p on wr.player_id=p.player_id
join league_members lm on lm.member_id = wr.member_id





