from data_dump import DataDump
from data_quality import DQC

if __name__ == "__main__":
    try:
        print(f'The process has been initialised.')
        DQC().dqc
        DataDump().dump
        print('Hooray, tasks have been completed.')
    except Exception as error:
        print(f'Something terribly went wrong, oups: {error}')