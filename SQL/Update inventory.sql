UPDATE Jeremypreseason 
SET Total_Units = Total_Units-(SELECT SUM(Quantity) FROM Estimates
								WHERE Product_num_ =Jeremypreseason.Product_num)
WHERE Product_num IN (SELECT Product_num_ from Estimates WHERE Date_entered ="add") 



		