Scripts to create database for ecommerce website:

CREATE TABLE pedidos (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_email varchar(256),
    cod_rastreio_logistica varchar(256),
    id_pagamento varchar(256),
    cep_de_entrega varchar(256),
    frete varchar(256)
);


CREATE TABLE itens_do_pedido (
	order_id int,
	item_id varchar(256),
	preco varchar(256),
	quantidade int
);


INSERT INTO public.pedidos (client_email, cod_rastreio_logistica, id_pagamento, cep_de_entrega) VALUES (10, value2 , value3, ...);

INSERT INTO itens_do_pedido (order_id, preco, item_id, quantidade) VALUES ();