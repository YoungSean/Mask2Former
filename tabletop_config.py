def add_tabletop_config(cfg):
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
    cfg.SOLVER.IMS_PER_BATCH = 4
    cfg.INPUT.MASK_FORMAT = "bitmask"  # alternative: "polygon"
    cfg.MODEL.MASK_ON = True
    cfg.DATASETS.TRAIN = ("tabletop_object_train",)
    # cfg.DATASETS.TEST= ("tabletop_object_test",)
    cfg.DATASETS.TEST = ()
    cfg.INPUT.MIN_SIZE_TRAIN = (480,)
    cfg.INPUT.MIN_SIZE_TEST = (480,)
    cfg.INPUT.MAX_SIZE_TRAIN = 800
    cfg.INPUT.MAX_SIZE_TEST = 800
    cfg.SOLVER.MAX_ITER = 2200
    #cfg.INPUT.CROP.ENABLED = False
    cfg.MODEL.WEIGHTS = "./output/model_final.pth"
    cfg.INPUT.MIN_SIZE_TEST = 0
    cfg.MODEL.MASK_FORMER.TEST.SEMANTIC_ON = False
    cfg.MODEL.MASK_FORMER.TEST.INSTANCE_ON = True

    # Some configs to be modified
    cfg.DATALOADER.NUM_WORKERS = 16 # on markov server, try 64