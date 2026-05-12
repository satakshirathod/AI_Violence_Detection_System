import h5py
import json

MODEL_PATH = "violence_detection_model.h5"

with h5py.File(MODEL_PATH, "r+") as f:
    model_config = f.attrs.get("model_config")

    if model_config is None:
        print("No model_config found in model file.")
        exit()

    if isinstance(model_config, bytes):
        model_config = model_config.decode("utf-8")

    config = json.loads(model_config)

    def remove_quantization_config(obj):
        if isinstance(obj, dict):
            obj.pop("quantization_config", None)

            for value in obj.values():
                remove_quantization_config(value)

        elif isinstance(obj, list):
            for item in obj:
                remove_quantization_config(item)

    remove_quantization_config(config)

    f.attrs.modify("model_config", json.dumps(config).encode("utf-8"))

print("Model fixed successfully!")