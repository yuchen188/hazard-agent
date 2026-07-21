# agent/router.py
class Router:
    def route(self, query):
        graph_keywords = [
            "产生",
            "污染物",
            "风险物质",
            "风险区域",
            "排放环节",
            "防治技术",
            "工艺",
            "设备",
            "关系"
        ]
        graph_score = 0
        for word in graph_keywords:
            if word in query:
                graph_score += 1
        if graph_score >=2:
            return "graph"
        if graph_score ==1:
            return "both"
        return "text"