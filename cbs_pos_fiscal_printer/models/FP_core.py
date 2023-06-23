#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""Tremol fiscal printer python core module."""
from datetime import datetime
from enum import Enum
import xml.etree.ElementTree as XML
import base64
import time

try:
    from urllib2 import urlopen, Request
except Exception:
    from urllib.request import urlopen, Request


class FP_core:
    """Tremol fiscal printer python core library."""
    _timestamp = 0
    __coreVersion = '1.0.0.4'
    __fp_datetime_format = "%d-%m-%Y %H:%M:%S"
    __lab_ip = "localhost"
    __lab_port = 4444
    __lab_url = "http://localhost:4444/"
    __w = False
    __ok = False
    __hdrs = {"Content-Type": "text/plain",
              "Keep-Alive": "timeout=60000",
              "Connection": "keep-alive",
              "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7"}

    @staticmethod
    def __range_with_step(start, end, step):
        while start < end:
            yield start
            start += step

    @staticmethod
    def __string_equal_true(text):
        return True if text == "1" or text == "True" else False

    def __send_req(self, my_url, xml_text=None):
        try:
            request_post = Request(my_url, data=xml_text, headers=self.__hdrs)
            req = urlopen(request_post)
            if req.code != 200:
                raise Exception("HTTP code " + str(req.code))
            lines = req.readlines()
            req.close()
            if not lines:
                raise ServerException("Server response missing", SErrorType.ServerResponseMissing)
            xml_parsed = XML.fromstringlist(lines)
            self.__throwOnServerError(xml_parsed)
            return xml_parsed
        except ServerException as fpe:
            raise fpe
        except Exception as ex:
            raise ServerException("Server connection error (" + str(ex) + ")", SErrorType.ServerConnectionError)

    def __analyzeResponse(self, res_root):
        """Analyzes the response from the FP"""
        props = res_root.findall("Res")
        length = len(props)
        result_obj = []
        ppp = 0
        for ppp in range(0, length):
            prop = props[ppp]
            typ = prop.get("Type")
            name = prop.get("Name")
            value = prop.get("Value")
            if name == "Reserve" or typ == "Reserve" or typ == "OptionHardcoded":
                continue  # SKIP
            if typ == "Text":
                result_obj.append(value)
            elif typ == "Number":
                result_obj.append(int(value))
            elif typ == "Decimal":
                result_obj.append(float(value))
            elif typ == "Option":
                result_obj.append(value)
            elif typ == "DateTime":
                result_obj.append(datetime.strptime(value, self.__fp_datetime_format))
            elif typ == "Base64":
                result_obj.append(base64.b64decode(value))
            elif typ == "Decimal_with_format":
                result_obj.append(float(value))
            elif typ == "Decimal_plus_80h":
                result_obj.append(float(value))
            elif typ == "Status":
                if value == "1":
                    result_obj.append(True)
                else:
                    result_obj.append(False)
            elif typ == "Null":
                result_obj.append(None)
            elif ppp == 0 and value == "@":
                result_obj.append(None)
            else:  # unknown typ => string
                result_obj.append(value)
            ppp += 1
        # self.__w = False # в do
        if ppp == 0:
            return None
        elif ppp == 1:
            # return result_obj[name]
            return result_obj[0]
        else:
            return result_obj

    def __checkVersion(self, res_root):
        self.__ok = False
        stgs = res_root.find("settings")
        vers = stgs.find("defVer")
        if vers is None:
            raise ServerException("Unable to get version of server definitions.", SErrorType.ServerResponseError)
        try:
            defv = int(vers.text)
            if defv > self._timestamp:
                raise ServerException("Server definitions are newer than client library.", SErrorType.ServerDefsMismatch)
            elif defv < self._timestamp:
                raise ServerException("Server definitions are older than client library.", SErrorType.ServerDefsMismatch)
            self.__ok = True
        except ServerException as fpe:
            raise fpe
        except Exception as ex:
            raise ServerException("Unable to get version of server definitions.", SErrorType.ServerResponseError)


    def __throwOnServerError(self, res_root):
        """Checks for error from the server"""
        res_code = int(res_root.get("Code"))
        if res_code != 0:
            err_node = res_root.find("Err")
            # source = err_node.get("Source");
            err_msg = err_node.find("Message").text
            if res_code == 40:
                ste1 = err_node.get("STE1")
                ste2 = err_node.get("STE2")
                raise ServerException(err_msg, res_code, int(ste1, 16), int(ste2, 16))
            else:
                raise ServerException(err_msg, res_code)

    def do(self, command_name, *arguments):
        """Sends command to ZfpLab server"""
        self.__w = True
        try:
            count = len(arguments)
            if count > 0 and count % 2 == 1:
                raise Exception("Invalid number of arguments!")
            root = XML.fromstringlist("<Command></Command>")
            root.set("Name", command_name)
            if count > 0:
                args = XML.SubElement(root, "Args")
                for aaa in FP_core.__range_with_step(0, count, 2):
                    if arguments[aaa] is None or arguments[aaa+1] is None:
                        continue
                    arg = XML.SubElement(args, "Arg")
                    arg.set("Name", arguments[aaa])
                    val = arguments[aaa + 1]
                    if isinstance(val, str):
                        arg.set("Value", val)
                    elif isinstance(val, Enum):
                        arg.set("Value", val.value)
                    elif isinstance(val, datetime):
                        dtt = val.strftime(self.__fp_datetime_format)
                        arg.set("Value", dtt)
                    elif isinstance(val, bytearray):
                        b64 = base64.b64encode(val)
                        arg.set("Value", b64.decode("utf-8"))
                    else:
                        arg.set("Value", str(val))

            text = XML.tostring(root)
            resp = self.__send_req(self.__lab_url, text)
            return self.__analyzeResponse(resp)
        except ServerException as fpe:
            raise fpe
        except Exception as ex:
            raise ServerException(str(ex), SErrorType.ServerErr)
        finally:
            self.__w = False

    def getVersionCore(self):
        """Returns the verion of the core library"""
        return self.__coreVersion

    def getVersionDefinitions(self):
        """Returns the definitions of the generated library"""
        return self._timestamp

    def isWorking(self):
        """Action in proggress."""
        return self.__w

    def isCompatible(self):
        """Returns true if server definitions and generated code are with the same versions."""
        return self.__ok

    def serverGetSettings(self):
        """Gets ZfpLab server settings."""
        stgs = __FPServerSettings__()
        stgs.ipaddress = self.__lab_ip
        stgs.tcp_port = self.__lab_port
        return stgs

    def serverSetSettings(self, ipaddress, tcp_port):
        """Sets ZfpLab server settings."""
        self.__lab_ip = ipaddress
        self.__lab_port = tcp_port
        if not self.__lab_ip.startswith("http"):
            self.__lab_url = "http://"
        self.__lab_url += self. __lab_ip
        if self.__lab_port > 0:
            self.__lab_url += ":" + str(self.__lab_port)
        if not self.__lab_url.endswith("/"):
            self.__lab_url += "/"

    def serverFindDevice(self):
        """Finds device connected on USB or serial port."""
        self.__w = True
        try:
            finddev = self.__lab_url + "finddevice"
            root = self.__send_req(finddev)
            found = __FPDeviceSettings__()
            stgs = root.find("device")
            if stgs is not None:
                found.serial_port = stgs.find("com").text
                found.baud_rate = int(stgs.find("baud").text)
                found.is_working_on_tcp = False
                return found
            else:
                return None
        except ServerException as fpe:
            raise fpe
        except Exception as ex:
            raise ServerException("Server Connection error (" + str(ex) + ")", SErrorType.ServerConnectionError)
        finally:
            self.__w = False

    def serverGetDeviceSettings(self):
        """Gets the device settings."""
        self.__w = True
        try:
            settings = self.__lab_url + "settings"
            root = self.__send_req(settings)
            devs = __FPDeviceSettings__()
            stgs = root.find("settings")
            devs.is_working_on_tcp = FP_core.__string_equal_true(stgs.find("tcp").text)
            devs.serial_port = stgs.find("com").text
            devs.baud_rate = int(stgs.find("baud").text)
            devs.ipaddress = stgs.find("ip").text
            devs.tcp_port = int(stgs.find("port").text)
            devs.password = stgs.find("password").text
            devs.keep_port_open = FP_core.__string_equal_true(stgs.find("keepPortOpen"))
            return devs
        except ServerException as fpe:
            raise fpe
        except Exception as ex:
            raise ServerException("Server Connection error (" + str(ex) + ")", SErrorType.ServerConnectionError)
        finally:
            self.__w = False

    def serverSetDeviceSerialSettings(self, com, baud):
        """Sets Device serial port communication settings"""
        self.__w = True
        try:
            url = self.__lab_url + "settings(com="+com+",baud="+str(baud)+",tcp=0)"
            root = self.__send_req(url)
            try:
                self.__checkVersion(root)
            except ServerException as fpe:
                if fpe.code == SErrorType.ServerResponseError:
                    time.sleep(0.6)
                    root = self.__send_req(url)
                    self.__checkVersion(root)
                else:
                    raise fpe
        finally:
            self.__w = False

    def serverSetDeviceTcpSettings(self, ipaddress, tcp_port, password=None):
        """Sets Device LAN/WIFI communication settings"""
        self.__w = True
        try:
            url = self.__lab_url + "settings(ip=" + ipaddress + "," + "port=" + str(tcp_port) + ",tcp=1"
            if password is not None:
                url += (",password=" + password)
            url += ")"
            root = self.__send_req(url)
            try:
                self.__checkVersion(root)
            except ServerException as fpe:
                if fpe.code == SErrorType.ServerResponseError:
                    time.sleep(0.6)
                    root = self.__send_req(url)
                    self.__checkVersion(root)
                else:
                    raise fpe
        finally:
            self.__w = False

    def serverGetClients(self):
        """Gets ZfpLab server connected clients"""
        self.__w = True
        try:
            url = self.__lab_url + "clients"
            root = self.__send_req(url)
            client_nodes = root.findall("Client")
            clients = []
            for ccc in range(0, client_nodes.count):
                client = __FPClient__()
                client.ident = client_nodes[ccc].find("Id").text
                client.ipaddress = client_nodes[ccc].find("ip").text
                client.is_connected = FP_core.__string_equal_true(root.find("PortIsOpen").text)
                clients.append(client)
                continue
            return clients
        finally:
            self.__w = False

    def serverRemoveClient(self, ipaddress):
        """Removes client from the server"""
        self.__w = True
        try:
            url = self.__lab_url + "clientremove(ip=" + ipaddress + ")"
            self.__send_req(url)
        finally:
            self.__w = False

    def serverCloseDeviceConnection(self):
        """Closes the connection of the current client"""
        self.__w = True
        try:
            url = self.__lab_url + "clientremove(who=me)"
            self.__send_req(url)
        finally:
            self.__w = False

    def serverRemoveAllClients(self):
        """Removes all clients from the server"""
        self.__w = True
        try:
            url = self.__lab_url + "clientremove(who=all)"
            self.__send_req(url)
        finally:
            self.__w = False

    def serverSetLog(self, enable):
        """Enables or disables ZfpLab server log"""
        self.__w = True
        try:
            if enable:
                url = self.__lab_url + "log(on=1)"
            else:
                url = self.__lab_url + "log(on=0)"
            self.__send_req(url)
        finally:
            self.__w = False


class __FPServerSettings__:
    """ZfpLab server settings."""
    ipaddress = "localhost"
    tcp_port = 4444


class __FPClient__:
    """Connected clients."""
    ident = ""
    ipaddress = "localhost"
    is_connected = False


class __FPDeviceSettings__:
    """Device settings."""
    is_working_on_tcp = True
    ipaddress = "192.168.88.133"
    tcp_port = 8000
    password = "123456"
    serial_port = "COM1"
    baud_rate = 115200
    keep_port_open = False


class SErrorType:
    """SErrorType"""
    OK = 0
    # The current library version and the fiscal device firmware is not matching
    ServMismatchBetweenDefinitionAndFPResult = 9
    ServDefMissing = 10
    ServArgDefMissing = 11
    ServCreateCmdString = 12
    ServUndefined = 19
    # When the server can not connect to the fiscal device
    ServSockConnectionFailed = 30
    # Wrong device TCP password
    ServTCPAuth = 31
    ServWrongTcpConnSettings = 32
    ServWrongSerialPortConnSettings = 33
    # Processing of other clients command is taking too long
    ServWaitOtherClientCmdProcessingTimeOut = 34
    ServDisconnectOtherClientErr = 35
    FPException = 40
    ClientArgDefMissing = 50
    ClientAttrDefMissing = 51
    ClientArgValueWrongFormat = 52
    ClientSettingsNotInitialized = 53
    ClientInvalidGetFormat = 62
    ClientInvalidPostFormat = 63
    ServerAddressNotSet = 100
    # Specify server ServerAddress property
    ServerConnectionError = 101
    # Connection from this app to the server is not established
    ServerResponseMissing = 102
    ServerResponseError = 103
    # The current library version and server definitions version do not match
    ServerDefsMismatch = 104
    ClientXMLCanNotParse = 105,
    PaymentNotSupported = 201,
    ServerErr = 1000


class ServerException(Exception):
    """ZfpLab server or device error
    :param code: int code from enumeration SErrorType\n
    :type code: int\n
    :param ste1: int if code==40 or None\n
    :type ste1: int\n
    :param ste2: int if code==40 or None\n
    :type ste2: int\n
    """
    def __init__(self, message, code, ste1=None, ste2=None):
        super(ServerException, self).__init__(message)
        self.code = code
        self.ste1 = ste1
        self.ste2 = ste2
        self.isFiscalPrinterError = (code == SErrorType.FPException)

