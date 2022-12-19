output_format = """
; Summary: FoD Rule List

#BEGIN

[wildcard]
%s

[regexp]

#END
"""
domains_file = open("domains")
domains = domains_file.read().splitlines()

output_file = open("switchy-omega-rules.ssrl", "w")
output_domain_rules = []

for domain in domains:
    output_domain_rules.append(("@*://*" + domain + "/*\n"))

output_domain_rules[-2] = output_domain_rules[-2][:-1]

out = output_format % ("".join(output_domain_rules[:-1]))

output_file.write(out[1:-1])
