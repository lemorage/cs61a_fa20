.read data.sql


CREATE TABLE average_prices AS
  SELECT category AS category, AVG(MSRP) AS average_price
    FROM products
    GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store AS store, item AS item, MIN(price) AS lowest_price
    FROM inventory
    GROUP BY item;


-- Helper Table for Q3
CREATE TABLE best_deal AS
  SELECT category AS category, name AS name, rating / MSRP AS ratio
    FROM products;


CREATE TABLE shopping_list AS
  SELECT item AS item, store AS store
    FROM best_deal, lowest_prices
    WHERE name = item
    GROUP BY category
      HAVING MAX(ratio);


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) AS total 
    FROM (SELECT Mbs AS Mbs
      FROM shopping_list, stores
      WHERE stores.store = shopping_list.store);

