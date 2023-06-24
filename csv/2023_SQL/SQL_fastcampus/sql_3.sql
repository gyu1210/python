Drop database if exists pokemon;
create database pokemon;
use pokemon;
create table mypokemon(
number int,
name varchar(20),
type varchar(10),
attack int,
defense int,
capture_date date
);
insert into mypokemon (number,name, type,
 attack, defense, capture_date)
 values(10, 'caterpie','bug',30,35,'2019-10-14'),
 (25, 'pikachu','electric',55,40,'2018-11-04'),
 (26, 'raichu','electric',90,55,'2019-05-28'),
 (125, 'electabuzz','electric',83,57,'2021-10-03'),
 (133,'eevee','normal',55,50,'2021-10-03'),
 (137,'porygon','normal',60,70,'2021-01-16'),
 (152,'chikorita','grass',49,65,'2020-03-05'),
 (153,'bayleef','grass',55,50,'2022-01-01');
  select * from mypokemon;

#1) 이름과 이름의 글자수를 이름의 글자수로 정렬(글자수가 적은것부터-)
select name,length(name)
from pokemon.mypokemon
order by length(name);

#2) 방어력순위를 보여주는 컬럼='defense_rank', 이름과함께, 
#방어력순위 :방어력이 큰 순서대로
#공동순위가 있으면 다음순서로 스킵 
select name, defense,
rank() over (order by defense desc) as defense_rank
from pokemon.mypokemon;

#3)포켓몬을 포획한지 가준날짜까지 몇일이 지났는지 = 'days'
#기준날짜: 2022년 2월 14일
select DATEDIFF ('2022-02-14',capture_date) as days
from pokemon.mypokemon;

#1) 포켓몬의 이름을 마지막3개문자만 'last_char'라는 별명 
select name , right (name,3) as last_char
from pokemon.mypokemon;

#2) 포켓몬 이름을 왼쪽에서 2개문자를 'left2'라는 별명
select name , left(name, 2) as left2
from pokemon.mypokemon;

#3) 포켓몬이름에서 o가 포함된 포켓몬만 모든 소문자o를 대문자 O로 바꿔 'bigO'라는별명 
#ex)이름이 'pokemon'일 경우 'bigO'의 값은 'pOkemOn'
/*select name , replace(name, 'o','O') as bigO
from pokemon.mypokemon;*/

select replace(name, 'o','O') as bigO
from pokemon.mypokemon
where name like '%o%';

#4) 포켓몬 타입을 가장 첫번째 글자 1자, 가장 마지막글자 1자를 합친후 대문자로 변환 
#'typecode' 라는 별명, 이름
#타입이 'water'일경우 'type_code'의 값은 'WR'
select type , 
upper(concat (left(type,1), right(type,1)))
as type_code
from pokemon.mypokemon; 

#5) 포켓몬 이름의 글자수가 8보다 큰 포켓몬의 데이터를 전부
/*select *, length (name) >8
from pokemon.mypokemon; */
select *
from pokemon.mypokemon
where length(name) >8;

#6) 모든 포켓몬의 공격력 평균을 정수로 반올림 'avg_of_attack'별명
/*select avg (attack),  ceiling(attack) as avg_of_attack
from pokemon.mypokemon
group by ceiling(attack);*/
select round(avg(attack)) as avg_of_attack
from pokemon.mypokemon;

#7) 모든 포켓몬 방어력을 정수로 내림 'avg_of_defense'별명
select floor(avg(defense)) as avg_of_defense
from pokemon.mypokemon;

#8) 이름의 길이가 8미만인 포켓몬의 공격력의 2제곱 'attack2' 별명
/*select attack^2 = length (name) <8 as attack2, name
from pokemon.mypokemon;*/
select power(attack,2) as attack2, name
from pokemon.mypokemon
where length(name)<8;

#9) 모든포켓몬의 공격력을 2로 나눈 나머지 'div2'라는 별명
select mod(attack,2) as div2 , name
from pokemon.mypokemon;

#10) 공격력이 50이하인 포켓몬의 공격력을 방어력으로 뺀 값의 절댓값 'diff'라는 별명, 이름
/*select abs(attack >= 50 - defense) as diff, name
from pokemon.mypokemon;*/
select abs(attack -defense) as diff, name
from pokemon.mypokemon
where attack <=50;

#11) 현재날짜,시간 'now_date', 'now_time'별명
select current_date() as now_date , current_time() as now_time;
/*from pokemon.mypokemon;*/

#12) 포켓몬을 포획한 달(월,month)을 숫자와 영어로, 숫자는 month_num, 영어는 month_eng 별명
select month(capture_date) as month_num, monthname(capture_date) as month_eng
from pokemon.mypokemon;

#13) 포켓몬을 포획한 날의 요일을 숫자와 영어로. 숫자'day_num'. 영어'day_eng'별명
select dayofweek(capture_date) as day_num, dayname(capture_date) as day_eng
from pokemon.mypokemon;

#14) 포켓몬을 포획한 날의 연도, 월, 일을 각각 숫자로. 연도는 year, 월 month, 일 day 별명 
select year(capture_date) as year, month(capture_date) as month, day(capture_date) as day
from pokemon.mypokemon;


Drop database if exists pokemon;
create database pokemon;
use pokemon;
create table mypokemon(
number int,
name varchar(20),
type varchar(10),
height float,
weight float
);
insert into mypokemon (number,name, type, height, weight)
 values(10, 'caterpie','bug',0.3,2.9),
 (25, 'pikachu','electric',0.4,6),
 (26, 'raichu','electric',0.8,30),
 (133, 'eevee', 'normal',0.3,6.5),
 (137, 'porygon', 'normal',0.8,36.5),
 (152,'chikorita','grass',0.9,6.4),
 (153,'bayleef','grass',1.2,15.8),
 (172,'pichu','electric',0.3,2),
 (470,'leafeon','grass',1.25,5);
  select * from mypokemon;

#15) 이름의 길이가 5보다 큰 포켓몬들의 type을 기준으로 그룹화,
# 몸무게의 평균이 20이상인 그룹의 타입과 몸무게의 평균 , 몸무게의 평균을 내림차순 
/*select type,name, avg(weight)
from pokemon.mypokemon
group by type,name
having length (name)> 5 
order by avg(weight) >20 desc;*/

select type,avg(weight)
from pokemon.mypokemon
where length (name)> 5 
group by type
having  avg(weight) >20 
order by 2 desc;

#16) 번호가 200보다 작은 포켓몬들이 type을 기준으로 그룹화,
#몸무게의 최댓값이 10보다 크거나 같고 최솟값이 2보다 크거나 같은 그룹의 
#타입, 키의 초솟값, 최댓값, 키의 최솟값으로 내림차순,
#만약 키의 최솟값이 같다면 키의 최댓값의 내림차순으로 정렬 
/*select number,type,weight
from pokemon.mypokemon
where length(number)<200 
group by number,type,weight
having max(10)>= weight <= min(2)
order by type,min(height),max(height);*/
select type, min(height), max(height)
from pokemon.mypokemon
where number <200
group by type
having max(weight)>=10  and min(weight)>=2
order by 2 desc, 3 desc;

select type, name, height, case when type="electric" then "new value" else type end as pokemon_greater_than_point_five
from pokemon.mypokemon
where number <200;


Drop database if exists pokemon;
create database pokemon;
use pokemon;
drop table mypokemon;
create table mypokemon(
number int,
name varchar(20),
type varchar(10),
attack int,
defense int
);
insert into mypokemon (number,name, type,
 attack, defense)
 values(10, 'caterpie','bug',30,35),
 (25, 'pikachu','electric',55,40),
 (26, 'raichu','electric',90,55),
 (125, 'electabuzz','electric',83,57),
 (133,'eevee','normal',55,50),
 (137,'porygon','normal',60,70),
 (152,'chikorita','grass',49,65),
 (153,'bayleef','grass',55,50),
 (153,'pichu','electric',40,15),
 (153,'leafeon','grass',110,130);
  select * from mypokemon;
  
 # 1)공격력과 방어려의 합이 120 보다 크면 'verystrong',90보다크면'strong'
 #모두해당되지 않으면'not strong'를 반환하는 함수 isStrong을 만들고 사용하기
# attack ,defense를 입력값
#결과값 데이터 타입은 varchar(20)

/*
delimiter// 
create function getAbility (attack int, defense int)
returns varchar(20)
begin 
declare a int;
declare b int;
declare ability varchar(20);
set a = attack ;
set b = defense ;
select *
case 
when attack+defense >120 then 'verystrong'
when attack+defense >90 then 'strong'
else 'not strong'
end as isStrong
From pokemon.mypokemon
//
delimiter ; */

set global log_bin_trust_function_creators = 1;
delimiter // 
Drop function if  exists isStrong;
create function isStrong (attack int, defense int)
returns varchar(20)
begin 
declare a int;
declare b int;
declare isstrong varchar(20);
set a = attack ;
set b = defense ;
select case
when a+b >120 then 'verystrong'
when a+b >90 then 'strong'
else 'not strong'
end into isstrong;
return isstrong;
end
// 
delimiter ;

select name, isStrong(attack,defense) as isStrong
from mypokemon;



#1) 포켓몬의 테이블과 능력치 테이블을 함쳐 포켓몬 이름, 공격력, 방어력을 한번에 가져오기
#포켓몬 테이블에 있는 모든 포켓몬 데이터가져오기, 만약 포켓몬의 능력치 데이터를 구할수 없다면 NULL

Drop database if exists pokemon;
create database pokemon;
use pokemon;
create table mypokemon(
number int,
name varchar(20),
type varchar(10)
);
insert into mypokemon (number,name, type)
 values(10, 'caterpie','bug'),
 (25, 'pikachu','electric'),
 (26, 'raichu','electric'),
 (133,'eevee','normal'),
 (152,'chikorita','grass');
 
 create table ability(
number int,
height float,
weight float,
attack int,
defense int,
speed int
);
insert into ability (number,height,weight, attack,defense,speed)
 values(10, 0.3,2.9,30,35,45),
 (25,0.4,6,55,40,90),
 (125, 1.1, 30, 83, 57,105),
 (133,0.3,6.5,55,50,55),
 (137,0.8,36.5,60,70,40);
 
 /*select *
 from mypokemon
 inner join ability
 on mypokemon.number = ability.number ;*/
 
 select name, attack, defense
 from mypokemon
 left join ability
 on mypokemon.number = ability.number;



#2) 포켓몬 테이블과 능력치 테이블을 합쳐서 포켓몬 번호와 이름을 한번에 가져오기
#능력치 테이블에 있는 모든 포켓몬의 데이터 가져오기, 만약 포켓몬의 이름데이터 구할수 없을때 NULL
/*select *
from mypokemom
inner join ability
on mypokemon.number = ability.number;*/

select name, attack, defense
from mypokemon
right join ability
on mypokemon.number = ability.number;


select *
from mypokemon right join ability
on mypokemon.number = ability.number;


 
  
  
  



