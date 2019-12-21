# -*- coding:UTF-8 -*-
# Time          : 2019-11-20 17:55
# Author        : xiexin
# File          : aes_com.py
# Description   : 加解密

import subprocess
import chardet
import sys
import json


class AES(object):
    # 如需加key，需要使用def __init__(self, data，key)
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def encrypt(self):
        command = "java -jar F:/python/AWL/testFile/encrytor.jar"
        arg0 = self.data
        arg1 = self.key
        # cmd = [command, arg0]
        cmd = [command, arg0, arg1]  # 如需加key，需要传入arg1
        new_cmd = " ".join(cmd)
        stdout, stderr = subprocess.Popen(new_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        encoding = chardet.detect(stdout)["encoding"]
        en_result = stdout.decode(encoding)
        return en_result

    def decrypt(self):
        command = "java -jar F:/python/AWL/testFile/decryptor.jar"
        arg0 = self.data
        arg1 = self.key
        # cmd = [command, arg0]
        cmd = [command, arg0, arg1]  # 如需加key，需要传入arg1
        new_cmd = " ".join(cmd)
        stdout, stderr = subprocess.Popen(new_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        encoding = chardet.detect(stdout)["encoding"]
        print(encoding)
        de_result = stdout.decode(encoding)
        return de_result


if __name__ == '__main__':
    key = "893261785611546766@**xmenWYAX&hu"

    # 加密
    encry = '{"OUT_USER_NAME":"暹粒"}'
    encry1 = json.dumps(encry)
    AES1 = AES(encry1, key)  # 需加key时使用下面这句
    print("加密：\n" + AES1.encrypt())

    # 解密
    decry = '6F968DF141EFC37FA743EA22B294EBF70AA3E0F555FC4AF5B045A0C598562E218EA2CC1722F8D1237744CF076B14BBB69857E177E83D5EE1F5A3C2A4714C40E4952BDBA974B1D54D042C3B72D0457A191CB6668690322E9BA450704CD264453877A65DF6C1F161B28234206F16181BE332AE77E77BF3160B8DF501252B4CEB00683FE36D3126BDF44A8E62E38D4F20AF591FEC53ED14A681756DB3CC3120615F198D14789BE8CB992DC0F6502FE4C41E888F5F28A940D1332773F4E2808D88D0A58474CBD03B5B6A2934F1C2D24053E28EAD3AD7FB5263A61999FF6C3F09506F0F3B5AFECDCCBD3A2BEE4D5E53E27FFD756D0AD366A8BD3BD38AF889E0D6EE09C7ADCB644A6BEBF76003E2441CFBC0F64C1736ADF4B97E8667D3DCC96F6091818B896A384B6C6D741E7C2D1BB08DB99D34CA214A1DA614CD807E5CCE19217C7591D1CEA2D889A6DD6FB7C8410C9C0B271A25FFCB05A4268C9883D68879E1D11B0814EB5E542ECDB4B719FA240CFB64DA98AF6D0486C32655C2911B55AA493A20867B01606127B62B4370772D3094176A51F24DBD7A63C1E572C5A165028D21AC3C6260EED4B6C1017D035BE6C6ED268F8BA8F94245C6CEC85B04B803F679FB9AFDE422F3CD0AE44B494C2A5E7816AD436F8EE0DEF416C0C2EA5841913901141E41A206FC0CCA9289A9E7FE43FBC3F3ED38F9AEB8E60D92C8C77FA8E3E5E50012BD63EE93AA245B4BD9CFF0D17E1C2B7CACC91028590C70E35BFF308EBAD8D6078AA99501C5AE3F0A8933D4CD0D1026E922B1CDF53EF01BFC2AF3ABE5CD56C64D4C1DD5476D6D6DCEBA3283DB91345CDBCAC9F8A189BBCADB0D678D7A859A60539C91E06572175E25E50EDB39CE27938E'
    AES2 = AES(decry, key).decrypt()
    # f = chardet.detect(AES2)
    # print(f)
    print("解密：\n" + AES2.encode('utf-8').decode('unicode_escape'))
