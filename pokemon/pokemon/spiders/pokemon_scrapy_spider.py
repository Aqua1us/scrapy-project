# -*- coding: utf-8 -*-
import scrapy
from pokemon.items import PokemonItem


# Scrapyスパイダー
class PokemonScrapySpider(scrapy.Spider):
    name = 'pokemon_base_data_list'
    allowed_domains = ['pokemondb.net']
    start_urls = ["https://pokemondb.net/pokedex/all"]

    # HTTPレスポンスのパース
    def parse(self, response):
        table = response.xpath('//*[@id="pokedex"]')
        rows = table.xpath('tbody/tr/td[1]/text()').extract()

        for row in range(1, len(rows)):
            index = table.xpath('tbody/tr[' + str(row) + ']/td[1]/text()').extract()

            base_name = table.xpath('tbody/tr[' + str(row) + ']/td[2]/a/text()').extract()
            info = table.xpath('tbody/tr[' + str(row) + ']/td[2]/small/text()').extract()
            name = base_name[0] + ' (' + info[0] + ')' if (len(info) > 0) else base_name[0]

            stats_t = table.xpath('tbody/tr[' + str(row) + ']/td[4]/text()').extract()      # Total
            stats_h = table.xpath('tbody/tr[' + str(row) + ']/td[5]/text()').extract()      # HP
            stats_a = table.xpath('tbody/tr[' + str(row) + ']/td[6]/text()').extract()      # Attack
            stats_b = table.xpath('tbody/tr[' + str(row) + ']/td[7]/text()').extract()      # Defense
            stats_c = table.xpath('tbody/tr[' + str(row) + ']/td[8]/text()').extract()      # Sp. Atk
            stats_d = table.xpath('tbody/tr[' + str(row) + ']/td[9]/text()').extract()      # Sp. Def
            stats_s = table.xpath('tbody/tr[' + str(row) + ']/td[10]/text()').extract()     # Speed

            yield PokemonItem(
                index=index,
                name=name,
                total=stats_t,
                hp=stats_h,
                attack=stats_a,
                defense=stats_b,
                sp_attack=stats_c,
                sp_defense=stats_d,
                speed=stats_s)
