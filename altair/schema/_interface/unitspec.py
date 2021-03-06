# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .config import Config
from .data import Data
from .mark import Mark
from .transform import Transform
from .unitencoding import UnitEncoding


class UnitSpec(BaseObject):
    """Wrapper for Vega-Lite UnitSpec definition.
    
    Attributes
    ----------
    config: Config
        Configuration object.
    data: Data
        An object describing the data source.
    description: Unicode
        An optional description of this mark for commenting purpose.
    encoding: UnitEncoding
        A key-value mapping between encoding channels and definition of fields.
    mark: Mark
        The mark type.
    name: Unicode
        Name of the visualization for later reference.
    transform: Transform
        An object describing filter and new field calculation.
    """
    config = T.Instance(Config, allow_none=True, default_value=None, help="""Configuration object.""")
    data = T.Instance(Data, allow_none=True, default_value=None, help="""An object describing the data source.""")
    description = T.Unicode(allow_none=True, default_value=None, help="""An optional description of this mark for commenting purpose.""")
    encoding = T.Instance(UnitEncoding, allow_none=True, default_value=None, help="""A key-value mapping between encoding channels and definition of fields.""")
    mark = Mark(allow_none=True, default_value=None, help="""The mark type.""")
    name = T.Unicode(allow_none=True, default_value=None, help="""Name of the visualization for later reference.""")
    transform = T.Instance(Transform, allow_none=True, default_value=None, help="""An object describing filter and new field calculation.""")
    
    def __init__(self, config=None, data=None, description=None, encoding=None, mark=None, name=None, transform=None, **kwargs):
        kwds = dict(config=config, data=data, description=description, encoding=encoding, mark=mark, name=name, transform=transform)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(UnitSpec, self).__init__(**kwargs)