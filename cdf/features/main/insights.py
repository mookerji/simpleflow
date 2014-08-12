from cdf.core.insights import Insight
from cdf.query.filter import EqFilter, LtFilter, GteFilter, BetweenFilter


def get_http_code_ranges_insights():
    #insights by http ranges
    result = []
    for range_start in [200, 300, 400, 500]:
        range_name = "{}xx".format(range_start / 100)
        insight = Insight(
            "code:{}".format(range_name),
            "{} Urls".format(range_name),
            BetweenFilter("http_code", [range_start, range_start + 99]).to_dict()
        )
        result.append(insight)

    #special range for codes lower than 0
    result.append(
        Insight(
            "code:network_errors",
            "Network Errors",
            LtFilter("http_code", 0).to_dict()
        )
    )

    return result


def get_http_code_insights():
    #insights by http code
    result = []
    for code in [200, 301, 302, 304, 403, 404, 410]:
        insight = Insight(
            "code:{}".format(code),
            "{} Urls".format(code),
            EqFilter("http_code", code).to_dict()
        )
        result.append(insight)
    return result


def get_strategic_urls_insights():
    return []
    #FIXME uncomment this when strategic urls have been implemented
#    return [
#        Insight(
#            "strategic:1",
#            "Strategic Urls",
#            EqFilter("strategic", True).to_dict()
#        ),
#        Insight(
#            "strategic:0",
#            "Non Strategic Urls",
#            EqFilter("strategic", False).to_dict()
#        )
#    ]


def get_content_type_insights():
    #insights for content types
    result = []
    for content_type in ["text/html", "text/css"]:
        insight = Insight(
            "content:{}".format(content_type),
            "{} Urls".format(content_type[len("text/"):].upper()),
            EqFilter("content_type", content_type).to_dict()
        )
        result.append(insight)
    return result


def get_protocol_insights():
    result = []
    for protocol in ["http", "https"]:
        insight = Insight(
            "protocol:{}".format(protocol),
            "{} Urls".format(protocol.upper()),
            EqFilter("protocol", protocol).to_dict()
        )
        result.append(insight)
    return result


#speed insights
def get_speed_insights():
    field = "delay_last_byte"
    return [
        Insight(
            "speed:fast",
            "Fast Urls",
            LtFilter(field, 500).to_dict()
        ),
        Insight(
            "speed:medium",
            "Medium Urls",
            BetweenFilter(field, [500, 999]).to_dict()
        ),
        Insight(
            "speed:slow",
            "Slow Urls",
            BetweenFilter(field, [1000, 1999]).to_dict()
        ),
        Insight(
            "speed:slowest",
            "Slowest Urls",
            GteFilter(field, 2000).to_dict()
        ),
    ]


def get_strategic_urls_speed_insights():
    return []
    #FIXME uncomment when strategic urls have been implemented
#    field = "delay_last_byte"
#    strategic_predicate = EqFilter("strategic", True)
#    return [
#        Insight(
#            "speed:fast_strategic",
#            "Fast Strategic Urls",
#            {
#                "and": [
#                    strategic_predicate.to_dict(),
#                    LtFilter(field, 500).to_dict()
#                ]
#            }
#        ),
#        Insight(
#            "speed:medium_strategic",
#            "Medium Strategic Urls",
#            {
#                "and": [
#                    strategic_predicate.to_dict(),
#                    BetweenFilter(field, [500, 999]).to_dict()
#                ]
#            }
#        ),
#        Insight(
#            "speed:slow_strategic",
#            "Slow Strategic Urls",
#            {
#                "and": [
#                    strategic_predicate.to_dict(),
#                    BetweenFilter(field, [1000, 1999]).to_dict()
#                ]
#            }
#        ),
#        Insight(
#            "speed:slowest_strategic",
#            "Slowest Strategic Urls",
#            {
#                "and": [
#                    strategic_predicate.to_dict(),
#                    GteFilter(field, 2000).to_dict()
#                ]
#            }
#        ),
#    ]


#insights for domain/subdomains
def get_domain_insights():
    www_predicate = EqFilter("host", "www")
    return [
        Insight(
            "domain:www",
            "Urls from www",
            www_predicate.to_dict()
        ),
        Insight(
            "not www",
            "Urls from subdomains",
            {"not": www_predicate.to_dict()}
        )
    ]


def get_average_speed_insights():
    field = "delay_last_byte"
    return [
        Insight(
            "speed:avg",
            "Average Load time (in ms)",
            aggs=[
                    {
                        'metrics': [
                            {"avg": field}
                        ]
                    }
                ]
        )
    ]
    #TODO"speed:strategic_avg", "Average Load time on strategic urls (in ms)", {"field": "strategic", "value": true}),


def get_average_depth_insights():
    field = "depth"
    return [
        Insight(
            "depth:avg",
            "Average Depth",
            aggs=[
                    {
                        'metrics': [
                            {"avg": field}
                        ]
                    }
                ]
        )
    ]
    #TODO"depth:strategic_avg", "Average Depth on strategic urls", {"field": "strategic", "value": true}),


def get_insights():
    insights = []
    insights.extend(get_http_code_ranges_insights())
    insights.extend(get_http_code_insights())
    insights.extend(get_strategic_urls_insights())
    insights.extend(get_content_type_insights())
    insights.extend(get_protocol_insights())
    insights.extend(get_speed_insights())
    insights.extend(get_strategic_urls_speed_insights())
    insights.extend(get_domain_insights())
    insights.extend(get_average_speed_insights())
    insights.extend(get_average_depth_insights())
    return insights

#actual insight definition
insights = get_insights()
