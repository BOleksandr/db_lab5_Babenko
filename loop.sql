do $$
declare
	model Cellphone.model%type;
	brand Cellphone.brand%type;
begin
	model := 'Model #';
	brand := 'Brand #';
	
	for counter in 6..11
		loop
			insert into Cellphone(cellphone_id, model, brand)
			values(counter, model || counter, brand || counter);
		end loop;
end;
$$

select * from cellphone;