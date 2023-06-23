#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tremol fiscal printer python module."""
from .FP_core import FP_core
from enum import Enum
from datetime import datetime


class FP(FP_core):
    """Tremol fiscal printer python library."""

    FP_core._timestamp = 2108021650

    def ReadGPRS_Signal(self):
        """
        Provides information about device's GPRS signal.\n
        :rtype: str
        """
        return self.do("ReadGPRS_Signal")

    def ReadDailyAvailableAmounts(self):
        """
        Provides information about the amounts on hand by type of payment.\n
        """
        return __DailyAvailableAmountsRes__(*self.do("ReadDailyAvailableAmounts"))

    def PrintArticleReport(self, OptionZeroing):
        """
        Prints an article report with or without zeroing ('Z' or 'X').\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Not zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintArticleReport", 'OptionZeroing', OptionZeroing)

    def ReadDecimalPoint(self):
        """
        Provides information about the current (the last value stored into the FM) decimal point format.\n
        :rtype: Enums.OptionDecimalPointPosition
        """
        return self.do("ReadDecimalPoint")

    def ProgParameters(self, POSNum, OptionPrintLogo, OptionAutoOpenDrawer, OptionAutoCut, OptionExternalDispManagement, OptionEnableCurrency, OptionUSBHost):
        """
        Programs the number of POS, printing of logo, Cash drawer opening, display mode, cutting permission. Changes in USBHost parameter will power off the printer.\n
        :param POSNum: 4 symbols for number of POS in format ####\n
        :type POSNum: float\n
        :param OptionPrintLogo: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionPrintLogo: Enums.OptionPrintLogo\n
        :param OptionAutoOpenDrawer: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionAutoOpenDrawer: Enums.OptionAutoOpenDrawer\n
        :param OptionAutoCut: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionAutoCut: Enums.OptionAutoCut\n
        :param OptionExternalDispManagement: 1 symbol of value: 
         - '1' - Manual 
         - '0' - Auto\n
        :type OptionExternalDispManagement: Enums.OptionExternalDispManagement\n
        :param OptionEnableCurrency: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionEnableCurrency: Enums.OptionEnableCurrency\n
        :param OptionUSBHost: 1 symbol, FP Only, with value: 
         - '0' - No 
         - '1' - Yes\n
        :type OptionUSBHost: Enums.OptionUSBHost\n
        """
        self.do("ProgParameters", 'POSNum', POSNum, 'OptionPrintLogo', OptionPrintLogo, 'OptionAutoOpenDrawer', OptionAutoOpenDrawer, 'OptionAutoCut', OptionAutoCut, 'OptionExternalDispManagement', OptionExternalDispManagement, 'OptionEnableCurrency', OptionEnableCurrency, 'OptionUSBHost', OptionUSBHost)

    def StornoPLU(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Registers the correction article with specified name, price, quantity, VAT class and discount/addition on the transaction.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price with minus sign for storno operation\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("StornoPLU", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def StartTest_Lan(self):
        """
        Start LAN test on the device and print out the result\n
        """
        self.do("StartTest_Lan")

    def ReadDepartment(self, DepNum):
        """
        Provides information for the programmed data, the turnover from the stated department number\n
        :param DepNum: 2 symbols for deparment number in format: ##\n
        :type DepNum: float\n
        """
        return __DepartmentRes__(*self.do("ReadDepartment", 'DepNum', DepNum))

    def ReadStornoNameMessage(self):
        """
        Provide information about the Storno Name Message.\n
        :rtype: str
        """
        return self.do("ReadStornoNameMessage")

    def ReadEJByReceiptNum(self, StartNum, EndNum):
        """
        Read Electronic Journal Report from receipt number to receipt number.\n
        :param StartNum: 6 symbols for initial receipt number included in report in format ######.\n
        :type StartNum: float\n
        :param EndNum: 6 symbols for final receipt number included in report in format ######.\n
        :type EndNum: float\n
        """
        self.do("ReadEJByReceiptNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def PrintSpecialEventsFMReport(self):
        """
        Print all special FM events report.\n
        """
        self.do("PrintSpecialEventsFMReport")

    def ReadCurrencyAmountsByOperator(self, OperNum):
        """
        Provides information about the accumulated amounts from sale of foreign currency, currency purchase and commissions for operator.\n
        :param OperNum: Symbol from '1' to '20' corresponding to 
        operator's number\n
        :type OperNum: str\n
        """
        return __CurrencyAmountsByOperatorRes__(*self.do("ReadCurrencyAmountsByOperator", 'OperNum', OperNum))

    def ProgPLUgeneral(self, PLUNum, Name, Price, OptionPrice, OptionVATClass, BelongToDepNum, AlteTaxNum, AlteTaxValue, OptionTransaction=None):
        """
        Programs the general data for a certain article in the internal database. The price may have variable length, while the name field is fixed.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Name: 34 symbols for article name; Symbol for LF=7Ch - '|'; separator for 
        MU=80h or 60h followed up to 3 symbols for unit.\n
        :type Name: str\n
        :param Price: 1 to 10 symbols for article price\n
        :type Price: float\n
        :param OptionPrice: 1 byte for Price flag with next value: 
         - '0'- Free price is disable valid only programmed price 
         - '1'- Free price is enable 
         - '2'- Limited price\n
        :type OptionPrice: Enums.OptionPrice\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param BelongToDepNum: BelongToDepNo + 80h. 1 symbol for article department attachment, 
        formed in the following manner: example: Dep01 = 81h, Dep02 =\n
        :type BelongToDepNum: float\n
        :param AlteTaxNum: Up to 11 symbols for Alte Tax number\n
        :type AlteTaxNum: float\n
        :param AlteTaxValue: Up to 11 symbols for Alte tax value\n
        :type AlteTaxValue: float\n
        :param OptionTransaction: 1 symbol with value: 
         - '1' - Active Single transaction in receipt 
         - '0' - Inactive default value 
        Note: this parameter is not obligatory\n
        :type OptionTransaction: Enums.OptionTransaction\n
        """
        self.do("ProgPLUgeneral", 'PLUNum', PLUNum, 'Name', Name, 'Price', Price, 'OptionPrice', OptionPrice, 'OptionVATClass', OptionVATClass, 'BelongToDepNum', BelongToDepNum, 'AlteTaxNum', AlteTaxNum, 'AlteTaxValue', AlteTaxValue, 'OptionTransaction', OptionTransaction)

    def ProgCustomerVATNum(self, Password, OwnerVATNum, OptionTypeVATregistration):
        """
        Program the owner's VAT number and VAT registration type.\n
        :param Password: 6-symbol string\n
        :type Password: str\n
        :param OwnerVATNum: 15 symbols for VAT number\n
        :type OwnerVATNum: str\n
        :param OptionTypeVATregistration: 1 symbol for type of owner's VAT registration: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionTypeVATregistration: Enums.OptionTypeVATregistration\n
        """
        self.do("ProgCustomerVATNum", 'Password', Password, 'OwnerVATNum', OwnerVATNum, 'OptionTypeVATregistration', OptionTypeVATregistration)

    def PrintOrStoreEJByReceiptNum(self, OptionReportStorage, StartNum, EndNum):
        """
        Store Electronic Journal Report from receipt number to receipt number to External USB Flash memory, External SD card or Print.\n
        :param OptionReportStorage: 2 symbols for destination: 
         - 'J1' - Printing  
         - 'J2' - Storage in External USB Flash memory. 
         - 'J4' - Storage in External SD card memory\n
        :type OptionReportStorage: Enums.OptionReportStorage\n
        :param StartNum: 6 symbols for initial receipt number in format ###### 
        included in report.\n
        :type StartNum: float\n
        :param EndNum: 6 symbolsfor final receipt number included in format ###### 
        in report.\n
        :type EndNum: float\n
        """
        self.do("PrintOrStoreEJByReceiptNum", 'OptionReportStorage', OptionReportStorage, 'StartNum', StartNum, 'EndNum', EndNum)

    def PrintDiscountOrAddition(self, OptionType, OptionDisplay, DiscAddV=None, DiscAddP=None):
        """
        Percent or value discount/addition over sum of transaction or over subtotal sum depends on parameter "OptionType".\n
        :param OptionType: 1 symbol with value  
        - '2' - Defined from the device  
        - '1' - Over subtotal 
        - '0' - Over transaction sum\n
        :type OptionType: Enums.OptionType\n
        :param OptionDisplay: 1 symbol with value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionDisplay: Enums.OptionDisplay\n
        :param DiscAddV: 1 to 10 symbols for the value of the discount/addition. 
        Use minus sign '-' for discount\n
        :type DiscAddV: float\n
        :param DiscAddP: 1 to 7 symbols for the percentage value of the 
        discount/addition. Use minus sign '-' for discount\n
        :type DiscAddP: float\n
        :rtype: float
        """
        return self.do("PrintDiscountOrAddition", 'OptionType', OptionType, 'OptionDisplay', OptionDisplay, 'DiscAddV', DiscAddV, 'DiscAddP', DiscAddP)

    def SetFiscalNum(self, Password, VATNum, FMNum, OptionTypeVATregistration):
        """
        Stores the VAT registration and Fiscal Memory number into the operative memory.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        :param VATNum: 15 symbols VAT registration number\n
        :type VATNum: str\n
        :param FMNum: 10 symbols Fiscal Memory serial number\n
        :type FMNum: str\n
        :param OptionTypeVATregistration: 1 symbol for type of owner's VAT registration: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionTypeVATregistration: Enums.OptionTypeVATregistration\n
        """
        self.do("SetFiscalNum", 'Password', Password, 'VATNum', VATNum, 'FMNum', FMNum, 'OptionTypeVATregistration', OptionTypeVATregistration)

    def PrintOrStoreEJ(self, OptionReportStorage):
        """
        Store whole Electronic Journal report to External USB Flash memory, External SD card or Print.\n
        :param OptionReportStorage: 2 symbols for destination: 
         - 'J1' - Printing  
         - 'J2' - Storage in External USB Flash memory. 
         - 'J4' - Storage in External SD card memory\n
        :type OptionReportStorage: Enums.OptionReportStorage\n
        """
        self.do("PrintOrStoreEJ", 'OptionReportStorage', OptionReportStorage)

    def ProgCIFNameMessage(self, Password, CIFName):
        """
        Program the contents of a CIF name message.\n
        :param Password: 6-symbol string\n
        :type Password: str\n
        :param CIFName: 8 symbols for CIF name\n
        :type CIFName: str\n
        """
        self.do("ProgCIFNameMessage", 'Password', Password, 'CIFName', CIFName)

    def ReadUsedComModule(self):
        """
        Provides information about the communication module, used for talking with the server\n
        :rtype: Enums.OptionCommunicationModule
        """
        return self.do("ReadUsedComModule")

    def RestorePreviousHeader(self):
        """
        Restore previous header if current header is not saved into fiscal memory.\n
        """
        self.do("RestorePreviousHeader")

    def CashDrawerOpen(self):
        """
        Opens cash drawer\n
        """
        self.do("CashDrawerOpen")

    def SetTCPpassword(self, PassLength, Password):
        """
        Program device's TCP password. To apply use - 4Eh / N - Save network settings\n
        :param PassLength: Up to 3 symbols for the password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the TCP password\n
        :type Password: str\n
        """
        self.do("SetTCPpassword", 'PassLength', PassLength, 'Password', Password)

    def DisplayTextLines1and2(self, Text):
        """
        Shows a 40-symbol text in the two display lines.\n
        :param Text: 40 symbols text\n
        :type Text: str\n
        """
        self.do("DisplayTextLines1and2", 'Text', Text)

    def ReadEJByZReportNum(self, StartNum, EndNum):
        """
        Read Electronic Journal Report from report number to report number.\n
        :param StartNum: 4 symbols for initial number report in format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for final number report in format ####\n
        :type EndNum: float\n
        """
        self.do("ReadEJByZReportNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def SellPLUFromFD_DB(self, OptionSign, PLUNum, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None):
        """
        Registers the sale or correction of a specified quantity of an article of the internal database of the FD.\n
        :param OptionSign: 1 symbol with optional value: 
         - '+' - Sale 
         - '-' - Correction\n
        :type OptionSign: Enums.OptionSign\n
        :param PLUNum: 5 symbols for number of article of FPR's db in format: #####\n
        :type PLUNum: float\n
        :param Quantity: 1 to 10 symbols for article's quantity sold\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 symbols for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        """
        self.do("SellPLUFromFD_DB", 'OptionSign', OptionSign, 'PLUNum', PLUNum, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed)

    def ReadDateTime(self):
        """
        Provides information about the current date and time.\n
        :rtype: datetime
        """
        return self.do("ReadDateTime")

    def PayExactSum(self, OptionPaymentType):
        """
        Register the payment in the receipt with specified type of payment and exact amount received.\n
        :param OptionPaymentType: 1 symbol for payment type: 
         - '0' - Payment 0 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6 
         - '7' - Payment 7 
         - '8' - Payment 8 
         - '9' - Payment 9\n
        :type OptionPaymentType: Enums.OptionPaymentType\n
        """
        self.do("PayExactSum", 'OptionPaymentType', OptionPaymentType)

    def StartTest_WiFi(self):
        """
        Start WiFi test on the device and print out the result\n
        """
        self.do("StartTest_WiFi")

    def SetDeviceMAC_Address(self, DeviceMAC):
        """
        Provides information about TCP device MAC address\n
        :param DeviceMAC: 12 symbols for device MAC\n
        :type DeviceMAC: str\n
        """
        self.do("SetDeviceMAC_Address", 'DeviceMAC', DeviceMAC)

    def ReadFMfreeRecords(self):
        """
        Read the number of the remaining free records for Z-report in the Fiscal Memory.\n
        :rtype: str
        """
        return self.do("ReadFMfreeRecords")

    def ReadBluetooth_Password(self):
        """
        Provides information about device's Bluetooth password.\n
        """
        return __Bluetooth_PasswordRes__(*self.do("ReadBluetooth_Password"))

    def CancelReceipt(self):
        """
        Cancel the opened fiscal receipt.\n
        """
        self.do("CancelReceipt")

    def SellPLUfromDep(self, NamePLU, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, DepNum=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article belonging to department with specified name, price, quantity and/or discount/addition on the transaction. The VAT of article got from department to which article belongs.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DepNum: 1 symbol for article department attachment, 
        formed in the following manner; example: Dep01 = 81h, Dep02 = 82h … 
        Dep19 = 93h\n
        :type DepNum: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellPLUfromDep", 'NamePLU', NamePLU, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'DepNum', DepNum, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def Read_IdleTimeout(self):
        """
        Provides information about device's idle timeout. This timeout is for closing the connection if there is an inactivity. Maximal value - 7200, minimal value 1. 0 is for never close the connection. This option can be used only if the device has LAN or WiFi.\n
        :rtype: float
        """
        return self.do("Read_IdleTimeout")

    def ProgOperator(self, Number, Name, Password):
        """
        Programs the operator's name and password.\n
        :param Number: Symbols from '1' to '20' corresponding to operator's number\n
        :type Number: float\n
        :param Name: 20 symbols for operator's name\n
        :type Name: str\n
        :param Password: 4 symbols for operator's password\n
        :type Password: str\n
        """
        self.do("ProgOperator", 'Number', Number, 'Name', Name, 'Password', Password)

    def StoreDetailedFMReportByZNum(self, StartNum, EndNum, OptionStorage=None):
        """
        Storage a detailed FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        :param OptionStorage: 1 symbol for destination: 
         - '2' - Storage in External USB Flash memory. 
         - '4' - Storage in External SD card memory\n
        :type OptionStorage: Enums.OptionStorage\n
        """
        self.do("StoreDetailedFMReportByZNum", 'StartNum', StartNum, 'EndNum', EndNum, 'OptionStorage', OptionStorage)

    def ReadCIFNameMessage(self):
        """
        Provide information about the CIF name message.\n
        :rtype: str
        """
        return self.do("ReadCIFNameMessage")

    def SetBluetooth_Password(self, PassLength, Password):
        """
        Program device's Bluetooth password.\n
        :param PassLength: Up to 3 symbols for the BT password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the BT password\n
        :type Password: str\n
        """
        self.do("SetBluetooth_Password", 'PassLength', PassLength, 'Password', Password)

    def ReadGPRS_APN(self):
        """
        Provides information about device's GRPS APN.\n
        """
        return __GPRS_APNRes__(*self.do("ReadGPRS_APN"))

    def ReadPLUqty(self, PLUNum):
        """
        Provides information about the quantity registers of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUqtyRes__(*self.do("ReadPLUqty", 'PLUNum', PLUNum))

    def ScanAndPrintWiFiNetworks(self):
        """
        Scan and print all available WiFi networks\n
        """
        self.do("ScanAndPrintWiFiNetworks")

    def SetServerCommunicationModule(self, OptionCommunicationModule):
        """
        Program the communication module, which used to talk with the server\n
        :param OptionCommunicationModule: 1 symbol with value: 
         - '0' - GSM 
         - '1' - LAN\n
        :type OptionCommunicationModule: Enums.OptionCommunicationModule\n
        """
        self.do("SetServerCommunicationModule", 'OptionCommunicationModule', OptionCommunicationModule)

    def ReadGPRS_Username(self):
        """
        Provides information about device's GPRS username.\n
        """
        return __GPRS_UsernameRes__(*self.do("ReadGPRS_Username"))

    def ReceivedOnAccount_PaidOut(self, OperNum, OperPass, Amount, Text=None):
        """
        Registers cash received on account or paid out.\n
        :param OperNum: Symbol from 1 to 20 corresponding to the operator's number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param Amount: 1 to 10 symbols for the amount lodged/withdrawn\n
        :type Amount: float\n
        :param Text: Text - TextLength-2 symbols length\n
        :type Text: str\n
        """
        self.do("ReceivedOnAccount_PaidOut", 'OperNum', OperNum, 'OperPass', OperPass, 'Amount', Amount, 'Text', Text)

    def StoreDetailedFMReportByDate(self, StartDate, EndDate, OptionStorage=None):
        """
        Storage a detailed FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        :param OptionStorage: 1 symbol for destination: 
         - '2' - Storage in External USB Flash memory. 
         - '4' - Storage in External SD card memory\n
        :type OptionStorage: Enums.OptionStorage\n
        """
        self.do("StoreDetailedFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate, 'OptionStorage', OptionStorage)

    def SaveNetworkSettings(self):
        """
        After every change on Idle timeout, LAN/WiFi/GPRS usage, LAN/WiFi/TCP/GPRS password or TCP auto start networks settings this Save command needs to be execute.\n
        """
        self.do("SaveNetworkSettings")

    def ReadECRprofileConnectionPeriod(self):
        """
        Provides information about period in which the sending attempt is made.\n
        :rtype: float
        """
        return self.do("ReadECRprofileConnectionPeriod")

    def ActivateSIM(self, Password):
        """
        Activates the SIM card.\n
        :param Password: 10-symbols string\n
        :type Password: str\n
        """
        self.do("ActivateSIM", 'Password', Password)

    def DirectCommand(self, Input):
        """
        Executes the direct command .\n
        :param Input: Raw request to FP\n
        :type Input: str\n
        :rtype: str
        """
        return self.do("DirectCommand", 'Input', Input)

    def ReadDetailedFMReportByZNum(self, StartNum, EndNum):
        """
        Storage a detailed FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("ReadDetailedFMReportByZNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def UnlockDeviceforUpdate(self, Password):
        """
        Unlocks the device for update procedure.\n
        :param Password: 10-symbols string\n
        :type Password: str\n
        """
        self.do("UnlockDeviceforUpdate", 'Password', Password)

    def DisbleServiceContract(self, Password):
        """
        Set service contract disable\n
        :param Password: 6 symbols for service password\n
        :type Password: str\n
        """
        self.do("DisbleServiceContract", 'Password', Password)

    def OpenSpecialDocumentReceipt(self, OperNum, OperPass, OptionCustomerReceiptPrintType, CustomerVATNum, InvRecipient, InvFree1, InvFree2, InvFree3, InvFree4, Address):
        """
        Opens a special Customer fiscal receipt document assigned to the specified operator, Customer data and print type depends on CustomerReceiptPrintType parameter.\n
        :param OperNum: Symbol from 1 to 20 corresponding to operator's 
        number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param OptionCustomerReceiptPrintType: 1 symbol with value: 
         - '1' - Step by step printing 
         - '3' - Postponed printing 
         - '5' - Buffered printing\n
        :type OptionCustomerReceiptPrintType: Enums.OptionCustomerReceiptPrintType\n
        :param CustomerVATNum: 15 ASCII symbols text for Customer VAT number\n
        :type CustomerVATNum: str\n
        :param InvRecipient: 30 ASCII symbols for Recipient name\n
        :type InvRecipient: str\n
        :param InvFree1: 20 ASCII symbols for free text line\n
        :type InvFree1: str\n
        :param InvFree2: 20 ASCII symbols for free text line\n
        :type InvFree2: str\n
        :param InvFree3: 20 ASCII symbols for free text line\n
        :type InvFree3: str\n
        :param InvFree4: 20 ASCII symbols for free text line\n
        :type InvFree4: str\n
        :param Address: 30 ASCII symbols for customer address\n
        :type Address: str\n
        """
        self.do("OpenSpecialDocumentReceipt", 'OperNum', OperNum, 'OperPass', OperPass, 'OptionCustomerReceiptPrintType', OptionCustomerReceiptPrintType, 'CustomerVATNum', CustomerVATNum, 'InvRecipient', InvRecipient, 'InvFree1', InvFree1, 'InvFree2', InvFree2, 'InvFree3', InvFree3, 'InvFree4', InvFree4, 'Address', Address)

    def OpenCurrencySaleReceipt(self, OperNum, OperPass, OptionCurrencySaleRcpPrintType, Text1, Text2, Text3, Text4, Text5, Text6):
        """
        Opens a fiscal receipt assigned to the specified operator for Currency Sale transaction.\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param OptionCurrencySaleRcpPrintType: 1 symbol with value 
         - '0' - Step by step printing 
         - '2' - Postponed printing\n
        :type OptionCurrencySaleRcpPrintType: Enums.OptionCurrencySaleRcpPrintType\n
        :param Text1: 26 symbols free text for header line 1 in the receipt\n
        :type Text1: str\n
        :param Text2: 26 symbols free text for header line 2 in the receipt\n
        :type Text2: str\n
        :param Text3: 26 symbols free text for header line 3 in the receipt\n
        :type Text3: str\n
        :param Text4: 26 symbols free text for header line 4 in the receipt\n
        :type Text4: str\n
        :param Text5: 26 symbols free text for header line 5 in the receipt\n
        :type Text5: str\n
        :param Text6: 26 symbols free text for header line 6 in the receipt\n
        :type Text6: str\n
        """
        self.do("OpenCurrencySaleReceipt", 'OperNum', OperNum, 'OperPass', OperPass, 'OptionCurrencySaleRcpPrintType', OptionCurrencySaleRcpPrintType, 'Text1', Text1, 'Text2', Text2, 'Text3', Text3, 'Text4', Text4, 'Text5', Text5, 'Text6', Text6)

    def SetWiFi_NetworkName(self, WiFiNameLength, WiFiNetworkName):
        """
        Program device's WiFi network name where it will connect. To apply use - 4Eh / N - Save network settings\n
        :param WiFiNameLength: Up to 3 symbols for the WiFi network name len\n
        :type WiFiNameLength: float\n
        :param WiFiNetworkName: Up to 100 symbols for the device's WiFi ssid network name\n
        :type WiFiNetworkName: str\n
        """
        self.do("SetWiFi_NetworkName", 'WiFiNameLength', WiFiNameLength, 'WiFiNetworkName', WiFiNetworkName)

    def ProgCustomerData(self, CustomerNum, VATNumber, CustomerCompanyName, Address, FreeLine1, FreeLine2, FreeLine3, FreeLine4):
        """
        Programs the customer DB for special customer receipt issuing.\n
        :param CustomerNum: 3 symbols for customer number in order in format ###\n
        :type CustomerNum: float\n
        :param VATNumber: 15 symbols for customer VAT registration number\n
        :type VATNumber: str\n
        :param CustomerCompanyName: 30 symbols for customer name\n
        :type CustomerCompanyName: str\n
        :param Address: 30 symbols for address on customer\n
        :type Address: str\n
        :param FreeLine1: 20 ASCII symbols for customer data\n
        :type FreeLine1: str\n
        :param FreeLine2: 20 ASCII symbols for customer data\n
        :type FreeLine2: str\n
        :param FreeLine3: 20 ASCII symbols for customer data\n
        :type FreeLine3: str\n
        :param FreeLine4: 20 ASCII symbols for customer data\n
        :type FreeLine4: str\n
        """
        self.do("ProgCustomerData", 'CustomerNum', CustomerNum, 'VATNumber', VATNumber, 'CustomerCompanyName', CustomerCompanyName, 'Address', Address, 'FreeLine1', FreeLine1, 'FreeLine2', FreeLine2, 'FreeLine3', FreeLine3, 'FreeLine4', FreeLine4)

    def ReadDeviceMAC_Address(self):
        """
        Provides information about TCP device MAC address\n
        :rtype: str
        """
        return self.do("ReadDeviceMAC_Address")

    def SellPLUwithSpecifiedVAT(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article with specified name, price, quantity, VAT class and/or discount/addition on the transaction.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values: 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellPLUwithSpecifiedVAT", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ReadFirstZReportNumFromDate(self, DateFrom):
        """
        Provide information about first located Z report, having the same date or the date after the input date\n
        :param DateFrom: 6 symbols for specified date in format "DDMMYY"\n
        :type DateFrom: datetime\n
        :rtype: float
        """
        return self.do("ReadFirstZReportNumFromDate", 'DateFrom', DateFrom)

    def PrintBriefFMReportByDate(self, StartDate, EndDate):
        """
        Print a brief FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("PrintBriefFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def DisplayTextLine1(self, Text):
        """
        Shows a 20-symbol text in the upper display line.\n
        :param Text: 20 symbols text\n
        :type Text: str\n
        """
        self.do("DisplayTextLine1", 'Text', Text)

    def ReadServerAddress(self):
        """
        Provides information about the ECR's password\n
        """
        return __ServerAddressRes__(*self.do("ReadServerAddress"))

    def ReadVATrates(self):
        """
        Provides information about the current VAT rates (the last value stored in FM).\n
        """
        return __VATratesRes__(*self.do("ReadVATrates"))

    def ReadServiceWarningMessages(self, Password):
        """
        Read the programmed service contract warning message text.\n
        :param Password: 6 symbols for service password\n
        :type Password: str\n
        """
        return __ServiceWarningMessagesRes__(*self.do("ReadServiceWarningMessages", 'Password', Password))

    def ReadDailyReceivedSalesAmounts(self):
        """
        Provides information about the amounts received from sales by type of payment.\n
        """
        return __DailyReceivedSalesAmountsRes__(*self.do("ReadDailyReceivedSalesAmounts"))

    def ReadLastAndTotalReceiptNum(self):
        """
        Provides information about the number of the last issued receipt.\n
        """
        return __LastAndTotalReceiptNumRes__(*self.do("ReadLastAndTotalReceiptNum"))

    def ProgPLUqty(self, PLUNum, AvailableQuantity, OptionQuantityType):
        """
        Programs available quantity and Quantiy type for a certain article in the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param AvailableQuantity: Up to 11 symbols for quantity in stock\n
        :type AvailableQuantity: float\n
        :param OptionQuantityType: 1 symbol for Quantity flag with next value:  
         - '0'- Availability of PLU stock is not monitored  
         - '1'- Disable negative quantity  
         - '2'- Enable negative quantity\n
        :type OptionQuantityType: Enums.OptionQuantityType\n
        """
        self.do("ProgPLUqty", 'PLUNum', PLUNum, 'AvailableQuantity', AvailableQuantity, 'OptionQuantityType', OptionQuantityType)

    def ClearDisplay(self):
        """
        Clears the display.\n
        """
        self.do("ClearDisplay")

    def SellFractQtyPLUwithSpecifiedVAT(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article with specified VAT. If department is present the relevant accumulations are perfomed in its registers.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 3 to 10 symbols for quantity in format fractional format (e.g. 1/3)\n
        :type Quantity: str\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellFractQtyPLUwithSpecifiedVAT", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def SetDHCP_Enabled(self, OptionDhcpStatus):
        """
        Program device's TCP network DHCP enabled or disabled. To apply use - 4Eh / N - Save network settings\n
        :param OptionDhcpStatus: 1 symbol with value: 
         - '0' - Disabled 
         - '1' - Enabled\n
        :type OptionDhcpStatus: Enums.OptionDhcpStatus\n
        """
        self.do("SetDHCP_Enabled", 'OptionDhcpStatus', OptionDhcpStatus)

    def ReadSerialNum(self):
        """
        Provides information about the manufactoring number of the fiscal device.\n
        :rtype: str
        """
        return self.do("ReadSerialNum")

    def SetGPRS_APN(self, GPRS_APN_Len, APN):
        """
        Program device's GPRS APN. To apply use - SaveNetworkSettings()\n
        :param GPRS_APN_Len: Up to 3 symbols for the APN len\n
        :type GPRS_APN_Len: float\n
        :param APN: Up to 100 symbols for the device's GPRS APN\n
        :type APN: str\n
        """
        self.do("SetGPRS_APN", 'GPRS_APN_Len', GPRS_APN_Len, 'APN', APN)

    def ReadLastCurrencyReceiptNum(self):
        """
        Provides information about the fiscal receipt counters for Currency Exchange Offices\n
        """
        return __LastCurrencyReceiptNumRes__(*self.do("ReadLastCurrencyReceiptNum"))

    def ReadDailyPObyOperator(self, OperNum):
        """
        Read the PO by type of payment and the total number of operations by specified operator\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        """
        return __DailyPObyOperatorRes__(*self.do("ReadDailyPObyOperator", 'OperNum', OperNum))

    def ReadCustomerVATNum(self):
        """
        Provide information about the owner's VAT number and VAT registration type\n
        """
        return __CustomerVATNumRes__(*self.do("ReadCustomerVATNum"))

    def SetSerialNum(self, Password, SerialNum):
        """
        Stores the Manufacturing number into the operative memory.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        :param SerialNum: 11 symbol Manufacturing number\n
        :type SerialNum: str\n
        """
        self.do("SetSerialNum", 'Password', Password, 'SerialNum', SerialNum)

    def PrintDetailedFMPaymentsReportByZNum(self, StartNum, EndNum):
        """
        Print a detailed FM payment report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("PrintDetailedFMPaymentsReportByZNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def ProgPLUprice(self, PLUNum, Price, OptionPrice, AlteTaxNum, AlteTaxValue):
        """
        Program the price for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Price: Up to 10 symbols for article price\n
        :type Price: float\n
        :param OptionPrice: 1 byte for Price flag with next value: 
         - '0'- Free price is disable valid only programmed price 
         - '1'- Free price is enable 
         - '2'- Limited price\n
        :type OptionPrice: Enums.OptionPrice\n
        :param AlteTaxNum: Up to 11 symbols for Alte Tax number\n
        :type AlteTaxNum: float\n
        :param AlteTaxValue: Up to 11 symbols for Alte tax value\n
        :type AlteTaxValue: float\n
        """
        self.do("ProgPLUprice", 'PLUNum', PLUNum, 'Price', Price, 'OptionPrice', OptionPrice, 'AlteTaxNum', AlteTaxNum, 'AlteTaxValue', AlteTaxValue)

    def RawRead(self, Count, EndChar):
        """
         Reads raw bytes from FP.\n
        :param Count: How many bytes to read if EndChar is not specified\n
        :type Count: float\n
        :param EndChar: The character marking the end of the data. If present Count parameter is ignored.\n
        :type EndChar: str\n
        :rtype: bytearray
        """
        return self.do("RawRead", 'Count', Count, 'EndChar', EndChar)

    def StornoPLUwithSpecifiedVATfromDep(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, DepNum=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Registers the correction of article with specified name, price, quantity, VAT class and/or discount/addition on the transaction.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price with minus sign for storno operation\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 2 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 2 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 2 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DepNum: 1 symbol for article department attachment, 
        formed in the following manner; example: Dep01 = 81h, Dep02 = 82h … 
        Dep19 = 93h\n
        :type DepNum: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("StornoPLUwithSpecifiedVATfromDep", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'DepNum', DepNum, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ReadDHCP_Status(self):
        """
        Provides information about device's DHCP status\n
        :rtype: Enums.OptionDhcpStatus
        """
        return self.do("ReadDHCP_Status")

    def ReadTCP_Addresses(self, OptionAddressType):
        """
        Provides information about device's IP address, subnet mask, gateway address, DNS address.\n
        :param OptionAddressType: 1 symbol with value: 
         - '2' - IP address 
         - '3' - Subnet Mask 
         - '4' - Gateway address 
         - '5' - DNS address\n
        :type OptionAddressType: Enums.OptionAddressType\n
        """
        return __TCP_AddressesRes__(*self.do("ReadTCP_Addresses", 'OptionAddressType', OptionAddressType))

    def ReadECRprofileType(self):
        """
        Provides information about device's profile type.\n
        :rtype: Enums.OptionProfileType
        """
        return self.do("ReadECRprofileType")

    def ProgHeader(self, OptionHeaderLine, HeaderText):
        """
        Program the contents of a header lines.\n
        :param OptionHeaderLine: 1 symbol with value: 
         - '1' - Header 1 
         - '2' - Header 2 
         - '3' - Header 3 
         - '4' - Header 4 
         - '5' - Header 5 
         - '6' - Header 6 
         - '7' - Header 7 
         - '8' - Header 8\n
        :type OptionHeaderLine: Enums.OptionHeaderLine\n
        :param HeaderText: TextLength symbols for header lines\n
        :type HeaderText: str\n
        """
        self.do("ProgHeader", 'OptionHeaderLine', OptionHeaderLine, 'HeaderText', HeaderText)

    def CloseNonFiscalReceipt(self):
        """
        Closes the non-fiscal receipt.\n
        """
        self.do("CloseNonFiscalReceipt")

    def PrintBriefFMPaymentsReportByZNum(self, StartNum, EndNum):
        """
        Print a brief payment FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("PrintBriefFMPaymentsReportByZNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def UnpairAllDevices(self):
        """
        Removes all paired devices.\n
        """
        self.do("UnpairAllDevices")

    def DisplayDateTime(self):
        """
        Shows the current date and time on the display.\n
        """
        self.do("DisplayDateTime")

    def SetTCP_AutoStart(self, OptionTCPAutoStart):
        """
        Set device's TCP autostart . To apply use - 4Eh / N - Save network settings\n
        :param OptionTCPAutoStart: 1 symbol with value: 
         - '0' - No 
         - '1' - Yes\n
        :type OptionTCPAutoStart: Enums.OptionTCPAutoStart\n
        """
        self.do("SetTCP_AutoStart", 'OptionTCPAutoStart', OptionTCPAutoStart)

    def PrintOrStoreEJByDate(self, OptionReportStorage, StartRepFromDate, EndRepFromDate):
        """
        Store Electronic Journal Report from report from date to date to External USB Flash memory, External SD card or Print.\n
        :param OptionReportStorage: 2 symbols for destination: 
         - 'J1' - Printing  
         - 'J2' - Storage in External USB Flash memory. 
         - 'J4' - Storage in External SD card memory\n
        :type OptionReportStorage: Enums.OptionReportStorage\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        """
        self.do("PrintOrStoreEJByDate", 'OptionReportStorage', OptionReportStorage, 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate)

    def SetTCP_ActiveModule(self, OptionUsedModule):
        """
        Sets the used TCP module for communication - Lan or WiFi. To apply use - 4Eh / N - Save network settings\n
        :param OptionUsedModule: 1 symbol with value: 
         - '1' - LAN 
         - '2' - WiFi\n
        :type OptionUsedModule: Enums.OptionUsedModule\n
        """
        self.do("SetTCP_ActiveModule", 'OptionUsedModule', OptionUsedModule)

    def SubtotalWithSpecifiedVAT(self, OptionPrinting, OptionDisplay, DiscAddV=None, OptionVATClass=None):
        """
        Calculates the subtotal amount for the specified VAT, with printing and display visualization options. Provides information about values of the calculated amounts. If a percent or value discount/addition has been specified the subtotal and the discount/addition value will be printed regardless the parameter for printing.\n
        :param OptionPrinting: 1 symbol with value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionPrinting: Enums.OptionPrinting\n
        :param OptionDisplay: 1 symbol with value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionDisplay: Enums.OptionDisplay\n
        :param DiscAddV: 1 to 10 symbols for the value of the 
        discount/addition\n
        :type DiscAddV: float\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :rtype: float
        """
        return self.do("SubtotalWithSpecifiedVAT", 'OptionPrinting', OptionPrinting, 'OptionDisplay', OptionDisplay, 'DiscAddV', DiscAddV, 'OptionVATClass', OptionVATClass)

    def ReadTCP_UsedModule(self):
        """
        Read the used TCP module for communication - Lan or WiFi. Command is available if the device support both modules only.\n
        :rtype: Enums.OptionUsedModule
        """
        return self.do("ReadTCP_UsedModule")

    def ReadServiceContractDate(self, Password):
        """
        Read the the service contract expiry date.\n
        :param Password: 6 symbols for service password\n
        :type Password: str\n
        """
        return __ServiceContractDateRes__(*self.do("ReadServiceContractDate", 'Password', Password))

    def PaperFeed(self):
        """
        Feeds 1 line of paper.\n
        """
        self.do("PaperFeed")

    def CloseReceipt(self):
        """
        Closes the opened fiscal receipt.\n
        """
        self.do("CloseReceipt")

    def ProgServiceContractDate(self, Password, ExpiryDate):
        """
        Program the service contract expiry date.\n
        :param Password: 6 symbols for service password\n
        :type Password: str\n
        :param ExpiryDate: 10 symbols for expiry date of service contract\n
        :type ExpiryDate: datetime\n
        """
        self.do("ProgServiceContractDate", 'Password', Password, 'ExpiryDate', ExpiryDate)

    def SellPLUfromDep_(self, NamePLU, DepNum, Price, Quantity=None, OptionVATClass=None, DiscAddP=None, DiscAddV=None, Category=None, DiscNamed=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article  with specified department. If VAT is present the relevant accumulations are perfomed in its  registers.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param DepNum: 1 symbol for article department 
        attachment, formed in the following manner; example: Dep01 = 81h, Dep02 
        = 82h … Dep19 = 93h\n
        :type DepNum: float\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param DiscAddP: 1 to 7 symbols for percentage of 
        discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param Category: 1..7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DiscNamed: 2 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellPLUfromDep_", 'NamePLU', NamePLU, 'DepNum', DepNum, 'Price', Price, 'Quantity', Quantity, 'OptionVATClass', OptionVATClass, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'Category', Category, 'DiscNamed', DiscNamed, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def PrintBarcode(self, OptionCodeType, CodeLen, CodeData):
        """
        Prints barcode from type stated by CodeType and CodeLen and with data stated in CodeData field.\n
        :param OptionCodeType: 1 symbol with possible values: 
         - '0' - UPC A 
         - '1' - UPC E 
         - '2' - EAN 13 
         - '3' - EAN 8 
         - '4' - CODE 39 
         - '5' - ITF 
         - '6' - CODABAR 
         - 'H' - CODE 93 
         - 'I' - CODE 128\n
        :type OptionCodeType: Enums.OptionCodeType\n
        :param CodeLen: 1..2 bytes for number of bytes according to the table\n
        :type CodeLen: float\n
        :param CodeData: From 0 to 255 bytes data in range according to the table\n
        :type CodeData: str\n
        """
        self.do("PrintBarcode", 'OptionCodeType', OptionCodeType, 'CodeLen', CodeLen, 'CodeData', CodeData)

    def PrintDepartmentReport(self, OptionZeroing):
        """
        Prints departments report\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Not zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintDepartmentReport", 'OptionZeroing', OptionZeroing)

    def ReadEJCustom(self, OptionStorageReport, FlagsReceipts, FlagsReports):
        """
        Read or Store Electronic Journal report and document content selecting. FlagsReceipts is a char with bits representing the receipt types. FlagsReports is a char with bits representing the report type.\n
        :param OptionStorageReport: 1 character with value 
         - 'j0' - To PC 
         - 'j2' - To USB Flash Drive 
         - 'j4' - To SD card\n
        :type OptionStorageReport: Enums.OptionStorageReport\n
        :param FlagsReceipts: 1 symbol for Receipts included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0  
        Flags.4=0  
        Flags.3=0  
        Flags.2=0  
        Flags.1=1 Yes, Flags.1=0 No (Include Invoice) 
        Flags.0=1 Yes, Flags.0=0 No (Include Fiscal Rcp)\n
        :type FlagsReceipts: str\n
        :param FlagsReports: 1 symbol for Reports included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0 
        Flags.4=0 
        Flags.3=1 Yes, Flags.3=0 No (Include Non-Fiscal Rcp) 
        Flags.2=0 
        Flags.1=1 Yes, Flags.1=0 No (Include Daily Z) 
        Flags.0=1 Yes, Flags.0=0 No (Include Duplicates)\n
        :type FlagsReports: str\n
        """
        self.do("ReadEJCustom", 'OptionStorageReport', OptionStorageReport, 'FlagsReceipts', FlagsReceipts, 'FlagsReports', FlagsReports)

    def DisplayTextLine2(self, Text):
        """
        Shows a 20-symbol text in the lower display line.\n
        :param Text: 20 symbols text\n
        :type Text: str\n
        """
        self.do("DisplayTextLine2", 'Text', Text)

    def ReadDailyCounters(self):
        """
        Provides information about the current reading of the daily-report- with-zeroing counter, the number of the last block stored in FM, the number of EJ and the date and time of the last block storage in the FM.\n
        """
        return __DailyCountersRes__(*self.do("ReadDailyCounters"))

    def PrintDetailedFMReportByZNum(self, StartNum, EndNum):
        """
        Print a detailed FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("PrintDetailedFMReportByZNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def StoreBriefFMReportByDate(self, StartDate, EndDate, OptionStorage=None):
        """
        Store a brief FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        :param OptionStorage: 1 symbol for destination: 
         - '2' - Storage in External USB Flash memory. 
         - '4' - Storage in External SD card memory\n
        :type OptionStorage: Enums.OptionStorage\n
        """
        self.do("StoreBriefFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate, 'OptionStorage', OptionStorage)

    def SetWiFi_Password(self, PassLength, Password):
        """
        Program device's WiFi network password where it will connect. To apply use - 4Eh / N - Save network settings\n
        :param PassLength: Up to 3 symbols for the WiFi password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the device's WiFi password\n
        :type Password: str\n
        """
        self.do("SetWiFi_Password", 'PassLength', PassLength, 'Password', Password)

    def StartTest_Bluetooth(self):
        """
        Start Bluetooth test on the device and print out the result\n
        """
        self.do("StartTest_Bluetooth")

    def PrintCurrentHeader(self):
        """
        Print current headers and Fiscal Memory operative header\n
        """
        self.do("PrintCurrentHeader")

    def ResetOdometer(self, Password):
        """
        Reset odometer function *the command is valid for ADPOS model only.\n
        :param Password: 6 symbols for access password\n
        :type Password: str\n
        """
        self.do("ResetOdometer", 'Password', Password)

    def EraseAllPLUs(self, Password):
        """
        Programs the PLU Category for a certain article (item) from the internal database.\n
        :param Password: 6 symbols for password\n
        :type Password: str\n
        """
        self.do("EraseAllPLUs", 'Password', Password)

    def ConfirmFiscalization(self, Password):
        """
        Confirm VAT number, type of VAT registration and Fiscal Memory number into the operative memory.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        """
        self.do("ConfirmFiscalization", 'Password', Password)

    def StoreCurrentHeaderInFM(self, Password):
        """
        Store the header into fiscal memory.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        """
        self.do("StoreCurrentHeaderInFM", 'Password', Password)

    def ReadDailyRAbyOperator(self, OperNum):
        """
        Read the RA by type of payment and the total number of operations by specified operator.\n
        :param OperNum: Symbols from 1 to 20corresponding to operator's number\n
        :type OperNum: float\n
        """
        return __DailyRAbyOperatorRes__(*self.do("ReadDailyRAbyOperator", 'OperNum', OperNum))

    def ReadOdometer(self):
        """
        Read odometer result.  *the command is valid for ADPOS model only.\n
        :rtype: float
        """
        return self.do("ReadOdometer")

    def ReadDuplicateInvoiceNumber(self):
        """
        Read the the number of the duplicates which can be printed after invoice receipt.\n
        :rtype: str
        """
        return self.do("ReadDuplicateInvoiceNumber")

    def ProgStornoNameMessage(self, StornoName):
        """
        Program the contents of storno name message.\n
        :param StornoName: TextLength symbols for storno name\n
        :type StornoName: str\n
        """
        self.do("ProgStornoNameMessage", 'StornoName', StornoName)

    def ReadPLUcategory(self, PLUNum):
        """
        Provides information about the category of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUcategoryRes__(*self.do("ReadPLUcategory", 'PLUNum', PLUNum))

    def StartTest_GPRS(self):
        """
        Start GPRS test on the device and print out the result\n
        """
        self.do("StartTest_GPRS")

    def ReadHeader(self, OptionHeaderLine):
        """
        Provides the content of the header lines.\n
        :param OptionHeaderLine: 1 byte with value: 
         - '1' - Header 1 
         - '2' - Header 2 
         - '3' - Header 3 
         - '4' - Header 4 
         - '5' - Header 5 
         - '6' - Header 6 
         - '7' - Header 7 
         - '8' - Header 8\n
        :type OptionHeaderLine: Enums.OptionHeaderLine\n
        """
        return __HeaderRes__(*self.do("ReadHeader", 'OptionHeaderLine', OptionHeaderLine))

    def ReadVATNum(self):
        """
        Read the VAT registration and Fiscal Memory numbers.\n
        """
        return __VATNumRes__(*self.do("ReadVATNum"))

    def CutPaper(self):
        """
        Start paper cutter. The command works only in fiscal printer devices.\n
        """
        self.do("CutPaper")

    def ReadDeviceModuleSupportByFirmware(self):
        """
        Provide an information about modules supported by device's firmware.\n
        """
        return __DeviceModuleSupportByFirmwareRes__(*self.do("ReadDeviceModuleSupportByFirmware"))

    def ReadWiFi_Password(self):
        """
        Read device's connected WiFi network password\n
        """
        return __WiFi_PasswordRes__(*self.do("ReadWiFi_Password"))

    def ReadDailyAmountsByVAT(self):
        """
        Provides information about the accumulated amount by VAT class.\n
        """
        return __DailyAmountsByVATRes__(*self.do("ReadDailyAmountsByVAT"))

    def ProgPLUbarcode(self, PLUNum, Barcode):
        """
        Program the Barcode number for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Barcode: 13 symbols for barcode\n
        :type Barcode: str\n
        """
        self.do("ProgPLUbarcode", 'PLUNum', PLUNum, 'Barcode', Barcode)

    def PrintDetailedFMReportByDate(self, StartDate, EndDate):
        """
        Prints a detailed FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("PrintDetailedFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def ReadBriefFMReportByNum(self, StartNum, EndNum):
        """
        Store a brief FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("ReadBriefFMReportByNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def SellFractQtyPLUwithSpecifiedVATfromDep(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, DepNum=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article with specified VAT. If department is present the relevant accumulations are perfomed in its registers.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 3 to 10 symbols for quantity in format fractional format (e.g. 1/3)\n
        :type Quantity: str\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DepNum: 1 symbol for article department attachment, 
        formed in the following manner; example: Dep01 = 81h, Dep02 = 82h … 
        Dep19 = 93h\n
        :type DepNum: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellFractQtyPLUwithSpecifiedVATfromDep", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'DepNum', DepNum, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ReadPLUgeneral(self, PLUNum):
        """
        Provides information about the general registers of the specified.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUgeneralRes__(*self.do("ReadPLUgeneral", 'PLUNum', PLUNum))

    def ReadDailyReceivedSalesAmountsByOperator(self, OperNum):
        """
        Read the amounts received from sales by type of payment and specified operator.\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's 
        number\n
        :type OperNum: float\n
        """
        return __DailyReceivedSalesAmountsByOperatorRes__(*self.do("ReadDailyReceivedSalesAmountsByOperator", 'OperNum', OperNum))

    def ReadDailyCurrency(self):
        """
        Provides information about the accumulated amounts from sale of foreign currency, currency purchase and commissions.\n
        """
        return __DailyCurrencyRes__(*self.do("ReadDailyCurrency"))

    def ReadCustomerData(self, CustomerNum):
        """
        Provide information for specified customer from FD database.\n
        :param CustomerNum: 3 symbols for customer number in order in format ###\n
        :type CustomerNum: float\n
        """
        return __CustomerDataRes__(*self.do("ReadCustomerData", 'CustomerNum', CustomerNum))

    def ProgCustomerReceiptNameMessage(self, CustRecieptName):
        """
        Program the contents of customer receipt name message.\n
        :param CustRecieptName: TextLength symbols for customer receipt name\n
        :type CustRecieptName: str\n
        """
        self.do("ProgCustomerReceiptNameMessage", 'CustRecieptName', CustRecieptName)

    def ReadCurrentReceiptInfo(self):
        """
        Read the current status of the receipt.\n
        """
        return __CurrentReceiptInfoRes__(*self.do("ReadCurrentReceiptInfo"))

    def ReadPLUallData(self, PLUNum):
        """
        Provides information about the all registers of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUallDataRes__(*self.do("ReadPLUallData", 'PLUNum', PLUNum))

    def ReadEJ(self):
        """
        Read whole Electronic Journal report from beginning to the end.\n
        """
        self.do("ReadEJ")

    def Payment(self, OptionPaymentType, Amount):
        """
        Registers the payment in the receipt with specified type of payment and amount received (if the payment type is 1-9 the amount of change due is not obligatory.)\n
        :param OptionPaymentType: 1 symbol for payment type: 
         - '0' - Payment 0 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6 
         - '7' - Payment 7 
         - '8' - Payment 8 
         - '9' - Payment 9\n
        :type OptionPaymentType: Enums.OptionPaymentType\n
        :param Amount: 1 to 10 characters for received amount\n
        :type Amount: float\n
        """
        self.do("Payment", 'OptionPaymentType', OptionPaymentType, 'Amount', Amount)

    def ReadFMcontent(self):
        """
        Provides consequently information about every single block stored in the FM starting with Acknowledgements and ending with end message.\n
        """
        self.do("ReadFMcontent")

    def SetDeviceTCP_Addresses(self, OptionAddressType, DeviceAddress):
        """
        Program device's network IP address, subnet mask, gateway address, DNS address. To apply use - 4Eh / N - Save network settings\n
        :param OptionAddressType: 1 symbol with value: 
         - '2' - IP address 
         - '3' - Subnet Mask 
         - '4' - Gateway address 
         - '5' - DNS address\n
        :type OptionAddressType: Enums.OptionAddressType\n
        :param DeviceAddress: 15 symbols for the selected address\n
        :type DeviceAddress: str\n
        """
        self.do("SetDeviceTCP_Addresses", 'OptionAddressType', OptionAddressType, 'DeviceAddress', DeviceAddress)

    def ReadLastDailyReportInfo(self):
        """
        Read the date and number of the last Z-report and the last RAM reset event.\n
        """
        return __LastDailyReportInfoRes__(*self.do("ReadLastDailyReportInfo"))

    def ReadECRprofileZreportSending(self):
        """
        Provides information about sending of Z report to server automatically after Z report or not.\n
        :rtype: Enums.OptionSendAfterZ
        """
        return self.do("ReadECRprofileZreportSending")

    def PrintOrStoreEJByZReportNum(self, OptionReportStorage, StartNum, EndNum):
        """
        Store Electronic Journal Report from report number to report number to External USB Flash memory, External SD card or Print.\n
        :param OptionReportStorage: 2 symbols for destination: 
         - 'J1' - Printing  
         - 'J2' - Storage in External USB Flash memory. 
         - 'J4' - Storage in External SD card memory\n
        :type OptionReportStorage: Enums.OptionReportStorage\n
        :param StartNum: 4 symbols for initial number report in format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for final number report in format ####\n
        :type EndNum: float\n
        """
        self.do("PrintOrStoreEJByZReportNum", 'OptionReportStorage', OptionReportStorage, 'StartNum', StartNum, 'EndNum', EndNum)

    def PrintText(self, Text):
        """
        Prints a free text.\n
        :param Text: Free text - TextLength symbols\n
        :type Text: str\n
        """
        self.do("PrintText", 'Text', Text)

    def PrintBriefFMReportByZNum(self, StartNum, EndNum):
        """
        Print a brief FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial FM report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final FM report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("PrintBriefFMReportByZNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def PrintBriefFMPaymentReportByDate(self, StartDate, EndDate):
        """
        Print a brief payment FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("PrintBriefFMPaymentReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def PrintOperatorReport(self, OptionZeroing, Number):
        """
        Prints an operator's report for a specified operator (0 = all operators) with or without zeroing ('Z' or 'X'). When a 'Z' value is specified the report should include all operators.\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Not zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        :param Number: Symbols from 0 to 20 corresponding to operator's number, 
        0 = all operators\n
        :type Number: float\n
        """
        self.do("PrintOperatorReport", 'OptionZeroing', OptionZeroing, 'Number', Number)

    def PrintSpecialFMReportByDate(self, StartDate, EndDate):
        """
        Prints the special FM events report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("PrintSpecialFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def ReadStatus(self):
        """
        Provides detailed 7-byte information about the current status of the fiscal printer.\n
        """
        return __StatusRes__(*self.do("ReadStatus"))

    def OpenReceipt(self, OperNum, OperPass, OptionFiscalReceiptPrintType):
        """
        Opens a fiscal receipt assigned to the specified operator and print type depends of FiscalReceiptPrintType parameter.\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's 
        number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param OptionFiscalReceiptPrintType: 1 symbol with value: 
         - '0' - Step by step printing 
         - '2' - Postponed printing 
         - '4' - Buffered Printing\n
        :type OptionFiscalReceiptPrintType: Enums.OptionFiscalReceiptPrintType\n
        """
        self.do("OpenReceipt", 'OperNum', OperNum, 'OperPass', OperPass, 'OptionFiscalReceiptPrintType', OptionFiscalReceiptPrintType)

    def CurrencyTransaction(self, CurrencyName, Rate, PerCurrencyUnit=None, Quantity=None, Commission=None):
        """
        Registers the sale/buying of currency with specified name,rate of exchange, quantity and percentage of commission and closes the receipt. The type of transaction - sale or purchase transaction depends on the receipt opening type. This command closes the receipt with payment cash or other type, defined in PaymentType field if present. The Quantity, Commission and PaymentType fields are not obligatory.\n
        :param CurrencyName: 3 symbols for currency name\n
        :type CurrencyName: str\n
        :param Rate: Up to 11 symbols "xxxxx.xxxxx" for rate of exchange\n
        :type Rate: float\n
        :param PerCurrencyUnit: Up to 6 digits for rate "per" factor\n
        :type PerCurrencyUnit: float\n
        :param Quantity: 1 to 8 symbols "xxxxxxxx" for amount of currency\n
        :type Quantity: float\n
        :param Commission: 1 to 5 symbols for percentage of commission\n
        :type Commission: float\n
        """
        self.do("CurrencyTransaction", 'CurrencyName', CurrencyName, 'Rate', Rate, 'PerCurrencyUnit', PerCurrencyUnit, 'Quantity', Quantity, 'Commission', Commission)

    def ReadEJByZBlocksCustom(self, OptionStorageReport, FlagsReceipts, FlagsReports, StartZNum, EndZNum):
        """
        Read or Store Electronic Journal Report by number of Z report blocks, CSV format option and document content. FlagsReceipts is a char with bits representing the receipt types. FlagsReports is a char with bits representing the report type.\n
        :param OptionStorageReport: 1 character with value 
         - 'j0' - To PC 
         - 'j2' - To USB Flash Drive 
         - 'j4' - To SD card\n
        :type OptionStorageReport: Enums.OptionStorageReport\n
        :param FlagsReceipts: 1 symbol for Receipts included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0  
        Flags.4=0  
        Flags.3=0  
        Flags.2=0  
        Flags.1=1 Yes, Flags.1=0 No (Include Invoice) 
        Flags.0=1 Yes, Flags.0=0 No (Include Fiscal Rcp)\n
        :type FlagsReceipts: str\n
        :param FlagsReports: 1 symbol for Reports included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0 
        Flags.4=0 
        Flags.3=1 Yes, Flags.3=0 No (Include Non-Fiscal Rcp) 
        Flags.2=0 
        Flags.1=1 Yes, Flags.1=0 No (Include Daily Z) 
        Flags.0=1 Yes, Flags.0=0 No (Include Duplicates)\n
        :type FlagsReports: str\n
        :param StartZNum: 4 symbols for initial number report in format ####\n
        :type StartZNum: float\n
        :param EndZNum: 4 symbols for final number report in format ####\n
        :type EndZNum: float\n
        """
        self.do("ReadEJByZBlocksCustom", 'OptionStorageReport', OptionStorageReport, 'FlagsReceipts', FlagsReceipts, 'FlagsReports', FlagsReports, 'StartZNum', StartZNum, 'EndZNum', EndZNum)

    def ProgPLUcategory(self, PLUNum, Category):
        """
        Programs the PLU Category for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        """
        self.do("ProgPLUcategory", 'PLUNum', PLUNum, 'Category', Category)

    def SetDateTime(self, DateTime):
        """
        Sets the date and time and prints the current values using the RECEIPT printer. 64h\n
        :param DateTime: Date Time parameter in format: DD-MM-YY [Space] HH:MM:SS\n
        :type DateTime: datetime\n
        """
        self.do("SetDateTime", 'DateTime', DateTime)

    def ProgDecimalPointPosition(self, Password, OptionDecimalPointPosition):
        """
        Stores a block containing the number format into the fiscal memory. Print the current status on the printer.\n
        :param Password: 6-symbol string\n
        :type Password: str\n
        :param OptionDecimalPointPosition: 1 symbol with values: 
         - '0'- Whole numbers 
         - '2' - Fractions\n
        :type OptionDecimalPointPosition: Enums.OptionDecimalPointPosition\n
        """
        self.do("ProgDecimalPointPosition", 'Password', Password, 'OptionDecimalPointPosition', OptionDecimalPointPosition)

    def ReadPLUprice(self, PLUNum):
        """
        Provides information about the price and price type of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUpriceRes__(*self.do("ReadPLUprice", 'PLUNum', PLUNum))

    def ReadOperatorNamePassword(self, Number):
        """
        Provides information about an operator's name and password.\n
        :param Number: Symbol from 1 to 20 corresponding to the number of operators\n
        :type Number: float\n
        """
        return __OperatorNamePasswordRes__(*self.do("ReadOperatorNamePassword", 'Number', Number))

    def ReadDailyCountersByOperator(self, OperNum):
        """
        Read the last operator's report number and date and time.\n
        :param OperNum: Symbols from 1 to 20 corresponding to 
        operator's number\n
        :type OperNum: float\n
        """
        return __DailyCountersByOperatorRes__(*self.do("ReadDailyCountersByOperator", 'OperNum', OperNum))

    def ReadPayments(self):
        """
        Provides information about all programmed types of payment.\n
        """
        return __PaymentsRes__(*self.do("ReadPayments"))

    def SellPLUwithSpecifiedVATfromDep(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, DepNum=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article with specified VAT. If department is present the relevant accumulations are perfomed in its registers.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DepNum: 1 symbol for article department attachment, 
        formed in the following manner; example: Dep01 = 81h, Dep02 = 82h … 
        Dep19 = 93h\n
        :type DepNum: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellPLUwithSpecifiedVATfromDep", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'DepNum', DepNum, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ProgPayment(self, OptionPaymentNum, Name, Rate=None):
        """
        Programs the name of the type of payment.\n
        :param OptionPaymentNum: 1 symbol for payment type: 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6 
         - '7' - Payment 7 
         - '8' - Payment 8 
         - '9' - Payment 9\n
        :type OptionPaymentNum: Enums.OptionPaymentNum\n
        :param Name: 10 symbols for payment type name\n
        :type Name: str\n
        :param Rate: 10 symbols for exchange rate in format: ####.#####  
        of the 9th payment type, maximal value 0420.00000\n
        :type Rate: float\n
        """
        self.do("ProgPayment", 'OptionPaymentNum', OptionPaymentNum, 'Name', Name, 'Rate', Rate)

    def PrintDiagnostics(self):
        """
        Prints out a diagnostic receipt.\n
        """
        self.do("PrintDiagnostics")

    def ProgFooter(self, OptionFooterLine, FooterText):
        """
        Program the contents of a footer lines.\n
        :param OptionFooterLine: 1 symbol for option footer lines: 
         - '1' - Footer 1 
         - '2' - Footer 2 
         - '3' - Footer 3\n
        :type OptionFooterLine: Enums.OptionFooterLine\n
        :param FooterText: TextLength symbols for footer line\n
        :type FooterText: str\n
        """
        self.do("ProgFooter", 'OptionFooterLine', OptionFooterLine, 'FooterText', FooterText)

    def PrintLastReceiptDuplicate(self):
        """
        Print a copy of the last receipt document issued\n
        """
        self.do("PrintLastReceiptDuplicate")

    def SetGPRS_Password(self, PassLength, Password):
        """
        Program device's GPRS password. To apply use - SaveNetworkSettings()\n
        :param PassLength: Up to 3 symbols for the GPRS password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the device's GPRS password\n
        :type Password: str\n
        """
        self.do("SetGPRS_Password", 'PassLength', PassLength, 'Password', Password)

    def SoftwareReset(self, Password):
        """
        Restore default parameters of the device.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        """
        self.do("SoftwareReset", 'Password', Password)

    def ReadTCP_Password(self):
        """
        Provides information about device's TCP password.\n
        """
        return __TCP_PasswordRes__(*self.do("ReadTCP_Password"))

    def ProgVATrates(self, Password, VATrateA, VATrateB, VATrateC, VATrateD):
        """
        Stores a block containing the values of the VAT rates into the fiscal memory. Print the values on the printer.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        :param VATrateA: Value of VAT rate A from 2 to 6 symbols with format ##.##\n
        :type VATrateA: float\n
        :param VATrateB: Value of VAT rate B from 2 to 6 symbols with format ##.##\n
        :type VATrateB: float\n
        :param VATrateC: Value of VAT rate C from 2 to 6 symbols with format ##.##\n
        :type VATrateC: float\n
        :param VATrateD: Value of VAT rate D from 2 to 6 symbols with format ##.##\n
        :type VATrateD: float\n
        """
        self.do("ProgVATrates", 'Password', Password, 'VATrateA', VATrateA, 'VATrateB', VATrateB, 'VATrateC', VATrateC, 'VATrateD', VATrateD)

    def ReadEJByDateCustom(self, OptionStorageReport, FlagsReceipts, FlagsReports, StartRepFromDate, EndRepFromDate):
        """
        Read or Store Electronic Journal Report by initial to end date and document content. FlagsReceipts is a char with bits representing the receipt types. FlagsReports is a char with bits representing the report type.\n
        :param OptionStorageReport: 2 characters with value: 
         - 'j0' - To PC 
         - 'j2' - To USB Flash Drive 
         - 'j4' - To SD card\n
        :type OptionStorageReport: Enums.OptionStorageReport\n
        :param FlagsReceipts: 1 symbol for Receipts included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0  
        Flags.4=0  
        Flags.3=0  
        Flags.2=0  
        Flags.1=1 Yes, Flags.1=0 No (Include Invoice) 
        Flags.0=1 Yes, Flags.0=0 No (Include Fiscal Rcp)\n
        :type FlagsReceipts: str\n
        :param FlagsReports: 1 symbol for Reports included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0 
        Flags.4=0 
        Flags.3=1 Yes, Flags.3=0 No (Include Non-Fiscal Rcp) 
        Flags.2=0 
        Flags.1=1 Yes, Flags.1=0 No (Include Daily Z) 
        Flags.0=1 Yes, Flags.0=0 No (Include Duplicates)\n
        :type FlagsReports: str\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        """
        self.do("ReadEJByDateCustom", 'OptionStorageReport', OptionStorageReport, 'FlagsReceipts', FlagsReceipts, 'FlagsReports', FlagsReports, 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate)

    def SetBluetooth_Status(self, OptionBTstatus):
        """
        Program device's Bluetooth module to be enabled or disabled.\n
        :param OptionBTstatus: 1 symbol with value: 
         - '0' - Disabled 
         - '1' - Enabled\n
        :type OptionBTstatus: Enums.OptionBTstatus\n
        """
        self.do("SetBluetooth_Status", 'OptionBTstatus', OptionBTstatus)

    def ReadEJByDate(self, StartRepFromDate, EndRepFromDate):
        """
        Read Electronic Journal Report initial date to report end date.\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        """
        self.do("ReadEJByDate", 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate)

    def ReadPLUbarcode(self, PLUNum):
        """
        Provides information about the barcode of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUbarcodeRes__(*self.do("ReadPLUbarcode", 'PLUNum', PLUNum))

    def ReadServerPasswordECRS(self):
        """
        Provides information about the ECR's password\n
        """
        return __ServerPasswordECRSRes__(*self.do("ReadServerPasswordECRS"))

    def ProgDepartment(self, Number, Name, OptionVATClass, Price=None, OptionDepPrice=None, Category=None, AdditionalName=None):
        """
        Set data for the stated department number from the internal FD database. Parameters Price, OptionDepPrice, AdditionalName and Category are not obligatory and require the previous not obligatory parameter.\n
        :param Number: 2 symbols department number in format: ##\n
        :type Number: float\n
        :param Name: 20 characters department name\n
        :type Name: str\n
        :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
         - 'A' - VAT Class A 
         - 'B' - VAT Class B 
         - 'C' - VAT Class C 
         - 'D' - VAT Class D 
         - 'E' - VAT Class E 
         - 'F' - Alte taxe\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: Up 10 symbols for department price\n
        :type Price: float\n
        :param OptionDepPrice: 1 symbol for Department flags with next value: 
         - '0' - Free price disabled  
         - '1' - Free price enabled  
         - '2' - Limited price 
         - '4' - Free price disabled for single transaction 
         - '5' - Free price enabled for single transaction 
         - '6' - Limited price for single transaction\n
        :type OptionDepPrice: Enums.OptionDepPrice\n
        :param Category: From 1 to 7 symbols for categoryin format: ####.##\n
        :type Category: float\n
        :param AdditionalName: 14 characters additional department name\n
        :type AdditionalName: str\n
        """
        self.do("ProgDepartment", 'Number', Number, 'Name', Name, 'OptionVATClass', OptionVATClass, 'Price', Price, 'OptionDepPrice', OptionDepPrice, 'Category', Category, 'AdditionalName', AdditionalName)

    def OpenCurrencyBuyingReceipt(self, OperNum, OperPass, OptionCurrencyBuyingRcpPrintType, Text1, Text2, Text3, Text4, Text5, Text6):
        """
        Opens a fiscal receipt assigned to the specified operator for Currency Purchase transaction.\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param OptionCurrencyBuyingRcpPrintType: 1 symbol with value 
         - '8' - Step by step printing 
         - ':' - Postponed printing\n
        :type OptionCurrencyBuyingRcpPrintType: Enums.OptionCurrencyBuyingRcpPrintType\n
        :param Text1: 26 symbols free text for header line 1 in the receipt\n
        :type Text1: str\n
        :param Text2: 26 symbols free text for header line 2 in the receipt\n
        :type Text2: str\n
        :param Text3: 26 symbols free text for header line 3 in the receipt\n
        :type Text3: str\n
        :param Text4: 26 symbols free text for header line 4 in the receipt\n
        :type Text4: str\n
        :param Text5: 26 symbols free text for header line 5 in the receipt\n
        :type Text5: str\n
        :param Text6: 26 symbols free text for header line 6 in the receipt\n
        :type Text6: str\n
        """
        self.do("OpenCurrencyBuyingReceipt", 'OperNum', OperNum, 'OperPass', OperPass, 'OptionCurrencyBuyingRcpPrintType', OptionCurrencyBuyingRcpPrintType, 'Text1', Text1, 'Text2', Text2, 'Text3', Text3, 'Text4', Text4, 'Text5', Text5, 'Text6', Text6)

    def SetIdle_Timeout(self, IdleTimeout):
        """
        Sets device's idle timeout setting. Set timeout for closing the connection if there is an inactivity. Maximal value - 7200, minimal value 1. 0 is for never close the connection. This option can be used only if the device has LAN or WiFi. To apply use - 4Eh / N - Save network settings\n
        :param IdleTimeout: 4 symbols for Idle timeout in format ####\n
        :type IdleTimeout: float\n
        """
        self.do("SetIdle_Timeout", 'IdleTimeout', IdleTimeout)

    def ReadTCP_AutoStartStatus(self):
        """
        Read device TCP Auto Start status\n
        :rtype: Enums.OptionTCPAutoStart
        """
        return self.do("ReadTCP_AutoStartStatus")

    def PrintLogo(self, Number):
        """
        Prints the programmed graphical logo with the stated number.\n
        :param Number: Number of logo to be printed. If missing prints logo with number 0\n
        :type Number: float\n
        """
        self.do("PrintLogo", 'Number', Number)

    def ReadDailyGeneralRegistersByOperator(self, OperNum):
        """
        Read the total number of customers, discounts, additions, corrections and accumulated amounts by specified operator.\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        """
        return __DailyGeneralRegistersByOperatorRes__(*self.do("ReadDailyGeneralRegistersByOperator", 'OperNum', OperNum))

    def ReadGPRS_Password(self):
        """
        Provides information about device's GPRS password.\n
        """
        return __GPRS_PasswordRes__(*self.do("ReadGPRS_Password"))

    def ProgDuplicatesNumber(self, DuplicatesNumber):
        """
        Program the the number of the duplicates which can be printed after invoice receipt.\n
        :param DuplicatesNumber: 1 symbol for number of duplicates which can be print. Possible values 
        from '0' to '5'.\n
        :type DuplicatesNumber: str\n
        """
        self.do("ProgDuplicatesNumber", 'DuplicatesNumber', DuplicatesNumber)

    def StornoPLUfromDep(self, NamePLU, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, DepNum=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Registers the correction of article with specified name, price, quantity, VAT class and/or discount/addition on the transaction.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param Price: 1 to 10 symbols for article's price with minus sign for storno operation\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DepNum: 1 symbol for article department attachment, 
        formed in the following manner; example: Dep01 = 81h, Dep02 = 82h … 
        Dep19 = 93h\n
        :type DepNum: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("StornoPLUfromDep", 'NamePLU', NamePLU, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'DepNum', DepNum, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ProgContractWarningMessages(self, Password, Line1, Line2, Line3):
        """
        Program the service contract expired warning message text.\n
        :param Password: 6 symbols for service password\n
        :type Password: str\n
        :param Line1: TextLength symbols for warning message of line 1\n
        :type Line1: str\n
        :param Line2: TextLength symbols for warning message of line 2\n
        :type Line2: str\n
        :param Line3: TextLength symbols for warning message of line 3\n
        :type Line3: str\n
        """
        self.do("ProgContractWarningMessages", 'Password', Password, 'Line1', Line1, 'Line2', Line2, 'Line3', Line3)

    def PrintCustomerReport(self, OptionZeroing):
        """
        Print Customer X or Z report\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Not zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintCustomerReport", 'OptionZeroing', OptionZeroing)

    def PrintDailyReport(self, OptionZeroing):
        """
        Depending on the parameter prints:  − daily fiscal report with zeroing and fiscal memory record, preceded by Electronic Journal report print ('Z'); − daily fiscal report without zeroing ('X');\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Not zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintDailyReport", 'OptionZeroing', OptionZeroing)

    def ProgExtDisplay(self, Password):
        """
        Preprograms the external display.\n
        :param Password: A 6-symbol string\n
        :type Password: str\n
        """
        self.do("ProgExtDisplay", 'Password', Password)

    def ReadFooter(self, OptionFooterLine):
        """
        Provides the content of the footer lines.\n
        :param OptionFooterLine: 1 symbol with value: 
         - '1' - Footer 1 
         - '2' - Footer 2 
         - '3' - Footer 3\n
        :type OptionFooterLine: Enums.OptionFooterLine\n
        """
        return __FooterRes__(*self.do("ReadFooter", 'OptionFooterLine', OptionFooterLine))

    def OpenNonFiscalReceipt(self, OperNum, OperPass, OptionNonFiscalPrintType):
        """
        Opens a non-fiscal receipt assigned to the specified operator and print type depends on NonFiscalPrintType parameter.\n
        :param OperNum: Symbols from '1' to '20' corresponding to operator's 
        number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param OptionNonFiscalPrintType: 1 symbol with value: 
         - '0' - Step by step printing 
         - '1' - Postponed printing\n
        :type OptionNonFiscalPrintType: Enums.OptionNonFiscalPrintType\n
        """
        self.do("OpenNonFiscalReceipt", 'OperNum', OperNum, 'OperPass', OperPass, 'OptionNonFiscalPrintType', OptionNonFiscalPrintType)

    def ReadECRprofileActiveDate(self):
        """
        Provides information about active profile date - date from which the account is valid or date from which we return to account 1 in case of mReset.\n
        :rtype: datetime
        """
        return self.do("ReadECRprofileActiveDate")

    def Subtotal(self, OptionPrinting, OptionDisplay, DiscAddV=None, DiscAddP=None):
        """
        Calculate the subtotal amount with printing and display visualization options. Provide information about values of the calculated amounts. If a percent or value discount/addition has been specified the subtotal and the discount/addition value will be printed regardless the parameter for printing.\n
        :param OptionPrinting: 1 symbol with value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionPrinting: Enums.OptionPrinting\n
        :param OptionDisplay: 1 symbol with value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionDisplay: Enums.OptionDisplay\n
        :param DiscAddV: 1 to 10 symbols for the value of the discount/addition\n
        :type DiscAddV: float\n
        :param DiscAddP: 1 to 7 symbols for the percentage value of the 
        discount/addition\n
        :type DiscAddP: float\n
        :rtype: float
        """
        return self.do("Subtotal", 'OptionPrinting', OptionPrinting, 'OptionDisplay', OptionDisplay, 'DiscAddV', DiscAddV, 'DiscAddP', DiscAddP)

    def PrintDetailedFMPaymentsReportByDate(self, StartDate, EndDate):
        """
        Print a detailed payment FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("PrintDetailedFMPaymentsReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def ReadLastZReportNumFromDate(self, DateFrom):
        """
        Provide information about last found Z report, having the same date or date before than the input date\n
        :param DateFrom: 6 symbols for specified date in format "DDMMYY"\n
        :type DateFrom: datetime\n
        :rtype: float
        """
        return self.do("ReadLastZReportNumFromDate", 'DateFrom', DateFrom)

    def ReadDailyRA(self):
        """
        Provides information about the RA amounts by type of payment and the total number of operations.\n
        """
        return __DailyRARes__(*self.do("ReadDailyRA"))

    def ReadGeneralDailyRegisters(self):
        """
        Provides information about the number of customers (number of fiscal receipt issued), number of discounts, additions and corrections made and the accumulated amounts.\n
        """
        return __GeneralDailyRegistersRes__(*self.do("ReadGeneralDailyRegisters"))

    def SetActiveLogo(self, LogoNumber):
        """
        Stores in the memory the graphic file under stated number. Prints information about loaded in the printer graphic files.\n
        :param LogoNumber: 1 character value from '0' to '9' or '?'. The number sets the active logo 
        number, and the '?' invokes only printing of information\n
        :type LogoNumber: str\n
        """
        self.do("SetActiveLogo", 'LogoNumber', LogoNumber)

    def ReadDisplayGreetingMessage(self):
        """
        Provide information about the display greeting message.\n
        :rtype: str
        """
        return self.do("ReadDisplayGreetingMessage")

    def PrintSpecialFMReportByZReportNum(self, StartNum, EndNum):
        """
        Print the special FM events report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        """
        self.do("PrintSpecialFMReportByZReportNum", 'StartNum', StartNum, 'EndNum', EndNum)

    def SetServerPasswordECRS(self, ParamLength, ServerPassword):
        """
        Program ECRS password\n
        :param ParamLength: Up to 2 symbols for parameter length\n
        :type ParamLength: float\n
        :param ServerPassword: Up to 64 symbols for server password\n
        :type ServerPassword: str\n
        """
        self.do("SetServerPasswordECRS", 'ParamLength', ParamLength, 'ServerPassword', ServerPassword)

    def ReadBluetooth_Status(self):
        """
        Providing information about if the device's Bluetooth module is enabled or disabled.\n
        :rtype: Enums.OptionBTstatus
        """
        return self.do("ReadBluetooth_Status")

    def SetGPRS_Username(self, GPRS_Username_Len, Username):
        """
        Program device's GPRS user name. To apply use - SaveNetworkSettings()\n
        :param GPRS_Username_Len: Up to 3 symbols for the username len\n
        :type GPRS_Username_Len: float\n
        :param Username: Up to 100 symbols for the device's GPRS username\n
        :type Username: str\n
        """
        self.do("SetGPRS_Username", 'GPRS_Username_Len', GPRS_Username_Len, 'Username', Username)

    def PrintHourlyReport(self):
        """
        Print hourly report *the command is valid for ADPOS model only.\n
        """
        self.do("PrintHourlyReport")

    def SellFractQtyPLUfromDep(self, NamePLU, Price, Quantity=None, DiscAddP=None, DiscAddV=None, DiscNamed=None, Category=None, DepNum=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Register the sell (for correction use minus sign in the price field) of article with specified VAT. If department is present the relevant accumulations are perfomed in its registers.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 3 to 10 symbols for quantity in format fractional format (e.g. 1/3)\n
        :type Quantity: str\n
        :param DiscAddP: 1 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1 to 8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DepNum: 1 symbol for article department attachment, 
        formed in the following manner; example: Dep01 = 81h, Dep02 = 82h … 
        Dep19 = 93h\n
        :type DepNum: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellFractQtyPLUfromDep", 'NamePLU', NamePLU, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'DiscNamed', DiscNamed, 'Category', Category, 'DepNum', DepNum, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ReadDeviceModuleSupport(self):
        """
        Provide an information about modules supported by the device.\n
        """
        return __DeviceModuleSupportRes__(*self.do("ReadDeviceModuleSupport"))

    def StoreEJByZReportNum(self, OptionRecieptXmlStorage, StartNum, EndNum):
        """
        Storage of receipts xml files by Z-report number to USB Flash memory or SD card memory.\n
        :param OptionRecieptXmlStorage: 2 symbols for destination: 
        - 'Jx' - Storage in External USB Flash memory. 
        - 'JX' - Storage in External SD card memory\n
        :type OptionRecieptXmlStorage: Enums.OptionRecieptXmlStorage\n
        :param StartNum: 4 symbols for initial number report in format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for final number report in format ####\n
        :type EndNum: float\n
        """
        self.do("StoreEJByZReportNum", 'OptionRecieptXmlStorage', OptionRecieptXmlStorage, 'StartNum', StartNum, 'EndNum', EndNum)

    def ReadWiFi_NetworkName(self):
        """
        Read device's connected WiFi network name\n
        """
        return __WiFi_NetworkNameRes__(*self.do("ReadWiFi_NetworkName"))

    def ReadParameters(self):
        """
        Provides information about the programmed number of POS and the current values of the logo, cutting permission, display mode, enable/disable currency in receipt and enable/disableUSB host mode.\n
        """
        return __ParametersRes__(*self.do("ReadParameters"))

    def ReadVersion(self):
        """
        Provides information about the device model and firmware version.\n
        :rtype: str
        """
        return self.do("ReadVersion")

    def RawWrite(self, Bytes):
        """
         Writes raw bytes to FP \n
        :param Bytes: The bytes in BASE64 ecoded string to be written to FP\n
        :type Bytes: bytearray\n
        """
        self.do("RawWrite", 'Bytes', Bytes)

    def ProgAlteTaxe(self, Number, Name):
        """
        Program the other charges (Alte taxe) name.\n
        :param Number: 1 symbol for number in order up to 7\n
        :type Number: str\n
        :param Name: 12 symbols for Alte taxe name\n
        :type Name: str\n
        """
        self.do("ProgAlteTaxe", 'Number', Number, 'Name', Name)

    def SellPLUwithSpecifiedVATfromDep_(self, NamePLU, DepNum, Price, Quantity=None, DiscAddP=None, DiscAddV=None, Category=None, DiscNamed=None, NamePLUextension=None, AdditionalNamePLU=None):
        """
        Registers the sell (for correction use minus sign in the price field)  of article with specified department, name, price, quantity and/or discount/addition on  the transaction.\n
        :param NamePLU: 30 symbols for article's name plus separator for MU=60h 
        followed up to 3 symbols for unit plus 2 symbols spaces\n
        :type NamePLU: str\n
        :param DepNum: 1 symbol for article department 
        attachment, formed in the following manner; example: Dep01 = 81h, Dep02 
        = 82h … Dep19 = 93h\n
        :type DepNum: float\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 1 to 7 symbols for percentage of 
        discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 1..8 for value of discount/addition\n
        :type DiscAddV: float\n
        :param Category: 1..7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        :param DiscNamed: 1 to 8 symbols for value of named discount\n
        :type DiscNamed: float\n
        :param NamePLUextension: 12 symbols for extension of the PLU Name: FP Only\n
        :type NamePLUextension: str\n
        :param AdditionalNamePLU: 108 symbols for additional PLU name\n
        :type AdditionalNamePLU: str\n
        """
        self.do("SellPLUwithSpecifiedVATfromDep_", 'NamePLU', NamePLU, 'DepNum', DepNum, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'Category', Category, 'DiscNamed', DiscNamed, 'NamePLUextension', NamePLUextension, 'AdditionalNamePLU', AdditionalNamePLU)

    def ReadDailyReturnedChangeAmountsByOperator(self, OperNum):
        """
        Read the amounts returned as change by different payment types for the specified operator.\n
        :param OperNum: Symbol from 1 to 20 corresponding to operator's 
        number\n
        :type OperNum: float\n
        """
        return __DailyReturnedChangeAmountsByOperatorRes__(*self.do("ReadDailyReturnedChangeAmountsByOperator", 'OperNum', OperNum))

    def ReadEJByReceiptNumCustom(self, OptionStorageReport, FlagsReceipts, FlagsReports, StartRcpNum, EndRcpNum):
        """
        Read or Store Electronic Journal Report from receipt number to receipt number and document content. FlagsReceipts is a char with bits representing the receipt types. FlagsReports is a char with bits representing the report type.\n
        :param OptionStorageReport: 1 character with value 
         - 'j0' - To PC 
         - 'j2' - To USB Flash Drive 
         - 'j4' - To SD card\n
        :type OptionStorageReport: Enums.OptionStorageReport\n
        :param FlagsReceipts: 1 symbol for Receipts included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0  
        Flags.4=0  
        Flags.3=0  
        Flags.2=0  
        Flags.1=1 Yes, Flags.1=0 No (Include Invoice) 
        Flags.0=1 Yes, Flags.0=0 No (Include Fiscal Rcp)\n
        :type FlagsReceipts: str\n
        :param FlagsReports: 1 symbol for Reports included in EJ: 
        Flags.7=0 
        Flags.6=1 
        Flags.5=0 
        Flags.4=0 
        Flags.3=1 Yes, Flags.3=0 No (Include Non-Fiscal Rcp) 
        Flags.2=0 
        Flags.1=1 Yes, Flags.1=0 No (Include Daily Z) 
        Flags.0=1 Yes, Flags.0=0 No (Include Duplicates)\n
        :type FlagsReports: str\n
        :param StartRcpNum: 6 symbols for initial receipt number included in report in format ######.\n
        :type StartRcpNum: float\n
        :param EndRcpNum: 6 symbols for final receipt number included in report in format ######.\n
        :type EndRcpNum: float\n
        """
        self.do("ReadEJByReceiptNumCustom", 'OptionStorageReport', OptionStorageReport, 'FlagsReceipts', FlagsReceipts, 'FlagsReports', FlagsReports, 'StartRcpNum', StartRcpNum, 'EndRcpNum', EndRcpNum)

    def CashPayCloseReceipt(self):
        """
        Paying the exact amount in cash and close the fiscal receipt.\n
        """
        self.do("CashPayCloseReceipt")

    def ProgDisplayGreetingMessage(self, DisplayGreetingText):
        """
        Program the contents of a Display Greeting message.\n
        :param DisplayGreetingText: 20 symbols for display greeting message\n
        :type DisplayGreetingText: str\n
        """
        self.do("ProgDisplayGreetingMessage", 'DisplayGreetingText', DisplayGreetingText)

    def ReadDailyPO(self):
        """
        Provides information about the PO amounts by type of payment and the total number of operations.\n
        """
        return __DailyPORes__(*self.do("ReadDailyPO"))

    def ReadAlteTaxe(self, Number):
        """
        Read the other charges (Alte taxe) name.\n
        :param Number: 1 symbol for number in order up to 7\n
        :type Number: str\n
        """
        return __AlteTaxeRes__(*self.do("ReadAlteTaxe", 'Number', Number))

    def ReadBriefFMReportByDate(self, StartDate, EndDate):
        """
        Store a brief FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("ReadBriefFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def StoreBriefFMReportByNum(self, StartNum, EndNum, OptionStorage=None):
        """
        Store a brief FM report by initial and end FM report number.\n
        :param StartNum: 4 symbols for the initial report number included in report, format ####\n
        :type StartNum: float\n
        :param EndNum: 4 symbols for the final report number included in report, format ####\n
        :type EndNum: float\n
        :param OptionStorage: 1 symbol for destination: 
         - '2' - Storage in External USB Flash memory. 
         - '4' - Storage in External SD card memory\n
        :type OptionStorage: Enums.OptionStorage\n
        """
        self.do("StoreBriefFMReportByNum", 'StartNum', StartNum, 'EndNum', EndNum, 'OptionStorage', OptionStorage)

    def ReadDetailedFMReportByDate(self, StartDate, EndDate):
        """
        Storage a detailed FM report by initial and end date.\n
        :param StartDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartDate: datetime\n
        :param EndDate: 6 symbols for final date in the DDMMYY format\n
        :type EndDate: datetime\n
        """
        self.do("ReadDetailedFMReportByDate", 'StartDate', StartDate, 'EndDate', EndDate)

    def PrintDetailedDailyReport(self, OptionZeroing):
        """
        Prints an extended daily financial report (an article report followed by a daily financial report) with or without zeroing ('Z' or 'X').\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Not zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintDetailedDailyReport", 'OptionZeroing', OptionZeroing)


class __DailyAvailableAmountsRes__:
    """
    :param AmountPayment0: Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment0: float\n
    :param AmountPayment1: Up to 11 symbols for the accumulated amount by payment type 1\n
    :type AmountPayment1: float\n
    :param AmountPayment2: Up to 11 symbols for the accumulated amount by payment type 2\n
    :type AmountPayment2: float\n
    :param AmountPayment3: Up to 11 symbols for the accumulated amount by payment type 3\n
    :type AmountPayment3: float\n
    :param AmountPayment4: Up to 11 symbols for the accumulated amount by payment type 4\n
    :type AmountPayment4: float\n
    :param AmountPayment5: Up to 11 symbols for the accumulated amount by payment type 5\n
    :type AmountPayment5: float\n
    :param AmountPayment6: Up to 11 symbols for the accumulated amount by payment type 6\n
    :type AmountPayment6: float\n
    :param AmountPayment7: Up to 11 symbols for the accumulated amount by payment type 7\n
    :type AmountPayment7: float\n
    :param AmountPayment8: Up to 11 symbols for the accumulated amount by payment type 8\n
    :type AmountPayment8: float\n
    :param AmountPayment9: Up to 11 symbols for the accumulated amount by payment type 9\n
    :type AmountPayment9: float\n
    """
    def __init__(self, AmountPayment0, AmountPayment1, AmountPayment2, AmountPayment3, AmountPayment4, AmountPayment5, AmountPayment6, AmountPayment7, AmountPayment8, AmountPayment9):
        self.AmountPayment0 = AmountPayment0
        self.AmountPayment1 = AmountPayment1
        self.AmountPayment2 = AmountPayment2
        self.AmountPayment3 = AmountPayment3
        self.AmountPayment4 = AmountPayment4
        self.AmountPayment5 = AmountPayment5
        self.AmountPayment6 = AmountPayment6
        self.AmountPayment7 = AmountPayment7
        self.AmountPayment8 = AmountPayment8
        self.AmountPayment9 = AmountPayment9


class __DepartmentRes__:
    """
    :param DepNum: 1..2 symbols for department number in format ##\n
    :type DepNum: float\n
    :param DepName: 34 symbols for department name\n
    :type DepName: str\n
    :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
     - 'A' - VAT Class A 
     - 'B' - VAT Class B 
     - 'C' - VAT Class C 
     - 'D' - VAT Class D 
     - 'E' - VAT Class E 
     - 'F' - Alte taxe\n
    :type OptionVATClass: Enums.OptionVATClass\n
    :param Turnover: 1..11 symbols for accumulated turnover of the department\n
    :type Turnover: float\n
    :param SoldQuantity: 1..11 symbols for sold quantity of the department\n
    :type SoldQuantity: float\n
    :param LastZReportNumber: 1..5 symbols for the number of last Z report in format #####\n
    :type LastZReportNumber: float\n
    :param LastZReportDate: 16 symbols for the date and hour in last Z report\n
    :type LastZReportDate: datetime\n
    :param Price: 1 to 10 symbols for department price\n
    :type Price: float\n
    :param OptionDepPrice: 1 symbol for Department flags with next value: 
     - '0' - Free price disabled  
     - '1' - Free price enabled  
     - '2' - Limited price 
     - '4' - Free price disabled for single transaction 
     - '5' - Free price enabled for single transaction 
     - '6' - Limited price for single transaction\n
    :type OptionDepPrice: Enums.OptionDepPrice\n
    :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
    :type Category: float\n
    """
    def __init__(self, DepNum, DepName, OptionVATClass, Turnover, SoldQuantity, LastZReportNumber, LastZReportDate, Price, OptionDepPrice, Category):
        self.DepNum = DepNum
        self.DepName = DepName
        self.OptionVATClass = OptionVATClass
        self.Turnover = Turnover
        self.SoldQuantity = SoldQuantity
        self.LastZReportNumber = LastZReportNumber
        self.LastZReportDate = LastZReportDate
        self.Price = Price
        self.OptionDepPrice = OptionDepPrice
        self.Category = Category


class __CurrencyAmountsByOperatorRes__:
    """
    :param OperNum: Symbol from 1 to 20 corresponding to operator's number\n
    :type OperNum: str\n
    :param Vanzari_op: Up to 12 symbols for accumulated amount of sales of currency 
    without commission\n
    :type Vanzari_op: float\n
    :param Cumparari_op: Up to 12 symbols for accumulated amount of currency purchase 
    without commission\n
    :type Cumparari_op: float\n
    :param Commission_vanzari_op: Up to 12 symbols for accumulated amount of commissions in sales\n
    :type Commission_vanzari_op: float\n
    :param Commission_cumparari_op: Up to 12 symbols for accumulated amount of commissions in 
    purchase\n
    :type Commission_cumparari_op: float\n
    """
    def __init__(self, OperNum, Vanzari_op, Cumparari_op, Commission_vanzari_op, Commission_cumparari_op):
        self.OperNum = OperNum
        self.Vanzari_op = Vanzari_op
        self.Cumparari_op = Cumparari_op
        self.Commission_vanzari_op = Commission_vanzari_op
        self.Commission_cumparari_op = Commission_cumparari_op


class __Bluetooth_PasswordRes__:
    """
    :param PassLength: (Length) Up to 3 symbols for the BT password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the BT password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __GPRS_APNRes__:
    """
    :param GPRS_APN_Len: (Length) Up to 3 symbols for the APN length\n
    :type GPRS_APN_Len: float\n
    :param APN: Up to 100 symbols for the device's GPRS APN\n
    :type APN: str\n
    """
    def __init__(self, GPRS_APN_Len, APN):
        self.GPRS_APN_Len = GPRS_APN_Len
        self.APN = APN


class __PLUqtyRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param AvailableQuantity: Up to13 symbols for quantity in stock\n
    :type AvailableQuantity: float\n
    :param OptionQuantityType: 1 symbol for Quantity flag with next value:  
    - '0'- Availability of PLU stock is not monitored  
    - '1'- Disable negative quantity  
    - '2'- Enable negative quantity\n
    :type OptionQuantityType: Enums.OptionQuantityType\n
    """
    def __init__(self, PLUNum, AvailableQuantity, OptionQuantityType):
        self.PLUNum = PLUNum
        self.AvailableQuantity = AvailableQuantity
        self.OptionQuantityType = OptionQuantityType


class __GPRS_UsernameRes__:
    """
    :param GPRS_User_Len: (Length) Up to 3 symbols for the GPRS username length\n
    :type GPRS_User_Len: float\n
    :param Username: Up to 100 symbols for the device's GPRS username\n
    :type Username: str\n
    """
    def __init__(self, GPRS_User_Len, Username):
        self.GPRS_User_Len = GPRS_User_Len
        self.Username = Username


class __ServerAddressRes__:
    """
    :param ParamLength: Up to 3 symbols for parameter length\n
    :type ParamLength: float\n
    :param ServerAddress: Up to 100 symbols for server password\n
    :type ServerAddress: str\n
    """
    def __init__(self, ParamLength, ServerAddress):
        self.ParamLength = ParamLength
        self.ServerAddress = ServerAddress


class __VATratesRes__:
    """
    :param VATrateA: 6 symbols for VATrates of VAT class A in format ##.##%\n
    :type VATrateA: float\n
    :param VATrateB: 6 symbols for VATrates of VAT class B in format ##.##%\n
    :type VATrateB: float\n
    :param VATrateC: 6 symbols for VATrates of VAT class C in format ##.##%\n
    :type VATrateC: float\n
    :param VATrateD: 6 symbols for VATrates of VAT class D in format ##.##%\n
    :type VATrateD: float\n
    :param VATrateE: 6 symbols for VATrates of VAT class E in format ##.##%\n
    :type VATrateE: float\n
    :param AlteTaxeF: 6 symbols for VATrates of Alte Taxe F in format ##.##%\n
    :type AlteTaxeF: float\n
    """
    def __init__(self, VATrateA, VATrateB, VATrateC, VATrateD, VATrateE, AlteTaxeF):
        self.VATrateA = VATrateA
        self.VATrateB = VATrateB
        self.VATrateC = VATrateC
        self.VATrateD = VATrateD
        self.VATrateE = VATrateE
        self.AlteTaxeF = AlteTaxeF


class __ServiceWarningMessagesRes__:
    """
    :param Password: 6 symbols for service password 
    '3' '3' - for warning message\n
    :type Password: str\n
    :param Line1: TextLength symbols for warning message for line 1\n
    :type Line1: str\n
    :param Line2: TextLength symbols for warning message for line 2\n
    :type Line2: str\n
    :param Line3: TextLength symbols for warning message for line 3\n
    :type Line3: str\n
    """
    def __init__(self, Password, Line1, Line2, Line3):
        self.Password = Password
        self.Line1 = Line1
        self.Line2 = Line2
        self.Line3 = Line3


class __DailyReceivedSalesAmountsRes__:
    """
    :param AmountPayment0: Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment0: float\n
    :param AmountPayment1: Up to 11 symbols for the accumulated amount by payment type 1\n
    :type AmountPayment1: float\n
    :param AmountPayment2: Up to 11 symbols for the accumulated amount by payment type 2\n
    :type AmountPayment2: float\n
    :param AmountPayment3: Up to 11 symbols for the accumulated amount by payment type 3\n
    :type AmountPayment3: float\n
    :param AmountPayment4: Up to 11 symbols for the accumulated amount by payment type 4\n
    :type AmountPayment4: float\n
    :param AmountPayment5: Up to 11 symbols for the accumulated amount by payment type 5\n
    :type AmountPayment5: float\n
    :param AmountPayment6: Up to 11 symbols for the accumulated amount by payment type 6\n
    :type AmountPayment6: float\n
    :param AmountPayment7: Up to 11 symbols for the accumulated amount by payment type 7\n
    :type AmountPayment7: float\n
    :param AmountPayment8: Up to 11 symbols for the accumulated amount by payment type 8\n
    :type AmountPayment8: float\n
    :param AmountPayment9: Up to 11 symbols for the accumulated amount by payment type 9\n
    :type AmountPayment9: float\n
    """
    def __init__(self, AmountPayment0, AmountPayment1, AmountPayment2, AmountPayment3, AmountPayment4, AmountPayment5, AmountPayment6, AmountPayment7, AmountPayment8, AmountPayment9):
        self.AmountPayment0 = AmountPayment0
        self.AmountPayment1 = AmountPayment1
        self.AmountPayment2 = AmountPayment2
        self.AmountPayment3 = AmountPayment3
        self.AmountPayment4 = AmountPayment4
        self.AmountPayment5 = AmountPayment5
        self.AmountPayment6 = AmountPayment6
        self.AmountPayment7 = AmountPayment7
        self.AmountPayment8 = AmountPayment8
        self.AmountPayment9 = AmountPayment9


class __LastAndTotalReceiptNumRes__:
    """
    :param LastReceiptNum: 4 symbols for the number of last issued fiscal receipt in format ####\n
    :type LastReceiptNum: float\n
    :param TotalReceiptCounter: 7 symbols for the number of totals issued fiscal receipts in format #######\n
    :type TotalReceiptCounter: float\n
    """
    def __init__(self, LastReceiptNum, TotalReceiptCounter):
        self.LastReceiptNum = LastReceiptNum
        self.TotalReceiptCounter = TotalReceiptCounter


class __LastCurrencyReceiptNumRes__:
    """
    :param LastReceiptNum: 4 symbols in format ####.  
    For the number of last issued fiscal receipts\n
    :type LastReceiptNum: float\n
    :param TotalReceiptCounter: 7 symbols in format #######.   
    
    For the number of totals issued fiscal receipts\n
    :type TotalReceiptCounter: float\n
    :param Daily_Vanzari_RecCounter: 4 symbols in format ####.  
    For the number of sale of currency receipts\n
    :type Daily_Vanzari_RecCounter: float\n
    :param Daily_Cumparari_RecCounter: 4 symbols in format ####. 
    For the number of currency purchase receipts\n
    :type Daily_Cumparari_RecCounter: float\n
    :param Daily_Anulat_RecCounter: 4 symbols in format ####. 
    For the number of cancel receipts\n
    :type Daily_Anulat_RecCounter: float\n
    """
    def __init__(self, LastReceiptNum, TotalReceiptCounter, Daily_Vanzari_RecCounter, Daily_Cumparari_RecCounter, Daily_Anulat_RecCounter):
        self.LastReceiptNum = LastReceiptNum
        self.TotalReceiptCounter = TotalReceiptCounter
        self.Daily_Vanzari_RecCounter = Daily_Vanzari_RecCounter
        self.Daily_Cumparari_RecCounter = Daily_Cumparari_RecCounter
        self.Daily_Anulat_RecCounter = Daily_Anulat_RecCounter


class __DailyPObyOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20corresponding to operator's number\n
    :type OperNum: float\n
    :param AmountPO_Payment0: Up to 11 symbols for the PO by type of payment 0\n
    :type AmountPO_Payment0: float\n
    :param AmountPO_Payment1: Up to 11 symbols for the PO by type of payment 1\n
    :type AmountPO_Payment1: float\n
    :param AmountPO_Payment2: Up to 11 symbols for the PO by type of payment 2\n
    :type AmountPO_Payment2: float\n
    :param AmountPO_Payment3: Up to 11 symbols for the PO by type of payment 3\n
    :type AmountPO_Payment3: float\n
    :param AmountPO_Payment4: Up to 11 symbols for the PO by type of payment 4\n
    :type AmountPO_Payment4: float\n
    :param AmountPO_Payment5: Up to 11 symbols for the PO by type of payment 5\n
    :type AmountPO_Payment5: float\n
    :param AmountPO_Payment6: Up to 11 symbols for the PO by type of payment 6\n
    :type AmountPO_Payment6: float\n
    :param AmountPO_Payment7: Up to 11 symbols for the PO by type of payment 7\n
    :type AmountPO_Payment7: float\n
    :param AmountPO_Payment8: Up to 11 symbols for the PO by type of payment 8\n
    :type AmountPO_Payment8: float\n
    :param AmountPO_Payment9: Up to 11 symbols for the PO by type of payment 9\n
    :type AmountPO_Payment9: float\n
    :param NumPO: 5 symbols for the total number of operations\n
    :type NumPO: float\n
    """
    def __init__(self, OperNum, AmountPO_Payment0, AmountPO_Payment1, AmountPO_Payment2, AmountPO_Payment3, AmountPO_Payment4, AmountPO_Payment5, AmountPO_Payment6, AmountPO_Payment7, AmountPO_Payment8, AmountPO_Payment9, NumPO):
        self.OperNum = OperNum
        self.AmountPO_Payment0 = AmountPO_Payment0
        self.AmountPO_Payment1 = AmountPO_Payment1
        self.AmountPO_Payment2 = AmountPO_Payment2
        self.AmountPO_Payment3 = AmountPO_Payment3
        self.AmountPO_Payment4 = AmountPO_Payment4
        self.AmountPO_Payment5 = AmountPO_Payment5
        self.AmountPO_Payment6 = AmountPO_Payment6
        self.AmountPO_Payment7 = AmountPO_Payment7
        self.AmountPO_Payment8 = AmountPO_Payment8
        self.AmountPO_Payment9 = AmountPO_Payment9
        self.NumPO = NumPO


class __CustomerVATNumRes__:
    """
    :param CustomerVATNum: 15 symbols for VAT number\n
    :type CustomerVATNum: str\n
    :param OptionTypeVATregistration: 1 symbol for type of owner's VAT registration: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionTypeVATregistration: Enums.OptionTypeVATregistration\n
    """
    def __init__(self, CustomerVATNum, OptionTypeVATregistration):
        self.CustomerVATNum = CustomerVATNum
        self.OptionTypeVATregistration = OptionTypeVATregistration


class __TCP_AddressesRes__:
    """
    :param OptionAddressType: (Address) 1 symbol with value: 
     - '2' - IP address 
     - '3' - Subnet Mask 
     - '4' - Gateway address 
     - '5' - DNS address\n
    :type OptionAddressType: Enums.OptionAddressType\n
    :param DeviceAddress: 15 symbols for the device's addresses\n
    :type DeviceAddress: str\n
    """
    def __init__(self, OptionAddressType, DeviceAddress):
        self.OptionAddressType = OptionAddressType
        self.DeviceAddress = DeviceAddress


class __ServiceContractDateRes__:
    """
    :param Password: 6 symbols for service password 
    '1' '1' - for date\n
    :type Password: str\n
    :param ExpiryDate: 10 symbols for expiry date of service contract\n
    :type ExpiryDate: datetime\n
    """
    def __init__(self, Password, ExpiryDate):
        self.Password = Password
        self.ExpiryDate = ExpiryDate


class __DailyCountersRes__:
    """
    :param LastReportNumFromReset: Up to 5 symbols for number of the last report from reset\n
    :type LastReportNumFromReset: float\n
    :param NumLastFMBlock: Up to 5 symbols for number of the last FM report\n
    :type NumLastFMBlock: float\n
    :param NumEJ: Up to 5 symbols for number of EJ\n
    :type NumEJ: float\n
    :param DateTime: 16 symbols for date and time of the last block storage in FM in 
    format "DD-MM-YYYY HH:MM"\n
    :type DateTime: datetime\n
    """
    def __init__(self, LastReportNumFromReset, NumLastFMBlock, NumEJ, DateTime):
        self.LastReportNumFromReset = LastReportNumFromReset
        self.NumLastFMBlock = NumLastFMBlock
        self.NumEJ = NumEJ
        self.DateTime = DateTime


class __DailyRAbyOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20corresponding to operator's number\n
    :type OperNum: float\n
    :param AmountRA_Payment0: Up to 11 symbols for the RA by type of payment 0\n
    :type AmountRA_Payment0: float\n
    :param AmountRA_Payment1: Up to 11 symbols for the RA by type of payment 1\n
    :type AmountRA_Payment1: float\n
    :param AmountRA_Payment2: Up to 11 symbols for the RA by type of payment 2\n
    :type AmountRA_Payment2: float\n
    :param AmountRA_Payment3: Up to 11 symbols for the RA by type of payment 3\n
    :type AmountRA_Payment3: float\n
    :param AmountRA_Payment4: Up to 11 symbols for the RA by type of payment 4\n
    :type AmountRA_Payment4: float\n
    :param AmountRA_Payment5: Up to 11 symbols for the RA by type of payment 5\n
    :type AmountRA_Payment5: float\n
    :param AmountRA_Payment6: Up to 11 symbols for the RA by type of payment 6\n
    :type AmountRA_Payment6: float\n
    :param AmountRA_Payment7: Up to 11 symbols for the RA by type of payment 7\n
    :type AmountRA_Payment7: float\n
    :param AmountRA_Payment8: Up to 11 symbols for the RA by type of payment 8\n
    :type AmountRA_Payment8: float\n
    :param AmountRA_Payment9: Up to 11 symbols for the RA by type of payment 9\n
    :type AmountRA_Payment9: float\n
    :param NumRA: 5 symbols for the total number of operations\n
    :type NumRA: str\n
    """
    def __init__(self, OperNum, AmountRA_Payment0, AmountRA_Payment1, AmountRA_Payment2, AmountRA_Payment3, AmountRA_Payment4, AmountRA_Payment5, AmountRA_Payment6, AmountRA_Payment7, AmountRA_Payment8, AmountRA_Payment9, NumRA):
        self.OperNum = OperNum
        self.AmountRA_Payment0 = AmountRA_Payment0
        self.AmountRA_Payment1 = AmountRA_Payment1
        self.AmountRA_Payment2 = AmountRA_Payment2
        self.AmountRA_Payment3 = AmountRA_Payment3
        self.AmountRA_Payment4 = AmountRA_Payment4
        self.AmountRA_Payment5 = AmountRA_Payment5
        self.AmountRA_Payment6 = AmountRA_Payment6
        self.AmountRA_Payment7 = AmountRA_Payment7
        self.AmountRA_Payment8 = AmountRA_Payment8
        self.AmountRA_Payment9 = AmountRA_Payment9
        self.NumRA = NumRA


class __PLUcategoryRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
    :type Category: float\n
    """
    def __init__(self, PLUNum, Category):
        self.PLUNum = PLUNum
        self.Category = Category


class __HeaderRes__:
    """
    :param OptionHeaderLine: (Line Number)1 byte with value: 
     - '1' - Header 1 
     - '2' - Header 2 
     - '3' - Header 3 
     - '4' - Header 4 
     - '5' - Header 5 
     - '6' - Header 6 
     - '7' - Header 7 
     - '8' - Header 8\n
    :type OptionHeaderLine: Enums.OptionHeaderLine\n
    :param HeaderText: LineLength symbols\n
    :type HeaderText: str\n
    """
    def __init__(self, OptionHeaderLine, HeaderText):
        self.OptionHeaderLine = OptionHeaderLine
        self.HeaderText = HeaderText


class __VATNumRes__:
    """
    :param VATNum: 15 symbols for owner's VAT registration number\n
    :type VATNum: str\n
    :param FMnum: 10 symbols for FM serial number\n
    :type FMnum: str\n
    :param OptionTypeVATregistration: 1 symbol for type of owner's VAT registration: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionTypeVATregistration: Enums.OptionTypeVATregistration\n
    """
    def __init__(self, VATNum, FMnum, OptionTypeVATregistration):
        self.VATNum = VATNum
        self.FMnum = FMnum
        self.OptionTypeVATregistration = OptionTypeVATregistration


class __DeviceModuleSupportByFirmwareRes__:
    """
    :param OptionLAN: 1 symbol for LAN support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionLAN: Enums.OptionLAN\n
    :param OptionWiFi: 1 symbol for WiFi support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionWiFi: Enums.OptionWiFi\n
    :param OptionGPRS: 1 symbol for GPRS support 
     - '0' - No 
     - '1' - Yes 
    BT (Bluetooth) 1 symbol for Bluetooth support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionGPRS: Enums.OptionGPRS\n
    :param OptionBT: (Bluetooth) 1 symbol for Bluetooth support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionBT: Enums.OptionBT\n
    """
    def __init__(self, OptionLAN, OptionWiFi, OptionGPRS, OptionBT):
        self.OptionLAN = OptionLAN
        self.OptionWiFi = OptionWiFi
        self.OptionGPRS = OptionGPRS
        self.OptionBT = OptionBT


class __WiFi_PasswordRes__:
    """
    :param PassLength: (Length) Up to 3 symbols for the WiFi password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the device's WiFi password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __DailyAmountsByVATRes__:
    """
    :param SaleAmountVATGrA: Up to 11 symbols for the amount accumulated in the VAT group A\n
    :type SaleAmountVATGrA: float\n
    :param SaleAmountVATGrB: Up to 11 symbols for the amount accumulated in the VAT group B\n
    :type SaleAmountVATGrB: float\n
    :param SaleAmountVATGrC: Up to 11 symbols for the amount accumulated in the VAT group C\n
    :type SaleAmountVATGrC: float\n
    :param SaleAmountVATGrD: Up to 11 symbols for the amount accumulated in the VAT group D\n
    :type SaleAmountVATGrD: float\n
    :param SaleAmountVATGrE: Up to 11 symbols for the amount accumulated in the VAT group E\n
    :type SaleAmountVATGrE: float\n
    :param SaleAmountAlteTaxeF: Up to 11 symbols for the amount accumulated in the Alte Taxe F\n
    :type SaleAmountAlteTaxeF: float\n
    """
    def __init__(self, SaleAmountVATGrA, SaleAmountVATGrB, SaleAmountVATGrC, SaleAmountVATGrD, SaleAmountVATGrE, SaleAmountAlteTaxeF):
        self.SaleAmountVATGrA = SaleAmountVATGrA
        self.SaleAmountVATGrB = SaleAmountVATGrB
        self.SaleAmountVATGrC = SaleAmountVATGrC
        self.SaleAmountVATGrD = SaleAmountVATGrD
        self.SaleAmountVATGrE = SaleAmountVATGrE
        self.SaleAmountAlteTaxeF = SaleAmountAlteTaxeF


class __PLUgeneralRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param PLUName: 34 symbols for article name /LF=7Ch, MU separator = 80h or 60h 
    followed up to 3 symbols for unit/\n
    :type PLUName: str\n
    :param Price: Up to 10 symbols for article price\n
    :type Price: float\n
    :param OptionPrice: 1 symbol for price flag with next value: 
     - '0'- Free price is disable valid only programmed price 
     - '1'- Free price is enable 
     - '2'- Limited price\n
    :type OptionPrice: Enums.OptionPrice\n
    :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
     - 'A' - VAT Class A 
     - 'B' - VAT Class B 
     - 'C' - VAT Class C 
     - 'D' - VAT Class D 
     - 'E' - VAT Class E 
     - 'F' - Alte taxe\n
    :type OptionVATClass: Enums.OptionVATClass\n
    :param BelongToDepNumber: BelongToDepNo + 80h, 1 symbol for PLU department = 0x80 … 0x93\n
    :type BelongToDepNumber: float\n
    :param AlteTaxNum: Up to 11 symbols for Alte Tax number\n
    :type AlteTaxNum: float\n
    :param AlteTaxValue: Up to 11 symbols for Alte tax value\n
    :type AlteTaxValue: float\n
    :param TurnoverAmount: Up to 11 symbols for PLU accumulated turnover\n
    :type TurnoverAmount: float\n
    :param SoldQuantity: Up to 11 symbols for Sales quantity of the article\n
    :type SoldQuantity: float\n
    :param LastZReportNumber: 5 symbols for the number of the last in format #####  
    article report with zeroing\n
    :type LastZReportNumber: float\n
    :param LastZReportDate: 16 symbols for the date and time of the last article report with zeroing\n
    :type LastZReportDate: datetime\n
    :param OptionSingleTransaction: 1 symbol with value: 
     - '0' - Inactive, default value 
     - '1' - Active Single transaction in receipt\n
    :type OptionSingleTransaction: Enums.OptionSingleTransaction\n
    :param AlteTaxTurnover: Up to 11 symbols for Alte Tax Turnover\n
    :type AlteTaxTurnover: float\n
    """
    def __init__(self, PLUNum, PLUName, Price, OptionPrice, OptionVATClass, BelongToDepNumber, AlteTaxNum, AlteTaxValue, TurnoverAmount, SoldQuantity, LastZReportNumber, LastZReportDate, OptionSingleTransaction, AlteTaxTurnover):
        self.PLUNum = PLUNum
        self.PLUName = PLUName
        self.Price = Price
        self.OptionPrice = OptionPrice
        self.OptionVATClass = OptionVATClass
        self.BelongToDepNumber = BelongToDepNumber
        self.AlteTaxNum = AlteTaxNum
        self.AlteTaxValue = AlteTaxValue
        self.TurnoverAmount = TurnoverAmount
        self.SoldQuantity = SoldQuantity
        self.LastZReportNumber = LastZReportNumber
        self.LastZReportDate = LastZReportDate
        self.OptionSingleTransaction = OptionSingleTransaction
        self.AlteTaxTurnover = AlteTaxTurnover


class __DailyReceivedSalesAmountsByOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param ReceivedSalesAmountPayment0: Up to 11 symbols for amounts received by sales for payment 0\n
    :type ReceivedSalesAmountPayment0: float\n
    :param ReceivedSalesAmountPayment1: Up to 11 symbols for amounts received by sales for payment 1\n
    :type ReceivedSalesAmountPayment1: float\n
    :param ReceivedSalesAmountPayment2: Up to 11 symbols for amounts received by sales for payment 2\n
    :type ReceivedSalesAmountPayment2: float\n
    :param ReceivedSalesAmountPayment3: Up to 11 symbols for amounts received by sales for payment 3\n
    :type ReceivedSalesAmountPayment3: float\n
    :param ReceivedSalesAmountPayment4: Up to 11 symbols for amounts received by sales for payment 4\n
    :type ReceivedSalesAmountPayment4: float\n
    :param ReceivedSalesAmountPayment5: Up to 11 symbols for amounts received by sales for payment 5\n
    :type ReceivedSalesAmountPayment5: float\n
    :param ReceivedSalesAmountPayment6: Up to 11 symbols for amounts received by sales for payment 6\n
    :type ReceivedSalesAmountPayment6: float\n
    :param ReceivedSalesAmountPayment7: Up to 11 symbols for amounts received by sales for payment 7\n
    :type ReceivedSalesAmountPayment7: float\n
    :param ReceivedSalesAmountPayment8: Up to 11 symbols for amounts received by sales for payment 8\n
    :type ReceivedSalesAmountPayment8: float\n
    :param ReceivedSalesAmountPayment9: Up to 11 symbols for amounts received by sales for payment 9\n
    :type ReceivedSalesAmountPayment9: float\n
    """
    def __init__(self, OperNum, ReceivedSalesAmountPayment0, ReceivedSalesAmountPayment1, ReceivedSalesAmountPayment2, ReceivedSalesAmountPayment3, ReceivedSalesAmountPayment4, ReceivedSalesAmountPayment5, ReceivedSalesAmountPayment6, ReceivedSalesAmountPayment7, ReceivedSalesAmountPayment8, ReceivedSalesAmountPayment9):
        self.OperNum = OperNum
        self.ReceivedSalesAmountPayment0 = ReceivedSalesAmountPayment0
        self.ReceivedSalesAmountPayment1 = ReceivedSalesAmountPayment1
        self.ReceivedSalesAmountPayment2 = ReceivedSalesAmountPayment2
        self.ReceivedSalesAmountPayment3 = ReceivedSalesAmountPayment3
        self.ReceivedSalesAmountPayment4 = ReceivedSalesAmountPayment4
        self.ReceivedSalesAmountPayment5 = ReceivedSalesAmountPayment5
        self.ReceivedSalesAmountPayment6 = ReceivedSalesAmountPayment6
        self.ReceivedSalesAmountPayment7 = ReceivedSalesAmountPayment7
        self.ReceivedSalesAmountPayment8 = ReceivedSalesAmountPayment8
        self.ReceivedSalesAmountPayment9 = ReceivedSalesAmountPayment9


class __DailyCurrencyRes__:
    """
    :param Vanzari: Up to 12 symbols for accumulated amount of sales of currency without 
    commission\n
    :type Vanzari: float\n
    :param Cumparari: Up to 12 symbols for accumulated amount of currency purchase 
    without commission\n
    :type Cumparari: float\n
    :param Commission_vanzari: Up to 12 symbols for accumulated amount of commissions in sales\n
    :type Commission_vanzari: float\n
    :param Commission_cumparari: Up to 12 symbols for accumulated amount of commissions in purchase\n
    :type Commission_cumparari: float\n
    """
    def __init__(self, Vanzari, Cumparari, Commission_vanzari, Commission_cumparari):
        self.Vanzari = Vanzari
        self.Cumparari = Cumparari
        self.Commission_vanzari = Commission_vanzari
        self.Commission_cumparari = Commission_cumparari


class __CustomerDataRes__:
    """
    :param CustomerNum: 3 symbols for customer number in order in format ###\n
    :type CustomerNum: float\n
    :param CustomerVatNum: 15 symbols for customer VAT registration number\n
    :type CustomerVatNum: str\n
    :param CustomerName: 30 symbols for customer name\n
    :type CustomerName: str\n
    :param CustomerAddress: 30 symbols for customer address\n
    :type CustomerAddress: str\n
    :param FreeLine1: 20 ASCII symbols for customer data\n
    :type FreeLine1: str\n
    :param FreeLine2: 20 ASCII symbols for customer data\n
    :type FreeLine2: str\n
    :param FreeLine3: 20 ASCII symbols for customer data\n
    :type FreeLine3: str\n
    :param FreeLine4: 20 ASCII symbols for customer data\n
    :type FreeLine4: str\n
    :param CustTurnover: 1..11 symbols for accumulated turnover of the customer\n
    :type CustTurnover: float\n
    """
    def __init__(self, CustomerNum, CustomerVatNum, CustomerName, CustomerAddress, FreeLine1, FreeLine2, FreeLine3, FreeLine4, CustTurnover):
        self.CustomerNum = CustomerNum
        self.CustomerVatNum = CustomerVatNum
        self.CustomerName = CustomerName
        self.CustomerAddress = CustomerAddress
        self.FreeLine1 = FreeLine1
        self.FreeLine2 = FreeLine2
        self.FreeLine3 = FreeLine3
        self.FreeLine4 = FreeLine4
        self.CustTurnover = CustTurnover


class __CurrentReceiptInfoRes__:
    """
    :param OptionIsReceiptOpened: 1 symbol with value: 
     - '0' - No 
     - '1' - Yes\n
    :type OptionIsReceiptOpened: Enums.OptionIsReceiptOpened\n
    :param SalesNumber: 3 symbols for number of sales\n
    :type SalesNumber: str\n
    :param SubtotalAmountVATGA: Up to 11 symbols for subtotal by VAT group A\n
    :type SubtotalAmountVATGA: float\n
    :param SubtotalAmountVATGB: Up to 11 symbols for subtotal by VAT group B\n
    :type SubtotalAmountVATGB: float\n
    :param SubtotalAmountVATGC: Up to 11 symbols for subtotal by VAT group C\n
    :type SubtotalAmountVATGC: float\n
    :param SubtotalAmountVATGD: Up to 11 symbols for subtotal by VAT group D\n
    :type SubtotalAmountVATGD: float\n
    :param SubtotalAmountVATGE: Up to 11 symbols for subtotal by VAT group E\n
    :type SubtotalAmountVATGE: float\n
    :param OptionForbiddenVoid: 1 symbol with value: 
     - '0' - allowed 
     - '1' - forbidden\n
    :type OptionForbiddenVoid: Enums.OptionForbiddenVoid\n
    :param OptionVATinReceipt: 1 symbol with value: 
     - '0' - with printing 
     - '1' - without printing\n
    :type OptionVATinReceipt: Enums.OptionVATinReceipt\n
    :param OptionReceiptFormat: (Format) 1 symbol with value: 
     - '1' - Detailed 
     - '0' - Brief\n
    :type OptionReceiptFormat: Enums.OptionReceiptFormat\n
    :param OptionInitiatedPayment: 1 symbol with value: 
     - '0' - initiated payment 
     - '1' - not initiated payment\n
    :type OptionInitiatedPayment: Enums.OptionInitiatedPayment\n
    :param OptionFinalizedPayment: 1 symbol with value: 
     - '0' - finalized payment 
     - '1' - not finalized payment\n
    :type OptionFinalizedPayment: Enums.OptionFinalizedPayment\n
    :param OptionPowerDownInReceipt: 1 symbol with value: 
    - '0' - No 
    - '1' - Yes\n
    :type OptionPowerDownInReceipt: Enums.OptionPowerDownInReceipt\n
    :param OptionClientReceipt: 1 symbol with value: 
     - '0' - standard receipt 
     - '1' - invoice (client) receipt\n
    :type OptionClientReceipt: Enums.OptionClientReceipt\n
    :param ChangeAmount: Up to 11 symbols the amount of the due change in the 
    stated payment type\n
    :type ChangeAmount: float\n
    :param OptionChangeType: 1 symbols with value: 
     - '0' - Change In Cash 
     - '1' - Same As The payment 
     - '2' - Change In Currency\n
    :type OptionChangeType: Enums.OptionChangeType\n
    :param AlteTaxeValue: Up to 11 symbols for alte taxe amount\n
    :type AlteTaxeValue: float\n
    """
    def __init__(self, OptionIsReceiptOpened, SalesNumber, SubtotalAmountVATGA, SubtotalAmountVATGB, SubtotalAmountVATGC, SubtotalAmountVATGD, SubtotalAmountVATGE, OptionForbiddenVoid, OptionVATinReceipt, OptionReceiptFormat, OptionInitiatedPayment, OptionFinalizedPayment, OptionPowerDownInReceipt, OptionClientReceipt, ChangeAmount, OptionChangeType, AlteTaxeValue):
        self.OptionIsReceiptOpened = OptionIsReceiptOpened
        self.SalesNumber = SalesNumber
        self.SubtotalAmountVATGA = SubtotalAmountVATGA
        self.SubtotalAmountVATGB = SubtotalAmountVATGB
        self.SubtotalAmountVATGC = SubtotalAmountVATGC
        self.SubtotalAmountVATGD = SubtotalAmountVATGD
        self.SubtotalAmountVATGE = SubtotalAmountVATGE
        self.OptionForbiddenVoid = OptionForbiddenVoid
        self.OptionVATinReceipt = OptionVATinReceipt
        self.OptionReceiptFormat = OptionReceiptFormat
        self.OptionInitiatedPayment = OptionInitiatedPayment
        self.OptionFinalizedPayment = OptionFinalizedPayment
        self.OptionPowerDownInReceipt = OptionPowerDownInReceipt
        self.OptionClientReceipt = OptionClientReceipt
        self.ChangeAmount = ChangeAmount
        self.OptionChangeType = OptionChangeType
        self.AlteTaxeValue = AlteTaxeValue


class __PLUallDataRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
    :type PLUNum: float\n
    :param PLUName: 34 symbols for article name (LF=7Ch, MU separator = 80h or 60h 
    followed up to 3 symbols for unit)\n
    :type PLUName: str\n
    :param Price: 1..10 symbols for article price\n
    :type Price: float\n
    :param FlagsPricePLU: 1 symbol for flags = 0x80 + FlagSinglTr + FlagQTY + OptionPrice 
    Where  
    OptionPrice: 
    0x00 - for free price is disable /valid only programmed price/ 
    0x01 - for free price is enable 
    0x02 - for limited price 
    FlagQTY: 
    0x00 - for availability of PLU stock is not monitored 
    0x04 - for disable negative quantity 
    0x08 - for enable negative quantity 
    FlagSingleTr: 
    0x00 - no single transaction 
    0x10 - single transaction is active\n
    :type FlagsPricePLU: str\n
    :param OptionVATClass: 1 symbol for article's VAT class with optional values:" 
     - 'A' - VAT Class A 
     - 'B' - VAT Class B 
     - 'C' - VAT Class C 
     - 'D' - VAT Class D 
     - 'E' - VAT Class E 
     - 'F' - Alte taxe\n
    :type OptionVATClass: Enums.OptionVATClass\n
    :param BelongToDepNumber: BelongToDepNo + 80h, 1 symbol for PLU department = 0x80 … 0x93\n
    :type BelongToDepNumber: float\n
    :param AlteTaxNum: Up to 11 symbols for Alte Tax number\n
    :type AlteTaxNum: float\n
    :param AlteTaxValue: Up to 11 symbols for Alte tax value\n
    :type AlteTaxValue: float\n
    :param Turnover: Up to 11 symbols for PLU accumulated turnover\n
    :type Turnover: float\n
    :param QuantitySold: Up to 11 symbols for Sales quantity of the article\n
    :type QuantitySold: float\n
    :param LastZReportNumber: Up to 5 symbols for the number of the last article report with zeroing\n
    :type LastZReportNumber: float\n
    :param LastZReportDate: 16 symbols for the date and time of the last article report with zeroing\n
    :type LastZReportDate: datetime\n
    :param AvailableQTY: (Available Quantity) - 1..11 symbols for quantity in stock\n
    :type AvailableQTY: float\n
    :param Barcode: 13 symbols for article barcode\n
    :type Barcode: str\n
    :param AlteTaxAmount: Up to 11 symbols for Alte tax amount\n
    :type AlteTaxAmount: float\n
    :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
    :type Category: float\n
    """
    def __init__(self, PLUNum, PLUName, Price, FlagsPricePLU, OptionVATClass, BelongToDepNumber, AlteTaxNum, AlteTaxValue, Turnover, QuantitySold, LastZReportNumber, LastZReportDate, AvailableQTY, Barcode, AlteTaxAmount, Category):
        self.PLUNum = PLUNum
        self.PLUName = PLUName
        self.Price = Price
        self.FlagsPricePLU = FlagsPricePLU
        self.OptionVATClass = OptionVATClass
        self.BelongToDepNumber = BelongToDepNumber
        self.AlteTaxNum = AlteTaxNum
        self.AlteTaxValue = AlteTaxValue
        self.Turnover = Turnover
        self.QuantitySold = QuantitySold
        self.LastZReportNumber = LastZReportNumber
        self.LastZReportDate = LastZReportDate
        self.AvailableQTY = AvailableQTY
        self.Barcode = Barcode
        self.AlteTaxAmount = AlteTaxAmount
        self.Category = Category


class __LastDailyReportInfoRes__:
    """
    :param LastZDailyReportDate: 10 symbols for last Z-report date in DD-MM-YYYY format\n
    :type LastZDailyReportDate: datetime\n
    :param LastZDailyReportNum: Up to 4 symbols for the number of the last daily report\n
    :type LastZDailyReportNum: float\n
    :param LastRAMResetNum: Up to 4 symbols for the number of the last RAM reset\n
    :type LastRAMResetNum: float\n
    """
    def __init__(self, LastZDailyReportDate, LastZDailyReportNum, LastRAMResetNum):
        self.LastZDailyReportDate = LastZDailyReportDate
        self.LastZDailyReportNum = LastZDailyReportNum
        self.LastRAMResetNum = LastRAMResetNum


class __StatusRes__:
    """
    :param FM_Read_only: FM Read only\n
    :type FM_Read_only: bool\n
    :param Power_down_in_opened_fiscal_receipt: Power down in opened fiscal receipt\n
    :type Power_down_in_opened_fiscal_receipt: bool\n
    :param Printer_not_ready_or_overheated: Printer not ready or overheated\n
    :type Printer_not_ready_or_overheated: bool\n
    :param Incorrect_time: Incorrect time\n
    :type Incorrect_time: bool\n
    :param Incorrect_date: Incorrect date\n
    :type Incorrect_date: bool\n
    :param RAM_reset: RAM reset\n
    :type RAM_reset: bool\n
    :param Date_and_time_hardware_error: Date and time hardware error\n
    :type Date_and_time_hardware_error: bool\n
    :param Printer_not_ready_or_no_paper: Printer not ready or no paper\n
    :type Printer_not_ready_or_no_paper: bool\n
    :param Reports_registers_overflow: Reports registers overflow\n
    :type Reports_registers_overflow: bool\n
    :param Blocking_after_24_hours: Blocking after 24 hours\n
    :type Blocking_after_24_hours: bool\n
    :param Non_zero_daily_report: Non-zero daily report\n
    :type Non_zero_daily_report: bool\n
    :param Non_zero_article_report: Non-zero article report\n
    :type Non_zero_article_report: bool\n
    :param Non_zero_operator_report: Non-zero operator report\n
    :type Non_zero_operator_report: bool\n
    :param Non_printed_copy: Non-printed copy\n
    :type Non_printed_copy: bool\n
    :param Opened_Non_fiscal_Receipt: Opened Non-fiscal Receipt\n
    :type Opened_Non_fiscal_Receipt: bool\n
    :param Opened_Fiscal_Receipt: Opened Fiscal Receipt\n
    :type Opened_Fiscal_Receipt: bool\n
    :param Standard_Cash_Receipt: Standard Cash Receipt\n
    :type Standard_Cash_Receipt: bool\n
    :param VAT_included_in_the_receipt: VAT included in the receipt\n
    :type VAT_included_in_the_receipt: bool\n
    :param EJ_near_full: EJ near full\n
    :type EJ_near_full: bool\n
    :param EJ_full: EJ full\n
    :type EJ_full: bool\n
    :param No_FM_module: No FM module\n
    :type No_FM_module: bool\n
    :param FM_error: FM error\n
    :type FM_error: bool\n
    :param FM_full: FM full\n
    :type FM_full: bool\n
    :param FM_near_full: FM near full\n
    :type FM_near_full: bool\n
    :param Decimal_point: Decimal point (1=fract, 0=whole)\n
    :type Decimal_point: bool\n
    :param FM_fiscalized: FM fiscalized\n
    :type FM_fiscalized: bool\n
    :param FM_produced: FM produced\n
    :type FM_produced: bool\n
    :param Printer_automatic_cutting: Printer: automatic cutting\n
    :type Printer_automatic_cutting: bool\n
    :param External_Display_Management: External Display Management\n
    :type External_Display_Management: bool\n
    :param Missing_external_display: Missing external display\n
    :type Missing_external_display: bool\n
    :param Drawer_automatic_opening: Drawer: automatic opening\n
    :type Drawer_automatic_opening: bool\n
    :param Customer_logo_included_in_the_receipt: Customer logo included in the receipt\n
    :type Customer_logo_included_in_the_receipt: bool\n
    :param Service_jumper: Service jumper\n
    :type Service_jumper: bool\n
    :param No_Sec_IC: No Sec.IC\n
    :type No_Sec_IC: bool\n
    :param No_certificates: No certificates\n
    :type No_certificates: bool\n
    :param No_SD_card_response: No SD card response\n
    :type No_SD_card_response: bool\n
    :param Wrong_SD_card: Wrong SD card\n
    :type Wrong_SD_card: bool\n
    :param Near_Paper_end: Near Paper end\n
    :type Near_Paper_end: bool\n
    """
    def __init__(self, FM_Read_only, Power_down_in_opened_fiscal_receipt, Printer_not_ready_or_overheated, Incorrect_time, Incorrect_date, RAM_reset, Date_and_time_hardware_error, Printer_not_ready_or_no_paper, Reports_registers_overflow, Blocking_after_24_hours, Non_zero_daily_report, Non_zero_article_report, Non_zero_operator_report, Non_printed_copy, Opened_Non_fiscal_Receipt, Opened_Fiscal_Receipt, Standard_Cash_Receipt, VAT_included_in_the_receipt, EJ_near_full, EJ_full, No_FM_module, FM_error, FM_full, FM_near_full, Decimal_point, FM_fiscalized, FM_produced, Printer_automatic_cutting, External_Display_Management, Missing_external_display, Drawer_automatic_opening, Customer_logo_included_in_the_receipt, Service_jumper, No_Sec_IC, No_certificates, No_SD_card_response, Wrong_SD_card, Near_Paper_end):
        self.FM_Read_only = FM_Read_only
        self.Power_down_in_opened_fiscal_receipt = Power_down_in_opened_fiscal_receipt
        self.Printer_not_ready_or_overheated = Printer_not_ready_or_overheated
        self.Incorrect_time = Incorrect_time
        self.Incorrect_date = Incorrect_date
        self.RAM_reset = RAM_reset
        self.Date_and_time_hardware_error = Date_and_time_hardware_error
        self.Printer_not_ready_or_no_paper = Printer_not_ready_or_no_paper
        self.Reports_registers_overflow = Reports_registers_overflow
        self.Blocking_after_24_hours = Blocking_after_24_hours
        self.Non_zero_daily_report = Non_zero_daily_report
        self.Non_zero_article_report = Non_zero_article_report
        self.Non_zero_operator_report = Non_zero_operator_report
        self.Non_printed_copy = Non_printed_copy
        self.Opened_Non_fiscal_Receipt = Opened_Non_fiscal_Receipt
        self.Opened_Fiscal_Receipt = Opened_Fiscal_Receipt
        self.Standard_Cash_Receipt = Standard_Cash_Receipt
        self.VAT_included_in_the_receipt = VAT_included_in_the_receipt
        self.EJ_near_full = EJ_near_full
        self.EJ_full = EJ_full
        self.No_FM_module = No_FM_module
        self.FM_error = FM_error
        self.FM_full = FM_full
        self.FM_near_full = FM_near_full
        self.Decimal_point = Decimal_point
        self.FM_fiscalized = FM_fiscalized
        self.FM_produced = FM_produced
        self.Printer_automatic_cutting = Printer_automatic_cutting
        self.External_Display_Management = External_Display_Management
        self.Missing_external_display = Missing_external_display
        self.Drawer_automatic_opening = Drawer_automatic_opening
        self.Customer_logo_included_in_the_receipt = Customer_logo_included_in_the_receipt
        self.Service_jumper = Service_jumper
        self.No_Sec_IC = No_Sec_IC
        self.No_certificates = No_certificates
        self.No_SD_card_response = No_SD_card_response
        self.Wrong_SD_card = Wrong_SD_card
        self.Near_Paper_end = Near_Paper_end


class __PLUpriceRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param Price: 1..10 symbols for article price\n
    :type Price: float\n
    :param OptionPrice: 1 byte for Price flag with next value: 
     - '0'- Free price is disable valid only programmed price 
     - '1'- Free price is enable 
     - '2'- Limited price\n
    :type OptionPrice: Enums.OptionPrice\n
    :param AlteTaxNum: 1 symbol for Alte Tax number\n
    :type AlteTaxNum: str\n
    :param AlteTaxValue: Up to 11 symbols for Alte tax value\n
    :type AlteTaxValue: float\n
    """
    def __init__(self, PLUNum, Price, OptionPrice, AlteTaxNum, AlteTaxValue):
        self.PLUNum = PLUNum
        self.Price = Price
        self.OptionPrice = OptionPrice
        self.AlteTaxNum = AlteTaxNum
        self.AlteTaxValue = AlteTaxValue


class __OperatorNamePasswordRes__:
    """
    :param Number: Symbol from 1 to 20 corresponding to the number of operator\n
    :type Number: float\n
    :param Name: 20 symbols for operator's name\n
    :type Name: str\n
    :param Password: 4 symbols for operator's password\n
    :type Password: str\n
    """
    def __init__(self, Number, Name, Password):
        self.Number = Number
        self.Name = Name
        self.Password = Password


class __DailyCountersByOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param WorkOperatorsCounter: Up to 5 symbols for number of the work operators\n
    :type WorkOperatorsCounter: float\n
    :param LastOperatorReportDateTime: 16 symbols for date and time of the last operator's report in 
    format DD-MM-YYYY HH:MM\n
    :type LastOperatorReportDateTime: datetime\n
    """
    def __init__(self, OperNum, WorkOperatorsCounter, LastOperatorReportDateTime):
        self.OperNum = OperNum
        self.WorkOperatorsCounter = WorkOperatorsCounter
        self.LastOperatorReportDateTime = LastOperatorReportDateTime


class __PaymentsRes__:
    """
    :param NamePaym0: 10 symbols for type 0 of payment name\n
    :type NamePaym0: str\n
    :param NamePaym1: 10 symbols for type 1 of payment name\n
    :type NamePaym1: str\n
    :param NamePaym2: 10 symbols for type 2 of payment name\n
    :type NamePaym2: str\n
    :param NamePaym3: 10 symbols for type 3 of payment name\n
    :type NamePaym3: str\n
    :param NamePaym4: 10 symbols for type 4 of payment name\n
    :type NamePaym4: str\n
    :param NamePaym5: 10 symbols for type 5 of payment name\n
    :type NamePaym5: str\n
    :param NamePaym6: 10 symbols for type 6 of payment name\n
    :type NamePaym6: str\n
    :param NamePaym7: 10 symbols for type 7 of payment name\n
    :type NamePaym7: str\n
    :param NamePaym8: 10 symbols for type 8 of payment name\n
    :type NamePaym8: str\n
    :param NamePaym9: 10 symbols for type 9 of payment name\n
    :type NamePaym9: str\n
    :param ExchangeRate: 10 symbols for exchange rate of payment type 9 in format: ####.#####\n
    :type ExchangeRate: float\n
    """
    def __init__(self, NamePaym0, NamePaym1, NamePaym2, NamePaym3, NamePaym4, NamePaym5, NamePaym6, NamePaym7, NamePaym8, NamePaym9, ExchangeRate):
        self.NamePaym0 = NamePaym0
        self.NamePaym1 = NamePaym1
        self.NamePaym2 = NamePaym2
        self.NamePaym3 = NamePaym3
        self.NamePaym4 = NamePaym4
        self.NamePaym5 = NamePaym5
        self.NamePaym6 = NamePaym6
        self.NamePaym7 = NamePaym7
        self.NamePaym8 = NamePaym8
        self.NamePaym9 = NamePaym9
        self.ExchangeRate = ExchangeRate


class __TCP_PasswordRes__:
    """
    :param PassLength: (Length) Up to 3 symbols for the password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the TCP password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __PLUbarcodeRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param Barcode: 13 symbols for article barcode\n
    :type Barcode: str\n
    """
    def __init__(self, PLUNum, Barcode):
        self.PLUNum = PLUNum
        self.Barcode = Barcode


class __ServerPasswordECRSRes__:
    """
    :param ParamLength: Up to 2 symbols for parameter length\n
    :type ParamLength: float\n
    :param ServerPassword: Up to 64 symbols for server password\n
    :type ServerPassword: str\n
    """
    def __init__(self, ParamLength, ServerPassword):
        self.ParamLength = ParamLength
        self.ServerPassword = ServerPassword


class __DailyGeneralRegistersByOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param CustomersNum: Up to 5 symbols for number of customers\n
    :type CustomersNum: float\n
    :param DiscountsNum: Up to 5 symbols for number of discounts\n
    :type DiscountsNum: float\n
    :param DiscountsAmount: Up to 11 symbols for accumulated amount of discounts\n
    :type DiscountsAmount: float\n
    :param AdditionsNum: Up to 5 symbols for number ofadditions\n
    :type AdditionsNum: float\n
    :param AdditionsAmount: Up to 11 symbols for accumulated amount of additions\n
    :type AdditionsAmount: float\n
    :param CorrectionsNum: Up to 5 symbols for number of corrections\n
    :type CorrectionsNum: float\n
    :param CorrectionsAmount: Up to 11 symbols for accumulated amount of corrections\n
    :type CorrectionsAmount: float\n
    """
    def __init__(self, OperNum, CustomersNum, DiscountsNum, DiscountsAmount, AdditionsNum, AdditionsAmount, CorrectionsNum, CorrectionsAmount):
        self.OperNum = OperNum
        self.CustomersNum = CustomersNum
        self.DiscountsNum = DiscountsNum
        self.DiscountsAmount = DiscountsAmount
        self.AdditionsNum = AdditionsNum
        self.AdditionsAmount = AdditionsAmount
        self.CorrectionsNum = CorrectionsNum
        self.CorrectionsAmount = CorrectionsAmount


class __GPRS_PasswordRes__:
    """
    :param PassLength: (Length) Up to 3 symbols for the GPRS password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the device's GPRS password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __FooterRes__:
    """
    :param OptionFooterLine: (Line Number)1 symbol with value: 
     - '1' - Footer 1 
     - '2' - Footer 2 
     - '3' - Footer 3\n
    :type OptionFooterLine: Enums.OptionFooterLine\n
    :param FooterText: LineLength symbols for footer line\n
    :type FooterText: str\n
    """
    def __init__(self, OptionFooterLine, FooterText):
        self.OptionFooterLine = OptionFooterLine
        self.FooterText = FooterText


class __DailyRARes__:
    """
    :param AmountPayment0: Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment0: float\n
    :param AmountPayment1: Up to 11 symbols for the accumulated amount by payment type 1\n
    :type AmountPayment1: float\n
    :param AmountPayment2: Up to 11 symbols for the accumulated amount by payment type 2\n
    :type AmountPayment2: float\n
    :param AmountPayment3: Up to 11 symbols for the accumulated amount by payment type 3\n
    :type AmountPayment3: float\n
    :param AmountPayment4: Up to 11 symbols for the accumulated amount by payment type 4\n
    :type AmountPayment4: float\n
    :param AmountPayment5: Up to 11 symbols for the accumulated amount by payment type 5\n
    :type AmountPayment5: float\n
    :param AmountPayment6: Up to 11 symbols for the accumulated amount by payment type 6\n
    :type AmountPayment6: float\n
    :param AmountPayment7: Up to 11 symbols for the accumulated amount by payment type 7\n
    :type AmountPayment7: float\n
    :param AmountPayment8: Up to 11 symbols for the accumulated amount by payment type 8\n
    :type AmountPayment8: float\n
    :param AmountPayment9: Up to 11 symbols for the accumulated amount by payment type 9\n
    :type AmountPayment9: float\n
    :param NumRA: Up to 5 symbols for the total number of operations\n
    :type NumRA: float\n
    """
    def __init__(self, AmountPayment0, AmountPayment1, AmountPayment2, AmountPayment3, AmountPayment4, AmountPayment5, AmountPayment6, AmountPayment7, AmountPayment8, AmountPayment9, NumRA):
        self.AmountPayment0 = AmountPayment0
        self.AmountPayment1 = AmountPayment1
        self.AmountPayment2 = AmountPayment2
        self.AmountPayment3 = AmountPayment3
        self.AmountPayment4 = AmountPayment4
        self.AmountPayment5 = AmountPayment5
        self.AmountPayment6 = AmountPayment6
        self.AmountPayment7 = AmountPayment7
        self.AmountPayment8 = AmountPayment8
        self.AmountPayment9 = AmountPayment9
        self.NumRA = NumRA


class __GeneralDailyRegistersRes__:
    """
    :param CustomersNum: Up to 5 symbols for number of customers\n
    :type CustomersNum: float\n
    :param DiscountsNum: Up to 5 symbols for number of discounts\n
    :type DiscountsNum: float\n
    :param DiscountsAmount: Up to 11 symbols for accumulated amount of discounts\n
    :type DiscountsAmount: float\n
    :param AdditionsNum: Up to 5 symbols for number of additions\n
    :type AdditionsNum: float\n
    :param AdditionsAmount: Up to 11 symbols for accumulated amount of additions\n
    :type AdditionsAmount: float\n
    :param CorrectionsNum: Up to 5 symbols for number of corrections\n
    :type CorrectionsNum: float\n
    :param CorrectionsAmount: Up to 11 symbols for accumulated amount of corrections\n
    :type CorrectionsAmount: float\n
    """
    def __init__(self, CustomersNum, DiscountsNum, DiscountsAmount, AdditionsNum, AdditionsAmount, CorrectionsNum, CorrectionsAmount):
        self.CustomersNum = CustomersNum
        self.DiscountsNum = DiscountsNum
        self.DiscountsAmount = DiscountsAmount
        self.AdditionsNum = AdditionsNum
        self.AdditionsAmount = AdditionsAmount
        self.CorrectionsNum = CorrectionsNum
        self.CorrectionsAmount = CorrectionsAmount


class __DeviceModuleSupportRes__:
    """
    :param OptionLAN: 1 symbol for LAN support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionLAN: Enums.OptionLAN\n
    :param OptionWiFi: 1 symbol for WiFi support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionWiFi: Enums.OptionWiFi\n
    :param OptionGPRS: 1 symbol for GPRS support 
     - '0' - No 
     - '1' - Yes 
    BT (Bluetooth) 1 symbol for Bluetooth support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionGPRS: Enums.OptionGPRS\n
    :param OptionBT: (Bluetooth) 1 symbol for Bluetooth support 
     - '0' - No 
     - '1' - Yes\n
    :type OptionBT: Enums.OptionBT\n
    """
    def __init__(self, OptionLAN, OptionWiFi, OptionGPRS, OptionBT):
        self.OptionLAN = OptionLAN
        self.OptionWiFi = OptionWiFi
        self.OptionGPRS = OptionGPRS
        self.OptionBT = OptionBT


class __WiFi_NetworkNameRes__:
    """
    :param WiFiNameLength: (Length) Up to 3 symbols for the WiFi name length\n
    :type WiFiNameLength: float\n
    :param WiFiNetworkName: (Name) Up to 100 symbols for the device's WiFi network name\n
    :type WiFiNetworkName: str\n
    """
    def __init__(self, WiFiNameLength, WiFiNetworkName):
        self.WiFiNameLength = WiFiNameLength
        self.WiFiNetworkName = WiFiNetworkName


class __ParametersRes__:
    """
    :param POSNum: (POS No) 4 symbols for number of POS in format ####\n
    :type POSNum: float\n
    :param OptionPrintLogo: (Print Logo) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionPrintLogo: Enums.OptionPrintLogo\n
    :param OptionAutoOpenDrawer: (Auto Open Drawer) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionAutoOpenDrawer: Enums.OptionAutoOpenDrawer\n
    :param OptionAutoCut: (Auto Cut) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionAutoCut: Enums.OptionAutoCut\n
    :param OptionExternalDispManagement: (External Display Management) 1 symbol of value: 
     - '1' - Manual 
     - '0' - Auto\n
    :type OptionExternalDispManagement: Enums.OptionExternalDispManagement\n
    :param OptionEnableCurrency: (Enable Currency) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionEnableCurrency: Enums.OptionEnableCurrency\n
    :param OptionUSBHost: (USB in host mode)1 symbol with value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionUSBHost: Enums.OptionUSBHost\n
    """
    def __init__(self, POSNum, OptionPrintLogo, OptionAutoOpenDrawer, OptionAutoCut, OptionExternalDispManagement, OptionEnableCurrency, OptionUSBHost):
        self.POSNum = POSNum
        self.OptionPrintLogo = OptionPrintLogo
        self.OptionAutoOpenDrawer = OptionAutoOpenDrawer
        self.OptionAutoCut = OptionAutoCut
        self.OptionExternalDispManagement = OptionExternalDispManagement
        self.OptionEnableCurrency = OptionEnableCurrency
        self.OptionUSBHost = OptionUSBHost


class __DailyReturnedChangeAmountsByOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param ChangeAmountPayment0: Up to 11 symbols for amounts received by type of payment 0\n
    :type ChangeAmountPayment0: float\n
    :param ChangeAmountPayment1: Up to 11 symbols for amounts received by type of payment 1\n
    :type ChangeAmountPayment1: float\n
    :param ChangeAmountPayment2: Up to 11 symbols for amounts received by type of payment 2\n
    :type ChangeAmountPayment2: float\n
    :param ChangeAmountPayment3: Up to 11 symbols for amounts received by type of payment 3\n
    :type ChangeAmountPayment3: float\n
    :param ChangeAmountPayment4: Up to 11 symbols for amounts received by type of payment 4\n
    :type ChangeAmountPayment4: float\n
    :param ChangeAmountPayment5: Up to 11 symbols for amounts received by type of payment 5\n
    :type ChangeAmountPayment5: float\n
    :param ChangeAmountPayment6: Up to 11 symbols for amounts received by type of payment 6\n
    :type ChangeAmountPayment6: float\n
    :param ChangeAmountPayment7: Up to 11 symbols for amounts received by type of payment 7\n
    :type ChangeAmountPayment7: float\n
    :param ChangeAmountPayment8: Up to 11 symbols for amounts received by type of payment 8\n
    :type ChangeAmountPayment8: float\n
    :param ChangeAmountPayment9: Up to 11 symbols for amounts received by type of payment 9\n
    :type ChangeAmountPayment9: float\n
    """
    def __init__(self, OperNum, ChangeAmountPayment0, ChangeAmountPayment1, ChangeAmountPayment2, ChangeAmountPayment3, ChangeAmountPayment4, ChangeAmountPayment5, ChangeAmountPayment6, ChangeAmountPayment7, ChangeAmountPayment8, ChangeAmountPayment9):
        self.OperNum = OperNum
        self.ChangeAmountPayment0 = ChangeAmountPayment0
        self.ChangeAmountPayment1 = ChangeAmountPayment1
        self.ChangeAmountPayment2 = ChangeAmountPayment2
        self.ChangeAmountPayment3 = ChangeAmountPayment3
        self.ChangeAmountPayment4 = ChangeAmountPayment4
        self.ChangeAmountPayment5 = ChangeAmountPayment5
        self.ChangeAmountPayment6 = ChangeAmountPayment6
        self.ChangeAmountPayment7 = ChangeAmountPayment7
        self.ChangeAmountPayment8 = ChangeAmountPayment8
        self.ChangeAmountPayment9 = ChangeAmountPayment9


class __DailyPORes__:
    """
    :param AmountPayment0: Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment0: float\n
    :param AmountPayment1: Up to 11 symbols for the accumulated amount by payment type 1\n
    :type AmountPayment1: float\n
    :param AmountPayment2: Up to 11 symbols for the accumulated amount by payment type 2\n
    :type AmountPayment2: float\n
    :param AmountPayment3: Up to 11 symbols for the accumulated amount by payment type 3\n
    :type AmountPayment3: float\n
    :param AmountPayment4: Up to 11 symbols for the accumulated amount by payment type 4\n
    :type AmountPayment4: float\n
    :param AmountPayment5: Up to 11 symbols for the accumulated amount by payment type 5\n
    :type AmountPayment5: float\n
    :param AmountPayment6: Up to 11 symbols for the accumulated amount by payment type 6\n
    :type AmountPayment6: float\n
    :param AmountPayment7: Up to 11 symbols for the accumulated amount by payment type 7\n
    :type AmountPayment7: float\n
    :param AmountPayment8: Up to 11 symbols for the accumulated amount by payment type 8\n
    :type AmountPayment8: float\n
    :param AmountPayment9: Up to 11 symbols for the accumulated amount by payment type 9\n
    :type AmountPayment9: float\n
    :param NumPO: Up to 5 symbols for the total number of operations\n
    :type NumPO: float\n
    """
    def __init__(self, AmountPayment0, AmountPayment1, AmountPayment2, AmountPayment3, AmountPayment4, AmountPayment5, AmountPayment6, AmountPayment7, AmountPayment8, AmountPayment9, NumPO):
        self.AmountPayment0 = AmountPayment0
        self.AmountPayment1 = AmountPayment1
        self.AmountPayment2 = AmountPayment2
        self.AmountPayment3 = AmountPayment3
        self.AmountPayment4 = AmountPayment4
        self.AmountPayment5 = AmountPayment5
        self.AmountPayment6 = AmountPayment6
        self.AmountPayment7 = AmountPayment7
        self.AmountPayment8 = AmountPayment8
        self.AmountPayment9 = AmountPayment9
        self.NumPO = NumPO


class __AlteTaxeRes__:
    """
    :param Number: 1 symbol for number in order\n
    :type Number: str\n
    :param Name: 12 symbols for Alte taxe name\n
    :type Name: str\n
    """
    def __init__(self, Number, Name):
        self.Number = Number
        self.Name = Name


class Enums:
    """Enumerations"""

    class OptionZeroing(Enum):
        Not_zeroing = u'X'
        Zeroing = u'Z'

    class OptionDecimalPointPosition(Enum):
        Fractions = u'2'
        Whole_numbers = u'0'

    class OptionPrintLogo(Enum):
        No = u'0'
        Yes = u'1'

    class OptionAutoOpenDrawer(Enum):
        No = u'0'
        Yes = u'1'

    class OptionAutoCut(Enum):
        No = u'0'
        Yes = u'1'

    class OptionExternalDispManagement(Enum):
        Auto = u'0'
        Manual = u'1'

    class OptionEnableCurrency(Enum):
        No = u'0'
        Yes = u'1'

    class OptionUSBHost(Enum):
        No = u'0'
        Yes = u'1'

    class OptionVATClass(Enum):
        Alte_taxe = u'F'
        VAT_Class_A = u'A'
        VAT_Class_B = u'B'
        VAT_Class_C = u'C'
        VAT_Class_D = u'D'
        VAT_Class_E = u'E'

    class OptionDepPrice(Enum):
        Free_price_disabled = u'0'
        Free_price_disabled_for_single_transaction = u'4'
        Free_price_enabled = u'1'
        Free_price_enabled_for_single_transaction = u'5'
        Limited_price = u'2'
        Limited_price_for_single_transaction = u'6'

    class OptionPrice(Enum):
        Free_price_is_disable_valid_only_programmed_price = u'0'
        Free_price_is_enable = u'1'
        Limited_price = u'2'

    class OptionTransaction(Enum):
        Active_Single_transaction_in_receipt = u'1'
        Inactive_default_value = u'0'

    class OptionTypeVATregistration(Enum):
        No = u'0'
        Yes = u'1'

    class OptionReportStorage(Enum):
        Printing = u'J1'
        Storage_in_External_SD_card_memory = u'J4'
        Storage_in_External_USB_Flash_memory = u'J2'

    class OptionType(Enum):
        Defined_from_the_device = u'2'
        Over_subtotal = u'1'
        Over_transaction_sum = u'0'

    class OptionDisplay(Enum):
        No = u'0'
        Yes = u'1'

    class OptionCommunicationModule(Enum):
        GSM = u'0'
        LAN = u'1'

    class OptionSign(Enum):
        Correction = u'-'
        Sale = u'+'

    class OptionPaymentType(Enum):
        Payment_0 = u'0'
        Payment_1 = u'1'
        Payment_2 = u'2'
        Payment_3 = u'3'
        Payment_4 = u'4'
        Payment_5 = u'5'
        Payment_6 = u'6'
        Payment_7 = u'7'
        Payment_8 = u'8'
        Payment_9 = u'9'

    class OptionStorage(Enum):
        Storage_in_External_SD_card_memory = u'4'
        Storage_in_External_USB_Flash_memory = u'2'

    class OptionQuantityType(Enum):
        Availability_of_PLU_stock_is_not_monitored = u'0'
        Disable_negative_quantity = u'1'
        Enable_negative_quantity = u'2'

    class OptionCustomerReceiptPrintType(Enum):
        Buffered_printing = u'5'
        Postponed_printing = u'3'
        Step_by_step_printing = u'1'

    class OptionCurrencySaleRcpPrintType(Enum):
        Postponed_printing = u'2'
        Step_by_step_printing = u'0'

    class OptionDhcpStatus(Enum):
        Disabled = u'0'
        Enabled = u'1'

    class OptionAddressType(Enum):
        DNS_address = u'5'
        Gateway_address = u'4'
        IP_address = u'2'
        Subnet_Mask = u'3'

    class OptionProfileType(Enum):
        Profile_0 = u'0'
        Profile_1 = u'1'

    class OptionHeaderLine(Enum):
        Header_1 = u'1'
        Header_2 = u'2'
        Header_3 = u'3'
        Header_4 = u'4'
        Header_5 = u'5'
        Header_6 = u'6'
        Header_7 = u'7'
        Header_8 = u'8'

    class OptionTCPAutoStart(Enum):
        No = u'0'
        Yes = u'1'

    class OptionUsedModule(Enum):
        LAN = u'1'
        WiFi = u'2'

    class OptionPrinting(Enum):
        No = u'0'
        Yes = u'1'

    class OptionCodeType(Enum):
        CODABAR = u'6'
        CODE_128 = u'I'
        CODE_39 = u'4'
        CODE_93 = u'H'
        EAN_13 = u'2'
        EAN_8 = u'3'
        ITF = u'5'
        UPC_A = u'0'
        UPC_E = u'1'

    class OptionStorageReport(Enum):
        To_PC = u'j0'
        To_SD_card = u'j4'
        To_USB_Flash_Drive = u'j2'

    class OptionLAN(Enum):
        No = u'0'
        Yes = u'1'

    class OptionWiFi(Enum):
        No = u'0'
        Yes = u'1'

    class OptionGPRS(Enum):
        No = u'0'
        Yes = u'1'

    class OptionBT(Enum):
        No = u'0'
        Yes = u'1'

    class OptionSingleTransaction(Enum):
        Active_Single_transaction_in_receipt = u'1'
        Inactive_default_value = u'0'

    class OptionIsReceiptOpened(Enum):
        No = u'0'
        Yes = u'1'

    class OptionForbiddenVoid(Enum):
        allowed = u'0'
        forbidden = u'1'

    class OptionVATinReceipt(Enum):
        with_printing = u'0'
        without_printing = u'1'

    class OptionReceiptFormat(Enum):
        Brief = u'0'
        Detailed = u'1'

    class OptionInitiatedPayment(Enum):
        initiated_payment = u'0'
        not_initiated_payment = u'1'

    class OptionFinalizedPayment(Enum):
        finalized_payment = u'0'
        not_finalized_payment = u'1'

    class OptionPowerDownInReceipt(Enum):
        No = u'0'
        Yes = u'1'

    class OptionClientReceipt(Enum):
        invoice_client_receipt = u'1'
        standard_receipt = u'0'

    class OptionChangeType(Enum):
        Change_In_Cash = u'0'
        Change_In_Currency = u'2'
        Same_As_The_payment = u'1'

    class OptionSendAfterZ(Enum):
        No = u'0'
        Yes = u'1'

    class OptionFiscalReceiptPrintType(Enum):
        Buffered_Printing = u'4'
        Postponed_printing = u'2'
        Step_by_step_printing = u'0'

    class OptionPaymentNum(Enum):
        Payment_1 = u'1'
        Payment_2 = u'2'
        Payment_3 = u'3'
        Payment_4 = u'4'
        Payment_5 = u'5'
        Payment_6 = u'6'
        Payment_7 = u'7'
        Payment_8 = u'8'
        Payment_9 = u'9'

    class OptionFooterLine(Enum):
        Footer_1 = u'1'
        Footer_2 = u'2'
        Footer_3 = u'3'

    class OptionBTstatus(Enum):
        Disabled = u'0'
        Enabled = u'1'

    class OptionCurrencyBuyingRcpPrintType(Enum):
        Postponed_printing = u':'
        Step_by_step_printing = u'8'

    class OptionNonFiscalPrintType(Enum):
        Postponed_printing = u'1'
        Step_by_step_printing = u'0'

    class OptionRecieptXmlStorage(Enum):
        Storage_in_External_SD_card_memory = u'JX'
        Storage_in_External_USB_Flash_memory = u'Jx'


