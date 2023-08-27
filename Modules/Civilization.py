import nextcord

from .abcModule import abcModule
from exc import BotException


class CivilizationModule(abcModule):
    def __init__(self, client):
        super().__init__(client)
        self.commands = {"civ": self.cmd_civilization}
        self.civilizations = {
            "america": "1065754537178181661, AmericaAbrahamLincoln, Abraham-Lincoln, Abraham, Lincoln, Abe - 1065754539308879973, AmericaTeddyBullMoose, Teddy-BM, TeddyBM, BullMoose - 1065754542630764674, AmericaTeddyRoughRider, Teddy-RR, TeddyRR, RoughRider.",
            "arabia": "1065754545470324897, ArabiaSultan, Saladin-Sultan, Sultan, SaladinS, Saladin-S - 1065754549350060163, ArabiaSaladin , Saladin-Vizier, Vizier, SaladinV, Saladin-V.",
            "australia": "1065754551900188703, AustraliaJohnCurtin, Australia, John, Curtin.",
            "aztec": "1065754555024937090, AztecMontezuma, Aztec, Montezuma.",
            "babylon": "1065754557122084918, BabylonHammurabi, Babylon, Hammurabi.",
            "brazil": "1065754566492180560, BrazilPedroII, Brazil, Pedro - 1065754579976855572, ChinaQinShiHuang, Qin-Mandate-of-Heaven, QinMandateofHeaven, Mandate of Heaven, Qin Mandate of Heaven, Qin-M,QinM - 1065754582816395436, ChinaQinUnifier, Qin-Unifier, QinUnifier, Unifier, Qin-U, QinU - 1065754586494808144, ChinaWuZetian, Wu-Zetian, Wu Zetian, WuZetian - 1065754589984469022, ChinaYongle, Yongle.",
            "byzantine": "1065754570178953316, ByzantiumBasil, Byzantium, Basil - 1085884322013249666, ByzantiumTheodora, Theodora.",
            "canada": "1065754572762648707, CanadaWilfrid, Canada, Wilfrid, Wilfrid-Laurier, WilfirLaurier.",
            "china": "1065754575824494745, ChinaKublaiKhan, Kublai-China, KublaiChina, KublaiC.",
            "colombia": "1065754592182272030, GranColombiaSimonBolivar, Gran-Colombia, Colombia, GrandColombia, GranColombia, Simon, Bolivar, Grand-Combombia, Columbia.",
            "cree": "1065754595873267832, CreePoundmaker, Cree, Poundmaker.",
            "dutch": "1065754599077707807, DutchWilhelmina, Netherlands, Wilhelmina, Netherland, Dutch.",
            "egypt": "1065754602106011658, EgyptCleopatra, Egypt, Cleopatra - 1076186904799748178, EgyptPtolemaicCleopatra, Ptolemaic-Cleopatra, Cleopatra-P - 1076186907668648010, EgyptRamses, Ramses.",
            "england": "1065754605671166076. England Eleanor, Eleanor-En, EleanorEn, Eleanor-England, Eleanor-E, EleanorE - 1065754609093705838, EnglandVictoria, Victoria - 1088220086441103461, EnglandVictoriaageofsteam, Victoria age of steam, Victoria-steam, Victoria-age-of-steam, Victoria-S - 1088220081340829778, EnglandElizabethI, ElizabethI, Elizabeth.",
            "ethiopia": "1065754611706757232, EthiopiaMenelik, Ethiopia, Menelik.",
            "france": "1065756600314372166, FranceCatherineBlackQueen, Catherine-BQ, CatherineBQ, BlackQueen, BQ, France-BQ - 1065756603728547871, FranceCatherineMagnificent, Catherine-Magnificence, Magnificent, Magnificence, Catherine-M, France-M - 1065756606102503434, FranceEleanor, Eleanor-Fr, EleanorFr, Eleanor-France, Eleanor-F, EleanorF.",
            "gaul": "1065756609470546051, GaulAmbiorix, Gaul, Ambiorix.",
            "georgia": "1065756611865493605, GeorgiaTamar, Georgia, Tamar.",
            "germany": "1065756615371915365, GermanyFrederickBarbarossa, Germany, Frederick, Barbarossa - 1085884317135290379, GermanyLudwigII, Ludwig, LudwigII, Ludwig-II.",
            "greece": "1065756618928701440, GreeceGorgo, Gorgo - 1065756622586138705, GreecePericles, Pericles.",
            "america": "1065756625023021167, HungaryMatthias, Hungary, Matthias, MatthiasCorvinus.",
            "inca": "1065756628630118400, IncaPachacuti, Inca, Pachacuti, Incas.",
            "india": "1065756632140750889, IndiaChandragupta, Chandragupta, Chandra - 1065756634363744356, IndiaGandhi, Gandhi.",
            "indonesia": "1065756637794680963, IndonesiaGitarja, Indonesia, Gitarja.",
            "japan": "1065756641313706075, JapanHojoTokimune, Hojo-Tokimune, Japan, Hojo, Tokimune - 1065756643817705522, JapanTokugawa, Tokugawa, Tokugawa Leyasu.",
            "khmer": "1065756647630311444, KhmerJayavarmanVII, Khmer, Jayavarman.",
            "kongo": "1065756649979134042, KongoMvembaANzinga, Mvemba-a-Nzinga, Mvemba, Mvemba Nzinga, Mvemba-Nzinga - 1065756652797689898, KongoMbande, Mbande, Nzinga, Nzinga Mbande, Nzinga-Mbande.",
            "korea": "1065756656476098672, KoreaSeondeok, Korea, Seondeok - 1085884319907713087, KoreaSejong, Sejong .",
            "macedon": "1065756660775260350, MacedonAlexander, Macedon, Alexander.",
            "mali": "1065756664608854127, MaliMansa, Mali, Mansa, MansaMusa - 1076186902098616422, MaliSundiataKeita, Sundiata-Keita, SundiataKeita, Sundiata, Sundiata-K.",
            "maori": "1065756667351945246, MaoriKupe, Maori, Kupe.",
            "mapuche": "1065756670652854302, MapucheLautaro, Mapuche, Lautaro.",
            "maya": "1065756674322878474, MayaLadySixSky, Maya, Lady-Six, Mayas, LadySixSky.",
            "mongolia": "1065756676621344778, MongoliaGenghisKhan, Genghis-Khan, Genghis, GenghisKhan - 1065756680144568320, MongoliaKublaiKhan, Kublai-Mongolia, KublaiMongolia, KublaiM.",
            "norway": "1065756683818774619, NorwayHaraldHardrada, Norway, Harald, Hardrada - 1088220083354091602, NorwayHaraldHardradaVarangian, Harald-Varangian, Harald-V, Harald III, Harald-III.",
            "nubia": "1065811497181261894, NubiaAmanitore, Nubia, Amanitore.",
            "ottoman": "1065811501052596378, OttomanSuleiman, Suleiman-Kanuni, Suleiman-K, SuleimanK, Kanuni, Ottoman-K, OttomanK, - 1065811503514648576, OttomanMuhtesem, Suleiman-Muhtesem, Suleiman-M, SuleimanM, Muhtesem, Ottoman-M, OttomanM.",
            "persia": "1065811506702327919, PersiaCyrus, Persia, Cyrus, Persia-C, PersiaC - 1065811511118942258, PersiaNader, Nader-Shah, Nader Shah, Nader, Persia-N, PersiaN.",
            "phoenicia": "1065811513794904164, PhoeniciaDido, Phoenicia, Dido.",
            "poland": "1065811517288755260, PolandJadwiga, Poland, Jadwiga.",
            "portugal": "1065811521378197524, PortugalJoaoIII, Portugal, Joao.",
            "rome": "1065811525119528981, RomeCaesar, Julius-Caesar, JuliusCaesar, Julius, Caesar - 1065811529624199319, RomeTrajan, Rome, Trajan. ",
            "russia": "1065811532656689162, RussiaPeterTheGreat, Russia, Peter.",
            "scotland": "1065811537303969913, ScotlandRobertTheBruce, Scotland, Robert, Bruce.",
            "scythia": "1065811542446194759, ScythiaTomyris, Scythia, Tomyris.",
            "spain": "1065811545906483220, SpainPhilipII, Spain, Philip.",
            "sumeria": "292492522905927681, SumeriaGilgamesh, Sumeria, Gilgamesh.",
            "sweden": "537787897353601045, SwedenKristina, Sweden, Kristina.",
            "vietnam": "804867658263953428, VietnamBaTrieu, Vietnam, Ba-Trieu.",
            "zulu": "ZuluShaka, Zulu, Shaka, Zulus.",
        }

    async def cmd_civilization(self, *args: str, channel, message, **_):
        if not args:
            await channel.send("Please specify a civilization name, e.g., `.civ rome`.", delete_after=10.0)
            return

        civ_name = args[0].lower()
        civ_description = self.civilizations.get(civ_name)

        if civ_description:
            await channel.send(f"**{civ_name.capitalize()} names**: {civ_description}", delete_after=240.0)
            await message.delete()
        else:
            await channel.send(f"No information found for {civ_name.capitalize()} Civilization.")
