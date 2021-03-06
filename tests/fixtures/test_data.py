from tempfile import TemporaryDirectory

import numpy as np
import pandas as pd
import pyarrow as pa
from pyarrow import parquet
import pytest


@pytest.fixture
def parquet_file():
    df = pd.DataFrame(
        {'one': [-1, np.nan, 2.5],
         'two': ['foo', 'bar', 'baz'],
         'three': [True, False, True]}
    )
    table = pa.Table.from_pandas(df)
    with TemporaryDirectory() as tmp_path:
        pq_path = f'{tmp_path}/test.pq'
        parquet.write_table(table, pq_path)
        yield pq_path


@pytest.fixture
def parquet_file_s3_1(parquet_file, aws_session, aws_s3_bucket):
    aws_session.resource('s3')\
        .meta.client.upload_file(parquet_file, aws_s3_bucket, 'target1.parquet')
    return aws_s3_bucket, 'target1.parquet'


@pytest.fixture
def parquet_file_s3_2(parquet_file, aws_session, aws_s3_bucket):
    aws_session.resource('s3')\
        .meta.client.upload_file(parquet_file, aws_s3_bucket, 'target2.parquet')
    return aws_s3_bucket, 'target2.parquet'


@pytest.fixture
def text_file_s3_1(parquet_file, aws_session, aws_s3_bucket):
    aws_session.resource('s3')\
        .meta.client.upload_file(parquet_file, aws_s3_bucket, 'foo.text')
    return aws_s3_bucket, 'foo.text'
