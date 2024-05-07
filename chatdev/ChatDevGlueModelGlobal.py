from GlueModel import GlueModel

global_glue_model: GlueModel = None


# Workaround to avoid refactor to pas in the model
def set(glue_model: GlueModel):
    global global_glue_model
    global_glue_model = glue_model


def get() -> GlueModel:
    global global_glue_model
    return global_glue_model
