import promotions
import inspect
promos=[func for name,func in inspect.getmembers(promotions,inspect.isfunction)]
print(promos)
def best_promo(order):
	return max(promo(order) for promo in promos)