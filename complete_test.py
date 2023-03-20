from complete import is_tv

test_str = ("Eat.Drink.Man.Woman.1994.1080p.BluRay.DD2.0.x264-HDS\n"
	"Frozen.Planet.II.S01.2160p.UHD.BluRay.TrueHD.7.1.Atmos.HDR.x265-NOGRP\n"
	"Game.of.Thrones.S01-S08.2160p.UHD.BluRay.x265.10bit.HDR.TrueHD.7.1.Atmos-PTH\n"
	"Hanbun.Aoi.S01.2018.FOD.WEB-DL.1080p.H264.AAC-HDCTV\n"
	"Iron.Man.2008.2160p.HDR.UHD.BluRay.TrueHD.7.1.Atmos.2Audio.x265-10bit-HDS\n"
	"Iron.Man.2.2010.2160p.HDR.UHD.BluRay.TrueHD.7.1.Atmos.2Audio.x265-10bit-HDS\n"
	"Iron.Man.3.2013.2160p.HDR.UHD.BluRay.TrueHD.7.1.Atmos.2Audio.x265-10bit-HDS\n"
	"Lightyear.2022.2160p.Dovi.HDR.UHD.BluRay.TrueHD.7.1.Atmos.x265-10bit-HDS\n"
	"Marvel.Cinematic Universe.The.Infinity.Saga.23.Movies.Collection.2008-2019.UHD.BluRay.2160p.x265.10bit.HDR-PTH\n"
	"Moonfall.2022.2160p.WEB-DL.DDP5.1.Atmos.HDR.H.265-EVO\n"
	"The.Big.Bang.Theory.S01-12.1080p.Blu-Ray.AC3.x265.10bit-Yumi\n"
	"The.Ice.Age.Adventures.of.Buck.Wild.2022.2160p.WEB-DL.DDP5.1.Atmos.HDR.HEVC-TEPES.mkv\n"
	"The.Makanai.Cooking.for.the.Maiko.House.S01.1080p.NF.WEB-DL.DDP.5.1.H264-HHWEB\n"
	"The.Matrix.Resurrections.2021.Hybrid.2160p.WEB-DL.HEVC.Atmos.DDP5.1-HDH\n"
	"The.Secret.Life.of.Pets.2016.2160p.HDR.UHD.BluRay.TrueHD.7.1.Atmos.4Audio.x265-10bit-HDS\n"
	"The.Secret.Life.of.Pets.2.2019.2160p.HDR.UHD.BluRay.TrueHD.7.1.Atmos.x265-10bit-HDS\n"
	"Tokyo.Godfathers.2003.1080p.BluRay.DTS.x265-10bit-HDS\n"
	"Turning.Red.2022.Disney+.WEB-DL.4k.HEVC.HDR.DDP-AREY.mkv\n"
	"We.Made.a.Beautiful.Bouquet.2021.1080p.BluRay.x264.DTS-WiKi\n"
	"Westworld.S04E01.1080p.HMAX.WEB-DL.DD5.1.x264-NTb\n"
	"With.You.2016.S01.Complete.WEB-DL.2160p.H264.AAC2.0-PureTV\n"
	"Yes.Prime.Minister.COMPLETE.PACK.DVD.x264-P2P\n"
	"三体.Three.Body.S01.2023.2160p.WEB-DL.DDP5.1.Atmos.DV.H.265-HDSWEB\n"
	"三体广播剧.The.Three.Body.Problem.Radio.Play.2021.Complete.96Kbps.MP3\n"
	"利刃出鞘2.Glass.Onion.A.Knives.Out.Mystery.2022.2160p.HDR.DV.WEB-DL.Atmos.DDP5.1-AQLJ@HDSky\n"
	"力量之戒.The.Lord.of.the.Rings.The.Rings.of.Power.S01.2022.2160p.WEB-DL.DDP5.1.Atmos.HDR.DV.H265-AQLJ@HDSky\n"
	"北鼻异想世界.The.Wonderful.World.of.Babies.2018.WEB-DL.1080p.H265.AAC.2Audio-HDSWEB\n"
	"大明王朝1566.2007.S01\n"
	"奇异博士2.Doctor.Strange.in.the.Multiverse.of.Madness.2022.V3.IMAX.2160p.WEB-DL.DDP5.1.Atmos.HDR.HEVC-AQLJ@HDSky\n"
	"奇异博士（系列） [boxset]\n"
	"女王的棋局 The.Queen's.Gambit.2020.1080p.NF.WEBRip.AAC5.1.x264-HDSWEB\n"
	"婚礼\n"
	"新蝙蝠侠.The.Batman.2022.2160p.UHD.Blu-ray.HEVC.Atmos.TrueHD7.1-CHN@HDSky\n"
	"显微镜下的大明之丝绢案.Under.The.Microscope.S01.2023.2160p.WEB-DL.AAC.H265-HDSWEB\n"
	"最后生还者.The.Last.of.Us.S01.2023.WEB-DL.2160p.H265.Atmos.DDP5.1.HDR.DV-HDSWEB\n"
	"爱宠大机密（系列） [boxset]\n"
	"狂飙.The.Knockout.S01.2023.2160p.WEB-DL.H265.AAC-HHWEB\n"
	"狙击手.Snipers.2022.60fps.2160p.WEB-DL.DDP5.1.AAC.H265-HDSWEB.mkv\n"
	"王更新 - 明朝那些事儿 268全集\n"
	"短剧开始啦.The.Skit.Begins.S01.2021.1080p.FriDay.WEB-DL.AAC2.0.H264-HDSWEB\n"
	"穿靴子的猫2.Puss.in.Boots.The.Last.Wish.2022.2160p.MA.WEB-DL.DDP5.1.Atmos.HEVC.HDR.DV-AQLJ@HDSky\n"
	"美国队长（系列） [boxset]\n"
	"蚁人（系列） [boxset]\n"
	"请回答1988.Reply.1988.2015.1080p.NF.WEB-DL.DD2.0.x264-HDSWEB\n"
	"风味人间 第四季.Once.Upon.A.Bite.S04.2022.2160p.WEB-DL.DDP2.0.AAC2.0.H.265-HDSWEB\n"
	"黑亚当.Black.Adam.2022.2160p.MA.WEB-DL.DDP5.1.Atmos.HDR.DV.HEVC-AQLJ@HDSky\n"
	"黑豹2.Black.Panther.Wakanda.Forever.2022.IMAX.2160p.WEB-DL.H265.HDR.DV.TrueHD7.1.Atmos-AQLJ@HDSky\n"
	"黑豹（系列） [boxset]\n"
	"龙之家族.House.of.the.Dragon.S01.2022.2160p.HMAX.WEB-DL.DDP5.1.Atmos.HDR.DV.HEVC-AQLJ@HDSky")

l = test_str.split('\n')

for x in l:
    if is_tv(x):
        print('tv: [{}]'.format(x))
    else:
        print('movie: [{}]'.format(x) )