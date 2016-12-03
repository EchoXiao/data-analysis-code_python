###########################################################
LAX

select A.hawb, A.agent_ref, B.agent_ref from 
(
	select * from check_point 
	where  date_trunc('day', data_generated_time) = '2016-12-01'
	and network_code = 'LAX01S'
	and cp_code = '44'
) A  inner join
(
	select * 
	from check_point 
	where network_code = 'LAX02A'
	and cp_code = 'LP'
) B 
on A.hawb = B.hawb 
and upper(A.agent_ref) != upper(B.Agent_ref)

union

select hawb, cp_code, agent_ref
from check_point
where date_trunc('day', data_generated_time) = '2016-12-01'
and network_code = 'LAX02A'
and cp_code = 'LP'
and hawb not in (
	select hawb
	from check_point 
	where network_code = 'LAX01S'
	and cp_code = '44'
	)
	
	and left(agent_ref, 8) != '1Z1EF786'

###################################################################
JFK
---
print(excelfile)select A.hawb, A.agent_ref, B.agent_ref from 
(
	select * from check_point 
	where  date_trunc('day', data_generated_time) = '2016-12-01'
	and network_code = 'JFK01S'
	and cp_code = '44'
) A  inner join
(
	select * 
	from check_point 
	where network_code = 'JFK02A'
	and cp_code = 'LP'
) B 
on A.hawb = B.hawb 
and upper(A.agent_ref) != upper(B.Agent_ref)

union

select hawb, agent_ref, agent_ref
from check_point
where date_trunc('day', data_generated_time) = '2016-12-01'
and network_code = 'JFK02A'
and cp_code = 'LP'
and hawb not in (
	select hawb
	from check_point 
	where  date_trunc('day', data_generated_time) = '2016-12-01'
	and network_code = 'JFK01S'
	and cp_code = '44'
	and left(agent_ref, 8) != '1Z1EF786'
	)
	
