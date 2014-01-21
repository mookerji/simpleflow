from cdf.collections.urls.es_mapping_generation import generate_es_mapping
from cdf.streams.mapping import CONTENT_TYPE_NAME_TO_ID


SUGGEST_CLUSTERS = ['mixed']


CLUSTER_TYPE_TO_ID = {
    'pattern': {
        'host': 10,
        'path': 11,
        'qskey': 12,
    },
    'metadata': {
        CONTENT_TYPE_NAME_TO_ID['title']: 20,
        CONTENT_TYPE_NAME_TO_ID['h1']: 21,
        CONTENT_TYPE_NAME_TO_ID['h2']: 22,
        CONTENT_TYPE_NAME_TO_ID['h3']: 32
    }
}

URLS_DATA_MAPPING_DEPRECATED = {
    "urls": {
        "_routing": {
            "required": True,
            "path": "crawl_id"
        },
        "properties": {
            "url": {
                "type": "string",
                "index": "not_analyzed"
            },
            "url_hash": {"type": "long"},
            "byte_size": {"type": "long"},
            "date_crawled": {"type": "date"},
            "delay1": {"type": "long"},
            "delay2": {"type": "long"},
            "depth": {"type": "long"},
            "gzipped": {"type": "boolean"},
            "host": {
                "type": "string",
                "index": "not_analyzed"
            },
            "http_code": {"type": "long"},
            "id": {"type": "long"},
            "crawl_id": {"type": "long"},
            "patterns": {"type": "long"},
            "metadata_nb": {
                "properties": {
                    "description": {"type": "long"},
                    "h1": {"type": "long"},
                    "h2": {"type": "long"},
                    "title": {"type": "long"}
                }
            },
            "metadata": {
                "properties": {
                    "description": {
                        "type": "multi_field",
                        "fields": {
                            "description": {
                                "type": "string"
                            },
                            "untouched": {
                                "type": "string",
                                "index": "not_analyzed"
                            }
                        }
                    },
                    "h1": {
                        "type": "multi_field",
                        "fields": {
                            "h1": {
                                "type": "string"
                            },
                            "untouched": {
                                "type": "string",
                                "index": "not_analyzed"
                            }
                        }
                    },
                    "h2": {
                        "type": "multi_field",
                        "fields": {
                            "h2": {
                                "type": "string"
                            },
                            "untouched": {
                                "type": "string",
                                "index": "not_analyzed"
                            }
                        }
                    },
                    "title": {
                        "type": "multi_field",
                        "fields": {
                            "title": {
                                "type": "string"
                            },
                            "untouched": {
                                "type": "string",
                                "index": "not_analyzed"
                            }
                        }
                    }
                }
            },
            "metadata_duplicate_nb": {
                "properties": {
                    "title": {"type": "long"},
                    "description": {"type": "long"},
                    "h1": {"type": "long"}
                }
            },
            "metadata_duplicate": {
                "properties": {
                    "title": {"type": "long", "index": "no"},
                    "description": {"type": "long", "index": "no"},
                    "h1": {"type": "long", "index": "no"}
                }
            },
            "metadata_duplicate_is_first": {
                "properties": {
                    "title": {"type": "boolean"},
                    "description": {"type": "boolean"},
                    "h1": {"type": "boolean"}
                }
            },
            "inlinks_internal_nb": {
                "properties": {
                    "total": {"type": "long"},
                    "follow_unique": {"type": "long"},
                    "total_unique": {"type": "long"},
                    "follow": {"type": "long"},
                    "nofollow": {"type": "long"},
                    "nofollow_combinations": {
                        "properties": {
                            "key": {"type": "string"},
                            "value": {"type": "long"}
                        }
                    }
                }
            },
            "inlinks_internal": {"type": "long", "index": "no"},
            "outlinks_internal": {"type": "long", "index": "no"},
            "outlinks_internal_nb": {
                "properties": {
                    "total": {"type": "long"},
                    "follow_unique": {"type": "long"},
                    "total_unique": {"type": "long"},
                    "follow": {"type": "long"},
                    "nofollow": {"type": "long"},
                    "nofollow_combinations": {
                        "properties": {
                            "key": {"type": "string"},
                            "value": {"type": "long"}
                        }
                    }
                }
            },
            "outlinks_external_nb": {
                "properties": {
                    "total": {"type": "long"},
                    "follow": {"type": "long"},
                    "nofollow": {"type": "long"},
                    "nofollow_combinations": {
                        "properties": {
                            "key": {"type": "string"},
                            "value": {"type": "long"}
                        }
                    }
                }
            },
            "path": {
                "type": "string",
                "index": "not_analyzed"
            },
            "protocol": {
                "type": "string",
                "index": "not_analyzed"
            },
            "query_string": {
                "type": "string",
                "index": "not_analyzed"
            },
            "query_string_keys": {
                "type": "string",
                "index": "not_analyzed"
            },
            "canonical_from_nb": {"type": "long"},
            "canonical_from": {"type": "long", "index": "no"},
            "canonical_to": {
                "properties": {
                    "url": {"type": "string", "index": "no"},
                    "url_id": {"type": "long", "index": "no"}
                }
            },
            "canonical_to_equal": {"type": "boolean"},
            "redirects_to": {
                "properties": {
                    "http_code": {"type": "long"},
                    "url": {"type": "string"},
                    "url_id": {"type": "long"}
                }
            },
            "redirects_from_nb": {"type": "long"},
            "redirects_from": {
                "properties": {
                    "http_code": {"type": "long", "index": "no"},
                    "url_id": {"type": "long", "index": "no"}
                }
            },
            "error_links": {
                "properties": {
                    "3xx": {
                        "properties": {
                            "nb": {"type": "long"},
                            "urls": {"type": "long", "index": "no"}
                        }
                    },
                    "4xx": {
                        "properties": {
                            "nb": {"type": "long"},
                            "urls": {"type": "long", "index": "no"}
                        }
                    },
                    "5xx": {
                        "properties": {
                            "nb": {"type": "long"},
                            "urls": {"type": "long", "index": "no"}
                        }
                    },
                    "any": {
                        "properties": {
                            "nb": {"type": "long"}
                        }
                    }
                }
            }
        }
    }
}

# A intermediate definition of url data format
#
# Keys are represented in a path format
#   - ex. `metadata.h1`
#       This means `metadata` will be an object type and it
#       contains a field named `h1`
#
# Values contains
#   - type: data type of this field
#       - long: for numeric values
#       - string: for string values
#       - struct: struct can contains some inner fields, but these fields
#           won't be visible when querying
#           ex. `something.redirects_from:
#               [{`id`: xx, `http_code`: xx}, {...}, ...]`
#               `redirects_from` is visible, but `redirects_from.id` is not
#           Struct's inner fields have their own types
#
#   - settings (optional): a set of setting flags of this field
#       - es:not_analyzed: this field should not be tokenized by ES
#       - es:no_index: this field should not be indexed
#       - list: this field is actually a list of values in ES
#       - es:multi_field: a multi_field type keeps multiple copies of the same
#           data in different format (analyzed, not_analyzed etc.)
#           In case of `multi_field`, `field_type` must be specified for
#           determine the field's type

#
#   - default_value (optional): the default value if this field does not
#       exist

_NUMBER_TYPE = 'long'
_STRING_TYPE = 'string'
_BOOLEAN_TYPE = 'boolean'
_STRUCT_TYPE = 'struct'
_DATE_TYPE = 'date'

_NO_INDEX = 'no_index'
_NOT_ANALYZED = 'not_analyzed'
_LIST = 'list'
_MULTI_FIELD_TYPE = 'multi_field'


URLS_DATA_FORMAT_DEFINITION = {
    # url property data
    "url": {
        "type": _STRING_TYPE,
        "settings": {
            _NOT_ANALYZED
        }
    },
    "url_hash": {"type": _NUMBER_TYPE},
    "byte_size": {"type": _NUMBER_TYPE},
    "date_crawled": {"type": _DATE_TYPE},
    "delay1": {"type": _NUMBER_TYPE},
    "delay2": {"type": _NUMBER_TYPE},
    "depth": {"type": _NUMBER_TYPE},
    "gzipped": {"type": _BOOLEAN_TYPE},
    "host": {
        "type": _STRING_TYPE,
        "settings": {
            _NOT_ANALYZED
        }
    },
    "http_code": {"type": _NUMBER_TYPE},
    "id": {"type": _NUMBER_TYPE},
    "crawl_id": {"type": _NUMBER_TYPE},
    "patterns": {"type": _NUMBER_TYPE},
    "path": {
        "type": _STRING_TYPE,
        "settings": {
            _NOT_ANALYZED
        }
    },
    "protocol": {
        "type": _STRING_TYPE,
        "settings": {
            _NOT_ANALYZED
        }
    },
    "query_string": {
        "type": _STRING_TYPE,
        "settings": {
            _NOT_ANALYZED
        }
    },
    "query_string_keys": {
        "type": _STRING_TYPE,
        "settings": {
            _NOT_ANALYZED
        }
    },

    # metadata numbers
    "metadata_nb.title": {
        "type": _NUMBER_TYPE
    },
    "metadata_nb.h1": {
        "type": _NUMBER_TYPE
    },
    "metadata_nb.h2": {
        "type": _NUMBER_TYPE
    },
    "metadata_nb.description": {
        "type": _NUMBER_TYPE
    },

    # metadata contents
    "metadata.title": {
        "type": "multi_field",
        "field_type": _STRING_TYPE,
        "settings": {
            _LIST
        }
    },
    "metadata.h1": {
        "type": "multi_field",
        "field_type": _STRING_TYPE,
        "settings": {
            _LIST
        }
    },
    "metadata.h2": {
        "type": "multi_field",
        "field_type": _STRING_TYPE,
        "settings": {
            _LIST
        }
    },
    "metadata.description": {
        "type": "multi_field",
        "field_type": _STRING_TYPE,
        "settings": {
            _LIST
        }
    },

    # metadata duplication data
    "metadata_duplicate_nb.title": {"type": _NUMBER_TYPE},
    "metadata_duplicate_nb.description": {"type": _NUMBER_TYPE},
    "metadata_duplicate_nb.h1": {"type": _NUMBER_TYPE},

    "metadata_duplicate_is_first.title": {"type": _BOOLEAN_TYPE},
    "metadata_duplicate_is_first.description": {"type": _BOOLEAN_TYPE},
    "metadata_duplicate_is_first.h1": {"type": _BOOLEAN_TYPE},

    "metadata_duplicate.title": {
        "type": _NUMBER_TYPE,
        "settings": {
            _LIST,
            "no_index"
        }
    },
    "metadata_duplicate.h1": {
        "type": _NUMBER_TYPE,
        "settings": {
            _LIST,
            "no_index"
        }
    },
    "metadata_duplicate.description": {
        "type": _NUMBER_TYPE,
        "settings": {
            _LIST,
            "no_index"
        }
    },

    # incoming links data
    "inlinks_internal_nb.total": {"type": _NUMBER_TYPE},
    "inlinks_internal_nb.follow_unique": {"type": _NUMBER_TYPE},
    "inlinks_internal_nb.total_unique": {"type": _NUMBER_TYPE},
    "inlinks_internal_nb.follow": {"type": _NUMBER_TYPE},
    "inlinks_internal_nb.nofollow": {"type": _NUMBER_TYPE},
    "inlinks_internal_nb.nofollow_combinations": {
        "type": "struct",
        "values": {
            "key": {"type": _STRING_TYPE},
            "value": {"type": _NUMBER_TYPE}
        }
    },
    "inlinks_internal": {
        "type": _NUMBER_TYPE,
        "settings": {
            "no_index",
            _LIST
        }
    },

    # outgoing links data
    # internal outgoing links
    "outlinks_internal_nb.total": {"type": _NUMBER_TYPE},
    "outlinks_internal_nb.follow_unique": {"type": _NUMBER_TYPE},
    "outlinks_internal_nb.total_unique": {"type": _NUMBER_TYPE},
    "outlinks_internal_nb.follow": {"type": _NUMBER_TYPE},
    "outlinks_internal_nb.nofollow": {"type": _NUMBER_TYPE},
    "outlinks_internal_nb.nofollow_combinations": {
        "type": "struct",
        "values": {
            "key": {"type": _STRING_TYPE},
            "value": {"type": _NUMBER_TYPE}
        }
    },
    "outlinks_internal": {
        "type": _NUMBER_TYPE,
        "settings": {
            "no_index",
            _LIST
        }
    },

    # external outgoing links
    "outlinks_external_nb.total": {"type": _NUMBER_TYPE},
    "outlinks_external_nb.follow": {"type": _NUMBER_TYPE},
    "outlinks_external_nb.nofollow": {"type": _NUMBER_TYPE},
    "outlinks_external_nb.nofollow_combinations": {
        "type": "struct",
        "values": {
            "key": {"type": _STRING_TYPE},
            "value": {"type": _NUMBER_TYPE}
        }
    },


    # incoming canonical links data
    "canonical_from_nb": {"type": _NUMBER_TYPE},
    "canonical_from": {
        "type": _NUMBER_TYPE,
        "settings": {
            "no_index",
            _LIST
        }
    },

    # outgoing canonical link data
    "canonical_to": {
        "type": "struct",
        "default_value": None,
        "values": {
            "url": {"type": _STRING_TYPE},
            "url_id": {"type": _NUMBER_TYPE},
        },
        "settings": {
            "no_index"
        }
    },
    "canonical_to_equal": {"type": _BOOLEAN_TYPE},

    # outgoing redirection data
    "redirects_to": {
        "type": "struct",
        "default_value": None,
        "values": {
            "http_code": {"type": _NUMBER_TYPE},
            "url": {"type": _STRING_TYPE},
            "url_id": {"type": _NUMBER_TYPE}
        }
    },

    # incoming redirections data
    "redirects_from_nb": {"type": _NUMBER_TYPE},
    "redirects_from": {
        "type": "struct",
        "values": {
            "http_code": {"type": _NUMBER_TYPE},
            "url_id": {"type": _NUMBER_TYPE},
        },
        "settings": {
            _LIST,
            "no_index"
        }
    },

    # erroneous links data
    "error_links.3xx.nb": {"type": _NUMBER_TYPE},
    "error_links.4xx.nb": {"type": _NUMBER_TYPE},
    "error_links.5xx.nb": {"type": _NUMBER_TYPE},
    "error_links.any.nb": {"type": _NUMBER_TYPE},

    "error_links.3xx.urls": {
        "type": _NUMBER_TYPE,
        "settings": {
            "no_index",
            _LIST
        }
    },
    "error_links.4xx.urls": {
        "type": _NUMBER_TYPE,
        "settings": {
            "no_index",
            _LIST
        }
    },
    "error_links.5xx.urls": {
        "type": _NUMBER_TYPE,
        "settings": {
            "no_index",
            _LIST
        }
    },
}


# Generated constants
URLS_DATA_FIELDS = URLS_DATA_FORMAT_DEFINITION.keys()
URLS_DATA_MAPPING = generate_es_mapping(URLS_DATA_FORMAT_DEFINITION)