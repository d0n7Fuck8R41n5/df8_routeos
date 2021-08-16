from routeros import login

comment = 'pc_vnc'
router_os = login('user', 'password', 'ip')
nat_rule = router_os.query('/ip/firewall/nat/print').equal(comment='pc_vnc')
router_os = login('user', 'password', 'ip')
router_os('/ip/firewall/nat/enable', **{'.id': nat_rule[0]['.id']})
router_os.close()
