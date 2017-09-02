'''
Created on Jul 11, 2017

@author: make ma
'''
from SemanticObject import SemanticObject

class StockSemantic(SemanticObject):
    '''
    classdocs
    '''
    
    mapStockSlot = { \
        "name":"名称:", \
        "type": "类型：", \
        "time": "时间:", \
        "subject":"查询目标:", \
        "code":"代码:", \
        "list":"排行榜类型", \
        "size":"查排行榜家数" \
        }

    def __init__(self, obj_type, desc_obj, symantic_objs):
        '''
        Constructor
        '''
        SemanticObject.__init__(self, obj_type, desc_obj, symantic_objs)
        
    def getTts(self):
        return self.tts
    
    def process(self, handler):
        self.tts = ""
        if self.semanticObjs != None:
            obj = self.semanticObjs[0]
            self.modifier = obj.get("modifier")
            self.slots = obj.get("slots")
            
            if self.modifier[0] == "query":
                self.tts += "服务器返回的语义是：股市查询。具体如下："
                if self.slots != None and len(self.slots) > 0:
                    for slot in self.slots:
                        name = slot.get("name")
                        value = slot.get("value")
                        if name != None and value != None:
                            ttsName = StockSemantic.mapStockSlot.get(name)
                            if ttsName != None:
                                self.tts += ttsName + "," + value + "。"
            elif self.modifier[0] == "delete":                
                if self.slots != None and len(self.slots) > 0:
                    self.tts += "服务器返回的语义是：删除收藏的股票.具体如下:"
                    for slot in self.slots:
                        name = slot.get("name")
                        value = slot.get("value")
                        if name != None and value != None:
                            ttsName = StockSemantic.mapStockSlot.get(name)
                            if ttsName != None:
                                self.tts += ttsName + "," + value + "。"
                else:
                    self.tts += "服务器返回的语义是：删除收藏的所有股票."
            elif self.modifier[0] == "delete_all":                
                self.tts += "服务器返回的语义是：删除收藏的所有股票."
            elif self.modifier[0] == "can":                
                self.tts += "服务器返回的语义是：本系统有查询股价的功能吗"
            elif self.modifier[0] == "query_list":                
                self.tts += "服务器返回的语义是：查询排行榜。具体如下："
                if self.slots != None and len(self.slots) > 0:
                    for slot in self.slots:
                        name = slot.get("name")
                        value = slot.get("value")
                        if name != None and value != None:
                            ttsName = StockSemantic.mapStockSlot.get(name)
                            if ttsName != None:
                                self.tts += ttsName + "," + value + "。"
                           
                            
                