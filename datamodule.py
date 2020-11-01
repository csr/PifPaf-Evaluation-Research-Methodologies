import torch
from openpifpaf.datasets import DataModule, Coco
from openpifpaf import metric

try:
    import pycocotools.coco
    # monkey patch for Python 3 compat
    pycocotools.coco.unicode = str
except ImportError:
    pass

class Nightowls(DataModule):
    val_image_dir = '/Users/cesaredecal/nightowlsdata/nightowls_validation/'
    val_annotations = '/Users/cesaredecal/nightowlsdata/validation.json'

    def eval_loader(self):
        eval_data = Coco(
            image_dir=self.val_image_dir,
            ann_file=self.val_annotations,
        )
        return torch.utils.data.DataLoader(eval_data)

    def metrics(self):
        return [metric.Coco(
            pycocotools.coco.COCO(self.val_annotations),
            max_per_image=20,
            category_ids=[1],
            iou_type='keypoints',
        )]
