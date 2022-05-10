import requests


class CoreClient:
    def __init__(self, api_key, base_url="https://api.lumaserv.com"):
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

    def createSSHKey(self, body, queryParams={}):
        return self.request("POST", "/ssh-keys".format(), queryParams, body);


    def getSSHKeys(self, queryParams={}):
        return self.request("GET", "/ssh-keys".format(), queryParams);


    def createServerPriceRange(self, body, queryParams={}):
        return self.request("POST", "/server-price-ranges".format(), queryParams, body);


    def getServerPriceRanges(self, queryParams={}):
        return self.request("GET", "/server-price-ranges".format(), queryParams);


    def startServer(self, id, queryParams={}):
        return self.request("POST", "/servers/{id}/start".format(id=id), queryParams);


    def createAvailabilityZone(self, body, queryParams={}):
        return self.request("POST", "/availability-zones".format(), queryParams, body);


    def getAvailabilityZones(self, queryParams={}):
        return self.request("GET", "/availability-zones".format(), queryParams);


    def getServerTemplate(self, id, queryParams={}):
        return self.request("GET", "/server-templates/{id}".format(id=id), queryParams);


    def shutdownServer(self, id, queryParams={}):
        return self.request("POST", "/servers/{id}/shutdown".format(id=id), queryParams);


    def getServerFirewall(self, id, queryParams={}):
        return self.request("GET", "/server-firewalls/{id}".format(id=id), queryParams);


    def deleteServerFirewall(self, id, queryParams={}):
        return self.request("DELETE", "/server-firewalls/{id}".format(id=id), queryParams);


    def getServer(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}".format(id=id), queryParams);


    def deleteServer(self, id, queryParams={}):
        return self.request("DELETE", "/servers/{id}".format(id=id), queryParams);


    def updateServer(self, id, body, queryParams={}):
        return self.request("PUT", "/servers/{id}".format(id=id), queryParams, body);


    def getServerStorageClass(self, id, queryParams={}):
        return self.request("GET", "/server-storage-classes/{id}".format(id=id), queryParams);


    def restartServer(self, id, queryParams={}):
        return self.request("POST", "/servers/{id}/restart".format(id=id), queryParams);


    def restoreServer(self, id, body, queryParams={}):
        return self.request("POST", "/servers/{id}/restore".format(id=id), queryParams, body);


    def getSSLOrganisation(self, id, queryParams={}):
        return self.request("GET", "/ssl/organisations/{id}".format(id=id), queryParams);


    def deleteSSLOrganisation(self, id, queryParams={}):
        return self.request("DELETE", "/ssl/organisations/{id}".format(id=id), queryParams);


    def getServerAction(self, id, action_id, queryParams={}):
        return self.request("GET", "/servers/{id}/actions/{action_id}".format(id=id, action_id=action_id), queryParams);


    def getServerGraph(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}/graph".format(id=id), queryParams);


    def getSSLContact(self, id, queryParams={}):
        return self.request("GET", "/ssl/contacts/{id}".format(id=id), queryParams);


    def deleteSSLContact(self, id, queryParams={}):
        return self.request("DELETE", "/ssl/contacts/{id}".format(id=id), queryParams);


    def getDNSZones(self, queryParams={}):
        return self.request("GET", "/dns/zones".format(), queryParams);


    def recreateServer(self, id, queryParams={}):
        return self.request("POST", "/servers/{id}/recreate".format(id=id), queryParams);


    def createServerFirewall(self, body, queryParams={}):
        return self.request("POST", "/server-firewalls".format(), queryParams, body);


    def getServerFirewalls(self, queryParams={}):
        return self.request("GET", "/server-firewalls".format(), queryParams);


    def getServerFirewallRule(self, id, rule_id, queryParams={}):
        return self.request("GET", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), queryParams);


    def deleteServerFirewallRule(self, id, rule_id, queryParams={}):
        return self.request("DELETE", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), queryParams);


    def sendDomainVerification(self, name, queryParams={}):
        return self.request("POST", "/domains/{name}/verification".format(name=name), queryParams);


    def checkDomainVerification(self, name, queryParams={}):
        return self.request("GET", "/domains/{name}/verification".format(name=name), queryParams);


    def createServerHost(self, body, queryParams={}):
        return self.request("POST", "/server-hosts".format(), queryParams, body);


    def getServerHosts(self, queryParams={}):
        return self.request("GET", "/server-hosts".format(), queryParams);


    def createServer(self, body, queryParams={}):
        return self.request("POST", "/servers".format(), queryParams, body);


    def getServers(self, queryParams={}):
        return self.request("GET", "/servers".format(), queryParams);


    def deleteServerNetwork(self, id, network_id, queryParams={}):
        return self.request("DELETE", "/servers/{id}/networks/{network_id}".format(id=id, network_id=network_id), queryParams);


    def checkDomain(self, name, queryParams={}):
        return self.request("GET", "/domains/{name}/check".format(name=name), queryParams);


    def getDomain(self, name, queryParams={}):
        return self.request("GET", "/domains/{name}".format(name=name), queryParams);


    def deleteDomain(self, name, queryParams={}):
        return self.request("DELETE", "/domains/{name}".format(name=name), queryParams);


    def updateDomain(self, name, body, queryParams={}):
        return self.request("PUT", "/domains/{name}".format(name=name), queryParams, body);


    def getDomainHandle(self, code, queryParams={}):
        return self.request("GET", "/domain-handles/{code}".format(code=code), queryParams);


    def deleteDomainHandle(self, code, queryParams={}):
        return self.request("DELETE", "/domain-handles/{code}".format(code=code), queryParams);


    def updateDomainHandle(self, code, body, queryParams={}):
        return self.request("PUT", "/domain-handles/{code}".format(code=code), queryParams, body);


    def getAvailabilityZone(self, id, queryParams={}):
        return self.request("GET", "/availability-zones/{id}".format(id=id), queryParams);


    def updateAvailabilityZone(self, id, body, queryParams={}):
        return self.request("PUT", "/availability-zones/{id}".format(id=id), queryParams, body);


    def createServerBackup(self, body, queryParams={}):
        return self.request("POST", "/server-backups".format(), queryParams, body);


    def getServerBackups(self, queryParams={}):
        return self.request("GET", "/server-backups".format(), queryParams);


    def createSubnet(self, body, queryParams={}):
        return self.request("POST", "/subnets".format(), queryParams, body);


    def getSubnets(self, queryParams={}):
        return self.request("GET", "/subnets".format(), queryParams);


    def createServerVolume(self, body, queryParams={}):
        return self.request("POST", "/server-volumes".format(), queryParams, body);


    def getServerVolumes(self, queryParams={}):
        return self.request("GET", "/server-volumes".format(), queryParams);


    def getPleskLicenseType(self, id, queryParams={}):
        return self.request("GET", "/licenses/plesk-types/{id}".format(id=id), queryParams);


    def createServerStorageClass(self, body, queryParams={}):
        return self.request("POST", "/server-storage-classes".format(), queryParams, body);


    def getServerStorageClasses(self, queryParams={}):
        return self.request("GET", "/server-storage-classes".format(), queryParams);


    def getServerFirewallMember(self, id, member_id, queryParams={}):
        return self.request("GET", "/server-firewalls/{id}/members/{member_id}".format(id=id, member_id=member_id), queryParams);


    def deleteServerFirewallMember(self, id, member_id, queryParams={}):
        return self.request("DELETE", "/server-firewalls/{id}/members/{member_id}".format(id=id, member_id=member_id), queryParams);


    def search(self, queryParams={}):
        return self.request("GET", "/search".format(), queryParams);


    def getScheduledServerAction(self, id, action_id, queryParams={}):
        return self.request("GET", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), queryParams);


    def deleteScheduledServerAction(self, id, action_id, queryParams={}):
        return self.request("DELETE", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), queryParams);


    def createS3Bucket(self, body, queryParams={}):
        return self.request("POST", "/storage/s3/buckets".format(), queryParams, body);


    def getS3Buckets(self, queryParams={}):
        return self.request("GET", "/storage/s3/buckets".format(), queryParams);


    def getPleskLicenseTypes(self, queryParams={}):
        return self.request("GET", "/licenses/plesk-types".format(), queryParams);


    def getServerActions(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}/actions".format(id=id), queryParams);


    def getServerStatus(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}/status".format(id=id), queryParams);


    def createServerFirewallMember(self, id, body, queryParams={}):
        return self.request("POST", "/server-firewalls/{id}/members".format(id=id), queryParams, body);


    def getServerFirewallMembers(self, id, queryParams={}):
        return self.request("GET", "/server-firewalls/{id}/members".format(id=id), queryParams);


    def getServerPriceRange(self, id, queryParams={}):
        return self.request("GET", "/server-price-ranges/{id}".format(id=id), queryParams);


    def createSSLOrganisation(self, body, queryParams={}):
        return self.request("POST", "/ssl/organisations".format(), queryParams, body);


    def getSSLOrganisations(self, queryParams={}):
        return self.request("GET", "/ssl/organisations".format(), queryParams);


    def getSSLType(self, id, queryParams={}):
        return self.request("GET", "/ssl/types/{id}".format(id=id), queryParams);


    def getSSLTypes(self, queryParams={}):
        return self.request("GET", "/ssl/types".format(), queryParams);


    def getServerVariantPrice(self, id, variant_id, queryParams={}):
        return self.request("GET", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), queryParams);


    def deleteServerVariantPrice(self, id, variant_id, queryParams={}):
        return self.request("DELETE", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), queryParams);


    def updateServerVariantPrice(self, id, variant_id, body, queryParams={}):
        return self.request("PUT", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), queryParams, body);


    def deleteDNSRecord(self, name, id, queryParams={}):
        return self.request("DELETE", "/dns/zones/{name}/records/{id}".format(name=name, id=id), queryParams);


    def updateDNSRecord(self, name, id, body, queryParams={}):
        return self.request("PUT", "/dns/zones/{name}/records/{id}".format(name=name, id=id), queryParams, body);


    def getPleskLicense(self, id, queryParams={}):
        return self.request("GET", "/licenses/plesk/{id}".format(id=id), queryParams);


    def updatePleskLicense(self, id, body, queryParams={}):
        return self.request("PUT", "/licenses/plesk/{id}".format(id=id), queryParams, body);


    def createServerTemplate(self, body, queryParams={}):
        return self.request("POST", "/server-templates".format(), queryParams, body);


    def getServerTemplates(self, queryParams={}):
        return self.request("GET", "/server-templates".format(), queryParams);


    def getServerHost(self, id, queryParams={}):
        return self.request("GET", "/server-hosts/{id}".format(id=id), queryParams);


    def createServerFirewallRule(self, id, body, queryParams={}):
        return self.request("POST", "/server-firewalls/{id}/rules".format(id=id), queryParams, body);


    def getServerFirewallRules(self, id, queryParams={}):
        return self.request("GET", "/server-firewalls/{id}/rules".format(id=id), queryParams);


    def createScheduledServerAction(self, id, body, queryParams={}):
        return self.request("POST", "/servers/{id}/scheduled-actions".format(id=id), queryParams, body);


    def getScheduledServerActions(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}/scheduled-actions".format(id=id), queryParams);


    def unscheduleDomainDelete(self, name, queryParams={}):
        return self.request("POST", "/domains/{name}/unschedule-delete".format(name=name), queryParams);


    def stopServer(self, id, queryParams={}):
        return self.request("POST", "/servers/{id}/stop".format(id=id), queryParams);


    def createDNSZoneRecord(self, name, body, queryParams={}):
        return self.request("POST", "/dns/zones/{name}/records".format(name=name), queryParams, body);


    def getDNSZoneRecords(self, name, queryParams={}):
        return self.request("GET", "/dns/zones/{name}/records".format(name=name), queryParams);


    def updateDNSZoneRecords(self, name, body, queryParams={}):
        return self.request("PUT", "/dns/zones/{name}/records".format(name=name), queryParams, body);


    def getServerVolume(self, id, queryParams={}):
        return self.request("GET", "/server-volumes/{id}".format(id=id), queryParams);


    def deleteServerVolume(self, id, queryParams={}):
        return self.request("DELETE", "/server-volumes/{id}".format(id=id), queryParams);


    def updateServerVolume(self, id, body, queryParams={}):
        return self.request("PUT", "/server-volumes/{id}".format(id=id), queryParams, body);


    def createServerNetwork(self, id, body, queryParams={}):
        return self.request("POST", "/servers/{id}/networks".format(id=id), queryParams, body);


    def getServerNetworks(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}/networks".format(id=id), queryParams);


    def createServerVariant(self, body, queryParams={}):
        return self.request("POST", "/server-variants".format(), queryParams, body);


    def getServerVariants(self, queryParams={}):
        return self.request("GET", "/server-variants".format(), queryParams);


    def getServerStorage(self, id, queryParams={}):
        return self.request("GET", "/server-storages/{id}".format(id=id), queryParams);


    def getSSHKey(self, id, queryParams={}):
        return self.request("GET", "/ssh-keys/{id}".format(id=id), queryParams);


    def deleteSSHKey(self, id, queryParams={}):
        return self.request("DELETE", "/ssh-keys/{id}".format(id=id), queryParams);


    def createServerPriceRangeAssignment(self, body, queryParams={}):
        return self.request("POST", "/server-price-range-assignments".format(), queryParams, body);


    def getServerPriceRangeAssignments(self, queryParams={}):
        return self.request("GET", "/server-price-range-assignments".format(), queryParams);


    def getAddresses(self, queryParams={}):
        return self.request("GET", "/addresses".format(), queryParams);


    def getServerVariant(self, id, queryParams={}):
        return self.request("GET", "/server-variants/{id}".format(id=id), queryParams);


    def deleteServerVariant(self, id, queryParams={}):
        return self.request("DELETE", "/server-variants/{id}".format(id=id), queryParams);


    def deleteS3AccessKeyGrant(self, access_key_id, id, queryParams={}):
        return self.request("DELETE", "/storage/s3/access-keys/{access_key_id}/grants/{id}".format(access_key_id=access_key_id, id=id), queryParams);


    def createServerMedia(self, body, queryParams={}):
        return self.request("POST", "/server-medias".format(), queryParams, body);


    def getServerMedias(self, queryParams={}):
        return self.request("GET", "/server-medias".format(), queryParams);


    def getSubnet(self, id, queryParams={}):
        return self.request("GET", "/subnets/{id}".format(id=id), queryParams);


    def deleteSubnet(self, id, queryParams={}):
        return self.request("DELETE", "/subnets/{id}".format(id=id), queryParams);


    def attachServerVolume(self, id, body, queryParams={}):
        return self.request("POST", "/server-volumes/{id}/attach".format(id=id), queryParams, body);


    def createPleskLicense(self, body, queryParams={}):
        return self.request("POST", "/licenses/plesk".format(), queryParams, body);


    def getPleskLicenses(self, queryParams={}):
        return self.request("GET", "/licenses/plesk".format(), queryParams);


    def getS3AccessKey(self, id, queryParams={}):
        return self.request("GET", "/storage/s3/access-keys/{id}".format(id=id), queryParams);


    def deleteS3AccessKey(self, id, queryParams={}):
        return self.request("DELETE", "/storage/s3/access-keys/{id}".format(id=id), queryParams);


    def createS3AccessKey(self, body, queryParams={}):
        return self.request("POST", "/storage/s3/access-keys".format(), queryParams, body);


    def getS3AccessKeys(self, queryParams={}):
        return self.request("GET", "/storage/s3/access-keys".format(), queryParams);


    def getDNSZone(self, name, queryParams={}):
        return self.request("GET", "/dns/zones/{name}".format(name=name), queryParams);


    def updateDNSZone(self, name, body, queryParams={}):
        return self.request("PUT", "/dns/zones/{name}".format(name=name), queryParams, body);


    def createDomainHandle(self, body, queryParams={}):
        return self.request("POST", "/domain-handles".format(), queryParams, body);


    def getDomainHandles(self, queryParams={}):
        return self.request("GET", "/domain-handles".format(), queryParams);


    def getAddress(self, id, queryParams={}):
        return self.request("GET", "/addresses/{id}".format(id=id), queryParams);


    def createSSLCertificate(self, body, queryParams={}):
        return self.request("POST", "/ssl/certificates".format(), queryParams, body);


    def getSSLCertificates(self, queryParams={}):
        return self.request("GET", "/ssl/certificates".format(), queryParams);


    def scheduleDomainDelete(self, name, body, queryParams={}):
        return self.request("POST", "/domains/{name}/schedule-delete".format(name=name), queryParams, body);


    def getServerBackup(self, id, queryParams={}):
        return self.request("GET", "/server-backups/{id}".format(id=id), queryParams);


    def deleteServerBackup(self, id, queryParams={}):
        return self.request("DELETE", "/server-backups/{id}".format(id=id), queryParams);


    def getDomainPricingList(self, queryParams={}):
        return self.request("GET", "/pricing/domains".format(), queryParams);


    def getSSLCertificate(self, id, queryParams={}):
        return self.request("GET", "/ssl/certificates/{id}".format(id=id), queryParams);


    def createSubnetAddress(self, id, body, queryParams={}):
        return self.request("POST", "/subnets/{id}/addresses".format(id=id), queryParams, body);


    def createNetwork(self, body, queryParams={}):
        return self.request("POST", "/networks".format(), queryParams, body);


    def getNetworks(self, queryParams={}):
        return self.request("GET", "/networks".format(), queryParams);


    def getDomainAuthinfo(self, name, queryParams={}):
        return self.request("GET", "/domains/{name}/authinfo".format(name=name), queryParams);


    def removeDomainAuthinfo(self, name, queryParams={}):
        return self.request("DELETE", "/domains/{name}/authinfo".format(name=name), queryParams);


    def createServerStorage(self, body, queryParams={}):
        return self.request("POST", "/server-storages".format(), queryParams, body);


    def getServerStorages(self, queryParams={}):
        return self.request("GET", "/server-storages".format(), queryParams);


    def resizeServer(self, id, body, queryParams={}):
        return self.request("POST", "/servers/{id}/resize".format(id=id), queryParams, body);


    def restoreDomain(self, name, queryParams={}):
        return self.request("POST", "/domains/{name}/restore".format(name=name), queryParams);


    def createSSLContact(self, body, queryParams={}):
        return self.request("POST", "/ssl/contacts".format(), queryParams, body);


    def getSSLContacts(self, queryParams={}):
        return self.request("GET", "/ssl/contacts".format(), queryParams);


    def getServerMedia(self, id, queryParams={}):
        return self.request("GET", "/server-medias/{id}".format(id=id), queryParams);


    def deleteServerMedia(self, id, queryParams={}):
        return self.request("DELETE", "/server-medias/{id}".format(id=id), queryParams);


    def createS3AccessKeyGrant(self, access_key_id, body, queryParams={}):
        return self.request("POST", "/storage/s3/access-keys/{access_key_id}/grants".format(access_key_id=access_key_id), queryParams, body);


    def getS3AccessKeyGrants(self, access_key_id, queryParams={}):
        return self.request("GET", "/storage/s3/access-keys/{access_key_id}/grants".format(access_key_id=access_key_id), queryParams);


    def getServerPriceRangeAssignment(self, id, queryParams={}):
        return self.request("GET", "/server-price-range-assignments/{id}".format(id=id), queryParams);


    def deleteServerPriceRangeAssignment(self, id, queryParams={}):
        return self.request("DELETE", "/server-price-range-assignments/{id}".format(id=id), queryParams);


    def updateServerPriceRangeAssignment(self, id, body, queryParams={}):
        return self.request("PUT", "/server-price-range-assignments/{id}".format(id=id), queryParams, body);


    def getServerVNC(self, id, queryParams={}):
        return self.request("GET", "/servers/{id}/vnc".format(id=id), queryParams);


    def getNetwork(self, id, queryParams={}):
        return self.request("GET", "/networks/{id}".format(id=id), queryParams);


    def getLabels(self, queryParams={}):
        return self.request("GET", "/labels".format(), queryParams);


    def getS3Bucket(self, id, queryParams={}):
        return self.request("GET", "/storage/s3/buckets/{id}".format(id=id), queryParams);


    def deleteS3Bucket(self, id, queryParams={}):
        return self.request("DELETE", "/storage/s3/buckets/{id}".format(id=id), queryParams);


    def createDomain(self, body, queryParams={}):
        return self.request("POST", "/domains".format(), queryParams, body);


    def getDomains(self, queryParams={}):
        return self.request("GET", "/domains".format(), queryParams);


    def detachServerVolume(self, id, queryParams={}):
        return self.request("POST", "/server-volumes/{id}/detach".format(id=id), queryParams);


    def createServerVariantPrice(self, id, body, queryParams={}):
        return self.request("POST", "/server-price-ranges/{id}/variant-prices".format(id=id), queryParams, body);


    def getServerVariantPrices(self, id, queryParams={}):
        return self.request("GET", "/server-price-ranges/{id}/variant-prices".format(id=id), queryParams);


