"""
This module defines the default metadata and data dictionaries for each explanation method.
Note that the "name" field is automatically populated upon initialization of the corresponding
Explainer class.
"""
# Anchors
DEFAULT_META_ANCHOR = {"name": None,
                       "type": ["blackbox"],
                       "explanations": ["local"],
                       "params": {},
                       "version": None}  # type: dict
"""
Default anchor metadata.
"""

DEFAULT_DATA_ANCHOR = {"anchor": [],
                       "precision": None,
                       "coverage": None,
                       "raw": None}  # type: dict
"""
Default anchor data.
"""

DEFAULT_DATA_ANCHOR_IMG = {"anchor": [],
                           "segments": None,
                           "precision": None,
                           "coverage": None,
                           "raw": None}  # type: dict
"""
Default anchor image data.
"""

# CEM
DEFAULT_META_CEM = {"name": None,
                    "type": ["blackbox", "tensorflow", "keras"],
                    "explanations": ["local"],
                    "params": {},
                    "version": None}  # type: dict
"""
Default CEM metadata.
"""
DEFAULT_DATA_CEM = {"PN": None,
                    "PP": None,
                    "PN_pred": None,
                    "PP_pred": None,
                    "grads_graph": None,
                    "grads_num": None,
                    "X": None,
                    "X_pred": None
                    }  # type: dict
"""
Default CEM data.
"""

# Counterfactuals
DEFAULT_META_CF = {"name": None,
                   "type": ["blackbox", "tensorflow", "keras"],
                   "explanations": ["local"],
                   "params": {},
                   "version": None}  # type: dict
"""
Default counterfactual metadata.
"""

DEFAULT_DATA_CF = {"cf": None,
                   "all": [],
                   "orig_class": None,
                   "orig_proba": None,
                   "success": None}  # type: dict
"""
Default counterfactual data.
"""

# CFProto
DEFAULT_META_CFP = {"name": None,
                    "type": ["blackbox", "tensorflow", "keras"],
                    "explanations": ["local"],
                    "params": {},
                    "version": None}  # type: dict
"""
Default counterfactual prototype metadata.
"""

DEFAULT_DATA_CFP = {"cf": None,
                    "all": [],
                    "orig_class": None,
                    "orig_proba": None,
                    "id_proto": None
                    }  # type: dict
"""
Default counterfactual prototype metadata.
"""

# KernelSHAP
KERNEL_SHAP_PARAMS = [
    'link',
    'group_names',
    'grouped',
    'groups',
    'weights',
    'summarise_background',
    'summarise_result',
    'transpose',
    'kwargs',
]
"""
KernelShap parameters updated and returned in ``metadata['params']``.
See :py:class:`alibi.explainers.shap_wrappers.KernelShap`.
"""

DEFAULT_META_KERNEL_SHAP = {
    "name": None,
    "type": ["blackbox"],
    "task": None,
    "explanations": ["local", "global"],
    "params": dict.fromkeys(KERNEL_SHAP_PARAMS),
    "version": None
}  # type: dict
"""
Default KernelShap metadata.
"""

DEFAULT_DATA_KERNEL_SHAP = {
    "shap_values": [],
    "expected_value": [],
    "categorical_names": {},
    "feature_names": [],
    "raw": {
        "raw_prediction": None,
        "prediction": None,
        "instances": None,
        "importances": {},
    }
}  # type: dict
"""
Default KernelShap data.
"""

# ALE
DEFAULT_META_ALE = {
    "name": None,
    "type": ["blackbox"],
    "explanations": ["global"],
    "params": {},
    "version": None
}  # type: dict
"""
Default ALE metadata.
"""

DEFAULT_DATA_ALE = {
    "ale_values": [],
    "constant_value": None,
    "ale0": [],
    "feature_values": [],
    "feature_names": None,
    "target_names": None,
    "feature_deciles": None
}  # type: dict
"""
Default ALE data.
"""

# TreeShap
TREE_SHAP_PARAMS = [
    'model_output',
    'summarise_background',
    'summarise_result',
    'approximate',
    'interactions',
    'explain_loss',
    'algorithm',
    'kwargs'
]
"""
TreeShap parameters updated and returned in ``metadata['params']``.
See :py:class:`alibi.explainers.shap_wrappers.TreeShap`.
"""

DEFAULT_META_TREE_SHAP = {
    "name": None,
    "type": ["whitebox"],
    "task": None,  # updates with 'classification' or 'regression'
    "explanations": ["local", "global"],
    "params": dict.fromkeys(TREE_SHAP_PARAMS),
    "version": None
}  # type: dict
"""
Default TreeShap metadata.
"""

DEFAULT_DATA_TREE_SHAP = {
    "shap_values": [],
    "shap_interaction_values": [],
    "expected_value": [],
    "categorical_names": {},
    "feature_names": [],
    "raw": {
        "raw_prediction": None,
        "loss": None,
        "prediction": None,
        "instances": None,
        "labels": None,
        "importances": {},
    }
}  # type: dict

"""
Default TreeShap data.
"""

# Integrated gradients
DEFAULT_META_INTGRAD = {
    "name": None,
    "type": ["whitebox"],
    "explanations": ["local"],
    "params": {},
    "version": None
}  # type: dict
"""
Default IntegratedGradients metadata.
"""

DEFAULT_DATA_INTGRAD = {
    "attributions": None,
    "X": None,
    "forward_kwargs": None,
    "baselines": None,
    "predictions": None,
    "deltas": None
}  # type: dict
"""
Default IntegratedGradients data.
"""

DEFAULT_META_CFRL = {"name": None,
                     "type": ["blackbox"],
                     "explanations": ["local"],
                     "params": {},
                     "version": None}  # type: dict
"""
Default CounterfactualRL metadata.
"""

DEFAULT_DATA_CFRL = {"orig": None,
                     "cf": None,
                     "target": None,
                     "condition": None}  # type: dict
"""
Default CounterfactualRL data.
"""

# Similarity methods
DEFAULT_META_SIM = {"name": None,
                    "type": ["whitebox"],
                    "explanations": ["local"],
                    "params": {},
                    "version": None}  # type: dict
"""
Default SimilarityExplainer metadata.
"""

DEFAULT_DATA_SIM = {"scores": None,
                    "ordered_indices": None,
                    "most_similar": None,
                    "least_similar": None}  # type: dict
"""
Default SimilarityExplainer data.
"""

DEFAULT_META_PROTOSELECT = {"name": None,
                            "type": ["data"],
                            "explanation": ["global"],
                            "params": {},
                            "version": None}  # type: dict
"""
Default ProtoSelect metadata.
"""

DEFAULT_DATA_PROTOSELECT = {"prototypes": None,
                            "prototype_indices": None,
                            "prototype_labels": None}  # type: dict
"""
Default ProtoSelect data.
"""

# PartialDependence
DEFAULT_META_PD = {
    "name": None,
    "type": ["blackbox"],
    "explanations": ["global"],
    "params": {},
    "version": None
}  # type: dict
"""
Default PartialDependence metadata.
"""

DEFAULT_DATA_PD = {
    "feature_deciles": None,
    "pd_values": None,
    "ice_values": None,
    "feature_values": None,
    "feature_names": None,
}  # type: dict
"""
Default PartialDependence data.
"""

# PartialDependenceVariance
DEFAULT_META_PDVARIANCE = {
    "name": None,
    "type": ["blackbox"],
    "explanations": ["global"],
    "params": {},
    "version": None
}  # type: dict
"""
Default PartialDependenceVariance metadata.
"""

DEFAULT_DATA_PDVARIANCE = {
    "feature_deciles": None,
    "pd_values": None,
    "feature_values": None,
    "feature_names": None,
    "feature_importance": None,
    "feature_interaction": None,
    "conditional_importance": None,
    "conditional_importance_values": None
}  # type: dict
"""
Default PartialDependenceVariance data.
"""

# PermutationImportance
DEFAULT_META_PERMUTATION_IMPORTANCE = {
    "name": None,
    "type": ["blackbox"],
    "explanations": ["global"],
    "params": {},
    "version": None
}  # type: dict
"""
Default PermutationImportance metadata.
"""

DEFAULT_DATA_PERMUTATION_IMPORTANCE = {
    "feature_names": None,
    "metric_names": None,
    "feature_importance": None,
}  # type: dict
"""
Default PermutationImportance data.
"""
