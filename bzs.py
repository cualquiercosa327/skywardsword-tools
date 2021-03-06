import struct
import glob
import pprint
import json
import collections
import os
import storyflag
from util import *
import re

ROOMCOUNT = 16
LAYERCOUNT = 29

sizes = {'FILE':4,
         'SCEN':40,
         'CAM ':44,
         'PATH':12,
         'PNT ':16,
         'SPNT':16,
         'BPNT':40,
         'SPTH':12,
         'AREA':32,
         'EVNT':56,
         'PLY ':24,
         'OBJS':36,
         'OBJ ':36,
         'SOBS':48,
         'SOBJ':48,
         'STAS':48,
         'STAG':48,
         'SNDT':48,
         'DOOR':36,
         'LYSE':4,
         'STIF':20,
         'PCAM':36,
         'LYLT':4}

cumulative_flags_set = [
    [0x40,0x63,0xC4,0xB5,0x3F,0xB8,0xDD,0xF0,0xFF,0xCF,0x1E,0x79,0x00,0x00,0x1F,0x00],
    [0x00,0x00,0x00,0x01,0x20,0x34,0x01,0xF8,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00],
    [0xF8,0x03,0x00,0x08,0x00,0x00,0x00,0x08,0x00,0x00,0x00,0x00,0x40,0x10,0x80,0x00],
    [0x00,0x00,0x0C,0x10,0x00,0x00,0x00,0x00,0x00,0x40,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x40,0x00,0x90,0x24,0xC0,0xBF,0x12,0x00,0x06,0x10,0x22,0x02,0x07],
    [0x00,0x00,0x00,0x00,0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x84,0x00,0x03,0x0C],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x09,0x38,0x30,0x00,0x00,0x0C,0x02,0x20,0x1E,0x00,0x02,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0xC0,0x00,0xE0,0x00,0x00,0x00,0x00,0x00,0x02,0x00,0x00,0x00,0x00,0x01],
    [0x08,0x00,0x24,0xC4,0x00,0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x1C,0x00,0x7F,0xFE],
    [0x5D,0x40,0x16,0x80,0x00,0x18,0xE0,0x40,0x02,0x3B,0xA0,0x3F,0xFF,0xFF,0x01,0x03],
    [0x00,0x00,0x80,0x31,0x00,0x05,0x00,0x80,0x00,0x10,0x00,0x00,0x00,0x06,0x00,0x82],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x08,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x50,0x00,0x22,0x00,0x00,0xC0,0x00,0x00,0x04,0x1F,0xBC,0x02,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x08,0x00,0x00,0x01,0x00,0x80,0x00,0x00,0x00,0x10,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x04,0x00],
    [0x61,0x60,0x06,0x78,0x00,0x32,0x00,0x01,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x00,0x10,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x01,0x00,0x00,0x30,0x00,0x00]]

global stage_scens
global flagindex
flagindex = None
stage_scens = []
story_flags = set()

def parseBzs(data):
    name,count,ff,offset = struct.unpack('>4shhi',data[:12])
    name = name.decode('ascii')
    return parseObj(name, count, data[offset:])

def parseObj(objtype, quantity, data):
    global stage_scens
    global flagindex
    if objtype == 'V001':
        #root
        parsed = collections.OrderedDict()
        for i in range(quantity):
            addr = i*12
            name,count,ff,offset = struct.unpack('>4shhi',data[addr:addr+12])
            name = name.decode('ascii')
            parsed[name]=parseObj(name,count,data[addr+offset:])
            #if name != 'LAY ':
            #    parsed[name]=len(parsed[name])
        return parsed
    elif objtype == 'LAY ':
        #different layers of the room (always 29 of them)
        assert quantity == LAYERCOUNT
        parsed = {}
        for i in range(quantity):
            addr = i*8
            count,ff,offset = struct.unpack('>hhi',data[addr:addr+8])
            parsed['l%d'%i] = parseObj('V001',count,data[addr+offset:])
        return parsed
            
    elif objtype in ('OBJN','ARCN'):
        parsed = []
        for i in range(quantity):
            addr = data[2*i]*0x100 + data[2*i+1]
            name = toStr(data[addr:])
            parsed.append(name)
        return parsed
    elif objtype == 'RMPL':
        parsed = collections.OrderedDict()
        for i in range(quantity):
            rmpldata = data[4*i:]
            rmpl_id = rmpldata[0]
            count = rmpldata[1]
            addr = rmpldata[2]*0x100 + rmpldata[3]
            parsed[rmpl_id] = []
            for j in range(count):
                parsed[rmpl_id].append(rmpldata[addr+2*j:addr+2*j+2])
        return parsed

    else:
        parsed = []
        for i in range(quantity):
            item = data[sizes[objtype]*i:sizes[objtype]*(i+1)]

            if objtype == 'FILE':
                assert quantity == 1
                parsed_item = item
                return parsed_item
            elif objtype == 'SCEN':
                #link to other stage
                parsed_item = unpack('name room layer entrance byte4 byte5 flag6 zero flag8','>32sbbbbbbbb',item)
                parsed_item['name'] = toStr(parsed_item['name'])
                stage_scens.append(parsed_item)
            elif objtype == 'CAM ':
                parsed_item = unpack('unk1 posx posy posz angle unk2 name','>4s3ff8s16s', item)
                parsed_item['name'] = toStr(parsed_item['name'])
            elif objtype in ('PATH','SPTH'):
                parsed_item = item
            elif objtype in ('PNT ','SPNT'):
                parsed_item = unpack('posx posy posz unk','>3f4s',item)
            elif objtype == 'BPNT':
                parsed_item = unpack('pos1x pos1y pos1z pos2x pos2y pos2z pos3x pos3y pos3z unk','>3f3f3f4s',item)
            elif objtype == 'AREA':
                parsed_item = unpack('posx posy posz sizex sizey sizez unk','>3f3f8s',item)
            elif objtype == 'EVNT':
                parsed_item = unpack('unk name','>24s32s',item)
                parsed_item['name'] = toStr(parsed_item['name'])
            elif objtype == 'PLY ':
                #room entrance
                parsed_item = unpack('byte1 byte2 play_cutscene byte4 posx posy posz unk2 entrance_id','>bbbb3f6sh',item)
                if parsed_item['play_cutscene'] != -1:
                    print('%d: entrance %d -- cutscene %d'%(i,parsed_item['entrance_id'],parsed_item['play_cutscene']))
            elif objtype in ('OBJS','OBJ ','DOOR'):
                parsed_item = unpack('byte1 tosky_scen_link scen_link byte4 unk1 posx posy posz                   event_flag transition_type unk2 talk_behaviour unk3 name','>bbbb4s3fbb2sh2s8s',item)
                parsed_item['name'] = toStr(parsed_item['name'])
            elif objtype in ('SOBS','SOBJ','STAS','STAG','SNDT'):
                parsed_item = unpack('byte1 tosky_scen_link scen_link byte4 unk1 posx posy posz sizex sizey sizez event_flag transition_type unk2 talk_behaviour unk3 name','>bbbb4s3f3fbb2sh2s8s',item)
                parsed_item['name'] = toStr(parsed_item['name'])
            
            elif objtype == 'LYSE':
                #logic for overriding layer when attempting to load layer 0
                parsed_item = unpack('story_flag night layer','>hbb',item)
                #if parsed_item['story_flag'] == -1:
                #    print ('\tDefault, night=%d -- layer=%d'%(parsed_item['night'], parsed_item['layer']))
                #else:
                #    print ('\tFlag %04X (JP %s / US %s), night=%d -- layer=%d'%(parsed_item['story_flag'],
                #                                                        storyflag.flagid_to_spreadsheet(False,parsed_item['story_flag']),
                #                                                        storyflag.flagid_to_spreadsheet(True,parsed_item['story_flag']),
                #                                                        parsed_item['night'],
                #                                                        parsed_item['layer']))
                story_flags.add(parsed_item['story_flag'])
            elif objtype == 'STIF':
                #Stage Info
                assert quantity == 1
                parsed_item = unpack('wtf1 wtf2 wtf3 byte1 flagindex byte3 byte4 unk','>3fbbbb4s',item)
                flagindex = parsed_item['flagindex']
                return parsed_item
            elif objtype == 'PCAM':
                parsed_item = unpack('pos1x pos1y pos1z pos2x pos2y pos2z angle wtf unk','>3f3fff4s',item)
            elif objtype == 'LYLT':
                #Demo definitions
                parsed_item = unpack('layer demo_high demo_low dummy','>bbbb',item)
                assert parsed_item['dummy'] == -1
                
            else:
                raise Exception(objtype)

            if type(parsed_item) == collections.OrderedDict and 'name' in parsed_item:
                if parsed_item['name'] == 'HrpHint' and parsed_item['byte4'] != -1:
                    cumulative_flags_set[flagindex]=setBit(cumulative_flags_set[flagindex],parsed_item['byte4'])
                #if parsed_item['name'] == 'TBox' and parsed_item['unk2'][0] != 0xFF:
                #    cumulative_flags_set[flagindex]=setBit(cumulative_flags_set[flagindex],parsed_item['unk2'][0])
                
            parsed.append(parsed_item)
            #if type(parsed_item) != bytes and 'name' in parsed_item and parsed_item['name'] == 'Door':
            #    if 0 <= parsed_item['scen_link'] < len(stage_scens):
            #        print('\tDoor %f %f %f  -- scene: %s' % (parsed_item['posx'],parsed_item['posy'],parsed_item['posz'],stage_scens[parsed_item['scen_link']]))
            #    else:
            #        print('\tDoor %f %f %f  -- scene: invalid exit %d' % (parsed_item['posx'],parsed_item['posy'],parsed_item['posz'],parsed_item['scen_link']))

        return parsed



for stageid in os.listdir('Stage'):
    stage_scens = []
    flagindex = None
    print(stageid+' - '+stagenames[stageid])
    stagepath = 'Stage/%s/%s_stg_l0/dat/stage.bzs'%(stageid,stageid)
    stage = parseBzs(open(stagepath, 'rb').read())
    stage['rooms'] = collections.OrderedDict()
    for i in range(ROOMCOUNT):
        roomid = 'r%02d'%i
        roompath = 'Stage/%s/%s_stg_l0/rarc/%s_r%02d/dat/room.bzs' % (stageid,stageid,stageid,i)
        if os.path.isfile(roompath):
            print(stageid, roomid)
            stage_scens = []
            room = parseBzs(open(roompath, 'rb').read())
            stage['rooms'][roomid]=room
    if 'RMPL' in stage:
        assert len(stage['rooms']) == len(stage['RMPL'])
    else:
        assert len(stage['rooms']) == 1
    f2=open('output/stage/%s.json'%stageid,'w',encoding='utf-8')
    f2.write(objToJson(stage))
    s = objToJson(stage)
    #if '"r01"' in s:
    #    for roomid in stage['rooms']:
    #        room = stage['rooms'][roomid]
    #        r = objToJson(room)
    #        if 'saveObj' in r and len(room['PLY ']) > 1:
    #            for ply in room['PLY ']:
    #                if ply['play_cutscene'] != -1:
    #                    print('!!!!!! '+stageid+' '+roomid+' entrance '+str(ply['entrance_id']))
    f2.close()


print('-----------------------------------------------')
print('50 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E 5F')
print('-----------------------------------------------')
for i in range(len(flagindex_names)):
    print(flagindex_names[i])
    printHex(cumulative_flags_set[i])

