res = {'responses': [{'error': {
    'root_cause': [{'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@165e57fd on QueueResizingEsThreadPoolExecutor[name = _0JhsXR/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 100ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@1376e451[Running, pool size = 4, active threads = 4, queued tasks = 1655, completed tasks = 690118297]]'
                   }, {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@64c03cd1 on QueueResizingEsThreadPoolExecutor[name = EnJDM16/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 41.8ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@49c12cb8[Running, pool size = 4, active threads = 4, queued tasks = 1658, completed tasks = 667588237]]'
                   }, {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@77d48f96 on QueueResizingEsThreadPoolExecutor[name = _0JhsXR/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 115.4ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@1376e451[Running, pool size = 4, active threads = 4, queued tasks = 1654, completed tasks = 690118298]]'
                   }, {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@4fd10f99 on QueueResizingEsThreadPoolExecutor[name = EnJDM16/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 41.8ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@49c12cb8[Running, pool size = 4, active threads = 4, queued tasks = 1658, completed tasks = 667588237]]'
                   }, {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@560ee437 on QueueResizingEsThreadPoolExecutor[name = _0JhsXR/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 115.4ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@1376e451[Running, pool size = 4, active threads = 4, queued tasks = 1654, completed tasks = 690118298]]'
                   }],
    'type': 'search_phase_execution_exception',
    'reason': 'all shards failed',
    'phase': 'fetch',
    'grouped': True,
    'failed_shards': [{
        'shard': 0,
        'index': 'palissy1641337046672',
        'node': '_0JhsXR8QRC2RwCFewW43A',
        'reason': {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@165e57fd on QueueResizingEsThreadPoolExecutor[name = _0JhsXR/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 100ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@1376e451[Running, pool size = 4, active threads = 4, queued tasks = 1655, completed tasks = 690118297]]'
                   },
        }, {
        'shard': 1,
        'index': 'palissy1641337046672',
        'node': 'EnJDM16tQqeGk8W5Re8TrQ',
        'reason': {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@64c03cd1 on QueueResizingEsThreadPoolExecutor[name = EnJDM16/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 41.8ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@49c12cb8[Running, pool size = 4, active threads = 4, queued tasks = 1658, completed tasks = 667588237]]'
                   },
        }, {
        'shard': 2,
        'index': 'palissy1641337046672',
        'node': '_0JhsXR8QRC2RwCFewW43A',
        'reason': {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@77d48f96 on QueueResizingEsThreadPoolExecutor[name = _0JhsXR/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 115.4ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@1376e451[Running, pool size = 4, active threads = 4, queued tasks = 1654, completed tasks = 690118298]]'
                   },
        }, {
        'shard': 3,
        'index': 'palissy1641337046672',
        'node': 'EnJDM16tQqeGk8W5Re8TrQ',
        'reason': {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@4fd10f99 on QueueResizingEsThreadPoolExecutor[name = EnJDM16/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 41.8ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@49c12cb8[Running, pool size = 4, active threads = 4, queued tasks = 1658, completed tasks = 667588237]]'
                   },
        }, {
        'shard': 4,
        'index': 'palissy1641337046672',
        'node': '_0JhsXR8QRC2RwCFewW43A',
        'reason': {'type': 'es_rejected_execution_exception',
                   'reason': 'rejected execution of org.elasticsearch.common.util.concurrent.TimedRunnable@560ee437 on QueueResizingEsThreadPoolExecutor[name = _0JhsXR/search, queue capacity = 1000, min queue capacity = 1000, max queue capacity = 1000, frame size = 2000, targeted response rate = 1s, task execution EWMA = 115.4ms, adjustment amount = 50, org.elasticsearch.common.util.concurrent.QueueResizingEsThreadPoolExecutor@1376e451[Running, pool size = 4, active threads = 4, queued tasks = 1654, completed tasks = 690118298]]'
                   },
        }],
    }, 'status': 429}]}

import logging

if "responses" not in res or len(res["responses"]) < 1:
  logging.error(f"error while parsing {res}")
  raise Exception("error!")

elif "error" in res["responses"][0] and res["responses"][0].get("status") == 429:
  print("got error 429")

elif "hits" not in res["responses"][0]:
  logging.error(f"error while parsing {res}")
  raise Exception("error!")
