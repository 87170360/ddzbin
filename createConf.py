#coding=utf-8

import types
import collections

conf_dir="./conf/"
pid_dir="./pid/"
log_dir="./log/"


def DictToJson(dict_content):
	list_item=[]
	for (k,v) in dict_content.items():
		str_k=""
		if type(k) is types.StringType: 
			str_k="\"%s\""%k
		else:
			str_k=str(k)
	
		if type(v) is types.StringType:
			str_v="\"%s\""%v
		elif type(v) is types.DictType:
			str_v=DictToJson(v)
		else:
			str_v=str(v)

		list_item.append(str_k+":"+str_v)

	result_str=",".join(list_item)

	return  "{"+result_str+"}"

venue_cfg={
		"hl":{
			"low": {
				"port": { "start":8500, 	 "nu":1, "name":"low",   "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":10, "doubletime":10, "outtime":25, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3,
                    "roomscore":20, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:1001"
					},
				},

			"middle":{
				"port":{ "start":8600, "nu":1,  "name":"middle","host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":10, "doubletime":10, "outtime":25, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3,
                    "roomscore":60, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:1002"
					},
				},

			"high":{
				"port":{ "start":8700, 	 "nu":1 , "name":"high",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":10, "doubletime":10, "outtime":25, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3,
                    "roomscore":80, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:1003"
					},
				},
			"master":{
				"port":{ "start":8750, 	 "nu":1 , "name":"master",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":10, "doubletime":10, "outtime":25, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3,
                    "roomscore":80, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:1004"
					},
				},
			},
		"lz":{
			"low": {
				"port": { "start":8800, 	 "nu":1, "name":"low",   "host":"0.0.0.0" },
				"table":{
                    "begin": 1, "end": 1000, 
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:2001"
					},
				},

			"middle":{
				"port":{ "start":8900, "nu":1,  "name":"middle","host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:2002"
					},
				},

			"high":{
				"port":{ "start":9000, 	 "nu":1 , "name":"high",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:2003"
					},
				},
			"master":{
				"port":{ "start":8750, 	 "nu":1 , "name":"master",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":10, "doubletime":10, "outtime":25, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3,
                    "roomscore":80, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "venuename":"venue:2004"
					},
				},
			},
		"bs":{
			"low": {
				"port": { "start":9200, 	 "nu":1, "name":"low",   "host":"0.0.0.0" },
				"table":{
                    "begin": 1, "end": 1000, 
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "bill":1, "venuename":"venue:3001"
					},
				},

			"middle":{
				"port":{ "start":9300, "nu":1,  "name":"middle","host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "bill":1, "venuename":"venue:3002"
					},
				},

			"high":{
				"port":{ "start":9400, 	 "nu":1 , "name":"high",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "bill":1, "venuename":"venue:3003"
					},
				},
			"master":{
				"port":{ "start":9400, 	 "nu":1 , "name":"high",  "host":"0.0.0.0" },
				"table":{
					"begin": 1, "end": 1000,
                    "calltime":300, "doubletime":300, "outtime":300, "second_outtime":5, "kicktime":1, "updatetime":1, "showtime":3, "grabtime":10,
                    "roomscore":10, "roomtax":10, "allowancemoney":3000, "motionmoney":500, "roomlimit":5000, "bill":1, "venuename":"venue:3004"
					},
				},
			},
		}

sql_cfg={
		"host":"127.0.0.1",
		"port":3306,
		"user":"zjh_game",
		"pass":"zjh_game",
		"dbname":"zjh_game"
		}

sub_redis_cfg={
		"host":"127.0.0.1",
		"portStart":6200,
		"nu":1,
		"pass":"wszgame"
		}

pub_redis_cfg={
		"host":"127.0.0.1",
		"portStart":6200,
		"nu":1,
		"pass":"wszgame"
		}



data_redis_cfg={
		"host":"127.0.0.1",
		"portStart":6000,
		"nu":10,
		"pass":"wszgame"
		}

eventlog_redis_cfg={
		"host":"127.0.0.1",
		"port":6200,
		"pass":"wszgame"
		}

cache_redis_cfg={
		"host":"127.0.0.1",
		"port":6100,
		"pass":"wszgame"
		}

speaker_redis_cfg={
		"host":"127.0.0.1",
		"port":6200,
		"pass":"wszgame"
		}


logfile_cfg={
		"level": 5,
		"console": 0,
		"rotate": 1,
		"max_size": 1073741824,
		"max_file": 10
		}


game_template_str="""\t"game":{ "host":"%s", "port":%d }"""

redis_template_str="""{ "host":"%s", "port":%d, "pass":"%s" }"""

log_template_str="""\t"log":{"log_file":"%s","level":%d,"console":%d,"rotate":%d,"max_size":%d,"max_file":%d}"""

data_redis_str="""\t"main-db":[\n"""
str_list=[]
for i in range(data_redis_cfg["portStart"],data_redis_cfg["portStart"]+data_redis_cfg["nu"]):
	str_list.append("\t\t"+redis_template_str%(data_redis_cfg["host"],i,data_redis_cfg["pass"]))
data_redis_str+=",\n".join(str_list)
data_redis_str+="\n\t]"

sub_redis_str="""\t"sub-db":[\n"""
str_list=[]
for i in range(sub_redis_cfg["portStart"],sub_redis_cfg["portStart"]+sub_redis_cfg["nu"]):
	str_list.append("\t\t"+redis_template_str%(sub_redis_cfg["host"],i,sub_redis_cfg["pass"]))

sub_redis_str+=",\n".join(str_list)
sub_redis_str+="\n\t]"

pub_redis_str="""\t"pub-db":[\n"""
str_list=[]
for i in range(pub_redis_cfg["portStart"],pub_redis_cfg["portStart"]+pub_redis_cfg["nu"]):
	str_list.append( "\t\t"+redis_template_str%(pub_redis_cfg["host"],i,pub_redis_cfg["pass"]))

pub_redis_str+=",\n".join(str_list)
pub_redis_str+="\n\t]"

eventlog_redis_str="""\t"eventlog-db":{"host":"%s","port":%d,"pass":"%s"}"""%(eventlog_redis_cfg["host"],eventlog_redis_cfg["port"],eventlog_redis_cfg["pass"])

cache_redis_str="""\t"cache-db":{"host":"%s","port":%d,"pass":"%s"}"""%(cache_redis_cfg["host"],cache_redis_cfg["port"],cache_redis_cfg["pass"])

speaker_redis_str="""\t"speaker-db":{"host":"%s","port":%d,"pass":"%s"}"""%(speaker_redis_cfg["host"],speaker_redis_cfg["port"],speaker_redis_cfg["pass"])

#hlddz
def create_hlddz(venue_name,info):
	for k,v in info.items():
		port=v["port"]
		for i in range(port["start"],port["start"]+port["nu"]):
			name=venue_name+"ddz_"+k+str(i-port["start"])

			file_content="{\n"

			#self 
			file_content+="""\t"self":"%s" """%(conf_dir+name+".conf")+",\n"


			#pid 
			file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

			#log 
			log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])

			file_content+=log_str+",\n"


			#game 
			file_content+=game_template_str%(port["host"],i)+",\n"

			#redis
			file_content+=data_redis_str+",\n"

			#event log 
			file_content+=eventlog_redis_str+",\n"

			file_content+=cache_redis_str+",\n"

			table_str="\t\"tables\":{"
			for tk,tv in v["table"].items():
				if type(tv) == str:
					table_str+=""""%s":"%s","""%(tk,tv)
				else :
					table_str+=""""%s":%d,"""%(tk,tv)

			table_str+=""""xxxx":"xxxx"}\n"""

			file_content+=table_str

			file_content+="}\n"



			fd=open(conf_dir+name+".conf","w+")
			fd.write(file_content)
			fd.close()

			print file_content

#lzddz
def create_lzddz(venue_name,info):
	for k,v in info.items():
		port=v["port"]
		for i in range(port["start"],port["start"]+port["nu"]):
			name=venue_name+"ddz_"+k+str(i-port["start"])

			file_content="{\n"

			#self 
			file_content+="""\t"self":"%s" """%(conf_dir+name+".conf")+",\n"


			#pid 
			file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

			#log 
			log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])

			file_content+=log_str+",\n"


			#game 
			file_content+=game_template_str%(port["host"],i)+",\n"

			#redis
			file_content+=data_redis_str+",\n"

			#event log 
			file_content+=eventlog_redis_str+",\n"

			file_content+=cache_redis_str+",\n"

			table_str="\t\"tables\":{"
			for tk,tv in v["table"].items():
				if type(tv) == str:
					table_str+=""""%s":"%s","""%(tk,tv)
				else :
					table_str+=""""%s":%d,"""%(tk,tv)

			table_str+=""""xxxx":"xxxx"}\n"""

			file_content+=table_str

			file_content+="}\n"



			fd=open(conf_dir+name+".conf","w+")
			fd.write(file_content)
			fd.close()

			print file_content

#bsddz
def create_bsddz(venue_name,info):
	for k,v in info.items():
		port=v["port"]
		for i in range(port["start"],port["start"]+port["nu"]):
			name=venue_name+"ddz_"+k+str(i-port["start"])

			file_content="{\n"

			#self 
			file_content+="""\t"self":"%s" """%(conf_dir+name+".conf")+",\n"


			#pid 
			file_content+="""\t"pid_file":"%s" """%(pid_dir+name+".pid")+",\n"

			#log 
			log_str=log_template_str%(log_dir+name+".log",logfile_cfg["level"],logfile_cfg["console"],logfile_cfg["rotate"],logfile_cfg["max_size"],logfile_cfg["max_file"])

			file_content+=log_str+",\n"


			#game 
			file_content+=game_template_str%(port["host"],i)+",\n"

			#redis
			file_content+=data_redis_str+",\n"

			#event log 
			file_content+=eventlog_redis_str+",\n"

			file_content+=cache_redis_str+",\n"

			table_str="\t\"tables\":{"
			for tk,tv in v["table"].items():
				if type(tv) == str:
					table_str+=""""%s":"%s","""%(tk,tv)
				else :
					table_str+=""""%s":%d,"""%(tk,tv)

			table_str+=""""xxxx":"xxxx"}\n"""

			file_content+=table_str

			file_content+="}\n"



			fd=open(conf_dir+name+".conf","w+")
			fd.write(file_content)
			fd.close()

			print file_content

#hlddz
create_hlddz("hl",venue_cfg["hl"])
#lzddz
create_lzddz("lz",venue_cfg["lz"])
#bsddz
create_bsddz("bs",venue_cfg["bs"])

