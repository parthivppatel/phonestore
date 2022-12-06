BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "phone_app_mobile" (
	"id"	integer NOT NULL,
	"brand"	varchar(100),
	"name"	varchar(100),
	"price"	integer,
	"network"	varchar(50),
	"display"	varchar(300),
	"os"	varchar(50),
	"description"	text,
	"img"	varchar(200) NOT NULL,
	"ram"	varchar(100),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "phone_app_mobile" ("id","brand","name","price","network","display","os","description","img","ram") VALUES (5,'realme','Realme Narzo 50i',27999,'4G','16.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of All Taxes
EMI starts at ₹358 Per Month.','../static/images/re1.jpg','2 GB RAM | 32 GB ROM'),
 (6,'realme','Realme C35',20999,'4G','16.76 cm (6.6 inch) Full HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹565. No Cost EMI available','../static/images/re2.jpg','4 GB RAM | 64 GB ROM'),
 (7,'realme','Realme C30',25999,'LTE','16.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹312','../static/images/re3.jpg','2 GB RAM | 32 GB ROM'),
 (8,'realme','Realme Narzo 50i PRIME',27999,'LTE','Display: 6.5 inch HD+ display with 400nits','Android 11','EMI starts at ₹430. No Cost EMI available ','../static/images/re4.jpg','4 GB RAM | 64 GB ROM'),
 (9,'realme','realme C33 ',17999,'5G','16.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹478.','../static/images/re5.jpg','3 GB RAM | 32 GB ROM'),
 (10,'realme','Realme 6 PRO',19999,'4G','Display: 6.5 inch HD+ display with 400nits','Android 11','EMI starts at ₹430. No Cost EMI available ','../static/images/re6.jpg','4 GB RAM | 64 GB ROM'),
 (11,'realme','realme X3 ',25999,'4G','17.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹488.','../static/images/re7.jpg','4 GB RAM | 32 GB ROM'),
 (12,'realme','Realme Nazro',28999,'4G','17.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of All Taxes
EMI starts at ₹758 Per Month.','../static/images/re8.jpg','4 GB RAM | 32 GB ROM'),
 (13,'realme','Realme C35',18999,'4G','16.76 cm (6.6 inch) Full HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹475. No Cost EMI available','../static/images/re9.jpg','4 GB RAM | 64 GB ROM'),
 (14,'realme','Realme x3',2999,'LTE','16.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹412','../static/images/re10.jpg','2 GB RAM | 32 GB ROM'),
 (15,'oppo','F21s Pro',15999,'LTE','16.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹1,051','../static/images/oppo1.jpg','8 GB RAM | 128 GB ROM'),
 (16,'oppo','OPPO Reno8 5G',20999,'4G','16.33 cm (6.43 inch) Full HD Display','Android 12.0','Inclusive of all taxes
EMI starts at ₹1,405','../static/images/oppo2.jpg','8 GB RAM | 128 GB ROM'),
 (17,'oppo','Oppo A17k',9999,'LTE','16.51 cm (6.5 inch) HD+ Display','Android 12','Inclusive of all taxes
EMI starts at ₹478','../static/images/oppo3.jpg','3 GB RAM | 64 GB ROM'),
 (18,'oppo','Oppo F21 Pro',17999,'4G','Display: 6.5 inch HD+ display with 400nits','Android 11','EMI starts at ₹1030. No Cost EMI available ','../static/images/oppo4.jpg',' 8 GB RAM | 128 GB ROM'),
 (19,'oppo','oppo A16k',12999,'4G','16.55cm (6.52") HD+ Big Screen','Android 11','Inclusive of all taxes
EMI starts at ₹578.','../static/images/oppo5.jpg','4 GB RAM | 32 GB ROM'),
 (20,'vivo','Vivo Y33T',17999,'4G','16.71cm (6.58") FHD+ Display ','Funtouch OS 12','Inclusive of All Taxes
EMI starts at ₹958 Per Month.','../static/images/vivo1.jpg','8GB RAM + 128GB Storage'),
 (21,'vivo','vivo Y22',14999,'5G','16.63 cm (6.55" inch) HD+ LCD Display','Funtouch OS 12','Inclusive of all taxes
EMI starts at ₹765. No Cost EMI available','../static/images/vivo2.jpg','4GB RAM | 64GB internal memory'),
 (22,'nokia','Nokia G11',11999,'2G,3 G,4G','6.5” (16.51 cm) display','Android 12','Inclusive of all taxes
EMI starts at ₹444','../static/images/nokia1.jpg','4GB RAM & 64GB internal storage'),
 (23,'nokia','Nokia G21',12999,'LTE','16.51 cm (6.5 inch) HD+ Display','Android 11 64bits','Inclusive of all taxes
EMI starts at ₹890. No Cost EMI available ','../static/images/nokia2.jpg','6GB RAM & 128GB'),
 (24,'redmi','Redmi 9A Sport',7499,'MIUI 12','16.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹788.','../static/images/redmi1.jpg','3 GB RAM | 32 GB ROM'),
 (25,'redmi','Redmi 9 Activ',8499,'LTE','MIUI 12, Android MIUI 12','Android 12','EMI starts at ₹530. No Cost EMI available ','../static/images/redmi2.jpg','4 GB RAM | 64 GB STORAGE'),
 (26,'plus','OnePlus Nord 2T',28999,'4G','17.51 cm (6.5 inch) HD+ Display','Android 11','Inclusive of all taxes
EMI starts at ₹688.','../static/images/plus1.jpg','8 GB RAM | 128 GB STORAGE'),
 (27,'plus','OnePlus Nord CE 2',28999,'5G','17.51 cm (6.5 inch) HD+ Display','OxygenOS','Inclusive of All Taxes
EMI starts at ₹958 Per Month.','../static/images/plus2.jpg','4 GB RAM | 64 GB STORAGE'),
 (28,'plus','OnePlus 6',16499,'5G','16.76 cm (6.6 inch) Full HD+ Display','Android','Inclusive of all taxes
EMI starts at ₹675. No Cost EMI available','../static/images/plus3.jpg','8GB RAM | 128GB Storage'),
 (29,'plus','OnePlus Nord 2T',12999,'4G','16.51 cm (6.5 inch) HD+ Display','OxygenOS','Inclusive of all taxes
EMI starts at ₹512','../static/images/plus4.jpg','4 GB RAM | 32 GB ROM'),
 (42,'iphone','Apple iPhone 14 Pro',139900,'5G','15.54 cm (6.1-inch) Super Retina XDR display','IOS','Inclusive of all taxes
EMI starts at ₹6,717.','../static/images/iphone1.jpg','6 GB RAM | 256 GB STORAGE'),
 (43,'iphone','Apple iPhone 13 ',74000,'5G','16.51 cm (6.5 inch) HD+ Display','IOS','Inclusive of all taxes
EMI starts at ₹4,444','../static/images/iphone2.jpg',NULL),
 (44,'iphone','Apple iPhone 11',55000,'5G','15.54 cm (6.1-inch) Super Retina XDR display','IOS','Inclusive of all taxes
EMI starts at ₹2,444','../static/images/iphone3.jpg',NULL),
 (45,'iphone','iPhone 12 ',89000,'5G','6.5” (16.51 cm) display','IOS','Inclusive of all taxes
EMI starts at ₹3,444','../static/images/iphone4.jpg',NULL),
 (46,'iphone','Apple iPhone 13 ',110000,'4G','15.54 cm (6.1-inch) Super Retina XDR display','IOS','Inclusive of all taxes
EMI starts at ₹7,444','../static/images/iphone5.jpg',NULL),
 (47,'iphone','Apple iPhone 14',40000,'5G','16.63 cm (6.55" inch) HD+ LCD Display','IOS','Inclusive of all taxes
EMI starts at ₹3,444','../static/images/iphone6.jpg',NULL);
COMMIT;
