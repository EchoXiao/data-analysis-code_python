
  
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

  








