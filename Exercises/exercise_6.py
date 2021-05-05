from random import randint

class Application:
    def generate_random_points(self):
        """[Generate two randoms number between 0-2000]

        Returns:
            [tuple]: [generate ramdom int origin start / end]
        """
        return randint(0, 2000), randint(0, 2000)

    def calculate_days(self, n):
        """Calculate days estimated by n
 
        Args:
            n ([type]): [integer result of  int(dist / 100) ]

        Returns:
            [type]: [description]
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        aux1 = 0
        aux2 = 1
        for i in range(1, n):
            sum = aux1 + aux2
            print(f"aux1: {aux1}, aux2: {aux2}")
            print(sum)
            aux1 = aux2
            aux2 = sum
        return sum

    def estimate_days_time_delivery(self, start, end):
        """
        Estima el tiempo de entrega de la entrega de una compra online (en días), 
        en función de la distancia que existe entre una dirección de origen y destino.]

        Args:
            start (int): start origin destiny value 
            end (int): end origin destiny value

        Returns:
            [int]: estimated delivery days 
        """
        print(f"origen: {start} | destino: {end}")
        dist = abs(start - end)
        print (f"distancia :{dist}")
        n = int(dist / 100)
        print(f"(distancia/100):{n}")
        days_estimated =  self.calculate_days(n)
        return f"días entrega estimado : {days_estimated}"


app = Application()
origen, destino =  app.generate_random_points()
result = app.estimate_days_time_delivery(origen, destino)
print(result)