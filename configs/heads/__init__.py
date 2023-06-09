import imp
from .linear_head import LinearClsHead
from .stacked_head import StackedLinearClsHead
from .cls_head import ClsHead
from .vision_transformer_head import VisionTransformerClsHead
from .deit_head import DeiTClsHead
from .conformer_head import ConformerHead

__all__ = ['LinearClsHead', 'StackedLinearClsHead','ClsHead', 'VisionTransformerClsHead', 'DeiTClsHead', 'ConformerHead']