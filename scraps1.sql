-- MySQL dump 10.16  Distrib 10.1.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: scraps
-- ------------------------------------------------------
-- Server version	10.1.34-MariaDB-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ecmr`
--

DROP TABLE IF EXISTS `ecmr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ecmr` (
  `id_ecmr` int(2) NOT NULL,
  `nama_ecmr` varchar(50) NOT NULL,
  PRIMARY KEY (`id_ecmr`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecmr`
--

LOCK TABLES `ecmr` WRITE;
/*!40000 ALTER TABLE `ecmr` DISABLE KEYS */;
INSERT INTO `ecmr` VALUES (1,'OLX');
/*!40000 ALTER TABLE `ecmr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produk`
--

DROP TABLE IF EXISTS `produk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produk` (
  `id_barang` varchar(15) NOT NULL,
  `judul` varchar(50) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `deskripsi` varchar(500) DEFAULT NULL,
  `link` varchar(255) NOT NULL,
  `link_img` varchar(255) NOT NULL,
  `id_ecmr` int(2) NOT NULL,
  PRIMARY KEY (`id_barang`),
  KEY `fk_ecmrid` (`id_ecmr`),
  CONSTRAINT `fk_ecmrid` FOREIGN KEY (`id_ecmr`) REFERENCES `ecmr` (`id_ecmr`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produk`
--

LOCK TABLES `produk` WRITE;
/*!40000 ALTER TABLE `produk` DISABLE KEYS */;
INSERT INTO `produk` VALUES ('501771130','Jual LG G4 Full Se',1400000,'jual lg g4 full set plus baterai tambahan dll mulus normal harga NETT bisa di cek lgsg kondisi brg nya fast respon WA COD Kedawung','','',1),('501774608','LG G4 Dual SIM 4G Muluss',1125000,'Jual LG G4 3 32 Mulus 90 95 Bisa 4G semua sim indo Kamera seperti SLR Dual SIM 4G Sudah terpasang tempered glass bonus hardcase Spek Layar 5 5 1440x2560px kamera 16mp jernih video 4k Qualcomm Snapdragon 808 Hexa Core Internal 32GB Ram 3GB untuk lebih lengkapnya silahkan cek google Minat Hub No WA yang sudah tertera Untuk SMS maaf slowres diutamakan WA Nego wajar ya gan cod sekitaran veteran suhat Terima Kasih','','',1),('501775255','LG V20 4/64 Fullset Mulus 4G Lanca',2320000,'Jual LG V20 Ex Internasional 4 64 Mulus 92 95 4G semua sim indo Fullset OEM Single SIM Sudah terpasang tempered glass Fingerprint aman Spek Qualcomm Snapdragon 820 Layar 5 7 1440x2560px Kamera Belakang Dual Kamera 16mp f 1 8 8mp f 2 4 Video 4K Stereo sound rec Kamera Depan 5mp f 1 9 USB Type C Internal 64GB Ram 4GB Micro SD up to 512gb spek lebih lengkapnya silahkan cek di google Nego Wajar ya gan Cod sekitar veteran suhat Minat Hub No WA yang sudah tertera Untuk SMS Slowres yaa Terima Kasih','','',1),('502321767','Jual cepat LG K10,Ram 2,internal 16',1050000,'jual cepat LG KA 10 full set minus headset Ram 2 5 3 inc mulus nego','','',1),('502351359','Lg g4 leather dual sim bisa',1250000,'dijual lg g4 leather ram 3 32 dual sim 4g mesin normal camera bening batre awet SN 610 aman anti botlop fisik lumayan mulus kelengkapan hp cas dusbok di jual 1250 bisa tt asal cocok cod malang kota wa profil fast reapon','','',1),('502386953','Jual cepat LG K 10 Ram 2,internal 16.5 inc',1050000,'jual cepat LG K10 fullset minus headset Ram 2 5 inc normal nego','','',1),('502442834','LG G5 SE ex garansi resmi, GOLD',1550000,'kemulusan 93 aksesoris semua berfungsi normal HP semua berfungsi normal free case armor yg bagus dan ga macho seharga 80rb ini barang resmi ya selama saya pegang tak ada kendala 1 pun jangan samakan dengan yg garansi luar yg cacat dan sering bootlop apabila minat WA saja ya kalo sms ga bakal direspon maklum ga punya pulsa','','',1),('502540258','LG V20 MINI second original garansi 2 minggu',2400000,'Ready Taraphone malang boskuu Kondisi 98 mulus Layar no SHADOW bisa semua sim indonesia FU Jaringan 4G josss LCD casing pasti orignal bisa di cek sepuasnya Harga sama semua Warna GARANSI TOKO 2 MINGGU RETUR GANTI UNIT BARU 1 MINGGU SPESIFIKASI Network Technology GSM HSPA LTE 2G bands GSM 850 900 1800 1900 SIM 1 SIM 2 dual SIM model only 3G bands HSDPA 850 900 1700 AWS 1900 2100 4G bands LTE band 1 2100 2 1900 3 1800 4 1700 2100 5 850 7 260Speed HSPA 42 2 5 76 Mbps LTE A Cat6 Cat9 3CA or LTE A Ca','','',1),('502540426','LG NEXUS 5 second original garansi',1350000,'Ready Taraphone malang boskuu Kondisi 98 mulus Layar no SHADOW bisa semua sim indonesia FU Jaringan 4G josss LCD casing pasti orignal bisa di cek sepuasnya Harga sama semua Warna GARANSI TOKO 2 MINGGU RETUR GANTI UNIT BARU 1 MINGGU SPESIFIKASI Network Technology GSM CDMA HSPA LTE 2G bands GSM 850 900 1800 1900 all versions CDMA 800 1900 North American version 3G bands HSDPA 80North American version HSDPA 850 900 1700 1900 2100 4G bands LTE band 1 2100 2 1900 4 1700 2100 5 850 17 700 19 800 25 19','','',1),('502599185','Lg k8 warna biru',900000,'dijual hp lg k8 masih mulus dan lecet pemakaian saja ram 1 5 8 android m 6 hp dosbuuk charge kitab hardcase harga pas 900 ribu cod suhat saja','','',1),('502748832','Lg v20 dual sim bos resmi indo 4/64',2700000,'normal poll fullset spekk game bos tt s7 edge siap nambah bos nego alus','','',1),('502782496','LG G4 Dua kartu 1.2',1200000,'LG G4 Dua kartu ram 3 mulusss lengkap dusbook minat langsung wa sms','','',1),('502792416','LG Nexus 5 Black Mulus Garansi',1325000,'Taraphone malang Ready LG nexus 5 black BATANGAN ya bos mulus semua normal bosku Kamera jernih Garansi 2 minggu Alamat jalan soekarno hatta no 83c depan RM ocean garden suhat malang Jangan lupa mampir dilapak taraphone yang baru ya bosku Harga nego aja yaaa bosku Selebihnya silakan cek langsung di lapak pilih sendiri ya bosku Supaya tidak ada dusta diantara kita TARAPHONE MELAYANI COD surabaya dan bali Tidak menerima tukar tambah atau jual selain pembelian dari taraphone Nomor tlp wa admin panji','','',1),('502793850','LG G4 resmi lengkap mulus',1450000,'jual lg g4 garansi resmi indonesia bukan at t ato docomo y sudah anti bootloop karna sempat dapat retur resmi dr lg gan komplit handsfree AKG original ram 3 rom 32 kamera super duper ngeri gan komplit dengan nota pembelian juga gan hehehe kondisi super normal mulus tanpa cacat langsung pantau aja gan perum bumi asri sengkaling Blok CC No 11 malang','','',1);
/*!40000 ALTER TABLE `produk` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-04 12:05:20
