# model settings
# Only for evaluation
model_cfg = dict(
    backbone=dict(
        type='SwinTransformer',
        arch='base',
        img_size=384,
        stage_cfgs=dict(block_cfgs=dict(window_size=12))),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=2,
        in_channels=1024,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5)))

# dataloader pipeline
train_pipeline = (
    dict(type='CenterCrop', size=1600),
    dict(type='RandomResizedCrop', size=384),
    dict(type='RandomHorizontalFlip', p=0.5),
dict(type='RandAugment', num_ops=1,magnitude=8),
    dict(type='ToTensor'),
    dict(type='Normalize', mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
dict(type='RandomErasing',p=0.25,ratio=(0.02,1/3))
)
val_pipeline = (
        dict(type='CenterCrop', size=1600),
    dict(type='Resize', size=384),
    dict(type='ToTensor'),
    dict(type='Normalize', mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
)

# train
data_cfg = dict(
    batch_size = 12,
    num_workers = 4,
    train = dict(
        pretrained_flag = True,
        pretrained_weights = 'datas/swin_base_patch4_window12_384_22kto1k-d59b0d1d.pth',
        freeze_flag = False,
        freeze_layers = ('backbone',),
        epoches = 150,
    ),
    test=dict(
        ckpt = 'logs/SwinTransformer/2022-10-10-15-22-01/Val_Epoch077-Acc90.625.pth',
        metrics = ['accuracy', 'precision', 'recall', 'f1_score', 'confusion'],
        metric_options = dict(
            topk = (1,5),
            thrs = None,
            average_mode='none'
    )
    )
)

# batch 32
# lr = 5e-4 * 32 / 64
# optimizer
optimizer_cfg = dict(
    type='AdamW',
    lr=5e-4 * 8/ 64,
    weight_decay=0.0005,
    eps=1e-8,
    betas=(0.9, 0.999),)

# learning 
lr_config = dict(
    type='CosineAnnealingLrUpdater',
    by_epoch=True,
    min_lr_ratio=1e-3,
    warmup='linear',
    warmup_ratio=1e-3,
    warmup_iters=2,
    warmup_by_epoch=True
)
