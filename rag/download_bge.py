from modelscope import snapshot_download


model_dir = snapshot_download(
    model_id="AI-ModelScope/bge-small-zh-v1.5",
    cache_dir="/root/autodl-tmp/hazard-agent/models"
)

print(model_dir)