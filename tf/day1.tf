locals {
  input      = file("../input/day1.txt")
  inputlist  = compact(split("\n", local.input))
  inputleft  = [for v in local.inputlist : regex("[0-9]+", v)]
  inputright = [for v in local.inputlist : regexall("[0-9]+", v)[1]]
  leftsort   = sort(local.inputleft)
  rightsort  = sort(local.inputright)
  diff       = [for i, v in local.rightsort : (tonumber(v) - tonumber(local.leftsort[i]))]
  a          = [for v in local.diff : v > 0 ? v : v * -1]
  count      = [for v in local.inputleft : sum([for k in local.inputright : v == k ? 1 : 0])]
  b          = [for i, v in local.inputleft : tonumber(v) * local.count[i]]
}

output "AnswerA" {
  value = sum(local.a)
}
output "AnswerB" {
  value = sum(local.b)
}