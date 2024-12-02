locals {
  input = compact(split("\n", file("../input/day2.txt")))
  rows = [for row in local.input :
    {
      row : regexall("\\d+", row)
    }
  ]
  rowdiffs = [for i in local.rows :
    {
      row : i.row,
      inc : i.row[1] > i.row[0],
      diffs : [for k in range(length(i.row) - 1) : i.row[k + 1] - i.row[k]],
    }
  ]
  checks = [for i in local.rowdiffs :
    {
      row : i.row,
      cnt : length(i.diffs),
      ok : length([for k in i.diffs : k if abs(k) >= 1 && abs(k) <= 3]),
      ok2 : length([for k in i.diffs : k if(k > 0 && i.inc || k < 0 && !i.inc)]),
    }
  ]
  checka = [for i in local.checks :
    {
      row : i.row,
      aok : i.cnt == i.ok && i.cnt == i.ok2
    }
  ]
  a = [for i in local.checka : i if i.aok]
  brows = [for i in local.checka: 
    { 
      alts : [for j, k in range(length(i.row)) : 
        { 
          row : [for l, m in i.row : m if l != j] 
        }
      ]
    }
    if !i.aok
  ]
  bdiffs = [for i in local.brows : 
    {
      altdiffs : [for k in i.alts : 
        { 
          inc : k.row[1] > k.row[0],
          diffs : [for l in range(length(k.row) - 1) : k.row[l + 1] - k.row[l]] 
        }
      ]
    }
  ]
  bchecks = [for i in local.bdiffs :
    {
      altdiffs : [for k in i.altdiffs : 
        { cnt : length(k.diffs),
          ok : length([for l in k.diffs : l if abs(l) >= 1 && abs(l) <= 3]),
          ok2 : length([for l in k.diffs : l if(l > 0 && k.inc || l < 0 && !k.inc)])
        }
      ]
    }
  ]
  b = [for i in local.bchecks :
    { 
      bok : [for k in i.altdiffs : k if k.cnt == k.ok && k.cnt == k.ok2]
    }
  ]
}

output "AnswerA" {
  value = length(local.a)
}
output "AnswerB" {
  value = length(local.a) + length([for i in local.b: i if length(i.bok) > 0])
}