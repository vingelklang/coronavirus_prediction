from data_grabbers.data_grabber import DataGrabber
from data_grabbers.graphs_data_grabber import GraphsDataGrabber

class GERCasesDataGrabber(DataGrabber):
    DATASET_PREFIX = "germany_daily_cases"
    PATH = "country/germany"
    GRAPH_ID = "graph-cases-daily"
    SERIES_NAME = "Daily Cases"

    def __init__(self):
        super()

    def grab_data(self):
        graphs_grabber = GraphsDataGrabber()

        data = graphs_grabber.get_data(path=GERCasesDataGrabber.PATH, graph_id=GERCasesDataGrabber.GRAPH_ID, series_name=GERCasesDataGrabber.SERIES_NAME)
        filename = self.get_dataset_file_name()

        self.save_data_to_file(filename, data)

    def get_dataset_file_name(self, dataset_date=""):
        return super().get_dataset_file_name(GERCasesDataGrabber.DATASET_PREFIX, dataset_date=dataset_date)
