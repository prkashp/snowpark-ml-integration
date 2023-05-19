from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T

import tensorflow as TF
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import utils.config as cf 

sess = Session.builder.configs(cf.conn_params).create()
print(sess)
output= sess.sql('Create database if not exists DWH')
print(output.collect())