# Print Room content. One entry per campaign, strongest first.
# (aotw slug, title, brand, year, [image ids from image.adsoftheworld.com with size])
# To add a campaign: add a line. Local images go in assets/print/ and use 'local:filename@WxH'.
AOTW = 'https://www.adsoftheworld.com/campaigns/'
IMG = 'https://image.adsoftheworld.com/'

PRINT = [
 ('', 'Talk Go Taya You', 'Glo', '', ['glo-taya-1@1132x1600', 'glo-taya-2@1132x1600']),
 ('welcome-to-my-kitchen', 'Welcome to My Kitchen', 'Flour Mills Nigeria', '2022', ['do7owd2xc97mwexpiwql2m34sdxu@2200x1467', '047e39vyufeef6qd7l0ly1veouva@2200x1467', 'i02if8t1akqiww7yqgfx09vritd6@2200x1467', 'lx7sqfu1ig3l2ag47ss5mw20iz3k']),
 ('get-relief', 'Get Relief', 'Algafen', '2021', ['vuard0vj92cm0e88mpfjgq9ksr2b', 'vs4zyfjsyutyw2hzef2nc8xjqx32', 'jpayxiuxcvhtcdrzvaxxosjdtj6o']),
 ('fast-relief', 'Fast Relief', 'Algafen', '2021', ['xucgpabawtlkl416i1wggghqx51u', 'mlal8bakufkvqjapqje7rgx5e12p', 'c0egi82n8vtgceb819qstm2ht9zs']),
 ('motherhood-sentence', 'Motherhood Sentence', 'Love, Peace and Mental Health Foundation', '2022', ['y1faxdu9tw2lj8humj2gb7o9r949@2200x1589', 'ztrvf6legzu3sxv6u7h279iymunj@2200x1589', '5flvruw3rehcpefbyme0oiuhphzp@2200x1589']),
 ('being-ok-for-real', 'Being OK for Real', 'Love, Peace and Mental Health Foundation', '2022', ['85x5iwhbmsp9s760zm6it56h1s5u@1555x2200', 'fy57ar0z26yqeqb2lrnozn1upcco@1555x2200', '9freudyuf7dh0xu71o1imvvsretw@1555x2200', '416y6sbfvr6p2kaauhnmghnwbt5m@1501x1501', 'g3r67ty2kmx4ddna2we9hg5xg766@1501x1501', 'irov1dxwe4akna7lcvzrukx00a9y@1501x1501']),
 ('colour-our-world', 'Colour Our World', 'La Casera', '2022', ['trm5b37zgycrgpfz659c7ykgzl6c@1556x2200', 's05ljrh8vsbninmytobg846twvxc@2196x2200', 'ctb7p48fci0p54grql3nuo8oh7jb@1556x2200']),
 ('chaos-1d994972-0687-4eb0-96a7-7b966f5fbc56', 'Chaos', 'La Casera', '2022', ['um94lb6dy570eofvdngxkrv9v5vt', 'b5dbn06cmvqhyr4zsh93mu2sls7s', 'dmd1v6sbtnrsyl3hzzea73ch4sf9', 'sezaeqm13yuq6fa63yi719nf01gy']),
 ('findind-x', 'Finding X', 'X3M Ideas', '2022', ['7zsu31d69pqud9xe44tfakxweh0r@1556x2200', 'bqaso1doac1hd9qhchzsdks1q2cg@1556x2200', 'iemmnpky2qjokhgjxkiuzc1adww7@1556x2200']),
 ('adopt-a-gift', 'Adopt a Gift', 'Heritage Homes Orphanage', '2023', ['xzl3131juy4hp3ifxx3qvkfdtawy@2200x1465', '40lp97jx7kplijph6tgiu7was1xd@2200x1465', 'fidrc2jyfiy1m5kgcmanwzojqhj5@2200x1465', 'vloc66oki1oyr1xjq8y7aa9qqyjv@2200x1465', 'ocmo60ygbwvj1zun6kplezfzc8jo@2200x1211', '9tnymnlxrasimv7divswmyer5twc@2200x1238']),
 ('child-adopters', 'Child Adopters', 'Heritage Homes Orphanage', '2023', ['irrheyt3npqp0poz65wb4fj23ssh@2200x1465', 'gx9xl9pgpry2080nw4irdnooooav@2200x1465', 'hltcprxeeytdn6vyw06qjvd27kka@2200x1465']),
 ('body-and-mind', 'Body and Mind', 'Mentally Aware Nigeria Initiative', '2021', ['ow21qqvbewn23w3ugc58u8af88p4', 'wiauw8kogra5ac3r0yklcmq7e1bz', 'nr6ewbrkm7j7pr4nx2vqixm1snrq']),
 ('warrior-waterloo', 'Warrior Waterloo', 'Mentally Aware Nigeria Initiative', '2020', ['mn1lfclwj25yu0kez5106lkl9q3c', 'a9d4uc0rxfdxaj4fqwf2k3n76utl', '4rdvgz654i9i7r70n5mck8o38940']),
 ('laif-awards-2022', 'LAIF Awards 2022', 'AAAN', '2022', ['ro7betj0sl08xwgxba7rfsirm0tb@1555x2200', '8laf7icsd0ttowcb9k2kz10x7lkk@1555x2200', 'lx4wbwm2j7fk06mfz4xfm96zzhp1@1555x2200', 'afd7kmyu4xpt5b9lk0hc8t2m49gx@2000x2000', 'h2uwmsimgodc7kecw7pk6b79qmuv@2000x2000', 'dwc17cstxesrljfbohxyy57j6mrs@2000x2000', 'ap8e737b6z725fa7irszsvg8d6dw@2000x2000', '8rcswvrc0ekp9aq317loum5glnoo@2000x2000', '552klciv5w8joj4l6dt6pmes9cwy@2000x2000']),
 ('queue-for-democracy', 'Queue for Democracy', 'The Extra Step Initiative', '2023', ['ft3fdfcv2wuojlgtru9i9uvfrl4m@2048x2048', '8s079lc4r5jcl8qjrlo3oixfoiuk@2048x2048', 'f91pq8gcppb3f8gd90e6xjr55avp@2048x2048']),
 ('festive-trash', 'Festive Trash', 'Recycle Edge', '2023', ['45vue3juu155hm7txnpub8wjtqlu@1760x2200', 'gfhexi87bp32oat35wewi8v4ghoj@1760x2200', '28fssaa3zxze222u1hqmr21h72by@1760x2200']),
 ('vote-for-your-future', 'Vote for Your Future', 'Neusroom', '2023', ['0hjhg3ke5tjy1ss1q2wnuj87fis9@1760x2200', '6g1bq6q3s1qvad654xi5v8bzdiv8@1760x2200', '1mcz5cx3gzmw9wgyfe1mm3tw12eo@1760x2200']),
 ('the-unwanted-pet', 'The Unwanted Pet', 'Mortein', '2024', ['0peggock2a67mtei2ieusbnra83i@1920x1080', 'gl8296iwddwqmxt4jkhkfow7p9zr@1920x1080', 'ygo3iskl5pt6vzc6jgsirjzlkfj4@1920x1080']),
]
