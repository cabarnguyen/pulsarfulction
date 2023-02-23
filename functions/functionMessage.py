from pulsar import Function
 
class EchoFunction(Function):
    def __init__(self):
        pass
  
    def process(self, input, context):
        return "{}!".format(input)
        # logger = context.get_logger()
        # evtTime = context.get_message_eventtime()
        # msgKey = context.get_message_key();
        
        # logger.info("""A message with a value of {0}, a key of {1}, 
        #   and an event time of {2} was received"""
        #   .format(input, msgKey, evtTime))
        
        # metricName = """function-%s-
        #   messages-received""".format(context.get_function_name())
        # context.record_metric(metricName, 1)
 
        # return input
