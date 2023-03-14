INSERT INTO public.store_producer(
	id, name)
	VALUES 
	(1, 'Jon Favreau'),
	(2, 'James Cameron'),
	(3, 'Peter Farrelly'),
	(4, 'Quentin Tarantino'),
	(5, 'Steven Spielberg'),
	(6, 'Borthers Russo'),
	(7, 'Chad Stahelski'),
	(8, 'Bong Joon Ho'),
	(9, 'Borthers Russo'),
	(10, 'Todd Phillips')
	;
	
INSERT INTO public.store_actor(
	id, name, gender, country)
	VALUES 
	(1, 'Robert Downey Jr.', 'M', 'USA'),
	(2, 'Chris Evans', 'M', 'USA'),
	(3, 'Tye Sheridan', 'M', 'USA'),
	(4, 'Sam Worthington', 'M', 'UK'),
	(5, 'Christoph Waltz', 'M', 'Austria'),
	(6, 'Leonardo DiCaprio', 'M', 'USA'),
	(7, 'Brad Pitt', 'M', 'USA'),
	(8, 'Mahershala Ali', 'M', 'USA'),
	(9, 'Keanu Reeves', 'M', 'Lebanon'),
	(10, 'Joaquin Phoenix', 'M', 'USA')
	;

INSERT INTO public.store_genre(
	id, name)
	VALUES 
	(1, 'Drama'),
	(2, 'Sci-fi'),
	(3, 'Comedy'),
	(4, 'Action'),
	(5, 'Biography'),
	(6, 'Horror'),
	(7, 'Romance'),
	(8, 'Animation')
	;

INSERT INTO public.store_product(
	id, name, price, digital, image, genre_id, producer_id, relese_date, title)
	VALUES 
	(1, 'Alita Battle Angel', 20, True, '/movies/Alita_Battle_Angel.png', 2, 2, '02-19-2019', 'A deactivated cyborg is revived, but can not remember anything of her past and goes on a quest to find out who she is.'),
	(2, 'Avatar', 20, True, '/movies/avatar.jpeg', 2, 2, 'dec-18-2009', 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.')
	(3, 'Avengers: Endgame', 20, True, '/movies/Avengers-Endgame.jpg', 4, 6, 'apr-26-2019', 'After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos actions and restore balance to the universe.'),
	(4, 'Green Book', 20, True, '/movies/greenbook.jpg', 5, 3, 'nov-18-2018', 'A working-class Italian-American bouncer becomes the driver of an African-American classical pianist on a tour of venues through the 1960s American South.'),
	(5, 'Iron man 1', 20, True, '/movies/Iron-Man-1.jpg', 4, 1, 'may-2-2008', 'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.'),
	(6, 'John Wick: Chapter 3 - Parabellum', 20, True, '/movies/johnwick3.jpg', 4, 7, 'may-18-2019', 'John Wick is on the run after killing a member of the international assassins guild, and with a $14 million price tag on his head, he is the target of hit men and women everywhere.'),
	(7, 'Joker', 20, True, '/movies/joker.jpg', 1, 10, 'oct-4-2019', 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.'),
	(8, 'Once Upon a Time... In Hollywood', 20, True, '/movies/once-upon-a-time-in-hollywood.jpg', 3, 4, 'jul-26-2019', 'A faded television actor and his stunt double strive to achieve fame and success in the final years of Hollywood is Golden Age in 1969 Los Angeles.'),
	(9, 'Parasite', 20, True, '/movies/parasite.jpg', 1, 8, 'nov-08-2019', 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.'),
	(10, 'Ready Player One', 20, True, '/movies/ready_player_one.jfif', 2, 5, 'mar-29-2018', 'When the creator of a virtual reality called the OASIS dies, he makes a posthumous challenge to all OASIS users to find his Easter Egg, which will give the finder his fortune and control of his world.'),
	(11, 'The Lion King', 20, True, '/movies/TheLionKing.jpg', 8, 1, 'jul-19-2019', 'After the murder of his father, a young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.')
	
	;

INSERT INTO public.store_perform(
	id, actor_id, movie_id)
	VALUES 
	(1, 1, 3),
	(2, 1, 5),
	(3, 2, 3),
	(4, 3, 10),
	(5, 4, 2),
	(6, 5, 1),
	(7, 6, 8),
	(8, 7, 8),
	(9, 8, 4),
	(10, 9, 6),
	(11, 10, 7)
	;