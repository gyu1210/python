Drop database if exists pokemon;
create database pokemon;
use pokemon;
create table mypokemon(
number int,
name varchar(20),
type varchar(10),
attack int,
defense int
);
create table friendpokemon(
number int,
name varchar(20),
type varchar(10),
attack int,
defense int
);
insert into mypokemon (number,name, type,attack, defense)
 values(10, 'caterpie','bug',30,35),
 (25, 'pikachu','electric',55,40),
 (26, 'raichu','electric',90,55),
 (133, 'eevee', 'normal',55,50),
 (152,'chikorita','grass',49,65);
 
 insert into friendpokemon (number,name, type,attack, defense)
 values(26, 'richu','electric',80,60),
 (125, 'electabuzz','electric',83,57),
 (137, 'porygon','normal',60,70),
 (153, 'bayleef', 'grass',62,80),
 (172,'pichu','electric',40,15),
 (470,'leafeon','grass',110,130);
 
 #1)내 포켓몬과 친구의 포켓몬에 어떤 타입들이 있는지 중복제외하고 갑은 타입은 한번씩만 가져오기
 select type 
 from mypokemon
 union
 select type
 from friendpokemon;
 
 #2) 내 포켓몬과 친구의 포켓몬중 grass 타입 포켓몬들의 포켓몬 번호와 이름을 중복포함여여 전부가져오기
/*select (type='grass'), number, name
from mypokemon
union all 
select (type ='grass'), number, name
from friendpokemon;*/

select number, name,'my' as Whose
from mypokemon
where type = 'grass'
union all
select number, name, "frined's" as Whose
from friendpokemon
where type = 'grass';

Drop database if exists pokemon;
create database pokemon;
use pokemon;
create table mypokemon(
number int,
name varchar(20));

insert into mypokemon (number,name)
 values(10, 'caterpie'),
 (25, 'pikachu'),
 (26, 'raichu'),
 (133, 'eevee'),
 (152,'chikorita');

create table ability(
number int,
type varchar(10),
height float,
weight float,
attack int,
defense int,
speed int
);
 
 insert into ability (number,type,height, weight,attack, defense,speed)
 values(10, 'bug',0.3,2.9,30,35,45),
 (25, 'electricz',0.4,6,55,40,90),
 (26, 'electric',0.8,30,90,55,110),
 (133, 'grass',0.3,6.5,55,50,55),
 (152,'electric',0.9,6.4,49,65,45);
 
 #1) 몸무게가 가장많이 나가는 포켓몬번호
 /*select number,weight_rank
 from (select number ,rank() over(order by weight desc)as weight_rank from ability) sub
 where weight_rank = 1;*/
 select number
 from ability
 where weight = (select max(weight) from ability);
 
 #2) 속도가 모든 전기 포켓몬의 공격력보다 하나라도 작은 포켓몬의 번호
 select number
 from ability
 where speed < any (select attack from ability where type = 'electric');
 
 #3) 공격력이 방어력보다 큰 포켓몬이 있다면 모든 포켓몬의 이름
 /*select name
 from mypokemon
 left join ability
 on mypokemon.number = ability.number
 where attack > all (select defense from ability);*/
 select name
 from mypokemon
 where exists (select * from ability where attack >defense);
 
 