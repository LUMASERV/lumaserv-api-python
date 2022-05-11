import requests


class CoreClient:
    def __init__(self, api_key, base_url="https://api.lumaserv.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json'
        })


    def request(self, method, path, params={}, body={}):
        r = self.session.request(method, self.base_url + path, data=data, params=params)
        f(r.status_code < 200 or (r.status_code >= 300 and r.status_code < 400):
            raise Exception("Status code is " + r.status_code + "!")
        return r.json()


    def create_s_s_h_key(self, body, query_params={}):
        return self.request("POST", "/ssh-keys", query_params, body);


    def get_s_s_h_keys(self, query_params={}):
        return self.request("GET", "/ssh-keys", query_params);


    def create_server_price_range(self, body, query_params={}):
        return self.request("POST", "/server-price-ranges", query_params, body);


    def get_server_price_ranges(self, query_params={}):
        return self.request("GET", "/server-price-ranges", query_params);


    def start_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/start".format(id=id), query_params);


    def create_availability_zone(self, body, query_params={}):
        return self.request("POST", "/availability-zones", query_params, body);


    def get_availability_zones(self, query_params={}):
        return self.request("GET", "/availability-zones", query_params);


    def get_server_template(self, id, query_params={}):
        return self.request("GET", "/server-templates/{id}".format(id=id), query_params);


    def shutdown_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/shutdown".format(id=id), query_params);


    def get_server_firewall(self, id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}".format(id=id), query_params);


    def delete_server_firewall(self, id, query_params={}):
        return self.request("DELETE", "/server-firewalls/{id}".format(id=id), query_params);


    def get_server(self, id, query_params={}):
        return self.request("GET", "/servers/{id}".format(id=id), query_params);


    def delete_server(self, id, query_params={}):
        return self.request("DELETE", "/servers/{id}".format(id=id), query_params);


    def update_server(self, id, body, query_params={}):
        return self.request("PUT", "/servers/{id}".format(id=id), query_params, body);


    def get_server_storage_class(self, id, query_params={}):
        return self.request("GET", "/server-storage-classes/{id}".format(id=id), query_params);


    def restart_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/restart".format(id=id), query_params);


    def restore_server(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/restore".format(id=id), query_params, body);


    def get_s_s_l_organisation(self, id, query_params={}):
        return self.request("GET", "/ssl/organisations/{id}".format(id=id), query_params);


    def delete_s_s_l_organisation(self, id, query_params={}):
        return self.request("DELETE", "/ssl/organisations/{id}".format(id=id), query_params);


    def get_server_action(self, id, action_id, query_params={}):
        return self.request("GET", "/servers/{id}/actions/{action_id}".format(id=id, action_id=action_id), query_params);


    def get_server_graph(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/graph".format(id=id), query_params);


    def get_s_s_l_contact(self, id, query_params={}):
        return self.request("GET", "/ssl/contacts/{id}".format(id=id), query_params);


    def delete_s_s_l_contact(self, id, query_params={}):
        return self.request("DELETE", "/ssl/contacts/{id}".format(id=id), query_params);


    def get_d_n_s_zones(self, query_params={}):
        return self.request("GET", "/dns/zones", query_params);


    def recreate_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/recreate".format(id=id), query_params);


    def create_server_firewall(self, body, query_params={}):
        return self.request("POST", "/server-firewalls", query_params, body);


    def get_server_firewalls(self, query_params={}):
        return self.request("GET", "/server-firewalls", query_params);


    def get_server_firewall_rule(self, id, rule_id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), query_params);


    def delete_server_firewall_rule(self, id, rule_id, query_params={}):
        return self.request("DELETE", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), query_params);


    def send_domain_verification(self, name, query_params={}):
        return self.request("POST", "/domains/{name}/verification".format(name=name), query_params);


    def check_domain_verification(self, name, query_params={}):
        return self.request("GET", "/domains/{name}/verification".format(name=name), query_params);


    def create_server_host(self, body, query_params={}):
        return self.request("POST", "/server-hosts", query_params, body);


    def get_server_hosts(self, query_params={}):
        return self.request("GET", "/server-hosts", query_params);


    def create_server(self, body, query_params={}):
        return self.request("POST", "/servers", query_params, body);


    def get_servers(self, query_params={}):
        return self.request("GET", "/servers", query_params);


    def delete_server_network(self, id, network_id, query_params={}):
        return self.request("DELETE", "/servers/{id}/networks/{network_id}".format(id=id, network_id=network_id), query_params);


    def check_domain(self, name, query_params={}):
        return self.request("GET", "/domains/{name}/check".format(name=name), query_params);


    def get_domain(self, name, query_params={}):
        return self.request("GET", "/domains/{name}".format(name=name), query_params);


    def delete_domain(self, name, query_params={}):
        return self.request("DELETE", "/domains/{name}".format(name=name), query_params);


    def update_domain(self, name, body, query_params={}):
        return self.request("PUT", "/domains/{name}".format(name=name), query_params, body);


    def get_domain_handle(self, code, query_params={}):
        return self.request("GET", "/domain-handles/{code}".format(code=code), query_params);


    def delete_domain_handle(self, code, query_params={}):
        return self.request("DELETE", "/domain-handles/{code}".format(code=code), query_params);


    def update_domain_handle(self, code, body, query_params={}):
        return self.request("PUT", "/domain-handles/{code}".format(code=code), query_params, body);


    def get_availability_zone(self, id, query_params={}):
        return self.request("GET", "/availability-zones/{id}".format(id=id), query_params);


    def update_availability_zone(self, id, body, query_params={}):
        return self.request("PUT", "/availability-zones/{id}".format(id=id), query_params, body);


    def create_server_backup(self, body, query_params={}):
        return self.request("POST", "/server-backups", query_params, body);


    def get_server_backups(self, query_params={}):
        return self.request("GET", "/server-backups", query_params);


    def create_subnet(self, body, query_params={}):
        return self.request("POST", "/subnets", query_params, body);


    def get_subnets(self, query_params={}):
        return self.request("GET", "/subnets", query_params);


    def create_server_volume(self, body, query_params={}):
        return self.request("POST", "/server-volumes", query_params, body);


    def get_server_volumes(self, query_params={}):
        return self.request("GET", "/server-volumes", query_params);


    def get_plesk_license_type(self, id, query_params={}):
        return self.request("GET", "/licenses/plesk-types/{id}".format(id=id), query_params);


    def create_server_storage_class(self, body, query_params={}):
        return self.request("POST", "/server-storage-classes", query_params, body);


    def get_server_storage_classes(self, query_params={}):
        return self.request("GET", "/server-storage-classes", query_params);


    def get_server_firewall_member(self, id, member_id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/members/{member_id}".format(id=id, member_id=member_id), query_params);


    def delete_server_firewall_member(self, id, member_id, query_params={}):
        return self.request("DELETE", "/server-firewalls/{id}/members/{member_id}".format(id=id, member_id=member_id), query_params);


    def search(self, query_params={}):
        return self.request("GET", "/search", query_params);


    def get_scheduled_server_action(self, id, action_id, query_params={}):
        return self.request("GET", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), query_params);


    def delete_scheduled_server_action(self, id, action_id, query_params={}):
        return self.request("DELETE", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), query_params);


    def create_s3_bucket(self, body, query_params={}):
        return self.request("POST", "/storage/s3/buckets", query_params, body);


    def get_s3_buckets(self, query_params={}):
        return self.request("GET", "/storage/s3/buckets", query_params);


    def get_plesk_license_types(self, query_params={}):
        return self.request("GET", "/licenses/plesk-types", query_params);


    def get_server_actions(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/actions".format(id=id), query_params);


    def get_server_status(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/status".format(id=id), query_params);


    def create_server_firewall_member(self, id, body, query_params={}):
        return self.request("POST", "/server-firewalls/{id}/members".format(id=id), query_params, body);


    def get_server_firewall_members(self, id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/members".format(id=id), query_params);


    def get_server_price_range(self, id, query_params={}):
        return self.request("GET", "/server-price-ranges/{id}".format(id=id), query_params);


    def create_s_s_l_organisation(self, body, query_params={}):
        return self.request("POST", "/ssl/organisations", query_params, body);


    def get_s_s_l_organisations(self, query_params={}):
        return self.request("GET", "/ssl/organisations", query_params);


    def get_s_s_l_type(self, id, query_params={}):
        return self.request("GET", "/ssl/types/{id}".format(id=id), query_params);


    def get_s_s_l_types(self, query_params={}):
        return self.request("GET", "/ssl/types", query_params);


    def get_server_variant_price(self, id, variant_id, query_params={}):
        return self.request("GET", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), query_params);


    def delete_server_variant_price(self, id, variant_id, query_params={}):
        return self.request("DELETE", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), query_params);


    def update_server_variant_price(self, id, variant_id, body, query_params={}):
        return self.request("PUT", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), query_params, body);


    def delete_d_n_s_record(self, name, id, query_params={}):
        return self.request("DELETE", "/dns/zones/{name}/records/{id}".format(name=name, id=id), query_params);


    def update_d_n_s_record(self, name, id, body, query_params={}):
        return self.request("PUT", "/dns/zones/{name}/records/{id}".format(name=name, id=id), query_params, body);


    def get_plesk_license(self, id, query_params={}):
        return self.request("GET", "/licenses/plesk/{id}".format(id=id), query_params);


    def update_plesk_license(self, id, body, query_params={}):
        return self.request("PUT", "/licenses/plesk/{id}".format(id=id), query_params, body);


    def create_server_template(self, body, query_params={}):
        return self.request("POST", "/server-templates", query_params, body);


    def get_server_templates(self, query_params={}):
        return self.request("GET", "/server-templates", query_params);


    def get_server_host(self, id, query_params={}):
        return self.request("GET", "/server-hosts/{id}".format(id=id), query_params);


    def create_server_firewall_rule(self, id, body, query_params={}):
        return self.request("POST", "/server-firewalls/{id}/rules".format(id=id), query_params, body);


    def get_server_firewall_rules(self, id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/rules".format(id=id), query_params);


    def create_scheduled_server_action(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/scheduled-actions".format(id=id), query_params, body);


    def get_scheduled_server_actions(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/scheduled-actions".format(id=id), query_params);


    def unschedule_domain_delete(self, name, query_params={}):
        return self.request("POST", "/domains/{name}/unschedule-delete".format(name=name), query_params);


    def stop_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/stop".format(id=id), query_params);


    def create_d_n_s_zone_record(self, name, body, query_params={}):
        return self.request("POST", "/dns/zones/{name}/records".format(name=name), query_params, body);


    def get_d_n_s_zone_records(self, name, query_params={}):
        return self.request("GET", "/dns/zones/{name}/records".format(name=name), query_params);


    def update_d_n_s_zone_records(self, name, body, query_params={}):
        return self.request("PUT", "/dns/zones/{name}/records".format(name=name), query_params, body);


    def get_server_volume(self, id, query_params={}):
        return self.request("GET", "/server-volumes/{id}".format(id=id), query_params);


    def delete_server_volume(self, id, query_params={}):
        return self.request("DELETE", "/server-volumes/{id}".format(id=id), query_params);


    def update_server_volume(self, id, body, query_params={}):
        return self.request("PUT", "/server-volumes/{id}".format(id=id), query_params, body);


    def create_server_network(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/networks".format(id=id), query_params, body);


    def get_server_networks(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/networks".format(id=id), query_params);


    def create_server_variant(self, body, query_params={}):
        return self.request("POST", "/server-variants", query_params, body);


    def get_server_variants(self, query_params={}):
        return self.request("GET", "/server-variants", query_params);


    def get_server_storage(self, id, query_params={}):
        return self.request("GET", "/server-storages/{id}".format(id=id), query_params);


    def get_s_s_h_key(self, id, query_params={}):
        return self.request("GET", "/ssh-keys/{id}".format(id=id), query_params);


    def delete_s_s_h_key(self, id, query_params={}):
        return self.request("DELETE", "/ssh-keys/{id}".format(id=id), query_params);


    def create_server_price_range_assignment(self, body, query_params={}):
        return self.request("POST", "/server-price-range-assignments", query_params, body);


    def get_server_price_range_assignments(self, query_params={}):
        return self.request("GET", "/server-price-range-assignments", query_params);


    def get_addresses(self, query_params={}):
        return self.request("GET", "/addresses", query_params);


    def get_server_variant(self, id, query_params={}):
        return self.request("GET", "/server-variants/{id}".format(id=id), query_params);


    def delete_server_variant(self, id, query_params={}):
        return self.request("DELETE", "/server-variants/{id}".format(id=id), query_params);


    def delete_s3_access_key_grant(self, access_key_id, id, query_params={}):
        return self.request("DELETE", "/storage/s3/access-keys/{access_key_id}/grants/{id}".format(access_key_id=access_key_id, id=id), query_params);


    def create_server_media(self, body, query_params={}):
        return self.request("POST", "/server-medias", query_params, body);


    def get_server_medias(self, query_params={}):
        return self.request("GET", "/server-medias", query_params);


    def get_subnet(self, id, query_params={}):
        return self.request("GET", "/subnets/{id}".format(id=id), query_params);


    def delete_subnet(self, id, query_params={}):
        return self.request("DELETE", "/subnets/{id}".format(id=id), query_params);


    def attach_server_volume(self, id, body, query_params={}):
        return self.request("POST", "/server-volumes/{id}/attach".format(id=id), query_params, body);


    def create_plesk_license(self, body, query_params={}):
        return self.request("POST", "/licenses/plesk", query_params, body);


    def get_plesk_licenses(self, query_params={}):
        return self.request("GET", "/licenses/plesk", query_params);


    def get_s3_access_key(self, id, query_params={}):
        return self.request("GET", "/storage/s3/access-keys/{id}".format(id=id), query_params);


    def delete_s3_access_key(self, id, query_params={}):
        return self.request("DELETE", "/storage/s3/access-keys/{id}".format(id=id), query_params);


    def create_s3_access_key(self, body, query_params={}):
        return self.request("POST", "/storage/s3/access-keys", query_params, body);


    def get_s3_access_keys(self, query_params={}):
        return self.request("GET", "/storage/s3/access-keys", query_params);


    def get_d_n_s_zone(self, name, query_params={}):
        return self.request("GET", "/dns/zones/{name}".format(name=name), query_params);


    def update_d_n_s_zone(self, name, body, query_params={}):
        return self.request("PUT", "/dns/zones/{name}".format(name=name), query_params, body);


    def create_domain_handle(self, body, query_params={}):
        return self.request("POST", "/domain-handles", query_params, body);


    def get_domain_handles(self, query_params={}):
        return self.request("GET", "/domain-handles", query_params);


    def get_address(self, id, query_params={}):
        return self.request("GET", "/addresses/{id}".format(id=id), query_params);


    def create_s_s_l_certificate(self, body, query_params={}):
        return self.request("POST", "/ssl/certificates", query_params, body);


    def get_s_s_l_certificates(self, query_params={}):
        return self.request("GET", "/ssl/certificates", query_params);


    def schedule_domain_delete(self, name, body, query_params={}):
        return self.request("POST", "/domains/{name}/schedule-delete".format(name=name), query_params, body);


    def get_server_backup(self, id, query_params={}):
        return self.request("GET", "/server-backups/{id}".format(id=id), query_params);


    def delete_server_backup(self, id, query_params={}):
        return self.request("DELETE", "/server-backups/{id}".format(id=id), query_params);


    def get_domain_pricing_list(self, query_params={}):
        return self.request("GET", "/pricing/domains", query_params);


    def get_s_s_l_certificate(self, id, query_params={}):
        return self.request("GET", "/ssl/certificates/{id}".format(id=id), query_params);


    def create_subnet_address(self, id, body, query_params={}):
        return self.request("POST", "/subnets/{id}/addresses".format(id=id), query_params, body);


    def create_network(self, body, query_params={}):
        return self.request("POST", "/networks", query_params, body);


    def get_networks(self, query_params={}):
        return self.request("GET", "/networks", query_params);


    def get_domain_authinfo(self, name, query_params={}):
        return self.request("GET", "/domains/{name}/authinfo".format(name=name), query_params);


    def remove_domain_authinfo(self, name, query_params={}):
        return self.request("DELETE", "/domains/{name}/authinfo".format(name=name), query_params);


    def create_server_storage(self, body, query_params={}):
        return self.request("POST", "/server-storages", query_params, body);


    def get_server_storages(self, query_params={}):
        return self.request("GET", "/server-storages", query_params);


    def resize_server(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/resize".format(id=id), query_params, body);


    def restore_domain(self, name, query_params={}):
        return self.request("POST", "/domains/{name}/restore".format(name=name), query_params);


    def create_s_s_l_contact(self, body, query_params={}):
        return self.request("POST", "/ssl/contacts", query_params, body);


    def get_s_s_l_contacts(self, query_params={}):
        return self.request("GET", "/ssl/contacts", query_params);


    def get_server_media(self, id, query_params={}):
        return self.request("GET", "/server-medias/{id}".format(id=id), query_params);


    def delete_server_media(self, id, query_params={}):
        return self.request("DELETE", "/server-medias/{id}".format(id=id), query_params);


    def create_s3_access_key_grant(self, access_key_id, body, query_params={}):
        return self.request("POST", "/storage/s3/access-keys/{access_key_id}/grants".format(access_key_id=access_key_id), query_params, body);


    def get_s3_access_key_grants(self, access_key_id, query_params={}):
        return self.request("GET", "/storage/s3/access-keys/{access_key_id}/grants".format(access_key_id=access_key_id), query_params);


    def get_server_price_range_assignment(self, id, query_params={}):
        return self.request("GET", "/server-price-range-assignments/{id}".format(id=id), query_params);


    def delete_server_price_range_assignment(self, id, query_params={}):
        return self.request("DELETE", "/server-price-range-assignments/{id}".format(id=id), query_params);


    def update_server_price_range_assignment(self, id, body, query_params={}):
        return self.request("PUT", "/server-price-range-assignments/{id}".format(id=id), query_params, body);


    def get_server_v_n_c(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/vnc".format(id=id), query_params);


    def get_network(self, id, query_params={}):
        return self.request("GET", "/networks/{id}".format(id=id), query_params);


    def get_labels(self, query_params={}):
        return self.request("GET", "/labels", query_params);


    def get_s3_bucket(self, id, query_params={}):
        return self.request("GET", "/storage/s3/buckets/{id}".format(id=id), query_params);


    def delete_s3_bucket(self, id, query_params={}):
        return self.request("DELETE", "/storage/s3/buckets/{id}".format(id=id), query_params);


    def create_domain(self, body, query_params={}):
        return self.request("POST", "/domains", query_params, body);


    def get_domains(self, query_params={}):
        return self.request("GET", "/domains", query_params);


    def detach_server_volume(self, id, query_params={}):
        return self.request("POST", "/server-volumes/{id}/detach".format(id=id), query_params);


    def create_server_variant_price(self, id, body, query_params={}):
        return self.request("POST", "/server-price-ranges/{id}/variant-prices".format(id=id), query_params, body);


    def get_server_variant_prices(self, id, query_params={}):
        return self.request("GET", "/server-price-ranges/{id}/variant-prices".format(id=id), query_params);


