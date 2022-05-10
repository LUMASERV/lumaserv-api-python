import requests


class BillingClient:
    def __init__(self, api_key, base_url="https://billing.lumaserv.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + . api_key,
            'Content-Type': 'application/json'
        })

    def request(self, method, path, params={}, body={}):
        r = self.session.request(method, self.base_url + path, data=data, params=params)
        f(r.status_code < 200 or (r.status_code >= 300 and r.status_code < 400):
            raise Exception("Status code is " + r.status_code + "!")
        return r.json()

    def getInvoiceFile(self, id, queryParams={}):
        return self.request("GET", "/invoices/{id}/file".format(id=id), queryParams);


    def createInvoicePosition(self, id, body, queryParams={}):
        return self.request("POST", "/invoices/{id}/positions".format(id=id), queryParams, body);


    def getInvoicePositions(self, id, queryParams={}):
        return self.request("GET", "/invoices/{id}/positions".format(id=id), queryParams);


    def getBillingPosition(self, id, queryParams={}):
        return self.request("GET", "/billing-positions/{id}".format(id=id), queryParams);


    def deleteBillingPosition(self, id, queryParams={}):
        return self.request("DELETE", "/billing-positions/{id}".format(id=id), queryParams);


    def updateBillingPosition(self, id, body, queryParams={}):
        return self.request("PUT", "/billing-positions/{id}".format(id=id), queryParams, body);


    def createBillingPosition(self, body, queryParams={}):
        return self.request("POST", "/billing-positions".format(), queryParams, body);


    def getBillingPositions(self, queryParams={}):
        return self.request("GET", "/billing-positions".format(), queryParams);


    def createCustomer(self, body, queryParams={}):
        return self.request("POST", "/customers".format(), queryParams, body);


    def getCustomers(self, queryParams={}):
        return self.request("GET", "/customers".format(), queryParams);


    def getDebits(self, queryParams={}):
        return self.request("GET", "/debits".format(), queryParams);


    def getCustomer(self, id, queryParams={}):
        return self.request("GET", "/customers/{id}".format(id=id), queryParams);


    def updateCustomer(self, id, body, queryParams={}):
        return self.request("PUT", "/customers/{id}".format(id=id), queryParams, body);


    def getOnlinePayments(self, queryParams={}):
        return self.request("GET", "/online-payments".format(), queryParams);


    def getServiceContractPosition(self, contract_id, id, queryParams={}):
        return self.request("GET", "/service-contracts/{contract_id}/positions/{id}".format(contract_id=contract_id, id=id), queryParams);


    def deleteServiceContractPosition(self, contract_id, id, queryParams={}):
        return self.request("DELETE", "/service-contracts/{contract_id}/positions/{id}".format(contract_id=contract_id, id=id), queryParams);


    def updateServiceContractPosition(self, contract_id, id, body, queryParams={}):
        return self.request("PUT", "/service-contracts/{contract_id}/positions/{id}".format(contract_id=contract_id, id=id), queryParams, body);


    def createInvoice(self, body, queryParams={}):
        return self.request("POST", "/invoices".format(), queryParams, body);


    def getInvoices(self, queryParams={}):
        return self.request("GET", "/invoices".format(), queryParams);


    def createServiceContractPosition(self, contract_id, body, queryParams={}):
        return self.request("POST", "/service-contracts/{contract_id}/positions".format(contract_id=contract_id), queryParams, body);


    def getServiceContractPositions(self, contract_id, queryParams={}):
        return self.request("GET", "/service-contracts/{contract_id}/positions".format(contract_id=contract_id), queryParams);


    def getOfferPosition(self, id, queryParams={}):
        return self.request("GET", "/offer-positions/{id}".format(id=id), queryParams);


    def deleteOfferPosition(self, id, queryParams={}):
        return self.request("DELETE", "/offer-positions/{id}".format(id=id), queryParams);


    def updateOfferPosition(self, id, body, queryParams={}):
        return self.request("PUT", "/offer-positions/{id}".format(id=id), queryParams, body);


    def getPaymentReminder(self, id, queryParams={}):
        return self.request("GET", "/payment-reminders/{id}".format(id=id), queryParams);


    def updatePaymentReminder(self, id, body, queryParams={}):
        return self.request("PUT", "/payment-reminders/{id}".format(id=id), queryParams, body);


    def createDebitMandate(self, body, queryParams={}):
        return self.request("POST", "/debit-mandates".format(), queryParams, body);


    def getDebitMandates(self, queryParams={}):
        return self.request("GET", "/debit-mandates".format(), queryParams);


    def getBankTransactions(self, queryParams={}):
        return self.request("GET", "/bank-transactions".format(), queryParams);


    def getDebitMandate(self, id, queryParams={}):
        return self.request("GET", "/debit-mandates/{id}".format(id=id), queryParams);


    def getBankTransaction(self, id, queryParams={}):
        return self.request("GET", "/bank-transactions/{id}".format(id=id), queryParams);


    def getOffer(self, id, queryParams={}):
        return self.request("GET", "/offers/{id}".format(id=id), queryParams);


    def updateOffer(self, id, body, queryParams={}):
        return self.request("PUT", "/offers/{id}".format(id=id), queryParams, body);


    def getInvoicePosition(self, invoice_id, id, queryParams={}):
        return self.request("GET", "/invoices/{invoice_id}/positions/{id}".format(invoice_id=invoice_id, id=id), queryParams);


    def deleteInvoicePosition(self, invoice_id, id, queryParams={}):
        return self.request("DELETE", "/invoices/{invoice_id}/positions/{id}".format(invoice_id=invoice_id, id=id), queryParams);


    def updateInvoicePosition(self, invoice_id, id, body, queryParams={}):
        return self.request("PUT", "/invoices/{invoice_id}/positions/{id}".format(invoice_id=invoice_id, id=id), queryParams, body);


    def createServiceContract(self, body, queryParams={}):
        return self.request("POST", "/service-contracts".format(), queryParams, body);


    def getServiceContracts(self, queryParams={}):
        return self.request("GET", "/service-contracts".format(), queryParams);


    def getInvoice(self, id, queryParams={}):
        return self.request("GET", "/invoices/{id}".format(id=id), queryParams);


    def deleteInvoice(self, id, queryParams={}):
        return self.request("DELETE", "/invoices/{id}".format(id=id), queryParams);


    def updateInvoice(self, id, body, queryParams={}):
        return self.request("PUT", "/invoices/{id}".format(id=id), queryParams, body);


    def getOnlinePayment(self, id, queryParams={}):
        return self.request("GET", "/online-payments/{id}".format(id=id), queryParams);


    def getDebit(self, id, queryParams={}):
        return self.request("GET", "/debits/{id}".format(id=id), queryParams);


    def createOffer(self, body, queryParams={}):
        return self.request("POST", "/offers".format(), queryParams, body);


    def getOffers(self, queryParams={}):
        return self.request("GET", "/offers".format(), queryParams);


    def getServiceContract(self, id, queryParams={}):
        return self.request("GET", "/service-contracts/{id}".format(id=id), queryParams);


    def deleteServiceContract(self, id, queryParams={}):
        return self.request("DELETE", "/service-contracts/{id}".format(id=id), queryParams);


    def updateServiceContract(self, id, body, queryParams={}):
        return self.request("PUT", "/service-contracts/{id}".format(id=id), queryParams, body);


    def createOfferPosition(self, body, queryParams={}):
        return self.request("POST", "/offer-positions".format(), queryParams, body);


    def getOfferPositions(self, queryParams={}):
        return self.request("GET", "/offer-positions".format(), queryParams);


    def createPaymentReminder(self, body, queryParams={}):
        return self.request("POST", "/payment-reminders".format(), queryParams, body);


    def getPaymentReminders(self, queryParams={}):
        return self.request("GET", "/payment-reminders".format(), queryParams);


