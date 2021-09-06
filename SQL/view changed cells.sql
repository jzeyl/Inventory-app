SELECT * from Jeremypreseason
WHERE Product_num IN (SELECT Product_num_ from Estimates WHERE Date_entered = "add")
