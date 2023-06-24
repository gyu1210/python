Drop database if exists pokemon;
create database pokemon;
use pokemon;
create table mypokemon(
number int,
name varchar(20),
type varchar(20),
height float,
weight float,
attack float,
defense float,
speed float
);
insert into mypokemon (number,name, type, height, weight,
 attack, defense, speed)
 values(10, 'caterpie','bug',0.3,2.9,30,35,45),
 (25, 'pikachu','electric',0.4,6,55,40,90),
 (26, 'raichu','electric',0.8,30,90,55,110),
 (133, 'eevee', 'normal',0.3,6.5,55,50,55),
 (152,'chikorita','grass',0.9,6.4,49,65,45);
  select * from mypokemon;
  
  #1) 이브이의 타입은?
  use pokemon;
  select type
  from mypokemon
  where name = 'eevee';
  
  #2)캐터피의 공격력과 방어력은?
  use pokemon;
  select attack, defense
  from mypokemon
  where name = 'caterpie';

  #3) 몸무게가 6kg 보다큰 모든 포켓몬의 데이터? 
  select *
  from pokemon.mypokemon
  where weight > 6;
  
  #4) 키가 0.5m 보다 크고, 6kg 보다 크커나 같은 포켓몬 이름 
  select name
  from pokemon.mypokemon
  where height > 0.5 and weight >= 6; 
  
  #5) 공격력이 50미만이거나 방여력50미만 이름, 'weak_pokemon'으로 
  select name as weak_pokemon
  from pokemon.mypokemon
  where attack <50 or defense <50;
  
  #6) 노말타입이 아닌 포켓몬들의 데이터 전부
  select *
  from pokemon.mypokemon
  where not (type = 'normal');
  
  #7) 타입이 (nornal, fire,water,grass)중에 하나인 포켓몬드르이 이름,타입? 
  select name, type
  from pokemon.mypokemon
  where type in ('normal', 'fire','water','grass');
  
  #8) 공격력 40과60 사이 이름, 공격력
  select attack, name
  from pokemon.mypokemon
  where attack between 40 and 60;
  
  #9) 이름에 'e' 가 포함된 포켓몬 이름? 
  select name
  from pokemon.mypokemon
  where name like '%e%';
  
  #10) 이름에 'i'포함되고 속도50 이하인 포켓몬 데이터 전부 
  select *
  from pokemon.mypokemon
  where name like '%i%' and speed <= 50;
  
  #11) 이름이 'chu'로 끝나는 이름,키,몸무게는 ?
  select name,height,weight
  from pokemon.mypokemon
  where name like '%chu';
  
  #12) 이름이 'e'로 끝나고 방어력이 50미만인 이름, 방어력?
  select name, defense
  from pokemon.mypokemon
  where name like '%e' and defense <50;
  
  #13) 공격력과 방어력의 차이가 10이상인 이름,공격력,방어력 ?
  select name, attack, defense
  from pokemon.mypokemon
  where attack - defense >=10 or defense -attack >=10;
  
  #14) 능력치의 합 (attack+defense+speed)이 150이상인 포켓몬의 이름과 능력치의 합 = total
  select name, attack+defense+speed as 'total'
  from pokemon.mypokemon
  where attack+defense+speed >= 150;