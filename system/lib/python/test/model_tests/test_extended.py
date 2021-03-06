import unittest, os
from model.extended import AttributeModel, ExtendedModel
from helper.install import InstallHelper
from helper.db import DBHelper, DBSelect

class SampleExtModel(ExtendedModel):
    """Sample model for ExtendedModel testing"""

    _table = 'sample'
    _pk = '_id'

    def _init(self):
        """Internal constuctor"""
        self._group = 'Default'
        super(SampleExtModel, self)._init()

    def set_attribute_group(self, group):
        """Set attribute group name"""
        self._group = group
        return self

    def get_attribute_group(self):
        """Get attribute group name"""
        return self._group

    @classmethod
    def _install(cls):
        """Install base table and attributes"""

        ExtendedModel.install()
        table = DBHelper.quote_identifier(cls._table)

        return (
            lambda: (
                DBHelper().query("""
                    CREATE TABLE %s (
                        "_id"    INTEGER PRIMARY KEY AUTOINCREMENT,
                        "static" TEXT NOT NULL DEFAULT ''
                    )
                """ % table),
                SampleExtModel._create_attribute_tables(),
                SampleExtModel._create_attribute(
                    'sample_attr_1', 'Sample Attribute #1', 'integer', 'Default'),
                SampleExtModel._create_attribute(
                    'sample_attr_2', 'Sample Attribute #2', 'text', 'Default'),
                SampleExtModel._create_attribute(
                    'sample_attr_3', 'Sample Attribute #3', 'real', 'Not Default')
            ),
        )

class TestExtendedModel(unittest.TestCase):
    """ExtendedModel test case class"""

    def setUp(self):
        """ExtendedModel test set up"""

        if os.path.isfile('/tmp/box.db'):
            os.unlink('/tmp/box.db')
        DBHelper().set_db('/tmp/box.db')
        InstallHelper.reset()
        SampleExtModel.install()

    def tearDown(self):
        """Clean up after test"""

        InstallHelper.reset()
        DBHelper().set_db(None)
        os.unlink('/tmp/box.db')
        SampleExtModel._group_index = {} # clear cached attr groups

    def test_get_attributes(self):
        """Test ExtendedModel.get_attributes"""

        sample = SampleExtModel()
        attrs = sample.get_attributes()
        self.assertEqual(len(attrs), 2)
        for attr in attrs:
            self.assertTrue(attr['code'] in ('sample_attr_1', 'sample_attr_2'))
        sample.set_attribute_group('Not Default')
        attrs = sample.get_attributes()
        self.assertEqual(len(attrs), 1)
        self.assertEqual(attrs[0]['code'], 'sample_attr_3')

    def test_save(self):
        """Test ExtendedModel.save"""

        pk = SampleExtModel({
            'static': 'static_value',
            'sample_attr_1': 57,
            'sample_attr_2': 'fifty-seven',
            'sample_attr_3': 57.0
        }).save().id()

        select = DBSelect(
            ('sample_attribute_integer', 'v'),
            ('value',)
        ).join(('attribute', 'a'), 'v.attribute = a._id', ()
        ).where('a.code = ?', 'sample_attr_1'
        ).where('a.parent = ?', 'sample'
        ).where('a.type = ?', 'integer'
        ).where('v.parent = ?', pk
        ).limit(1)
        self.assertEqual(select.query().fetchone()['value'], 57)

        select = DBSelect(
            ('sample_attribute_text', 'v'),
            ('value',)
        ).join(('attribute', 'a'), 'v.attribute = a._id', ()
        ).where('a.code = ?', 'sample_attr_2'
        ).where('a.parent = ?', 'sample'
        ).where('a.type = ?', 'text'
        ).where('v.parent = ?', pk
        ).limit(1)
        self.assertEqual(select.query().fetchone()['value'], 'fifty-seven')

        select = DBSelect(
            ('sample_attribute_real', 'v'),
            ('value',)
        ).join(('attribute', 'a'), 'v.attribute = a._id', ()
        ).where('a.code = ?', 'sample_attr_3'
        ).where('a.parent = ?', 'sample'
        ).where('a.type = ?', 'real'
        ).where('v.parent = ?', pk
        ).limit(1)
        # should fail since 'sample_attr_3' is in another group
        self.assertIsNone(select.query().fetchone())

    def test_load(self):
        """Test ExtendedModel.load"""

        pk = SampleExtModel({
            'static': 'static_value',
            'sample_attr_1': 57,
            'sample_attr_2': 'fifty-seven',
            'sample_attr_3': 57.0
        }).save().id()

        sample = SampleExtModel().load(pk)
        self.assertEqual(sample.id(), pk)
        self.assertEqual(sample.static(), 'static_value')
        self.assertEqual(sample.sample_attr_1(), 57)
        self.assertEqual(sample.sample_attr_2(), 'fifty-seven')
        self.assertIsNone(sample.sample_attr_3())

    def test_delete(self):
        """Test ExtendedModel.delete"""

        pk = SampleExtModel({
            'static': 'something',
            'sample_attr_1': 57
        }).save().id()

        # make sure model delete affects attribute tables
        int_attrs = DBSelect('sample_attribute_integer').query().fetchall()
        self.assertEqual(len(int_attrs), 1)
        SampleExtModel().load(pk).delete()
        int_attrs = DBSelect('sample_attribute_integer').query().fetchall()
        self.assertEqual(len(int_attrs), 0)

    def test_modelset_add_filter(self):
        """Test ExtendedModelSet filter function"""

        pk10 = SampleExtModel({
            'static': 'static_10',
            'sample_attr_1': 10,
            'sample_attr_2': 'ten'
        }).save().id()

        pk20 = SampleExtModel({
            'static': 'static_20',
            'sample_attr_1': 20,
            'sample_attr_2': 'twenty'
        }).save().id()

        pk30 = SampleExtModel({
            'static': 'static_30',
            'sample_attr_2': 'thirty'
        }).save().id()

        test_null = SampleExtModel.all().add_filter(
                        'sample_attr_1', {'null': True})
        self.assertEqual(len(test_null), 1)
        self.assertEqual(test_null[0].id(), pk30)
        test_or = SampleExtModel.all().add_filter(
            ('sample_attr_1', 'sample_attr_2'),
            (10,              {'like': '%ty%'})
        )
        self.assertEqual(len(test_or), 3)
        test_and = SampleExtModel.all(
                        ).add_filter('sample_attr_1', {'><': (5, 25)}
                        ).add_filter('sample_attr_2', {'like': '%en%'})
        self.assertEqual(len(test_and), 2)
        self.assertIn(test_and[0].id(), (pk10, pk20))
        self.assertIn(test_and[1].id(), (pk10, pk20))

