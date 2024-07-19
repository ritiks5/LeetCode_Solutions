SELECT 
    p.product_id, 
    ifnull(ROUND(sum(p.price * u.units)/sum(u.units),2),0) AS average_price
FROM 
    Prices p
left JOIN 
    UnitsSold u 
    ON u.product_id = p.product_id
and  
    u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY 
    p.product_id;
