from phishpedia import PhishpediaWrapper as phishpedia_cls
import os
import cv2

phishpedia = phishpedia_cls()

for x in [
    "1&1 Ionos+2019-07-28-22`34`40",
    "1&1 Ionos+2020-05-08-11`02`58",
    "1&1 Ionos+2019-07-28-23`07`22",
]:
    url_path = os.path.join(
        "/Users/mjarczewski/Repositories/Phishpedia/datasets/test_sites", x, "info.txt"
    )
    img_path = os.path.join(
        "/Users/mjarczewski/Repositories/Phishpedia/datasets/test_sites", x, "shot.png"
    )

    with open(url_path, "r") as file:
        url = file.read()
    img = cv2.imread(img_path)

    (
        phish_category,
        pred_target,
        matched_domain,
        plotvis,
        siamese_conf,
        _,
        logo_recog_time,
        logo_match_time,
    ) = phishpedia.test_orig_phishpedia(url, None, None, img)

    print(
        phish_category,
        pred_target,
        matched_domain,
        plotvis,
        siamese_conf,
        logo_recog_time,
        logo_match_time,
    )
