
select * from orders table                                    select * from users table
+-----------------------------------------------+             +-------------------------------------+
| id    | user_id | rental_type | renting_days |                | id   | email_add     | phone_num    |
| 1234  | 0001    | hto         |   3          |                | 0001 | xxx@gmail.com | xxx-xxxx-xxx |
| 1235  | 0002    | audio_hto   |   6          |                | 0002 | xxx@gmail.com | xxx-xxxx-xxx |
| 1236  | 0003    | purchase    |   9          |                | 0003 | xxx@gmail.com | xxx-xxxx-xxx |
| 1237  | 0001    | hto         |   17         |                | 0004 | xxx@gmail.com | xxx-xxxx-xxx |
+-----------------------------------------------+             +-------------------------------------+

select * from products table                                  select * from order_products table
+-------------------+                                         +--------------------+
| id    | type     |                                          | user_id | order_id |
| 00001 | wearable |                                          | 00001   | 00001    |
| 00002 | photo    |                                          | 00002   | 00002    |
| 00003 | audio    |                                          | 00003   | 00004    |    
| 00004 | drone    |                                          | 00001   | 00005    |
+-------------------+                                         +--------------------+

select * from price table
+-----------------------------------------------------+
| prod_id | price_4 | price_8 | price_12 | price_15 |
| 0001    | 30      |  4      |   4      |   4      |
| 0002    | 20      |  2      |   2      |   2      |
| 0003    | 40      |  10     |   3      |   3      |
| 0004    | 30      |  4      |   4      |   4      |
+-----------------------------------------------------+




  
# new user orders vs. repeat users orders 
  
select date_format(orders.created_at, "%y-%m") as orders_ym,
    date_format(users.created_at, "%y-%m") as users_ym, 
    count(distinct orders.id) as drones_total_orders,
    count(distinct(orders.user_id)) as new_users_orders_count,
    count(distinct orders.id) - count(distinct(orders.user_id)) as returned_users_orders_count
from orders
 join order_products
    on orders.id = order_products.order_id
 join products
    on products.id = order_products.product_id
 join users
    on users.id = orders.user_id
where products.product_type = "drone"
    and status not in ("in_progress", "canceled", "is_special")
group by orders_ym
having orders_ym = users_ym
  
  
  
# weekly avg. order value last year----------------------------------------------------------
  


# LTV of users
  # customer expenditures per visit
  # number of visit per week (the "purchase cycle")
  # the average customers lifespan
  # customer retention rate

  








