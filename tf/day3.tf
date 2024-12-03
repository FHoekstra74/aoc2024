locals {
  input      = join("", compact(split("\n", file("../input/day3.txt"))))
  parts      = regexall("mul\\(\\d+,\\d+\\)", local.input)
  partssplit = [for v in local.parts : regexall("\\d+", v)]
  a          = [for v in local.partssplit : tonumber(v[0]) * tonumber(v[1])]

  dos               = split("do()", local.input)
  dos_without_donts = [for v in local.dos : split("don't()", v)[0]]
  dos_parts         = [for v in local.dos_without_donts : regexall("mul\\(\\d+,\\d+\\)", v)]
  dos_partssplit    = [for v in concat(local.dos_parts...) : regexall("\\d+", v)]
  b                 = [for v in local.dos_partssplit : tonumber(v[0]) * tonumber(v[1])]
}

output "resultA" {
  value = sum(local.a)
}
output "resultB" {
  value = sum(local.b)
}