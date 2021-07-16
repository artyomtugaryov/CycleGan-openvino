import cv2
import numpy as np

from services.inference import IReader, Data


class TelegramImageReader(IReader):
    def __init__(self, source, file_id):
        super().__init__(source)
        self._file_id = file_id

    def read(self) -> Data:
        tg_file = self._source.bot.getFile(self._file_id)
        file_as_bytearray = tg_file.download_as_bytearray()
        data_as_np_array = np.frombuffer(file_as_bytearray, np.uint8)
        image_data = cv2.imdecode(data_as_np_array, cv2.IMREAD_COLOR)
        return Data(image_data)
