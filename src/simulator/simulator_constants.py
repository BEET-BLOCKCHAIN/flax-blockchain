from typing import Dict, Any

test_constants: Dict[str, Any] = {
    "DIFFICULTY_STARTING": 5,
    "DISCRIMINANT_SIZE_BITS": 16,
    "BLOCK_TIME_TARGET": 10,
    "MIN_BLOCK_TIME": 2,
    "DIFFICULTY_FACTOR": 3,
    "DIFFICULTY_EPOCH": 12,  # The number of blocks per epoch
    "DIFFICULTY_WARP_FACTOR": 4,  # DELAY divides EPOCH in order to warp efficiently.
    "DIFFICULTY_DELAY": 3,  # EPOCH / WARP_FACTOR
    "MIN_ITERS_STARTING": 50 * 2,
    "GENESIS_BLOCK": b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15N3\xd3\xf9H\xc2K\x96\xfe\xf2f\xa2\xbf\x87\x0e\x0f,\xd0\xd4\x0f6s\xb1".\\\xf5\x8a\xb4\x03\x84\x8e\xf9\xbb\xa1\xca\xdef3:\xe4?\x0c\xe5\xc6\x12\x80\x17\xd2\xcc\xd7\xb4m\x94\xb7V\x959\xed4\x89\x04b\x08\x07^\xca`\x8f#%\xe9\x9c\x9d\x86y\x10\x96W\x9d\xce\xc1\x15r\x97\x91U\n\x11<\xdf\xb2\xfc\xfb<\x13\x00\x00\x00\x98\xf4\x88\xcb\xb2MYo]\xaf \xd8a>\x06\xfe\xc8F\x8d\x15\x90\x15\xbb\x04\xd48\x10\xc6\xd8b\x82\x88\x7fx<\xe5\xe6\x8b\x8f\x84\xdd\x1cU"\x83\xfb7\x9d`\xb0I\xb3\xbe;bvE\xc6\x92\xdd\xbe\x988\xe9y;\xc6.\xa1\xce\x94\xdc\xd8\xab\xaf\xba\x8f\xd8r\x8br\xc8\xa0\xac\xc0\xe9T\x87\x08\x08\x8b#-\xb6o\xf0\x1f\x0bzv\xb3\x81\x1a\xd4\xf7\x01\xdf\xc5A\x11\xe0\x0c\xc0\x87\xa6\xc2v\xbbR\xc4{"\xa5\xe5\xe0bx7\xfa\n\xae\xea\xfe\x02\xac\xef\xec\xd1\xc2\xc55\x06{\xe1\x0c\xb2\x99q\xd7\xd8\xcb\x97\x86\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xde\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00%\x03\x00\x00\x004\x00*\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00[\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x01z\x00|\x00[\x00\xb2\xff\xc9\x00\x00\x00\x00\x00\x00\x05\xe9\x00\xac\xff\xdb\x00\xf0\xff\xc5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^h:\xb3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00}\xe7@\xfc\xa6\xaf\xc6\xec\xe8\xba\x19\xa3\x9b\x19vq\x91C\xa2\xe3\xde\x1f\xf1zB.\xf2\xc2\xc3,\x06\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x08\xde\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8b)\xaa\x96x8\xd76J\xa6\x8b[\x98\t\xe0\\\xe3^7qD\x8c\xf5q\x08\xf2\xa2\xc9\xb03mv\x00\x00\x0c\xbb\xa1\x06\xe0\x00N\x1f\xe8;}6F\xd7\xec\xc7\x83\x16T\x96\x1f\xe6\x88,\xa4\x9b\xa3Lo\xd0\xe6\x89jW\xac\xba\xae)\xe9\x91?\x97\x0fU\xf5\xd8\xdc\x9e\xce\xbf~\xad\xc2\xbc\x17v|\x947N\x0e\xfa\xff\xe6;\xce@|\xe9{\xe2:\xa8H\xb4\xb9\xde;<;-\x9a\x03\xbf\xa3\xff\xed\x81\x0cd\x80|(I\x9e\x8c\xa5\x83\xdf\x8a\x1aX\xc1#\x19uE`)\xeblV\x1d\x8f\xe6\x1f\xfa\x03\xe2\xf4b\xdfO\x9c\x11\x1fHJ2\xbfvC\x8b^\x8b)\xaa\x96x8\xd76J\xa6\x8b[\x98\t\xe0\\\xe3^7qD\x8c\xf5q\x08\xf2\xa2\xc9\xb03mv\x00\x00\x01\xd1\xa9J \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcc}q\x8d\x81\x9e`\xbfZ\x8a\xa6\xc7\xf0\x03\xc1s:\xd3\xf9p\xf1\x86\xe6yRU\xea\xa4\xd5*\x8b\x05;{\xfb\xcb\xed\xe8\xac\xb3\xfelR\xa3C\xa5\xe3~\x07\xfa\x1bv\xf87\xbb\xa7\xba\x1f\x82\x13\x1d\xe0\x19$\x1a\xbc&\x13\xb2\xe0\xe7\xd5\xa6\xbc\x15\xbc\xaa\x0e%|\xc0\x9bl\x91\xd9\xf7O\xef\xca\x00\\\xeeL\xa1\xd2\x0e\x00\x00',  # noqa: E501
    "COINBASE_FREEZE_PERIOD": 0,
}
