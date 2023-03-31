import logging
from logging.handlers import TimedRotatingFileHandler

# 创建 Logger 对象
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建控制台 Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# 创建文件 Handler
# 创建一个按天生成日志文件的处理器
log_file = "my_log.log"
file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
file_handler.setLevel(logging.INFO)
# 设置日志格式
file_handler.setFormatter(formatter)

# 将 Handler 添加到 Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 打印日志信息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
