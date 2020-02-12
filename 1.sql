CREATE DATABASE tests default CHARACTER SET UTF8;
CREATE TABLE `user_item` (
  `USERID` VARCHAR(20) NOT NULL ,
  `ITEMID` VARCHAR(45) NULL,
  `X_ITEM` FLOAT NULL DEFAULT 10,
  `Y_ITEM` FLOAT NULL DEFAULT 10,
  `Z_ITEM` INT NULL DEFAULT 99,
  `WIDTH` FLOAT NULL DEFAULT 50,
  `HEIGHT` FLOAT NULL DEFAULT 50
  );

insert into user_item values('admin','CAR', 10, 20,2, 10, 10);
insert into user_item values('admin','TREE', 40, 20,1,20,50);


CREATE TABLE `user_setting` (
  `USERID` VARCHAR(20) NOT NULL DEFAULT 'admin',
  `repo_color` varchar(45) DEFAULT '#ffffff'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into user_setting values('admin','#ffffff');


CREATE TABLE `tests`.`item` (
  `ITEMID` VARCHAR(20) NOT NULL,
  `ITEMDESC` VARCHAR(200) NULL);


insert into item values('Chao','차우차우는 중국에서 유래하였으며, 사자를 닮은 견종이다. 다부지고 짧은 체형에 균형이 잘 잡혀 있다. 조용하고 충성심이 강하다.');
insert into item values('Chiwawa','멕시코 출신으로 놀이나 장난을 좋아하지 않지만 질투심이 강해 주인을 독점하기를 바라며 다른 개와 상대할 경우에도 절대 지지 않으려는 성향이 강하다.');
insert into item values('Siberia','키 50~60cm, 체중 16~27kg의 중형견으로, 애틱허스키 또는 허스키라고도 한다. 에스키모개로서 북방 스피츠 계통의 품종이다.');
insert into item values('Sonata','현대 쏘나타는 1985년 출시 이후 현재까지 판매되고 있는 현대자동차의 중형차이자 대한민국의 대표적인 중형차이다. ');
insert into item values('Starex','현대자동차에서 1997년 3월 5일부터 생산 중인 후륜구동/4륜구동 중형 승합차.');
insert into item values('Avante','현대 아반떼는 현대자동차가 1995년 3월부터 시판하고 있는 준중형차이자 대한민국의 대표적인 준중형차이다. 대한민국에서는 엘란트라의 후속 차종으로 선보여 아반떼로 차명이 변경되었다.');
insert into item values('LG','LG PC 그램은 LG전자에서 개발한 Z930의 후속 제품으로 2014년 1월에 출시된 초기 제품 Z940기준 13.3 디스플레이에 무게가 이름 그대로 1kg도 안 되는 980그램(g)의 노트북이다. ');
insert into item values('Hansung','한국에서 가성비 끝판왕이라 불리는 노트북, 게임밍 노트북을 맞출때 최고의 성능을 자랑하나, 다른부분에서는 기대하지 않는 것이 좋다.');
insert into item values('Mac','맥북은 미국 애플사의 노트북 컴퓨터 브랜드및 시리즈이다. 맥북은 맥 라인업에 포함되며, 교육시장과 소비자시장을 공략한 제품이다.');
insert into item values('Sphinx','굉장히 원시적인 생김새와 스핑크스라는 이름 때문에 고대 이집트까지 연원이 거슬러 올라가는 유서 깊은 품종처럼 보일 수도 있지만, 실은 1960년대 캐나다에서 자연발생한 돌연변이 개체로부터 시작된 품종이라는 것이 정설이다.');
insert into item values('Scotishfold','고양이의 품종 중 하나. 동글동글하고 땅딸막한 외모로 세계적으로 가장 인기있는 품종 중 하나이며, 수요가 높아 몸값이 높다. 스코티시는 영국 스코틀랜드 출신을 의미하고 폴드는 접힌 것. 즉 귀가 접혔다는 것을 의미한다.');
insert into item values('Korea','흔히 코리안 쇼트헤어, 줄여서 코숏이라고도 부르는데, 한국의 토종 고양이들은 품종에 관한 관리, 개량, 분류 등을 당한 적이 없어서 공식적인 품종이 없고, 미국(아메리카)의 아메리칸 쇼트헤어에서 따온 일종의 은어이다. ');

