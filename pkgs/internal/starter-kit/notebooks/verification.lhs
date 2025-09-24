:ext OverloadedStrings
import Test.QuickCheck
import Data.List.Split (splitOn)

normalize :: String -> [Int]
normalize s = map read (splitOn ";" s)

prop_roundtrip :: [Int] -> Bool
prop_roundtrip xs = normalize (concatMap ((++ ";") . show) xs) == xs

main :: IO ()
main = quickCheck prop_roundtrip
