#GENERAL
#TODO:
# tags
ALL_TASKS = [  # ('title', '''html description''', ['gci categories'], ['tags'], [optional ticket numbers])

#TODO when is this task completed?
('Graphics and color blindness', '''\
	<p>Most of our interface is designed and coded by people without malfunctioning color
	vision. There are several impairments related to how colors are observed by others.
	Learn more about the topic <a href="http://en.wikipedia.org/wiki/Color_blindness"> on
	Wikipedia</a>. The percentages listed there might surprise you!</p>
	<p>Your task is to make Unknown Horizons easier for these players by finding problems with our
	current interface colors and suggesting graphics we should revise with this in mind.</p>
	<p>Converting a screenshot to black and white can (to some degree) simulate the way color blind
	people see, since then all color info is gone, and only the luminosity differences are visible.</p>
	<p>If you happen to know a color blind person: their feedback is very welcome and a nice bonus!</p>''',
	['User Interface', 'Outreach/Research'], [], [1116]),

#TODO more explanation of settings code, example commit for other settings, ticket comment
#TODO is this also in User Interface?
('Scroll settings', '''\
	<h2>Customizable scroll speed, option to disable mouse scrolling / panning</h2>
	<p>Your tasks:</p><ul>
	<li>Implement a new slider for our settings that allows players to alter how fast the
	map scrolls when pressing arrow keys or moving the mouse towards screen edges.</li>
	<li>Add a checkbox with the functionality of disabling mouse pan -- that is how we call the
	effect when you hold down the middle mouse button (MMB) and then move the mouse.</li></ul>''',
	['Code'], ['python'], [720]),

#TODO more explanations about selection code location
#TODO when is this task completed?
('Faster multiselection', '''\
	<p>When drawing a very large selection rectangle, the game takes up to a few seconds to process
	this. The bottleneck is probably the <code>getMatchingInstances</code> call.</p>
	<p>This should not happen, it would be preferable if calculations were done in the background
	while the game continues without interruptions.</p>
	<p>One solution might be to fake an incremental search: The rectangle where units and buildings
	are selected is partitioned into smaller rectangles, and an update only checks the rectangles
	at the fringe. These updates could be spread over a number of ticks too, e.g. such that it
	takes 0.5 sec max in total. This way, the game could feel slightly faster in this use case.</p>
	<p>Other suggestions might be better than this one and you are encouraged to propose them!</p>
	<p>You might also consider writing a very quick test case to compare the current implementation
	with the improved one.</p>''',
	['Code', 'Outreach/Research'], ['python'], [1675]),

('Trade route GUI test', '''\
	<p>Your task: Create a comprehensive gui test (or tests) where all elements of the trade route
	gui are covered by test interactions. It should also test that the behavior expected by
	changing the configuration is actually exhibited by the ship.</p>
	<p>This is an important task because these elements of the game are usually not touched when
	players or developers test the game.</p>
	<p>Find out about what GUI tests are <a href="http://wiki.unknown-horizons.org/w/Tests#GUI_tests">
	in our wiki</a> and more information about which parts to test in the ticket comments:</p>''',
	['Quality Assurance'], ['python'], [1864]),

('ATI driver issue suspected', '''\
	<p>Check the ticket comments and the FIFE ticket. If you have access to ATI hardware, please
	verify that the problem exists for you (if it does) and whether changing drivers has any effect
	(better or worse). Perhaps you even know or can investigate how other engines solved this?</p>''',
	['Outreach/Research'], [], [1382]),

('Icons unified', '''\
	<p>We're currently showing small images (icons) in our build menu to indicate what kind of
	building you will be able to construct after clicking on the buttons. Most of those buildings
	are so-called production buildings, i.e. they produce goods. This production is also visible in
	the overview tab (which is displayed after selecting buildings) and we use icons for resources
	here, too.</p>
	<p>Mostly, players are interested in exactly that: They are looking for a certain building that
	will provide one specific resource. Thus, we want to use the icons of output resources as build
	menu icon for each building where this is applicable and not confusing.</p>
	<p>Your task: Assemble a list of buildings in all our currently four tiers where the build menu
	icon does not match the icon of the main resource produced there. Should there be multiple
	resource productions (such as at the farm), an own icon is fine. If you're looking for a bonus
	task, you can also try to actually replace some of those offending icons on your own!</p>''',
	['User Interface'], [], [750]),

('Split buildingtool.py', '''\
	<p>Over the years, <code>horizons/gui/mousetools/buildingtool.py</code> became one of our
	largest files in the entire project. It currently reports 850 lines of code (LOC) and contains
	many simple functions. It is important to keep this frequently altered part of UH in a good
	shape so that maintainability does not suffer.</p>
	<p>Your task: Logic and actual worker functions should be split up in at least 2 files,
	probably 3 also is a good landmark. You will have to actually read the documentation about what
	each function does, confirm that by reading the code and then decide what goes where!</p>''',
	['Code'], ['python'], [1629]),

#1666
#870 and equivalents -- how to use, which tasks to make
#1773
#1461
#1921++
#more QA like 1864
]
