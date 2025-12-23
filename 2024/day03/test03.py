# 2024 Day 3 Part 1

from code03 import mul, mulnt

def test_part1():

    """
    It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

    For example, consider the following section of corrupted memory:
    
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

    """

    assert mul('mul(44,46)') == 2024
    assert mul('mul(123,4)') == 492
    assert mul('mul ( 2 , 4 )') == 0
    assert mul('mul(4*, mul(6,9!, ?(12,34)') == 0
    assert mul("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161

def test_part2():

    test_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert mulnt('do()') == 0
    assert mulnt("don't()") == 0
    assert mulnt("mul(2,5)") == 10
    assert mulnt("do()mul(4,5)") == 20
    assert mulnt("don't()mul(20,5)") == 0
    assert mulnt("mul(1,2)don't()mul(4,5)do()mul(7,8)mul(9,10)") == 1*2 + 7*8 + 9*10
    assert mulnt(test_data) == 48
    assert mulnt(");>]mul(437,864)^mul(880,907)}<how(){+[!' where()mul(215,270)from())@#mul(737,510)@<'why()+mul(634,344)$>::mul(528,832);{~<mul(514,817)>~who()who()(how(84,130)where(){%{mul(270,137)@") == 437*864 + 880*907 + 215*270 + 737*510 + 634*344 + 528*832 + 514*817 + 270*137

    assert mulnt(":mul(787,669)*]&^' @from()mul(896,940){where()when()]< -[mul(536,622)select()!{don't()-+^()!)}select()mul(287,737)&who()mul(452,401)from(763,594)$*when()select()&mul(804,971);}<~,(^%)[mul(148,448)mul(835,400)[}*$ #,do()?where(362,730)~why()#(;mul(448,254)'-/who() from():don't():what()'~(select()%mul(538,987): who()/#where()/what()where(587,42)select()mul(571,802)why()<]+}:#mul(446,206),/from()select()mul(271,435);#+^mul(8,739)-:~;<mul(361,969)+?^mul(238,723)<+<$<from()$$mul(93,726)}>?+~[#~mul(370,931)'}select()who()/when()from()%from()who()do()#mul(935,409)mul(356,457)]") == 787*669 + 896*940 + 536*622 + 448*254 + 935*409 + 356*457
    
    

if __name__ == "__main__":
    test_part2()
