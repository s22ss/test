# -*- coding: utf-8
# create_time: 2021-02-24
import os

from config.config import IMAGESDIR, LOGGER
from page.base_page import BasePage


class MaterialPage(BasePage):
    """素材管理page类"""

    def up_image(self, filename: dict):
        """
        上传图片
        :return:
        """
        try:
            filename = filename.get('filename')
            filedir = os.path.join(IMAGESDIR, filename)
            with open(file=filedir, mode='rb') as f:
                file = {"file": f}
                r = self.session.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload?type=image", files=file)
            LOGGER.info(
                f'Access to "up_image" url https://qyapi.weixin.qq.com/cgi-bin/media/upload?type=image success')
            return r
        except Exception as e:
            LOGGER.error(
                f'Access to "up_image" url https://qyapi.weixin.qq.com/cgi-bin/media/upload?type=image failed')
            raise e


if __name__ == "__main__":
    s = MaterialPage().up_image("my_wework.png")
    print(s.json())
