from enum import Enum
from typing import Dict, Union, List
from filip.semantics.semantic_models import\
	SemanticClass,\
	SemanticIndividual,\
	RelationField,\
	DataField,\
	SemanticDeviceClass,\
	DeviceAttributeField,\
	CommandField
from filip.semantics.semantic_manager import\
	SemanticManager,\
	InstanceRegistry


"""
Generated models file from vocabulary.
Models can be used for semantical descriptions.
"""


semantic_manager: SemanticManager = SemanticManager(
	instance_registry=InstanceRegistry(),
)

# ---------CLASSES--------- #


class Currency(SemanticClass):
	"""
	The Unit Of Measure For Price

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Energy_Unit(SemanticClass):
	"""
	The Unit Of Measure For Energy

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Illuminance_Unit(SemanticClass):
	"""
	The Unit Of Measure For Light

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Power_Unit(SemanticClass):
	"""
	The Unit Of Measure For Power

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Pressure_Unit(SemanticClass):
	"""
	The Unit Of Measure For Pressure

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Temperature_Unit(SemanticClass):
	"""
	The Unit Of Measure For Temperature

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Thing(SemanticClass):
	"""
	Predefined root_class

	Source: 
		None (Predefined)
	"""

	def __new__(cls, *args, **kwargs):
		kwargs['semantic_manager'] = semantic_manager
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, *args, **kwargs):
		kwargs['semantic_manager'] = semantic_manager
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Class1(Thing):
	"""
	Comment On Class 1

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.dataProp2._rules = [('value', [[]])]

			self.oProp1._rules = [('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()
			self.dataProp2.add(2)

			self.objProp5.add(Individual1())

	# Data fields

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Class1a(Class1):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.dataProp2._rules = [('value', [[]])]

			self.oProp1._rules = [('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()

	# Data fields

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Class1aa(Class1a):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.dataProp2._rules = [('value', [[]])]

			self.oProp1._rules = [('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()

	# Data fields

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Class1b(Class1):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.dataProp2._rules = [('value', [[]])]

			self.oProp1._rules = [('some', [[Class2]]), ('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()

	# Data fields

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='some Class2, some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Class2(Thing):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['customDataType1']])]

			self.oProp1._rules = [('min|1', [[Class1]])]
			self.objProp2._rules = [('only', [[Thing]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some customDataType1',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='min 1 Class1',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='only Thing',
		semantic_manager=semantic_manager)


class Class3(Thing):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['string']])]
			self.commandProp._rules = [('some', [['string']])]
			self.dataProp1._rules = [('only', [['customDataType4']])]

			self.oProp1._rules = [('value', [[Individual1]])]
			self.objProp2._rules = [('some', [[Class1]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()
			self.commandProp._instance_identifier = self.get_identifier()
			self.dataProp1._instance_identifier = self.get_identifier()

			self.oProp1.add(Individual1())
			self.objProp2.add(Individual1())

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some string',
		semantic_manager=semantic_manager)

	commandProp: DataField = DataField(
		name='commandProp',
		rule='some string',
		semantic_manager=semantic_manager)

	dataProp1: DataField = DataField(
		name='dataProp1',
		rule='only customDataType4',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='value Individual1',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some Class1, value Individual1',
		semantic_manager=semantic_manager)


class Class123(Class1, Class2, Class3):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['string']]), ('some', [['customDataType1']])]
			self.commandProp._rules = [('some', [['string']])]
			self.dataProp1._rules = [('only', [['customDataType4']])]
			self.dataProp2._rules = [('value', [[]])]

			self.oProp1._rules = [('value', [[Individual1]]), ('min|1', [[Class1]]), ('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('some', [[Class1]]), ('value', [[Individual1]]), ('only', [[Thing]]), ('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()
			self.commandProp._instance_identifier = self.get_identifier()
			self.dataProp1._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some string, some customDataType1',
		semantic_manager=semantic_manager)

	commandProp: DataField = DataField(
		name='commandProp',
		rule='some string',
		semantic_manager=semantic_manager)

	dataProp1: DataField = DataField(
		name='dataProp1',
		rule='only customDataType4',
		semantic_manager=semantic_manager)

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='value Individual1, min 1 Class1, some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some Class1, value Individual1, only Thing, some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Class13(Class1, Class3):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['string']])]
			self.commandProp._rules = [('some', [['string']])]
			self.dataProp1._rules = [('min|1', [['int']]), ('only', [['customDataType4']])]
			self.dataProp2._rules = [('exactly|1', [['boolean']]), ('value', [[]])]

			self.oProp1._rules = [('value', [[Individual1]]), ('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('some', [[Class1]]), ('value', [[Individual1]]), ('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()
			self.commandProp._instance_identifier = self.get_identifier()
			self.dataProp1._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some string',
		semantic_manager=semantic_manager)

	commandProp: DataField = DataField(
		name='commandProp',
		rule='some string',
		semantic_manager=semantic_manager)

	dataProp1: DataField = DataField(
		name='dataProp1',
		rule='min 1 int, only customDataType4',
		semantic_manager=semantic_manager)

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='exactly 1 boolean, value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='value Individual1, some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some Class1, value Individual1, some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Class3a(Class3):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['string']])]
			self.commandProp._rules = [('some', [['string']])]
			self.dataProp1._rules = [('only', [['customDataType4']])]

			self.oProp1._rules = [('value', [[Individual1]])]
			self.objProp2._rules = [('some', [[Class1]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()
			self.commandProp._instance_identifier = self.get_identifier()
			self.dataProp1._instance_identifier = self.get_identifier()

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some string',
		semantic_manager=semantic_manager)

	commandProp: DataField = DataField(
		name='commandProp',
		rule='some string',
		semantic_manager=semantic_manager)

	dataProp1: DataField = DataField(
		name='dataProp1',
		rule='only customDataType4',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='value Individual1',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some Class1, value Individual1',
		semantic_manager=semantic_manager)


class Class3aa(Class3a):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['string']])]
			self.commandProp._rules = [('some', [['string']])]
			self.dataProp1._rules = [('only', [['customDataType4']])]

			self.oProp1._rules = [('value', [[Individual1]])]
			self.objProp2._rules = [('some', [[Class1]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()
			self.commandProp._instance_identifier = self.get_identifier()
			self.dataProp1._instance_identifier = self.get_identifier()

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some string',
		semantic_manager=semantic_manager)

	commandProp: DataField = DataField(
		name='commandProp',
		rule='some string',
		semantic_manager=semantic_manager)

	dataProp1: DataField = DataField(
		name='dataProp1',
		rule='only customDataType4',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='value Individual1',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='some Class1, value Individual1',
		semantic_manager=semantic_manager)


class Class4(Thing):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.objProp4._rules = [('min|1', [[Class1]])]

			self.objProp4._instance_identifier = self.get_identifier()

	# Relation fields

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='min 1 Class1',
		semantic_manager=semantic_manager)


class Command(Thing):
	"""
	A Directive That A Device Must Support To Perform A Certain Function. A
	Command May Act Upon A State, But Does Not Necessarily Act Upon A State. For
	Example, The On Command Acts Upon The On/Off State, But The Get Command Does
	Not Act Upon Any State, It Simply Gives A Directive To Retrieve A Certain
	Value. We Propose Here A List Of Commands That Are Relevant For The Purpose
	Of Saref, But This List Can Be Extended.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Close_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Open_Close_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Open_Close_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Commodity(Thing):
	"""
	A Marketable Item For Which There Is Demand, But Which Is Supplied Without
	Qualitative Differentiation Across A Market. Saref Refers To Energy
	Commodities Such As Electricity, Gas, Coal And Oil. 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Coal(Commodity):
	"""
	A Type Of Commodity

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Device(Thing):
	"""
	A Tangible Object Designed To Accomplish A Particular Task In Households,
	Common Public Buildings Or Offices. In Order To Accomplish This Task, The
	Device Performs One Or More Functions. For Example, A Washing Machine Is
	Designed To Wash (Task) And To Accomplish This Task It Performs A Start And
	Stop Function. Devices Can Be Structured In Categories (Subclasses) That
	Reflect The Different Domain In Which A Device Is Used, E.G., Smart
	Appliances Domain (Subclass Functionrelated) Vs. Building Domain (Subclass
	Buildingrelated) Vs. Smart Grid Domain (Subclass Energyrelated). New
	Categories Can Be Defined,If Needed, To Reflect Other Differences, For
	Example Different Points Of View, Such As The Point Of View Of The Device'S
	User Vs. The Point Of View Of The Device'S Manufacturer. We Propose A List
	Of Devices That Are Relevant For The Purpose Of Saref, But This List Can Be
	Extended.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Building_Related(Device):
	"""
	A Category That Includes Devices As Described By Building Related Data
	Models, Such As Ifc And Fiemser 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Electricity(Commodity):
	"""
	A Type Of Commodity

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Energy_Related(Device):
	"""
	A Category That Considers Devices Based On Energy Consumption Information
	And Profiles To Optimize Energy Efficiency.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Function(Thing):
	"""
	The Functionality Necessary To Accomplish The Task For Which A Device Is
	Designed. A Device Can Be Designed To Perform More Than One Function.
	Functions Can Be Structured In Categories (Subclasses) That Reflect
	Different Points Of View, For Example, Considering The Specific Application
	Area For Which A Function Can Be Used (E.G., Light, Temperature, Motion,
	Heat, Power, Etc.), Or The Capability That A Function Can Support (E.G.,
	Receive, Reply, Notify, Etc.), And So Forth. 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('min|1', [[Command]])]

			self.Has_Command._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""


class Actuating_Function(Function):
	"""
	A Function That Allows To Transmit Data To Actuators, Such As Level Settings
	(E.G., Temperature) Or Binary Switching (E.G., Open/Close, On/Off)

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('min|1', [[Command]])]

			self.Has_Command._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""


class Event_Function(Function):
	"""
	A Function That Allows To Notify Another Device That A Certain Threshold
	Value Has Been Exceeded.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Notify_Command]]), ('min|1', [[Command]])]
			self.Has_Threshold_Measurement._rules = [('min|1', [[Measurement]])]

			self.Has_Command._instance_identifier = self.get_identifier()
			self.Has_Threshold_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only Notify_Command, min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""

	Has_Threshold_Measurement: RelationField = RelationField(
		name='Has_Threshold_Measurement',
		rule='min 1 Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associated With An Event Function To Notify That A Certain
	Threshold Measurement Has Been Exceeded
	"""


class Function_Related(Device):
	"""
	A Category That Considers Devices, Sensors And Their Specification In Terms
	Of Functions, States And Services

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Actuator(Function_Related):
	"""
	A Device Responsible For Moving Or Controlling A Mechanism Or System By
	Performing An Actuating Function

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Actuating_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Actuating_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Appliance(Function_Related):
	"""
	An Electrical/Mechanical Machine That Accomplish Some Household Functions,
	Such As Cleaning Or Cooking

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Gas(Commodity):
	"""
	A Type Of Commodity

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Generator(Energy_Related):
	"""
	A Type Of Energy-Related Device That Generates Energy

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Gertrude(Class1, Class2):
	"""
	Generated SemanticClass without description

	Source: 
		http://www.semanticweb.org/redin/ontologies/2020/11/untitled-ontology-25 (ParsingTesterOntology)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.attributeProp._rules = [('some', [['customDataType1']])]
			self.dataProp2._rules = [('value', [[]])]

			self.oProp1._rules = [('min|1', [[Class1]]), ('some', [[Class2], [Class4]])]
			self.objProp2._rules = [('only', [[Thing]]), ('some', [[Class1, Class2]])]
			self.objProp3._rules = [('some', [[Class3]])]
			self.objProp4._rules = [('some', [[Class1, Class2, Class3]])]
			self.objProp5._rules = [('some', [[Class1, Class2], [Class1, Class3]]), ('value', [[Individual1]])]

			self.oProp1._instance_identifier = self.get_identifier()
			self.objProp2._instance_identifier = self.get_identifier()
			self.objProp3._instance_identifier = self.get_identifier()
			self.objProp4._instance_identifier = self.get_identifier()
			self.objProp5._instance_identifier = self.get_identifier()
			self.attributeProp._instance_identifier = self.get_identifier()
			self.dataProp2._instance_identifier = self.get_identifier()

	# Data fields

	attributeProp: DataField = DataField(
		name='attributeProp',
		rule='some customDataType1',
		semantic_manager=semantic_manager)

	dataProp2: DataField = DataField(
		name='dataProp2',
		rule='value 2',
		semantic_manager=semantic_manager)

	# Relation fields

	oProp1: RelationField = RelationField(
		name='oProp1',
		rule='min 1 Class1, some (Class2 or Class4)',
		inverse_of=['objProp3'],
		semantic_manager=semantic_manager)

	objProp2: RelationField = RelationField(
		name='objProp2',
		rule='only Thing, some (Class1 and Class2)',
		semantic_manager=semantic_manager)

	objProp3: RelationField = RelationField(
		name='objProp3',
		rule='some Class3',
		inverse_of=['oProp1'],
		semantic_manager=semantic_manager)

	objProp4: RelationField = RelationField(
		name='objProp4',
		rule='some (Class1 and Class2) and Class3)',
		semantic_manager=semantic_manager)

	objProp5: RelationField = RelationField(
		name='objProp5',
		rule='some (Class1 and (Class2 or Class3)), value Individual1',
		semantic_manager=semantic_manager)


class Get_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Get_Current_Meter_Value_Command(Get_Command):
	"""
	A Type Of Get Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Get_Meter_Data_Command(Get_Command):
	"""
	A Type Of Get Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Get_Meter_History_Command(Get_Command):
	"""
	A Type Of Get Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Get_Sensing_Data_Command(Get_Command):
	"""
	A Type Of Get Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Hvac(Function_Related):
	"""
	Heating, Ventilation And Air Conditioning (Hvac) Device That Provides Indoor
	Environmental Comfort

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Comfort]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Comfort())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Comfort, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Level_Control_Function(Actuating_Function):
	"""
	An Actuating Function That Allows To Do Level Adjustments Of An Actuator In
	A Certain Range (E.G., 0%-100%), Such As Dimming A Light Or Set The Speed Of
	An Electric Motor. 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Set_Absolute_Level_Command], [Set_Relative_Level_Command], [Step_Down_Command], [Step_Up_Command]]), ('min|1', [[Command]])]

			self.Has_Command._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only (Set_Absolute_Level_Command or Set_Relative_Level_Command) or Step_Down_Command) or Step_Up_Command), min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""


class Lighting_Device(Function_Related):
	"""
	A Device Used For Illumination, Irradiation, Signaling, Or Projection

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Comfort]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Comfort())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Comfort, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Load(Energy_Related):
	"""
	A Type Of Energy-Related Device That Consumes Energy

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Measurement(Thing):
	"""
	Represents The Measured Value Made Over A Property. It Is Also Linked To The
	Unit Of Measure In Which The Value Is Expressed And The Timestamp Of The
	Measurement.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Timestamp._rules = [('only', [['dateTime']])]
			self.Has_Value._rules = [('exactly|1', [['float']])]

			self.Relates_To_Property._rules = [('only', [[Property]]), ('exactly|1', [[Property]])]

			self.Relates_To_Property._instance_identifier = self.get_identifier()
			self.Has_Timestamp._instance_identifier = self.get_identifier()
			self.Has_Value._instance_identifier = self.get_identifier()

	# Data fields

	Has_Timestamp: DataField = DataField(
		name='Has_Timestamp',
		rule='only dateTime',
		semantic_manager=semantic_manager)
	"""
	A Relationship Stating The Timestamp Of An Entity (E.G. A Measurement).
	"""

	Has_Value: DataField = DataField(
		name='Has_Value',
		rule='exactly 1 float',
		semantic_manager=semantic_manager)
	"""
	A Relationship Defining The Value Of A Certain Property, E.G., Energy Or
	Power
	"""

	# Relation fields

	Relates_To_Property: RelationField = RelationField(
		name='Relates_To_Property',
		rule='only Property, exactly 1 Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Measurement And The Property It Relates To
	"""


class Meter(Function_Related):
	"""
	A Device Built To Accurately Detect And Display A Quantity In A Form
	Readable By A Human Being. Further, A Device Of Category Saref:Meter That
	Performs A Saref:Meteringfunction.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Metering_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Metering_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Energy_Meter(Meter):
	"""
	An Energy Meter Is A Device Of Category Saref:Meter That Consists Of A
	Meter, Accomplishes The Tasks Saref:Meterreading And Saref:Energyefficiency,
	Performs The Saref:Meteringfunction And Is Used For The Purpose Of Measuring
	The Saref:Energy Property

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Energyefficiency]]), ('value', [[Meter_Reading]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('some', [[Meter]]), ('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Metering_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('some', [[Energy]]), ('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Energyefficiency())
			self.Accomplishes.add(Meter_Reading())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Energyefficiency, value Meter_Reading, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='some Meter, only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Metering_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='some Energy, only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Metering_Function(Function):
	"""
	A Function That Allows To Get Data From A Meter, Such As Current Meter
	Reading Or Instantaneous Demand

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Get_Current_Meter_Value_Command], [Get_Meter_Data_Command], [Get_Meter_History_Command]]), ('min|1', [[Command]])]
			self.Has_Meter_Reading_Type._rules = [('only', [[Commodity], [Property]])]
			self.Has_Meter_Reading._rules = [('only', [[Measurement]])]

			self.Has_Command._instance_identifier = self.get_identifier()
			self.Has_Meter_Reading_Type._instance_identifier = self.get_identifier()
			self.Has_Meter_Reading._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only (Get_Current_Meter_Value_Command or Get_Meter_Data_Command) or Get_Meter_History_Command), min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""

	Has_Meter_Reading_Type: RelationField = RelationField(
		name='Has_Meter_Reading_Type',
		rule='only (Commodity or Property)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Reading Type Of A Measurement (E.G., Water,
	Gas, Pressure , Energy , Power, Etc.)
	"""

	Has_Meter_Reading: RelationField = RelationField(
		name='Has_Meter_Reading',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Metering Function And The Measurement Of The
	Reading
	"""


class Micro_Renewable(Function_Related):
	"""
	A Device That Generates Renewable Energy From Natural Resources Such As Teh
	Sun, Wind And Water

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Energyefficiency]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Energyefficiency())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Energyefficiency, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Multimedia(Function_Related):
	"""
	A Device Designed To Display, Store, Record Or Play Multimedia Content Such
	As Audio, Images, Animation, Video 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Entertainment]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Entertainment())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Entertainment, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Network(Function_Related):
	"""
	A Device Used To Connect Other Devices In A Network, Such As Hub, Switch Or
	Router In A Local Area Network (Lan). 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Notify_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Off_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[On_Off_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only On_Off_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class On_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[On_Off_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only On_Off_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class On_Off_Function(Actuating_Function):
	"""
	An Actuating Function That Allows To Switch On And Off An Actuator

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Off_Command], [On_Command], [Toggle_Command]]), ('min|1', [[Command]])]

			self.Has_Command._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only (Off_Command or On_Command) or Toggle_Command), min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""


class Open_Close_Function(Actuating_Function):
	"""
	An Actuating Function That Allows To Open And Close A Device

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Close_Command], [Open_Command]]), ('min|1', [[Command]])]

			self.Has_Command._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only (Close_Command or Open_Command), min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""


class Open_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Open_Close_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Open_Close_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Pause_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Profile(Thing):
	"""
	A Specification Associated To A Device To Collect Information About A
	Certain Property (E.G., Energy) Or Commodity (E.G.Water) For Optimizing Its
	Usage In The Home, Office Or Building In Which The Device Is Located. This
	Specification Is About A Certain Property Or Commodity (Saref:Isabout), Can
	Be Calculated Over A Time Span (Saref:Hastime ) And Can Be Associated To
	Some Costs (Saref:Hasprice). An Example Is The Power Profile Defined In The
	Saref4Ener Extension That Can Be Associated To A Device For Optimizing The
	Energy Efficiency In The Home, Office Or Building In Which The Device Is
	Located.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Consists_Of._rules = [('only', [[Profile]])]
			self.Has_Price._rules = [('only', [[Price]])]
			self.Has_Time._rules = [('only', [[Time]])]
			self.Isabout._rules = [('only', [[Commodity], [Property]])]

			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Has_Price._instance_identifier = self.get_identifier()
			self.Has_Time._instance_identifier = self.get_identifier()
			self.Isabout._instance_identifier = self.get_identifier()

	# Relation fields

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Has_Price: RelationField = RelationField(
		name='Has_Price',
		rule='only Price',
		semantic_manager=semantic_manager)
	"""
	A Relationships Indentifying The Price Associated To An Entity
	"""

	Has_Time: RelationField = RelationField(
		name='Has_Time',
		rule='only Time',
		semantic_manager=semantic_manager)
	"""
	A Relationship To Associate Time Information To An Entity
	"""

	Isabout: RelationField = RelationField(
		name='Isabout',
		rule='only (Commodity or Property)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying What An Entity, Such As A Profile, Is About
	"""


class Property(Thing):
	"""
	Anything That Can Be Sensed, Measured Or Controlled In Households, Common
	Public Buildings Or Offices. We Propose Here A List Of Properties That Are
	Relevant For The Purpose Of Saref, But This List Can Be Extended.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Energy(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value Measured In An Energy Unit (Such As Kilowatt_Hour Or
	Watt_Hour). Furter Specializations Of The Saref:Energy Class Can Be Found In
	The Saref4Ener Extension, Where Classes Such As Energymax, Energymin And
	Energyexpected Are Defined. 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Humidity(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Humidity Unit

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Light(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Illuminance Unit (Lux)

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Motion(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Unit Of Measure For Motion

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Occupancy(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value (Saref:Hasvalue Property) That Is Measured In A Unit Of
	Measure For Occupancy

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Power(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Power Unit (Such As Watt Or Kilowatt). 
	Further Specializations Of The Saref:Power Class Can Be Found In The
	Saref4Ener Extension, Where Classes Such As Powermax, Powermin And
	Powerexpected Are Defined.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Pressure(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Pressure Unit (Bar Or Pascal)

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Price(Property):
	"""
	A Saref:Property Crelated To Some Measurements That Are Characterized By A
	Certain Value That Is Measured Using Saref:Currency

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Sensing_Function(Function):
	"""
	A Function That Allows To Transmit Data From Sensors, Such As Measurement
	Values (E.G., Temperature) Or Sensing Data (E.G., Occupancy)

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Get_Sensing_Data_Command]]), ('min|1', [[Command]])]
			self.Has_Sensing_Range_._rules = [('some', [[Measurement]])]
			self.Has_Sensor_Type._rules = [('only', [[Property]])]

			self.Has_Command._instance_identifier = self.get_identifier()
			self.Has_Sensing_Range_._instance_identifier = self.get_identifier()
			self.Has_Sensor_Type._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only Get_Sensing_Data_Command, min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""

	Has_Sensing_Range_: RelationField = RelationField(
		name='Has_Sensing_Range_',
		rule='some Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Sensing Function And A Measurement Identifying The
	Range Of A Sensor Detection
	"""

	Has_Sensor_Type: RelationField = RelationField(
		name='Has_Sensor_Type',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Sensing Type Of A Sensor Detection (I.E.,
	Temperature, Occupancy, Humidity, Motion , Smoke, Pressure, Etc.) 
	"""


class Sensor(Function_Related):
	"""
	A Device That Detects And Responds To Events Or Changes In The Physical
	Environment Such As Light, Motion, Or Temperature Changes. Further, A Device
	Of Category Saref:Sensor That Performs A Saref:Sensingfunction.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Sensing_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Sensing_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Service(Thing):
	"""
	A Service Is A Representation Of A Function To A Network That Makes The
	Function Discoverable, Registerable, Remotely Controllable By Other Devices
	In The Network. A Service Can Represent One Or More Functions. A Service Is
	Offered By A Device That Wants (A Certain Set Of) Its Function(S) To Be
	Discoverable, Registerable, Remotely Controllable By Other Devices In The
	Network. A Service Must Specify The Device That Is Offering The Service And
	The Function(S) To Be Represented.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Offered_By._rules = [('min|1', [[Device]])]
			self.Represents._rules = [('min|1', [[Function]])]

			self.Is_Offered_By._instance_identifier = self.get_identifier()
			self.Represents._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Offered_By: RelationField = RelationField(
		name='Is_Offered_By',
		rule='min 1 Device',
		inverse_of=['Offers'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Service And A Device That Offers The Service
	"""

	Represents: RelationField = RelationField(
		name='Represents',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Service And A Function.
	"""


class Set_Level_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Multi_Level_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Multi_Level_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Set_Absolute_Level_Command(Set_Level_Command):
	"""
	A Type Of Set Level Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Multi_Level_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Multi_Level_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Set_Relative_Level_Command(Set_Level_Command):
	"""
	A Type Of Set Level Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Multi_Level_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Multi_Level_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Smoke(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Unit Of Measure For Smoke

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Smoke_Sensor(Sensor):
	"""
	A Device That Consists Of A Sensor, Has Category Saref:Sensor, Performs The
	Saref:Sensingfunction And Saref:Eventfunction (Which Notifies That A Certain
	Threshold Has Been Exceeded), And Is Used For The Purpose Of Sensing A
	Property Of Type Saref:Smoke.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Safety]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('some', [[Sensor]]), ('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Event_Function]]), ('some', [[Sensing_Function]]), ('some', [[Sensing_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('some', [[Smoke]]), ('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Safety())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Safety, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='some Sensor, only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Event_Function, some Sensing_Function, some Sensing_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='some Smoke, only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Start_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Start_Stop_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Start_Stop_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Start_Stop_Function(Actuating_Function):
	"""
	An Actuating Function That Allows To Start And Stop A Device

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Has_Command._rules = [('only', [[Start_Command], [Stop_Command]]), ('min|1', [[Command]])]

			self.Has_Command._instance_identifier = self.get_identifier()

	# Relation fields

	Has_Command: RelationField = RelationField(
		name='Has_Command',
		rule='only (Start_Command or Stop_Command), min 1 Command',
		inverse_of=['Is_Command_Of'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between An Entity (Such As A Function) And A Command
	"""


class State(Thing):
	"""
	The State In Which A Device Can Be Found, E.G, On/Off/Standby, Or
	Online/Offline. We Propose Here A List Of States That Are Relevant For The
	Purpose Of Saref, But This List Can Be Extended.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Multi_Level_State(State):
	"""
	A Type Of State

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class On_Off_State(State):
	"""
	A Type Of State

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Off_State(On_Off_State):
	"""
	The State Of A Device That Is On

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class On_State(On_Off_State):
	"""
	The State Of A Device That Is Off 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Open_Close_State(State):
	"""
	A Type Of State

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Close_State(Open_Close_State):
	"""
	The State Of A Device That Is Close

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Open_State(Open_Close_State):
	"""
	The State Of A Device That Is Open 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Start_Stop_State(State):
	"""
	A Type Of State

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Start_State(Start_Stop_State):
	"""
	The State Of A Device That Is Started

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Step_Down_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Multi_Level_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Multi_Level_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Step_Up_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Multi_Level_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Multi_Level_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Stop_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[Start_Stop_State]]), ('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only Start_Stop_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Stop_State(Start_Stop_State):
	"""
	The State Of A Device That Is Stopped

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Storage(Energy_Related):
	"""
	A Type Of Energy-Related Device That Stores Energy

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Switch(Actuator):
	"""
	A Device Of Category Saref:Actuator That Performs An Actuating Function Of
	Type Saref:Onofffunction Or Saref:Openclosefunction

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Actuating_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Actuating_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Door_Switch(Switch):
	"""
	A Device Of Category Saref:Actuator That Consists Of A Switch, Accomplishes
	The Task Saref:Safety, Performs The Saref:Openclosefunction, Is Used For
	Controlling A Door, And Can Be Found In The State Saref:Openclosestate.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Safety]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('some', [[Switch]]), ('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Open_Close_Function]]), ('some', [[Actuating_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('some', [[Open_Close_State]]), ('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Safety())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Safety, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='some Switch, only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Open_Close_Function, some Actuating_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='some Open_Close_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Light_Switch(Switch):
	"""
	A Device Of Category Saref:Actuator That Consists Of A Switch, Accomplishes
	The Task Saref:Lighting, Performs The Saref:Onofffunction, Measures The
	Property Saref:Light, And Can Be Found In The State Saref:Onoffstate. It Can
	Offer A Switch On Service.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Lighting]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('some', [[Switch]]), ('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[On_Off_Function]]), ('some', [[Actuating_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('some', [[On_Off_State]]), ('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('some', [[Light]]), ('only', [[Property]])]
			self.Offers._rules = [('some', [[Switch_On_Service]]), ('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Lighting())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Lighting, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='some Switch, only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some On_Off_Function, some Actuating_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='some On_Off_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='some Light, only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='some Switch_On_Service, only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Switch_On_Service(Service):
	"""
	A Type Of Service That Represents An On/Off Function To The Network

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Offered_By._rules = [('some', [[Light_Switch]]), ('min|1', [[Device]])]
			self.Represents._rules = [('some', [[On_Off_Function]]), ('min|1', [[Function]])]

			self.Is_Offered_By._instance_identifier = self.get_identifier()
			self.Represents._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Offered_By: RelationField = RelationField(
		name='Is_Offered_By',
		rule='some Light_Switch, min 1 Device',
		inverse_of=['Offers'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Service And A Device That Offers The Service
	"""

	Represents: RelationField = RelationField(
		name='Represents',
		rule='some On_Off_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Service And A Function.
	"""


class Task(Thing):
	"""
	The Goal For Which A Device Is Designed (From A User Perspective). For
	Example, A Washing Machine Is Designed For The Task Of Washing. We Propose
	Here A List Of Tasks That Are Relevant For The Purpose Of Saref, But This
	List Can Be Extended.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Accomplished_By._rules = [('min|1', [[Device]])]

			self.Is_Accomplished_By._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Accomplished_By: RelationField = RelationField(
		name='Is_Accomplished_By',
		rule='min 1 Device',
		inverse_of=['Accomplishes'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Indentifying The Task Accomplished By A Certain Entity (E.G.,
	A Device)
	"""


class Temperature(Property):
	"""
	A Saref:Property Related To Some Measurements That Are Characterized By A
	Certain Value That Is Measured In A Temperature Unit (Degree_Celsius,
	Degree_Fahrenheit, Or Degree_Kelvin)

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Temperature_Sensor(Sensor):
	"""
	A Device That Consists Of A Sensor, Has Category Saref:Sensor, Performs The
	Saref:Sensingfunction And Is Used For The Purpose Of Sensing A Property Of
	Type Saref:Temperature

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Comfort]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('some', [[Sensor]]), ('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Sensing_Function]]), ('some', [[Sensing_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('only', [[Profile]])]
			self.Has_State._rules = [('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('some', [[Temperature]]), ('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Comfort())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Comfort, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='some Sensor, only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Sensing_Function, some Sensing_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='some Temperature, only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Time(Property):
	"""
	A Saref:Property That Allows To Specify The Time Concept In Terms Of
	Instants Or Intervals According To The Imported W3C Time Ontology.

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.Is_Controlled_By_Device._rules = [('only', [[Device]])]
			self.Is_Measured_By_Device._rules = [('only', [[Device]])]
			self.Relates_To_Measurement._rules = [('only', [[Measurement]])]

			self.Is_Controlled_By_Device._instance_identifier = self.get_identifier()
			self.Is_Measured_By_Device._instance_identifier = self.get_identifier()
			self.Relates_To_Measurement._instance_identifier = self.get_identifier()

	# Relation fields

	Is_Controlled_By_Device: RelationField = RelationField(
		name='Is_Controlled_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Control A Certain Property
	"""

	Is_Measured_By_Device: RelationField = RelationField(
		name='Is_Measured_By_Device',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Devices That Can Measure A Certain Property
	"""

	Relates_To_Measurement: RelationField = RelationField(
		name='Relates_To_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Property And The Measurements It Relates To
	"""


class Toggle_Command(Command):
	"""
	A Type Of Command

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]

			self.Acts_Upon._rules = [('only', [[State]])]
			self.Is_Command_Of._rules = [('min|1', [[Function]])]

			self.Acts_Upon._instance_identifier = self.get_identifier()
			self.Is_Command_Of._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	# Relation fields

	Acts_Upon: RelationField = RelationField(
		name='Acts_Upon',
		rule='only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A State
	"""

	Is_Command_Of: RelationField = RelationField(
		name='Is_Command_Of',
		rule='min 1 Function',
		inverse_of=['Has_Command'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Command And A Function.
	"""


class Washing_Machine(Appliance, Load):
	"""
	A Device Of Category Saref:Appliance And Saref:Load That Accomplishes The
	Task Saref:Washing, Performs An Actuating Function Of Type
	Saref:Startstopfunction, Can Be Found In The State Saref:Startstopstate, And
	Can Have A Saref:Profile That Characterizes Its Energy Consumption. 

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.Has_Description._rules = [('max|1', [['string']])]
			self.Has_Manufacturer._rules = [('max|1', [['string']])]
			self.Has_Model._rules = [('max|1', [['string']])]

			self.Accomplishes._rules = [('value', [[Washing]]), ('min|1', [[Task]])]
			self.Consists_Of._rules = [('only', [[Device]])]
			self.Controls_Property._rules = [('only', [[Property]])]
			self.Has_Function._rules = [('some', [[Start_Stop_Function]]), ('min|1', [[Function]])]
			self.Has_Profile._rules = [('some', [[Profile]]), ('only', [[Profile]])]
			self.Has_State._rules = [('some', [[Start_Stop_State]]), ('only', [[State]])]
			self.Has_Typical_Consumption._rules = [('only', [[Energy], [Power]])]
			self.Is_Used_For._rules = [('only', [[Commodity]])]
			self.Makes_Measurement._rules = [('only', [[Measurement]])]
			self.Measures_Property._rules = [('only', [[Property]])]
			self.Offers._rules = [('only', [[Service]])]

			self.Accomplishes._instance_identifier = self.get_identifier()
			self.Consists_Of._instance_identifier = self.get_identifier()
			self.Controls_Property._instance_identifier = self.get_identifier()
			self.Has_Function._instance_identifier = self.get_identifier()
			self.Has_Profile._instance_identifier = self.get_identifier()
			self.Has_State._instance_identifier = self.get_identifier()
			self.Has_Typical_Consumption._instance_identifier = self.get_identifier()
			self.Is_Used_For._instance_identifier = self.get_identifier()
			self.Makes_Measurement._instance_identifier = self.get_identifier()
			self.Measures_Property._instance_identifier = self.get_identifier()
			self.Offers._instance_identifier = self.get_identifier()
			self.Has_Description._instance_identifier = self.get_identifier()
			self.Has_Manufacturer._instance_identifier = self.get_identifier()
			self.Has_Model._instance_identifier = self.get_identifier()

			self.Accomplishes.add(Washing())

	# Data fields

	Has_Description: DataField = DataField(
		name='Has_Description',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Providing A Description Of An Entity (E.G., Device)
	"""

	Has_Manufacturer: DataField = DataField(
		name='Has_Manufacturer',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Manufacturer Of An Entity (E.G., Device)
	"""

	Has_Model: DataField = DataField(
		name='Has_Model',
		rule='max 1 string',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Model Of An Entity (E.G., Device)
	"""

	# Relation fields

	Accomplishes: RelationField = RelationField(
		name='Accomplishes',
		rule='value Washing, min 1 Task',
		inverse_of=['Is_Accomplished_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Certain Entity (E.G., A Device) And The Task It
	Accomplishes
	"""

	Consists_Of: RelationField = RelationField(
		name='Consists_Of',
		rule='only Device',
		semantic_manager=semantic_manager)
	"""
	A Relationship Indicating A Composite Entity That Consists Of Other Entities
	(E.G., A Temperature/Humidity Sensor That Consists Of A Temperature Sensor
	And A Humidity Sensor)
	"""

	Controls_Property: RelationField = RelationField(
		name='Controls_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Controlled By A Certain
	Device
	"""

	Has_Function: RelationField = RelationField(
		name='Has_Function',
		rule='some Start_Stop_Function, min 1 Function',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of Function Of A Device
	"""

	Has_Profile: RelationField = RelationField(
		name='Has_Profile',
		rule='some Profile, only Profile',
		semantic_manager=semantic_manager)
	"""
	A Relationship Associating A Profile To A Certain Entity (E.G., A Device)
	"""

	Has_State: RelationField = RelationField(
		name='Has_State',
		rule='some Start_Stop_State, only State',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Type Of State Of A Device
	"""

	Has_Typical_Consumption: RelationField = RelationField(
		name='Has_Typical_Consumption',
		rule='only (Energy or Power)',
		semantic_manager=semantic_manager)
	"""
	A Relationship Identifying The Typical (Energy Or Power) Consumption Of A
	Device
	"""

	Is_Used_For: RelationField = RelationField(
		name='Is_Used_For',
		rule='only Commodity',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Purpose For Which A Device Is Used For (E.G.,
	Controlling A Commodity)
	"""

	Makes_Measurement: RelationField = RelationField(
		name='Makes_Measurement',
		rule='only Measurement',
		semantic_manager=semantic_manager)
	"""
	A Relation Between A Device And The Measurements It Makes. Such Measurement
	Will Link Together The Value Of The Measurement, Its Unit Of Measure And The
	Property To Which It Relates.
	"""

	Measures_Property: RelationField = RelationField(
		name='Measures_Property',
		rule='only Property',
		semantic_manager=semantic_manager)
	"""
	A Relationship Specifying The Property That Can Be Measured By A Certain
	Device
	"""

	Offers: RelationField = RelationField(
		name='Offers',
		rule='only Service',
		inverse_of=['Is_Offered_By'],
		semantic_manager=semantic_manager)
	"""
	A Relationship Between A Device And A Service
	"""


class Water(Commodity):
	"""
	A Type Of Commodity

	Source: 
		https://w3id.org/saref (saref.ttl)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


# ---------Individuals--------- #


class Individual1(SemanticIndividual):
	_parent_classes: List[type] = [Class2, Class1]


class Individual2(SemanticIndividual):
	_parent_classes: List[type] = [Class1]


class Individual3(SemanticIndividual):
	_parent_classes: List[type] = [Class2, Class1, Class3]


class Individual4(SemanticIndividual):
	_parent_classes: List[type] = [Class1, Class2]


class United_States_Dollar(SemanticIndividual):
	_parent_classes: List[type] = [Currency]


class Bar(SemanticIndividual):
	_parent_classes: List[type] = [Pressure_Unit]


class Degree_Celsius(SemanticIndividual):
	_parent_classes: List[type] = [Temperature_Unit]


class Degree_Fahrenheit(SemanticIndividual):
	_parent_classes: List[type] = [Temperature_Unit]


class Euro(SemanticIndividual):
	_parent_classes: List[type] = [Currency]


class Kelvin(SemanticIndividual):
	_parent_classes: List[type] = [Temperature_Unit]


class Kilowatt(SemanticIndividual):
	_parent_classes: List[type] = [Power_Unit]


class Kilowatt_Hour(SemanticIndividual):
	_parent_classes: List[type] = [Energy_Unit]


class Lux(SemanticIndividual):
	_parent_classes: List[type] = [Illuminance_Unit]


class Pascal(SemanticIndividual):
	_parent_classes: List[type] = [Pressure_Unit]


class Great_Britain_Pound_Sterling(SemanticIndividual):
	_parent_classes: List[type] = [Currency]


class Watt(SemanticIndividual):
	_parent_classes: List[type] = [Power_Unit]


class Cleaning(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Close(SemanticIndividual):
	_parent_classes: List[type] = [Close_Command, Close_State]


class Comfort(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Drying(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Energyefficiency(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Entertainment(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Get_Current_Meter_Value(SemanticIndividual):
	_parent_classes: List[type] = [Get_Current_Meter_Value_Command]


class Get_Meter_Data(SemanticIndividual):
	_parent_classes: List[type] = [Get_Meter_Data_Command]


class Get_Meter_History(SemanticIndividual):
	_parent_classes: List[type] = [Get_Meter_History_Command]


class Get_Sensing_Data(SemanticIndividual):
	_parent_classes: List[type] = [Get_Sensing_Data_Command]


class Lighting(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Meter_Reading(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Notify(SemanticIndividual):
	_parent_classes: List[type] = [Notify_Command]


class Off_(SemanticIndividual):
	_parent_classes: List[type] = [Off_Command, Off_State]


class On(SemanticIndividual):
	_parent_classes: List[type] = [On_Command, On_State]


class Open(SemanticIndividual):
	_parent_classes: List[type] = [Open_Command, Open_State]


class Pause(SemanticIndividual):
	_parent_classes: List[type] = [Pause_Command]


class Safety(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Set_Absolute_Level(SemanticIndividual):
	_parent_classes: List[type] = [Set_Absolute_Level_Command]


class Set_Relative_Level(SemanticIndividual):
	_parent_classes: List[type] = [Set_Relative_Level_Command]


class Start(SemanticIndividual):
	_parent_classes: List[type] = [Start_Command, Start_State]


class Step_Down(SemanticIndividual):
	_parent_classes: List[type] = [Step_Down_Command]


class Step_Up(SemanticIndividual):
	_parent_classes: List[type] = [Step_Up_Command]


class Stop(SemanticIndividual):
	_parent_classes: List[type] = [Stop_Command, Stop_State]


class Toggle(SemanticIndividual):
	_parent_classes: List[type] = [Toggle_Command]


class Washing(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Wellbeing(SemanticIndividual):
	_parent_classes: List[type] = [Task]


class Watt_Hour(SemanticIndividual):
	_parent_classes: List[type] = [Energy_Unit]


# ---------Datatypes--------- #
semantic_manager.datatype_catalogue = {
	'customDataType1': {
		'type': 'enum',
		'enum_values': ['0', '15', '30'],
	},
	'customDataType2': {
		'type': 'string',
	},
	'customDataType3': {
		'type': 'string',
	},
	'customDataType4': {
		'type': 'enum',
		'enum_values': ['1', '2', '3', '4'],
	},
	'rational': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'real': {
		'type': 'number',
	},
	'PlainLiteral': {
		'type': 'string',
	},
	'XMLLiteral': {
		'type': 'string',
	},
	'Literal': {
		'type': 'string',
	},
	'anyURI': {
		'type': 'string',
	},
	'base64Binary': {
		'type': 'string',
	},
	'boolean': {
		'type': 'enum',
		'enum_values': ['True', 'False'],
	},
	'byte': {
		'type': 'number',
		'number_range_min': -128,
		'number_range_max': 127,
		'number_has_range': True,
	},
	'dateTime': {
		'type': 'date',
	},
	'dateTimeStamp': {
		'type': 'date',
	},
	'decimal': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'double': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'float': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'hexBinary': {
		'allowed_chars': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
		'type': 'string',
	},
	'int': {
		'type': 'number',
		'number_range_min': -2147483648,
		'number_range_max': 2147483647,
		'number_has_range': True,
	},
	'integer': {
		'type': 'number',
	},
	'language': {
		'type': 'string',
	},
	'long': {
		'type': 'number',
		'number_range_min': -9223372036854775808,
		'number_range_max': 9223372036854775807,
		'number_has_range': True,
	},
	'Name': {
		'type': 'string',
	},
	'NCName': {
		'forbidden_chars': [':'],
		'type': 'string',
	},
	'negativeInteger': {
		'type': 'number',
		'number_range_max': -1,
		'number_has_range': True,
	},
	'NMTOKEN': {
		'type': 'string',
	},
	'nonNegativeInteger': {
		'type': 'number',
		'number_range_min': 0,
		'number_has_range': True,
	},
	'nonPositiveInteger': {
		'type': 'number',
		'number_range_max': -1,
		'number_has_range': True,
	},
	'normalizedString': {
		'type': 'string',
	},
	'positiveInteger': {
		'type': 'number',
		'number_range_min': 0,
		'number_has_range': True,
	},
	'short': {
		'type': 'number',
		'number_range_min': -32768,
		'number_range_max': 32767,
		'number_has_range': True,
	},
	'string': {
		'type': 'string',
	},
	'token': {
		'type': 'string',
	},
	'unsignedByte': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 255,
		'number_has_range': True,
	},
	'unsignedInt': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 4294967295,
		'number_has_range': True,
	},
	'unsignedLong': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 18446744073709551615,
		'number_has_range': True,
	},
	'unsignedShort': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 65535,
		'number_has_range': True,
	},
}


class customDataType1(str, Enum):
	value_0 = '0'
	value_15 = '15'
	value_30 = '30'


class customDataType4(str, Enum):
	value_1 = '1'
	value_2 = '2'
	value_3 = '3'
	value_4 = '4'


# ---------Class Dict--------- #

semantic_manager.class_catalogue = {
	'Actuating_Function': Actuating_Function,
	'Actuator': Actuator,
	'Appliance': Appliance,
	'Building_Related': Building_Related,
	'Class1': Class1,
	'Class123': Class123,
	'Class13': Class13,
	'Class1a': Class1a,
	'Class1aa': Class1aa,
	'Class1b': Class1b,
	'Class2': Class2,
	'Class3': Class3,
	'Class3a': Class3a,
	'Class3aa': Class3aa,
	'Class4': Class4,
	'Close_Command': Close_Command,
	'Close_State': Close_State,
	'Coal': Coal,
	'Command': Command,
	'Commodity': Commodity,
	'Currency': Currency,
	'Device': Device,
	'Door_Switch': Door_Switch,
	'Electricity': Electricity,
	'Energy': Energy,
	'Energy_Meter': Energy_Meter,
	'Energy_Related': Energy_Related,
	'Energy_Unit': Energy_Unit,
	'Event_Function': Event_Function,
	'Function': Function,
	'Function_Related': Function_Related,
	'Gas': Gas,
	'Generator': Generator,
	'Gertrude': Gertrude,
	'Get_Command': Get_Command,
	'Get_Current_Meter_Value_Command': Get_Current_Meter_Value_Command,
	'Get_Meter_Data_Command': Get_Meter_Data_Command,
	'Get_Meter_History_Command': Get_Meter_History_Command,
	'Get_Sensing_Data_Command': Get_Sensing_Data_Command,
	'Humidity': Humidity,
	'Hvac': Hvac,
	'Illuminance_Unit': Illuminance_Unit,
	'Level_Control_Function': Level_Control_Function,
	'Light': Light,
	'Light_Switch': Light_Switch,
	'Lighting_Device': Lighting_Device,
	'Load': Load,
	'Measurement': Measurement,
	'Meter': Meter,
	'Metering_Function': Metering_Function,
	'Micro_Renewable': Micro_Renewable,
	'Motion': Motion,
	'Multi_Level_State': Multi_Level_State,
	'Multimedia': Multimedia,
	'Network': Network,
	'Notify_Command': Notify_Command,
	'Occupancy': Occupancy,
	'Off_Command': Off_Command,
	'Off_State': Off_State,
	'On_Command': On_Command,
	'On_Off_Function': On_Off_Function,
	'On_Off_State': On_Off_State,
	'On_State': On_State,
	'Open_Close_Function': Open_Close_Function,
	'Open_Close_State': Open_Close_State,
	'Open_Command': Open_Command,
	'Open_State': Open_State,
	'Pause_Command': Pause_Command,
	'Power': Power,
	'Power_Unit': Power_Unit,
	'Pressure': Pressure,
	'Pressure_Unit': Pressure_Unit,
	'Price': Price,
	'Profile': Profile,
	'Property': Property,
	'Sensing_Function': Sensing_Function,
	'Sensor': Sensor,
	'Service': Service,
	'Set_Absolute_Level_Command': Set_Absolute_Level_Command,
	'Set_Level_Command': Set_Level_Command,
	'Set_Relative_Level_Command': Set_Relative_Level_Command,
	'Smoke': Smoke,
	'Smoke_Sensor': Smoke_Sensor,
	'Start_Command': Start_Command,
	'Start_State': Start_State,
	'Start_Stop_Function': Start_Stop_Function,
	'Start_Stop_State': Start_Stop_State,
	'State': State,
	'Step_Down_Command': Step_Down_Command,
	'Step_Up_Command': Step_Up_Command,
	'Stop_Command': Stop_Command,
	'Stop_State': Stop_State,
	'Storage': Storage,
	'Switch': Switch,
	'Switch_On_Service': Switch_On_Service,
	'Task': Task,
	'Temperature': Temperature,
	'Temperature_Sensor': Temperature_Sensor,
	'Temperature_Unit': Temperature_Unit,
	'Thing': Thing,
	'Time': Time,
	'Toggle_Command': Toggle_Command,
	'Washing_Machine': Washing_Machine,
	'Water': Water,
	}


semantic_manager.individual_catalogue = {
	'Individual1': Individual1,
	'Individual2': Individual2,
	'Individual3': Individual3,
	'Individual4': Individual4,
	'United_States_Dollar': United_States_Dollar,
	'Bar': Bar,
	'Degree_Celsius': Degree_Celsius,
	'Degree_Fahrenheit': Degree_Fahrenheit,
	'Euro': Euro,
	'Kelvin': Kelvin,
	'Kilowatt': Kilowatt,
	'Kilowatt_Hour': Kilowatt_Hour,
	'Lux': Lux,
	'Pascal': Pascal,
	'Great_Britain_Pound_Sterling': Great_Britain_Pound_Sterling,
	'Watt': Watt,
	'Cleaning': Cleaning,
	'Close': Close,
	'Comfort': Comfort,
	'Drying': Drying,
	'Energyefficiency': Energyefficiency,
	'Entertainment': Entertainment,
	'Get_Current_Meter_Value': Get_Current_Meter_Value,
	'Get_Meter_Data': Get_Meter_Data,
	'Get_Meter_History': Get_Meter_History,
	'Get_Sensing_Data': Get_Sensing_Data,
	'Lighting': Lighting,
	'Meter_Reading': Meter_Reading,
	'Notify': Notify,
	'Off_': Off_,
	'On': On,
	'Open': Open,
	'Pause': Pause,
	'Safety': Safety,
	'Set_Absolute_Level': Set_Absolute_Level,
	'Set_Relative_Level': Set_Relative_Level,
	'Start': Start,
	'Step_Down': Step_Down,
	'Step_Up': Step_Up,
	'Stop': Stop,
	'Toggle': Toggle,
	'Washing': Washing,
	'Wellbeing': Wellbeing,
	'Watt_Hour': Watt_Hour,
	}
