#!/usr/bin/env python2

GCI = '''\
    <gci:task href="uh_{href}.xhtml">
        <gci:title>{title}</gci:title>
        <gci:tags>
{tags}
        </gci:tags>
        <gci:types>{categories}</gci:types>
        <gci:team>UH</gci:team>
        <gci:desc>
{desc}
        </gci:desc>
    </gci:task>'''

def print_one_task(title, desc, types, all_tags, tickets=None):
	tickets = tickets or []
	href = '_'.join(title.split()[:2]).lower()
	desc = '''\
        <h2>Unknown Horizons</h2>
        <p>Join <a href="http://www.unknown-horizons.org/irc/">our IRC channel</a>
	   when working on this task!</p>''' + desc + '''
<br />'''.join(' '*8 + '<a href="https://github.com/'
		'unknown-horizons/unknown-horizons/issues/{0}">'
		'<b>Ticket {0}</b></a>'.format(t)
		for t in tickets)
	desc = '        <div style="font-size:17px;">\n' + desc + '</div>'
	categories = ','.join(t for t in types)
	tags = ''.join('''\
            <gci:tag id="{tag_id}"/>'''.format(tag_id=tag_id)
		for tag_id in (['unknownhorizons'] + sorted(all_tags)))
	return GCI.format(**locals())

if __name__ == '__main__':
	from all_tasks import ALL_TASKS
	print '''\
<?xml version='1.0'?>
<gci:tasks xmlns="http://www.w3.org/1999/xhtml" xmlns:gci="gci">
'''
	for task in ALL_TASKS:
		if not task:
			continue
		print print_one_task(*task)
		print
	print '</gci:tasks>'
